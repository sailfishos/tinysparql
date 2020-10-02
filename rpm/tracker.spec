Name:       tracker
Summary:    Desktop-neutral metadata database and search tool
Version:    2.3.6
Release:    1
License:    LGPLv2+ and GPLv2+
URL:        https://wiki.gnome.org/Projects/Tracker
Source0:    %{name}-%{version}.tar.bz2
Source1:    tracker-configs.sh
Patch1:     001-Tracker-config-overrides.patch
Patch2:     002-allow-skip-reset-prompt.patch
Patch3:     003-Disable-trackertestutils.patch

BuildRequires:  meson >= 0.50
BuildRequires:  vala-devel >= 0.16
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  oneshot
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
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.40
BuildRequires:  pkgconfig(sqlite3) >= 3.11
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.0

Requires:   systemd-user-session-targets
Requires(post):   /sbin/ldconfig
Requires(postun): /sbin/ldconfig
%{_oneshot_requires_post}

Obsoletes:  tracker-utils

%description
Tracker is a powerful desktop-neutral first class object database,
tag/metadata database and search tool.

It consists of a common object database that allows entities to have an
almost infinite number of properties, metadata (both embedded/harvested as
well as user definable), a comprehensive database of keywords/tags and
links to other entities.

It provides additional features for file based objects including context
linking and audit trails for a file object.

Metadata indexers are provided by the tracker-miners package.

%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%meson -Dman=false -Ddocs=false -Dfunctional_tests=false \
       -Dnetwork_manager=disabled -Dstemmer=disabled \
       -Dunicode_support=icu \
       -Dbash_completion=no \
       -Dsystemd_user_services=%{_userunitdir}
%meson_build

%install
%meson_install

# oneshot run in install
install -D -m 755 %{SOURCE1} %{buildroot}/%{_oneshotdir}/tracker-configs.sh

%find_lang %{name}

%post
/sbin/ldconfig
glib-compile-schemas   /usr/share/glib-2.0/schemas/
if [ "$1" -ge 1 ]; then
systemctl-user daemon-reload || :
systemctl-user stop tracker-store.service || :
add-oneshot --new-users --all-users tracker-configs.sh || :
fi

%postun
/sbin/ldconfig
glib-compile-schemas   /usr/share/glib-2.0/schemas/
if [ "$1" -eq 0 ]; then
systemctl-user stop org.freedesktop.Tracker1.service || :
systemctl-user daemon-reload || :
fi

%files -f %{name}.lang
%defattr(-,root,root,-)
%license COPYING COPYING.LGPL COPYING.GPL
%{_bindir}/tracker
%{_libexecdir}/tracker-store
%{_libdir}/libtracker-control-*.so.*
%{_libdir}/libtracker-miner-*.so.*
%{_libdir}/libtracker-sparql-*.so.*
%{_libdir}/tracker-2.0/libtracker-data.so
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.service
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.*.xml
%{_datadir}/tracker/*.xml
%{_datadir}/tracker/stop-words/*
%{_datadir}/tracker/domain-ontologies/default.rule
%{_datadir}/tracker/ontologies/*
%{_userunitdir}/tracker-store.service
%attr(0755, -, -) %{_oneshotdir}/tracker-configs.sh

%files devel
%defattr(-,root,root,-)
%doc AUTHORS NEWS README.md
%{_includedir}/tracker-2.0/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Tracker-2.0.typelib
%{_libdir}/girepository-1.0/TrackerControl-2.0.typelib
%{_libdir}/girepository-1.0/TrackerMiner-2.0.typelib
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/tracker*.deps
%{_datadir}/vala/vapi/tracker*.vapi
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Tracker-2.0.gir
%{_datadir}/gir-1.0/TrackerControl-2.0.gir
%{_datadir}/gir-1.0/TrackerMiner-2.0.gir
