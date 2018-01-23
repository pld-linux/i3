Summary:	improved tiling wm
Name:		i3
Version:	4.14.1
Release:	0.1
License:	BSD
Group:		X11/Window Managers
Source0:	http://i3wm.org/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	0f4eec9e5a9f7be060bda41206b13f87
URL:		http://i3wm.org/
BuildRequires:	asciidoc
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libev-devel
BuildRequires:	libxcb-devel
BuildRequires:	pango-devel
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel
BuildRequires:	xcb-proto
BuildRequires:	xcb-util-cursor-devel
BuildRequires:	xcb-util-devel
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	xcb-util-wm-devel
BuildRequires:	xcb-util-xrm-devel
BuildRequires:	xmlto
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libxkbcommon-devel
BuildRequires:	xorg-lib-libxkbcommon-x11-devel
BuildRequires:	xorg-lib-libxkbfile
BuildRequires:	yajl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
i3 is a tiling window manager, completely written from scratch. The
target platforms are GNU/Linux and BSD operating systems, our code is
Free and Open Source Software (FOSS) under the BSD license. i3 is
primarily targeted at advanced users and developers.

%package devel
Summary:	Header files for %{name}
Group:		Development/Libraries

%description devel
Header files for %{name}.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-builddir \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_docdir}/i3

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE RELEASE-NOTES-%{version} docs/*.html
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/config
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/config.keycodes
%attr(755,root,root) %{_bindir}/i3
%attr(755,root,root) %{_bindir}/i3bar
%attr(755,root,root) %{_bindir}/i3-config-wizard
%attr(755,root,root) %{_bindir}/i3-dmenu-desktop
%attr(755,root,root) %{_bindir}/i3-dump-log
%attr(755,root,root) %{_bindir}/i3-input
%attr(755,root,root) %{_bindir}/i3-migrate-config-to-v4
%attr(755,root,root) %{_bindir}/i3-msg
%attr(755,root,root) %{_bindir}/i3-nagbar
%attr(755,root,root) %{_bindir}/i3-save-tree
%attr(755,root,root) %{_bindir}/i3-sensible-editor
%attr(755,root,root) %{_bindir}/i3-sensible-pager
%attr(755,root,root) %{_bindir}/i3-sensible-terminal
%attr(755,root,root) %{_bindir}/i3-with-shmlog
%{_datadir}/xsessions/%{name}.desktop
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/i3.1*
%{_mandir}/man1/i3bar.1*
%{_mandir}/man1/i3-config-wizard.1*
%{_mandir}/man1/i3-dmenu-desktop.1*
%{_mandir}/man1/i3-dump-log.1*
%{_mandir}/man1/i3-input.1*
%{_mandir}/man1/i3-migrate-config-to-v4.1*
%{_mandir}/man1/i3-msg.1*
%{_mandir}/man1/i3-nagbar.1*
%{_mandir}/man1/i3-save-tree.1*
%{_mandir}/man1/i3-sensible-editor.1*
%{_mandir}/man1/i3-sensible-pager.1*
%{_mandir}/man1/i3-sensible-terminal.1*
%{_datadir}/xsessions/i3-with-shmlog.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}/ipc.h
