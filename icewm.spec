Summary:	IceWM X11 Window Manager
Summary(pl):	IceWM - Mened¿er okienek X11
Name:		icewm
Version:	1.0.7
Release:	1
License:	GPL
Group:		X11/Window Managers
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fenêtres
Group(pl):	X11/Zarz±dcy Okien
Source0:	ftp://download.sourceforge.net/pub/sourceforge/icewm/%{name}-%{version}-7.tar.bz2
Source1:	IceWM.desktop
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
%define		_sysconfdir	/etc/X11/icewm

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
install -d $RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties

gzip -9nf README CHANGES TODO BUGS

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {README,CHANGES,TODO,BUGS}.gz doc/*.html
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}
%{_libdir}/X11/icewm
%{_datadir}/gnome/wm-properties/*
