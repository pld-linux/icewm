#
# TODO:
# - make a PLD-theme - default :]
# - bigger menu-file
#
Summary:	IceWM X11 Window Manager
Summary(pl):	IceWM - Mened¿er okienek X11
Name:		icewm
Version:	1.0.9
Release:	5
License:	LGPL
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fenêtres
Group(pl):	X11/Zarz±dcy Okien
Source0:	ftp://download.sourceforge.net/pub/sourceforge/icewm/%{name}-%{version}-2.tar.bz2
Source1:	IceWM.desktop
Source2:	%{name}.directory
Source3:	ftp://download.sourceforge.net/pub/sourceforge/icewm/iceicons-0.6.tar.gz
Source4:	IceWM.RunWM
Source5:	IceWM.wm_style
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-menu.patch
URL:		http://www.icewm.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	esound-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	imlib-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/icewm
%define		_wmstyledir	/etc/sysconfig/wmstyle
%define		_wmpropsdir	%{_datadir}/wm-properties

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

%package themes-base
Summary:	Pack of themes for icewm
Summary(pl):	Zestaw tematów dla icewm
Group:		Themes
Group(de):	Themen
Group(pl):	Motywy
Requires:	icewm

%description themes-base
Standard pack of themes delivered with icewm. All of them made by
Marko Macek: gtk2, metal2, motif, nice, warp3, warp4, win95

%description themes-base -l pl
Standardowy zestaw tematów dla IceWM'a, dostarczany wraz nim.
Wszystkie stworzone przez Marko Macek: gtk2, metal2, motif, nice,
warp3, warp4, win95

%prep -q
%setup -q
%patch0 -p1
%patch1 -p1

cd lib/icons
tar -xvf %{SOURCE3}
cd ../../

%build
export LDFLAGS
%configure \
	--prefix=%{_prefix} \
	--with-cfgdir=%{_sysconfdir} \
	--with-docdir=%{_docdir} \
	--with-gnome \
	--with-gnome-menus \
	--enable-i18n \
	--with-imlib \
	--with-shape \
	--with-sm \
	--enable-antialiasing \
	--enable-gradients \
	--enable-guievents \
	--enable-nls \
	--enable-xfreetype 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_wmstyledir},%{_applnkdir}/Settings/IceWM,%{_wmpropsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Settings/IceWM/.directory
install lib/keys $RPM_BUILD_ROOT%{_sysconfdir}/keys
install lib/menu $RPM_BUILD_ROOT%{_sysconfdir}/menu
install lib/preferences $RPM_BUILD_ROOT%{_sysconfdir}/preferences
install lib/toolbar $RPM_BUILD_ROOT%{_sysconfdir}/toolbar
install lib/winoptions $RPM_BUILD_ROOT%{_sysconfdir}/winoptions
install %{SOURCE4} $RPM_BUILD_ROOT%{_wmstyledir}/IceWM.sh
install %{SOURCE5} $RPM_BUILD_ROOT%{_wmstyledir}/IceWM.names


#mv -f %{_libdir}/X11/icewm/icons/* %{_pixmapsdir}/icewm/
#rm -rf %{_libdir}/X11/icewm/icons
#ln -s %{_pixmapsdir}/icewm $RPM_BUILD_ROOT%{_libdir}/X11/icewm/icons

gzip -9nf BUGS CHANGES FAQ PLATFORMS README TODO icewm.lsm

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz doc/*.*ml
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/*
%dir %{_applnkdir}/Settings/IceWM
%{_applnkdir}/Settings/IceWM/.directory
%{_wmpropsdir}/*
%dir %{_libdir}/X11/icewm
%{_libdir}/X11/icewm/icons
%{_libdir}/X11/icewm/ledclock
%{_libdir}/X11/icewm/mailbox
%{_libdir}/X11/icewm/taskbar
%dir %{_libdir}/X11/icewm/themes
%{_libdir}/X11/icewm/themes/Infadel2
%attr(755,root,root) %{_wmstyledir}/IceWM.sh
%attr(644,root,root) %{_wmstyledir}/IceWM.names

%files themes-base
%defattr(644,root,root,755)
%{_libdir}/X11/icewm/themes/gtk2
%{_libdir}/X11/icewm/themes/metal2
%{_libdir}/X11/icewm/themes/motif
%{_libdir}/X11/icewm/themes/nice
%{_libdir}/X11/icewm/themes/warp3
%{_libdir}/X11/icewm/themes/warp4
%{_libdir}/X11/icewm/themes/win95
