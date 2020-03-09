Name:       tracker

%define enable_demo 0

Summary:    An object database, tag/metadata database, search tool and indexer
Version:    1.12.4
Release:    1
License:    GPLv2+ and LGPLv2.1+ and BSD
URL:        http://ftp.gnome.org/pub/GNOME/sources/tracker/1.12/
Source0:    http://ftp.gnome.org/pub/GNOME/sources/%{name}/1.12/%{name}-%{version}.tar.xz
Source1:    tracker-libav-rpmlintrc
Source2:    10-rtf.rule
Source5:    tracker-configs.sh
Patch1:     001-install-the-data-generation-scripts.patch
Patch2:     002-Fix-CLEANFILE-for-automake.patch
Patch3:     003-Tracker-config-overrides.patch
Patch4:     004-tracker-Remove-nfo-language-and-fix-libmediaart-call.patch
Patch5:     005-Bugfix-for-GB740920-ensure-sourceiri-is-filled-in-on.patch
Patch6:     006-trackerlibav-get-metadata-from-audio-stream-instead-.patch
Patch7:     007-tracker-Drop-15gstreamerguessrule-Fixes-JB37082.patch
Patch8:     008-tracker-Fix-flac-tag-extraction-Fixes-JB35939.patch
Patch9:     009-tracker-Add-album-art-extraction-for-libav-and-flac-.patch
Patch10:    010-tracker-Use-Xing-mp3-header-when-available-Fixes-JB3.patch
Patch11:    011-revert-libmediaart-disable.patch
Patch13:    013-miner-Fix-mining-of-files-whose-data-was-inserted-by.patch
Patch14:    014-fix-systemd-unit-files.patch
Patch15:    015-allow-skip-reset-prompt.patch
Patch16:    016-Disable-libtracker-sparql-parallel-build.patch
Patch17:    017-libtracker-data-Fix-build-with-Vala-0.43.patch

Requires:   libmediaart
Requires:   unzip
Requires:   systemd
Requires:   systemd-user-session-targets
Requires:   qt5-plugin-platform-minimal
Requires(post): /sbin/ldconfig
Requires(post):  oneshot
Requires(postun): /sbin/ldconfig
BuildRequires:  gobject-introspection-devel
BuildRequires:  pkgconfig(libmediaart-2.0)
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.60
BuildRequires:  pkgconfig(enca)
BuildRequires:  pkgconfig(exempi-2.0)
BuildRequires:  pkgconfig(dconf)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.38.0
BuildRequires:  pkgconfig(gmime-2.6)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(id3tag)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libgsf-1)
BuildRequires:  pkgconfig(libiptcdata)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(sqlite3) >= 3.11
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(totem-plparser)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  gettext
BuildRequires:  libtool
BuildRequires:  vala-devel >= 0.16
BuildRequires:  giflib-devel
BuildRequires:  intltool
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel >= 3.8.2
BuildRequires:  perl-XML-Parser
BuildRequires:  pygobject2
BuildRequires:  python >= 2.6
BuildRequires:  dbus-python
BuildRequires:  fdupes
BuildRequires:  giflib-devel
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


%package tests
Summary:    Tests for tracker
Group:      System/X11
Requires:   %{name} = %{version}-%{release}
Requires:   dbus-python
Requires:   pygobject2
Requires:   python >= 2.6

%description tests
Functional tests for tracker to be run once tracker is installed in
the final environment.


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

%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{name} = %{version}-%{release}

%description doc
Man pages for %{name}.

%prep
%setup -q -n %{name}-%{version}/upstream
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1

%build
sed -i -e '/gtkdocize/d' autogen.sh
echo "EXTRA_DIST = missing-gtk-doc" > gtk-doc.make

chmod +x tests/functional-tests/create-tests-xml.py

%autogen --disable-static \
    --with-compile-warnings=no \
    --disable-gtk-doc \
    --disable-introspection \
    --disable-tracker-preferences \
	--disable-tracker-needle \
    --enable-unit-tests \
    --enable-functional-tests \
    --disable-introspection \
    --disable-gtk-doc \
    --disable-miner-evolution \
    --disable-miner-firefox \
    --disable-miner-thunderbird \
    --disable-miner-rss \
    --disable-miner-user-guides \
    --disable-miner-apps \
    --enable-guarantee-metadata \
    --with-unicode-support=libicu \
    --enable-libvorbis \
    --enable-libflac \
    --enable-generic-media-extractor=libav \
    --disable-enca \
    --enable-journal \
    --disable-icon \
    --disable-artwork \
    --enable-libgif \
    --disable-cfg-man-pages

touch tests/functional-tests/ttl/gen-test-data.stamp

make %{?_smp_mflags}

%install
rm -rf %{buildroot}

%make_install
mkdir -p %{buildroot}%{_libdir}/systemd/user/post-user-session.target.wants
ln -s ../tracker-store.service %{buildroot}%{_libdir}/systemd/user/post-user-session.target.wants/
ln -s ../tracker-miner-fs.service %{buildroot}%{_libdir}/systemd/user/post-user-session.target.wants/
ln -s ../tracker-extract.service %{buildroot}%{_libdir}/systemd/user/post-user-session.target.wants/

# oneshot run in install
mkdir -p %{buildroot}%{_oneshotdir}
cp -a %{SOURCE5} %{buildroot}%{_oneshotdir}
cp -a %{SOURCE2} %{buildroot}%{_datadir}/tracker/extract-rules/

%find_lang %{name}

%fdupes  %{buildroot}/%{_datadir}/

%post
/sbin/ldconfig
glib-compile-schemas   /usr/share/glib-2.0/schemas/
if [ "$1" -ge 1 ]; then
systemctl-user daemon-reload || :
systemctl-user try-restart tracker-store.service tracker-miner-fs.service tracker-extract.service || :
add-oneshot --new-users --all-users tracker-configs.sh || :
fi


%postun
/sbin/ldconfig
glib-compile-schemas   /usr/share/glib-2.0/schemas/
if [ "$1" -eq 0 ]; then
systemctl-user stop tracker-miner-fs.service tracker-store.service tracker-extract.service || :
systemctl-user daemon-reload || :
fi


%preun tests
# created during post install
rm -f /usr/share/tracker-tests/ttl/*
rm -f /usr/share/tracker-tests/source-data.pkl


%post tests
# this creates ~160MB of test data for the auto tests
cd /usr/share/tracker-tests/
/opt/tests/tracker/bin/generate /opt/tests/tracker/bin/max.cfg


%files -f %{name}.lang
%defattr(-,root,root,-)
%defattr(-, root, root, -)
%{_datadir}/dbus-1/services/*
%{_datadir}/tracker/miners/*
%{_datadir}/tracker/*.xml
%{_datadir}/tracker/stop-words/*
%{_datadir}/tracker/ontologies/*
%{_datadir}/vala/vapi/*
%{_datadir}/tracker/extract-rules/*
%dir %{_datadir}/tracker
%dir %{_datadir}/tracker/miners
%dir %{_datadir}/tracker/stop-words
%dir %{_datadir}/tracker/ontologies
%dir %{_datadir}/tracker/extract-rules
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%dir %{_libdir}/tracker-*
%dir %{_libdir}/tracker-*/extract-modules
%dir %{_libdir}/tracker-*/writeback-modules
%{_datadir}/glib-2.0/schemas/*.xml
%{_libdir}/libtracker-miner-*.so*
%{_libdir}/libtracker-sparql-*.so*
%{_libdir}/libtracker-control-*.so*
%{_libdir}/tracker-*/*.so*
%{_libdir}/tracker-*/extract-modules/*.so*
%{_libdir}/tracker-*/writeback-modules/*.so*
%{_libexecdir}/tracker-extract
%{_libexecdir}/tracker-miner-fs
%{_libexecdir}/tracker-store
%{_libexecdir}/tracker-writeback
%license COPYING COPYING.GPL COPYING.LGPL
%exclude %{_sysconfdir}/xdg/autostart/*.desktop
%{_libdir}/systemd/user/tracker-miner-fs.service
%{_libdir}/systemd/user/tracker-store.service
%{_libdir}/systemd/user/tracker-extract.service
%{_libdir}/systemd/user/tracker-writeback.service
%{_libdir}/systemd/user/post-user-session.target.wants/tracker-miner-fs.service
%{_libdir}/systemd/user/post-user-session.target.wants/tracker-store.service
%{_libdir}/systemd/user/post-user-session.target.wants/tracker-extract.service
%attr(0755, -, -) %{_oneshotdir}/tracker-configs.sh

%files tests
%defattr(-,root,root,-)
%{_datadir}/tracker-tests
/opt/tests/tracker

%files utils
%defattr(-,root,root,-)
%{_bindir}/tracker
%{_datadir}/bash-completion/completions/tracker

%files devel
%defattr(-,root,root,-)
%{_includedir}/tracker-*
%{_libdir}/pkgconfig/tracker-*.pc

%files doc
%defattr(-,root,root,-)
%{_mandir}/man1/%{name}-*
