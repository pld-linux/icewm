Summary:	IceWM X11 Window Manager
Summary(pl):	IceWM - Mened�er okienek X11
Name:		icewm
Version:	1.0.0
Release:	1
License:	GPL
Group:		X11/Window Managers
Group(pl):	X11/Zarz�dcy Okien
Source:		http://download.sourceforge.net/icewm/%{name}-%{version}.src.tar.gz
URL:		http://icewm.sourceforge.net/
BuildRequires:	imlib-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRequires:	XFree86-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/icewm

%description
Window Manager for X Window System. Can emulate the look of Windows'95,
OS/2 Warp 3,4, Motif. Tries to take the best features of the above systems.
Features multiple workspaces, opaque move/resize, task bar, window list,
mailbox status, digital clock. Fast and small.

%description -l pl
Mened�er okienek pod X11. Mo�e emulowa� wygl�d Windows'95, OS/2 Warp 3,4,
MWM. Mened�er ten pr�bije wybra� najjleprze cechy dost�pne w powy�szych
�rodowiskach jak wiele jednocze�nie obecnych przestrzeni roboczych, paski
narz�dziowe, status skrzynki z poczt�, cyfrowy zegar. Jest tak�e ma�y i
szybki przy tym.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure \
	--with-shape \
	--with-sm \
	--with-imlib \
	--with-gnome \
	--with-i18n

make PREFIX=/usr/X11R6 optimize="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

make install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir}/X11/icewm \
	ETCDIR=$RPM_BUILD_ROOT%{_sysconfdir}

gzip -9nf README CHANGES TODO BUGS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,CHANGES,TODO,BUGS}.gz doc/*.html
%dir %{_sysconfdir}
%{_libdir}/X11/icewm
%attr(755,root,root) %{_bindir}/*
