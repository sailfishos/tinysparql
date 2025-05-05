Name:       tinysparql
Summary:    Desktop-neutral metadata database and search tool
Version:    3.9.2
Release:    1
License:    LGPLv2+ and GPLv2+
URL:        https://gnome.pages.gitlab.gnome.org/tinysparql/
Source0:    %{name}-%{version}.tar.bz2
Patch1:     0001-Always-insert-timestamps-into-the-database-as-string.patch
Patch2:     0002-portal-Allow-D-Bus-activation-only-through-systemd.patch

BuildRequires:  meson >= 0.50
BuildRequires:  vala-devel >= 0.16
BuildRequires:  gettext
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.60
BuildRequires:  pkgconfig(gio-2.0) >= 2.46.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.46.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.46.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.46.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.46.0
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(sqlite3) >= 3.11
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.0
BuildRequires:  python3-gobject

Requires:   systemd-user-session-targets
Requires(post):   /sbin/ldconfig
Requires(postun): /sbin/ldconfig

Obsoletes:      tracker < 3.8
Provides:       tracker = %{version}-%{release}

%description
Tinysparql is a powerful desktop-neutral first class object database,
tag/metadata database and search tool.

It consists of a common object database that allows entities to have an
almost infinite number of properties, metadata (both embedded/harvested as
well as user definable), a comprehensive database of keywords/tags and
links to other entities.

It provides additional features for file based objects including context
linking and audit trails for a file object.

Metadata indexers are provided by the localsearch package.

%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}
Obsoletes:  tracker-devel < 3.8

%description devel
Development files for %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%meson -Dman=false -Ddocs=false \
       -Davahi=disabled \
       -Dstemmer=disabled \
       -Dunicode_support=icu \
       -Dbash_completion=false \
       -Dsystemd_user_services_dir=%{_userunitdir}

%meson_build

%install
%meson_install

%find_lang tinysparql3

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f tinysparql3.lang
%license COPYING COPYING.LGPL COPYING.GPL
%{_bindir}/tinysparql
%{_libexecdir}/tinysparql-sql
%{_libexecdir}/tinysparql-xdg-portal-3
%{_libdir}/libtinysparql-3.0.so.0*
%{_libdir}/tinysparql-3.0/
%{_datadir}/dbus-1/services/org.freedesktop.portal.Tracker.service
%{_userunitdir}/tinysparql-xdg-portal-3.service

%files devel
%doc AUTHORS NEWS README.md
%{_includedir}/tinysparql-3.0/
%{_libdir}/libtinysparql-3.0.so
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Tracker-3.0.typelib
%{_libdir}/girepository-1.0/Tsparql-3.0.typelib
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/tracker*.deps
%{_datadir}/vala/vapi/tracker*.vapi
%{_libdir}/pkgconfig/tinysparql-3.0.pc
%{_libdir}/pkgconfig/tracker-sparql-3.0.pc
%{_datadir}/vala/vapi/tinysparql-3.0.deps
%{_datadir}/vala/vapi/tinysparql-3.0.vapi
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Tracker-3.0.gir
%{_datadir}/gir-1.0/Tsparql-3.0.gir
