Name:       tracker

Summary:    An efficient search engine and triplestore for desktop, embedded and mobile.
Version:    2.3.4
Release:    1
License:    LGPLv2.1+ and BSD
URL:        https://gitlab.gnome.org/GNOME/%{name}/
Source0:    https://gitlab.gnome.org/GNOME/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2
Source1:    tracker-configs.sh
Patch1:     001-Tracker-config-overrides.patch
Patch2:     002-allow-skip-reset-prompt.patch
Patch3:     003-Disable-trackertestutils.patch

Requires:   unzip
Requires:   systemd
Requires:   systemd-user-session-targets

Requires(post): /sbin/ldconfig
Requires(post):  oneshot
Requires(postun): /sbin/ldconfig
BuildRequires:  meson >= 0.50
BuildRequires:  ninja
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.60
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.38.0
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(sqlite3) >= 3.11
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  gettext
BuildRequires:  vala-devel >= 0.16
BuildRequires:  intltool
BuildRequires:  fdupes
BuildRequires:  oneshot

%description
Tracker is a powerful desktop-neutral first class object database,
tag/metadata database, search tool and indexer.

It consists of a common object database that allows entities to have an
almost infinte number of properties, metadata (both embedded/harvested as
well as user definable), a comprehensive database of keywords/tags and
links to other entities.

It provides additional features for file based objects including context
linking and audit trails for a file object.

It has the ability to index, store, harvest metadata. retrieve and search
all types of files and other first class objects.

%package utils
Summary:    Tracker command line applications to lookup data
Group:      Development/Tools
Requires:   %{name} = %{version}-%{release}

%description utils
Tracker command line applications to lookup data.

%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%meson -Dman=false -Ddocs=false -Dfunctional_tests=false \
       -Dnetwork_manager=disabled -Dstemmer=disabled \
       -Dunicode_support=icu

%install
rm -rf %{buildroot}

%meson_install

rm %{buildroot}/etc/xdg/autostart/tracker-store.desktop

# oneshot run in install
mkdir -p %{buildroot}%{_oneshotdir}
cp -a %{SOURCE1} %{buildroot}%{_oneshotdir}

%find_lang %{name}

%fdupes  %{buildroot}/%{_datadir}/

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
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.service
%dir %{_datadir}/tracker
%{_datadir}/tracker/*.xml
%{_datadir}/tracker/stop-words/*
%{_datadir}/tracker/domain-ontologies/default.rule
%{_datadir}/tracker/ontologies/*
%{_datadir}/vala/vapi/tracker*.deps
%{_datadir}/vala/vapi/tracker*.vapi
%dir %{_libdir}/tracker-2.0
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.*.xml
%{_libdir}/libtracker-miner-*.so*
%{_libdir}/libtracker-sparql-*.so*
%{_libdir}/libtracker-control-*.so*
%{_libdir}/tracker-2.0/libtracker-data.so
%{_libexecdir}/tracker-store
%license COPYING COPYING.GPL COPYING.LGPL
%{_libdir}/systemd/user/tracker-store.service
%attr(0755, -, -) %{_oneshotdir}/tracker-configs.sh

%files utils
%defattr(-,root,root,-)
%{_bindir}/tracker
%{_datadir}/bash-completion/completions/tracker

%files devel
%defattr(-,root,root,-)
%{_includedir}/tracker-2.0
%{_libdir}/pkgconfig/tracker-*.pc
%{_libdir}/girepository-1.0/Tracker*.typelib
%{_datadir}/gir-1.0/Tracker*.gir

