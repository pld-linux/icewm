Summary:	IceWM X11 Window Manager
Summary(pl):	IceWM - Mened�er okienek X11
Name:		icewm
Version:	1.0.0
Release:	1
Copyright:	GPL
Group:		X11/Window Managers
Group(pl):	X11/Zarz�dcy Okien
Source:		http://www.kiss.uni-lj.si/~k4fr0235/icewm/devel/%{name}-%{version}.src.tar.gz
URL:		http://berta.fri.uni-lj.si/~markom/icewm/
BuildRoot:	/tmp/%{name}-%{version}-root

%define	_prefix	/usr/X11R6

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
./configure \
	--prefix=/usr/X11R6 \
	--sysconfdir=/etc/X11/icewm \
	--with-shape \
	--with-sm \
	--with-imlib \
	--with-gnome \
	--with-i18n

make PREFIX=/usr/X11R6 optimize="$RPM_OPT_FLAGS"

%install
make install \
	PREFIX=$RPM_BUILD_ROOT/usr/X11R6 \
	BINDIR=$RPM_BUILD_ROOT/usr/X11R6/bin \
	LIBDIR=$RPM_BUILD_ROOT/usr/X11R6/lib/X11/icewm \
	ETCDIR=$RPM_BUILD_ROOT/etc/X11/icewm

gzip -9nf README CHANGES TODO BUGS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,CHANGES,TODO,BUGS}.gz doc/*.html
/usr/X11R6/lib/X11/icewm
%attr(755,root,root) /usr/X11R6/bin/*
