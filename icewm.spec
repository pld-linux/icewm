#
# TODO:
# - make a PLD-theme - default :]
# - bigger menu-file
#
Summary:	IceWM X11 Window Manager
Summary(pl):	IceWM - mened¿er okienek X11
Name:		icewm
Version:	1.0.9
Release:	7
License:	LGPL
Group:		X11/Window Managers
Source0:	ftp://download.sourceforge.net/pub/sourceforge/icewm/%{name}-%{version}-2.tar.bz2
Source1:	IceWM.desktop
Source2:	%{name}.directory
Source3:	ftp://download.sourceforge.net/pub/sourceforge/icewm/iceicons-0.6.tar.gz
Source4:	IceWM.RunWM
Source5:	IceWM.wm_style
Source6:	%{name}-menu
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.icewm.org/
BuildRequires:	XFree86-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	imlib-devel
BuildRequires:	libstdc++-devel
Requires(pre):	fileutils
Requires(pre):	sh-utils
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
Summary:	Pack of themes for IceWM
Summary(pl):	Zestaw tematów dla IceWM
Group:		Themes
Requires:	icewm

%description themes-base
Standard pack of themes delivered with IceWM. All of them made by
Marko Macek: gtk2, metal2, motif, nice, warp3, warp4, win95.

%description themes-base -l pl
Standardowy zestaw tematów dla IceWMa, dostarczany wraz z nim.
Wszystkie stworzone przez Marko Macek: gtk2, metal2, motif, nice,
warp3, warp4, win95.

%prep -q
%setup -q
%patch0 -p1

cd lib/icons
tar -zxf %{SOURCE3}
cd ../..

%build
export LDFLAGS
%configure \
	--prefix=%{_prefix} \
	--with-cfgdir=%{_sysconfdir} \
	--with-docdir=%{_docdir} \
	--enable-i18n \
	--enable-guievents \
	--enable-xfreetype \
	--with-gnome-menus \
	--with-imlib
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_wmstyledir},%{_pixmapsdir}/icewm} \
	$RPM_BUILD_ROOT{%{_applnkdir}/Settings/IceWM,%{_wmpropsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Settings/IceWM/.directory
install %{SOURCE4} $RPM_BUILD_ROOT%{_wmstyledir}/IceWM.sh
install %{SOURCE5} $RPM_BUILD_ROOT%{_wmstyledir}/IceWM.names
install %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/menu
install lib/keys $RPM_BUILD_ROOT%{_sysconfdir}/keys
install lib/preferences $RPM_BUILD_ROOT%{_sysconfdir}/preferences
install lib/toolbar $RPM_BUILD_ROOT%{_sysconfdir}/toolbar
install lib/winoptions $RPM_BUILD_ROOT%{_sysconfdir}/winoptions

mv -f $RPM_BUILD_ROOT%{_libdir}/X11/icewm/icons/* $RPM_BUILD_ROOT%{_pixmapsdir}/icewm
rm -rf $RPM_BUILD_ROOT%{_libdir}/X11/icewm/icons
ln -s %{_pixmapsdir}/icewm $RPM_BUILD_ROOT%{_libdir}/X11/icewm/icons

gzip -9nf BUGS CHANGES FAQ PLATFORMS README* TODO icewm.lsm

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%pre
test -h %{_libdir}/X11/icewm/icons || rm -rf %{_libdir}/X11/icewm/icons

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz doc/*.*ml
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/*
%dir %{_applnkdir}/Settings/IceWM
%{_applnkdir}/Settings/IceWM/.directory
%{_wmpropsdir}/*
%{_pixmapsdir}/icewm
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
