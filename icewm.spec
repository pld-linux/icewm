Summary:	IceWM X11 Window Manager
Summary(pl):	IceWM - Mened¿er okienek X11
Name:		icewm
Version:	1.0.8
Release:	1
License:	LGPL
Group:		X11/Window Managers
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fenêtres
Group(pl):	X11/Zarz±dcy Okien
Source0:	ftp://download.sourceforge.net/pub/sourceforge/icewm/%{name}-%{version}-4.tar.bz2
Source1:	IceWM.desktop
Source2:	%{name}.directory
Patch0:		icewm-DESTDIR.patch
Patch1:		%{name}-time.patch
URL:		http://www.icewm.org/
BuildRequires:	autoconf
BuildRequires:	imlib-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRequires:	XFree86-devel
BuildRequires:	zlib-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc
%define		_wmpropsdir	%{_datadir}/wm-properties
%define		_localesdir	%{_prefix}/share/locale

%description
Window Manager for X Window System. Can emulate the look of
Windows'95, OS/2 Warp 3,4, Motif. Tries to take the best features of
the above systems. Features multiple workspaces, opaque move/resize,
task bar, window list, mailbox status, digital clock. Fast and small.

%description -l pl
Mened¿er okienek pod X11. Mo¿e emulowaæ wygl±d Windows'95, OS/2 Warp
3,4, MWM. Mened¿er ten próbuje wybraæ najlepsze cechy dostêpne w
powy¿szych ¶rodowiskach, jak: wiele jednocze¶nie obecnych przestrzeni
roboczych, paski narzêdziowe, status skrzynki z poczt±, cyfrowy zegar.
Jest przy tym ma³y i szybki.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoconf
%configure \
	--with-shape \
	--with-sm \
	--with-imlib \
	--with-gnome \
	--with-gnome-menus \
	--with-i18n \
	--enable-nls \
	--enable-guievents \
	--with-imlib 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT%{_wmpropsdir}
%{__install} -d $RPM_BUILD_ROOT%{_prefix}/share/applnk/Settings/IceWM

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__install} %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}
%{__install} %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Settings/IceWM/.directory
%{__install} lib/keys $RPM_BUILD_ROOT%{_sysconfdir}/X11/icewm/keys
%{__install} lib/menu $RPM_BUILD_ROOT%{_sysconfdir}/X11/icewm/menu
%{__install} lib/toolbar $RPM_BUILD_ROOT%{_sysconfdir}/X11/icewm/toolbar
%{__install} lib/preferences $RPM_BUILD_ROOT%{_sysconfdir}/X11/icewm/preferences
%{__install} lib/winoptions $RPM_BUILD_ROOT%{_sysconfdir}/X11/icewm/winoptions

gzip -9nf README CHANGES TODO BUGS COPYING FAQ INSTALL icewm.lsm PLATFORMS VERSION

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%doc *.gz doc/*.*ml
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root)
%dir %{_applnkdir}/Settings/IceWM
%{_applnkdir}/Settings/IceWM/.directory
%{_wmpropsdir}/*
#%{_localesdir}/*
%dir %{_libdir}/X11/icewm
%{_libdir}/X11/icewm/*
