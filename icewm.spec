Summary:	IceWM X11 Window Manager
Summary(pl):	IceWM - Mened¿er okienek X11
Name:		icewm
Version:	0.9.37
Release:	1
Copyright:	GPL
Group:		X11/Window Managers
Group(pl):	X11/Zarz±dcy Okien
Source:		http://www.kiss.uni-lj.si/~k4fr0235/icewm/devel/%{name}-%{version}.src.tar.gz
URL:		http://berta.fri.uni-lj.si/~markom/icewm/
BuildRoot:	/tmp/%{name}-%{version}

%description
Window Manager for X Window System. Can emulate the look of Windows'95,
OS/2 Warp 3,4, Motif. Tries to take the best features of the above systems.
Features multiple workspaces, opaque move/resize, task bar, window list,
mailbox status, digital clock. Fast and small.

%description -l pl
Mened¿er okienek pod X11. Mo¿e emulowaæ wygl±d Windows'95, OS/2 Warp 3,4,
MWM. Mened¿er ten próbije wybraæ najjleprze cechy dostêpne w powy¿szych
¶rodowiskach jak wiele jednocze¶nie obecnych przestrzeni roboczych, paski
narzêdziowe, status skrzynki z poczt±, cyfrowy zegar. Jest tak¿e ma³y i
szybki przy tym.

%prep
%setup -q

%build
./config \
	--with-shape \
	--with-sm \
	--with-imlib \
	--with-gnome \
#	--with-i18n

make PREFIX=/usr/X11R6 optimize="$RPM_OPT_FLAGS"

%install
make install \
	PREFIX=$RPM_BUILD_ROOT/usr/X11R6 \
	ETCDIR=$RPM_BUILD_ROOT/etc/X11/icewm

gzip -9nf README CHANGES TODO BUGS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,CHANGES,TODO,BUGS}.gz doc/*.html
/usr/X11R6/lib/X11/icewm
%attr(755,root,root) /usr/X11R6/bin/*

%changelog
* Fri Mar 19 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.9.34-1]
- added gzipping some %doc,
- added Group(pl).

* Fri Nov 20 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.9.17-1]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added using $RPM_OPT_FLAGS during compile,
- added pl translation,
- added %attr and %defattr macros in %files (allows build package from
  non-root account).
