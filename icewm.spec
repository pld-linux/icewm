#
# TODO:
# - make a PLD-theme - default :]
# - bigger menu-file
#
Summary:	IceWM X11 Window Manager
Summary(pl):	IceWM - Mened�er okienek X11
Name:		icewm
Version:	1.0.8
Release:	4
License:	LGPL
Group:		X11/Window Managers
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fen�tres
Group(pl):	X11/Zarz�dcy Okien
Source0:	ftp://download.sourceforge.net/pub/sourceforge/icewm/%{name}-%{version}-6.tar.bz2
Source1:	IceWM.desktop
Source2:	%{name}.directory
Patch0:		icewm-DESTDIR.patch
Patch1:		%{name}-time.patch
Patch2:		%{name}-menu.patch
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
%define		_sysconfdir	/etc/X11/icewm/
%define		_wmpropsdir	%{_datadir}/wm-properties

%description
Window Manager for X Window System. Can emulate the look of
Windows'95, OS/2 Warp 3,4, Motif. Tries to take the best features of
the above systems. Features multiple workspaces, opaque move/resize,
task bar, window list, mailbox status, digital clock. Fast and small.

%description -l pl
Mened�er okienek pod X11. Mo�e emulowa� wygl�d Windows'95, OS/2 Warp
3,4, MWM. Mened�er ten pr�buje wybra� najlepsze cechy dost�pne w
powy�szych �rodowiskach, jak: wiele jednocze�nie obecnych przestrzeni
roboczych, paski narz�dziowe, status skrzynki z poczt�, cyfrowy zegar.
Jest przy tym ma�y i szybki.

%package -n %{name}-themes-base
Summary:        Pack of themes for icewm
Summary(pl):    Zestaw temat�w dla icewm
Group:		Themes
Group(de):	Themen
Group(pl):	Motywy
Requires:	icewm

%description -n %{name}-themes-base
Standard pack of themes delivered with icewm.
All of them made by Marko Macek:
gtk2, metal2, motif, nice, warp3, warp4, win95

%description -n %{name}-themes-base -l pl
Standardowy zestaw temat�w dla IceWM'a, dostarczany wraz nim.
Wszystkie stwarzone przez Marko Macek:
gtk2, metal2, motif, nice, warp3, warp4, win95

%prep -q
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
autoconf
%configure \
	--with-shape \
	--with-docdir=/usr/share/doc \
	--with-cfgdir=%{_sysconfdir} \
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
%{__install} -d $RPM_BUILD_ROOT{%{_wmpropsdir},%{_applnkdir}/Settings/IceWM}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__install} %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}
%{__install} %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Settings/IceWM/.directory
%{__install} lib/keys $RPM_BUILD_ROOT%{_sysconfdir}/keys
%{__install} lib/menu $RPM_BUILD_ROOT%{_sysconfdir}/menu
%{__install} lib/toolbar $RPM_BUILD_ROOT%{_sysconfdir}toolbar
%{__install} lib/preferences $RPM_BUILD_ROOT%{_sysconfdir}/preferences
%{__install} lib/winoptions $RPM_BUILD_ROOT%{_sysconfdir}/winoptions

gzip -9nf README CHANGES TODO BUGS FAQ icewm.lsm PLATFORMS

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
%dir %{_libdir}/X11/icewm
%{_libdir}/X11/icewm/icons/*
%{_libdir}/X11/icewm/ledclock/*
%{_libdir}/X11/icewm/mailbox/*
%{_libdir}/X11/icewm/taskbar/*
%{_libdir}/X11/icewm/themes/Infadel2/*

%files -n %{name}-themes-base
%{_libdir}/X11/icewm/themes/gtk2/*
%{_libdir}/X11/icewm/themes/metal2/*
%{_libdir}/X11/icewm/themes/motif/*
%{_libdir}/X11/icewm/themes/nice/*
%{_libdir}/X11/icewm/themes/warp3/*
%{_libdir}/X11/icewm/themes/warp4/*
%{_libdir}/X11/icewm/themes/win95/*
