Summary:	improved tiling wm
Name:		i3
Version:	4.24
Release:	1
License:	BSD
Group:		X11/Window Managers
Source0:	https://i3wm.org/downloads/%{name}-%{version}.tar.xz
# Source0-md5:	239a821e091e383fb0e3981eac6f8ae9
Patch0:		%{name}-remember_ws_output.patch
URL:		http://i3wm.org/
BuildRequires:	asciidoc
BuildRequires:	bison
BuildRequires:	cairo-devel >= 1.14.4
BuildRequires:	flex
BuildRequires:	glib2
BuildRequires:	libev-devel
BuildRequires:	libxcb-devel
BuildRequires:	meson >= 0.47.0
BuildRequires:	ninja
BuildRequires:	pango-devel
BuildRequires:	pcre2-8-devel >= 10
BuildRequires:	perl-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	startup-notification-devel
BuildRequires:	tar >= 1:1.22
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
BuildRequires:	xz
BuildRequires:	yajl-devel
Requires:	cairo >= 1.14.4
Requires:	glib2
Requires:	pcre2-8 >= 10
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
%patch -P0 -p1
%{__sed} -i -e '1s,/usr/bin/env perl,%{__perl},' i3-save-tree i3-migrate-config-to-v4 i3-dmenu-desktop

%build
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT
%meson_install

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
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/ipc.h
