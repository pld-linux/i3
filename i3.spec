Summary:	improved tiling wm
Name:		i3
Version:	4.2
Release:	0.1
License:	BSD
Group:		X11/Window Managers
Source0:	http://i3wm.org/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	11b7e5ecdd837341978c72341cb890c6
URL:		http://i3wm.org/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libev-devel
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel
BuildRequires:	xcb-util-devel
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	xcb-util-wm-devel
BuildRequires:	xorg-lib-libXcursor-devel
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
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc LICENCE
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/config
%config %{_sysconfdir}/%{name}/config.keycodes
%config %{_sysconfdir}/%{name}/welcome
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/%{name}bar
%attr(755,root,root) %{_bindir}/%{name}-*
%{_datadir}/xsessions/%{name}.desktop
%{_desktopdir}/%{name}.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}/ipc.h
