# TODO:
# - make a PLD-theme - default :]
#
# Conditional build:
%bcond_without	gradients	# gradients (requires antialiasing which requires freetype)
%bcond_without	freetype	# xfreetype support (implies no antialiasing)
%bcond_without	guievents	# GUI events
%bcond_without	alsa		# ALSA sound for GUI events
%bcond_with	esd		# EsounD sound for GUI events
%bcond_without	yiff		# YIFF sound for GUI events
%bcond_with	gnome2		# support for GNOME2 menus and wm-properties

%if %{without guievents}
%undefine	with_alsa
%undefine	with_esd
%undefine	with_yiff
%endif
Summary:	IceWM X11 Window Manager
Summary(de.UTF-8):	IceWM ist ein Window Manager für X
Summary(es.UTF-8):	Administrador de Ventanas X11
Summary(pl.UTF-8):	IceWM - zarządca okienek X11
Summary(pt_BR.UTF-8):	Gerenciador de Janelas X11
Summary(ru.UTF-8):	Оконный менеджер для X11
Summary(uk.UTF-8):	Віконний менеджер для X11
Name:		icewm
Version:	1.4.2
%define	iceicons_ver		0.6
Release:	1
Epoch:		2
License:	LGPL v2
Group:		X11/Window Managers
#Source0Download: https://github.com/ice-wm/icewm/releases
Source0:	https://github.com/ice-wm/icewm/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	db9900056366adc163b2e501a5247bbc
Source1:	IceWM.desktop
Source3:	http://downloads.sourceforge.net/icewm/iceicons-%{iceicons_ver}.tar.gz
# Source3-md5:	53ed111a3c4d1e609bd1604ddccd4701
Source4:	icewm-startup.sh
Patch0:		%{name}-build-fixes.patch
URL:		https://ice-wm.org/
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	asciidoc
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.13.4
%{?with_esd:BuildRequires:	esound-devel}
BuildRequires:	fontconfig-devel
BuildRequires:	fribidi-devel >= 0.10.4
BuildRequires:	gdk-pixbuf2-xlib-devel >= 2.0
BuildRequires:	gettext-tools >= 0.19.6
BuildRequires:	glib2-devel >= 2.0
%{?with_gnome2:BuildRequires:	gnome-desktop2-devel >= 2.0}
%{?with_gnome2:BuildRequires:	gnome-vfs2-devel >= 2.0}
%{?with_gnome2:BuildRequires:	libgnomeui-devel >= 2.0}
%{?with_alsa:BuildRequires:	libsndfile-devel}
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2.4.2
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
%{?with_freetype:BuildRequires:	xorg-lib-libXft-devel >= 2.1}
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
%{?with_yiff:BuildRequires:	yiff-devel >= 2.14.7-3}
Requires(pre):	/bin/rm
Requires(pre):	/usr/bin/test
Requires:	shared-mime-info
Requires:	xinitrc-ng
Suggests:	vfmg >= 0.9.95
Conflicts:	filesystem < 3.0-20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wmpropsdir	/usr/share/gnome/wm-properties
%define		specflags_ia32	-fomit-frame-pointer

%description
Window Manager for X Window System. Can emulate the look of
Windows'95, OS/2 Warp 3,4, Motif. Tries to take the best features of
the above systems. Features multiple workspaces, opaque move/resize,
task bar, window list, mailbox status, digital clock. Fast and small.

%description -l es.UTF-8
Administrador de Ventanas para el X Window. Puede emular la apariencia
del Windows'95, OS/2 Warp 3 y 4 y el Motif. Intenta usar las mejores
características de los sistemas citados. Características: varios
ambientes de trabajo, movimiento/ redimensionamiento opaco, barra de
tareas, lista de ventanas, estado de la caja de entrada del correo y
reloj digital. Rápido y pequeño.

%description -l pl.UTF-8
Zarządca okienek pod X11. Może emulować wygląd Windows'95, OS/2 Warp
3, 4, MWM. Zarządca ten próbuje przejąć z powyższych środowisk ich
najlepsze cechy, takie jak: wiele jednocześnie obecnych przestrzeni
roboczych, paski narzędziowe, status skrzynki z pocztą, cyfrowy zegar.
Jest przy tym mały i szybki.

%description -l pt_BR.UTF-8
Gerenciador de Janelas para o X Window. Pode emular a aparência do
Windows'95, OS/2 Warp 3 e 4 e o Motif. Tenta usar as melhores
características dos sistemas citados. Características: vários
ambientes de trabalho, movimentação/ redimensionamento opaco, barra de
tarefas, lista de janelas, status da caixa de entrada do correio e
relógio digital. É rápido e pequeno.

%description -l ru.UTF-8
Оконный менеджер для X Window System. Может эмулировать внешний вид
Windows'95, OS/2 Warp 3,4, Motif. Старается взять лучшее из упомянутых
систем. Поддерживает несколько рабочих поверхностей, непрозрачное
перемещение окон, полоску заданий, список окон, статус почтового
ящика, цифровые часы. Быстрый и компактный.

%description -l uk.UTF-8
Віконний менеджер для X Window System. Може емулювати зовнішній вигляд
Windows'95, OS/2 Warp 3,4, Motif. Намагається взяти найкраще із
згаданих систем. Підтримує кілька робочих площин, непрозоре
переміщення вікон, смужку завдань, список вікон, стан поштової
скриньки, цифровий годинник. Швидкий та компактний.

%description -l de.UTF-8
IceWM ist ein in C++ programmierter, unter GPL stehender
Fenstermanager für das X11-Fenstersystem. Ziel von IceWM ist
Geschwindigkeit, Schlichtheit und Bedienerfreundlichkeit.

In der Standardeinstellung erinnert das Design von IceWM stark an
Microsoft Windows: Er verfügt über eine Taskleiste am unteren
Bildrand, das aktive Fenster lässt sich mit der Tastenkombination
ALT-TAB wechseln, etc.

%package themes-base
Summary:	Pack of themes for IceWM
Summary(pl.UTF-8):	Zestaw motywów dla IceWM-a
Group:		Themes
Requires:	icewm

%description themes-base
Standard pack of themes delivered with IceWM:
- CrystalBlue by BlueScorpio
- Helix by RudeSka and TigerT
- NanoBlue by lion1810
- metal2, motif, win32 by Marko Macek

This package contains also old themes, no longer installed by default
in IceWM 1.4:
- gtk2, nice, nice2, warp3, warp4 by Marko Macek
- yellowmotif by Andreas Leitgeb

%description themes-base -l pl.UTF-8
Standardowy zestaw motywów dla IceWM-a, dostarczany wraz z nim:
- CrystalBlue autorstwa BlueScorpio
- Helix autorstwa RudeSka i TigerT
- NanoBlue autorstwa lion1810
- metal2, motif, win32 autorstwa Marko Macka

Pakiet zawiera także stare motywy, nie instalowane domyślnie wraz z
IceWM-em 1.4:
- gtk2, nice, nice2, warp3, warp4 autorstwa Marko Macka
- yellowmotif autorstwa Andreasa Leitgeba

%prep
%setup -q
%patch0 -p1

tar -xzf %{SOURCE3} -C lib/icons

%{__sed} -i -e '/po\/Makefile.in/d' configure.ac

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	ASCIIDOC=/usr/bin/asciidoc \
	%{!?with_gradients:--disable-gradients} \
	%{?with_guievents:--enable-guievents --with-icesound=%{?with_alsa:ALSA,}OSS%{?with_yiff:,Y}%{?with_esd:,ESound}} \
	%{!?with_gnome2:--disable-menus-gnome2} \
	--enable-shaped-decorations \
	%{!?with_freetype:--disable-xfreetype --enable-corefonts} \
	--with-cfgdir=%{_sysconfdir}/X11/%{name} \
	--with-docdir=%{_docdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_wmpropsdir},%{_sysconfdir}/X11/%{name}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__sed} -e 's|^# IconPath=""|IconPath="%{_datadir}/pixmaps:%{_datadir}/icons"|' -i $RPM_BUILD_ROOT%{_datadir}/icewm/preferences

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/icewm

%{?with_gnome2:cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}}
cp -p %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/icewm/startup
cp -p lib/keys $RPM_BUILD_ROOT%{_sysconfdir}/X11/%{name}/keys
cp -p lib/toolbar $RPM_BUILD_ROOT%{_sysconfdir}/X11/%{name}/toolbar
cp -p lib/winoptions $RPM_BUILD_ROOT%{_sysconfdir}/X11/%{name}/winoptions
echo %{_bindir}/icewmbg > $RPM_BUILD_ROOT%{_sysconfdir}/X11/%{name}/startup
:> $RPM_BUILD_ROOT%{_sysconfdir}/X11/%{name}/restart

ln -s %{_datadir}/icewm/icons $RPM_BUILD_ROOT%{_pixmapsdir}/icewm

echo "menuprog \"Programs\" %{_datadir}/icewm/icons/folder_16x16.xpm vfmg -i -f -x -c -s icewm" > $RPM_BUILD_ROOT%{_sysconfdir}/X11/%{name}/menu

# old themes, no longer installed
cp -pr lib/themes/{gtk2,nice,nice2,warp3,warp4,yellowmotif} $RPM_BUILD_ROOT%{_datadir}/icewm/themes

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%pre
test -h %{_pixmapsdir}/icewm || rm -rf %{_pixmapsdir}/icewm

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS CHANGES ChangeLog NEWS PLATFORMS README.md THANKS TODO doc/*.html
%attr(755,root,root) %{_bindir}/icehelp
%attr(755,root,root) %{_bindir}/icesh
%if %{with guievents}
%attr(755,root,root) %{_bindir}/icesound
%endif
%attr(755,root,root) %{_bindir}/icewm
%attr(755,root,root) %{_bindir}/icewm-menu-fdo
%attr(755,root,root) %{_bindir}/icewm-session
%attr(755,root,root) %{_bindir}/icewm-set-gnomewm
%attr(755,root,root) %{_bindir}/icewmbg
%attr(755,root,root) %{_bindir}/icewmhint
%attr(755,root,root) %{_bindir}/icewmtray
%dir %{_sysconfdir}/X11/%{name}
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/X11/%{name}/keys
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/X11/%{name}/menu
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/X11/%{name}/toolbar
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/X11/%{name}/winoptions
%config(noreplace,missingok) %verify(not md5 mtime size) %attr(755,root,root) %{_sysconfdir}/X11/%{name}/restart
%config(noreplace,missingok) %verify(not md5 mtime size) %attr(755,root,root) %{_sysconfdir}/X11/%{name}/startup
%{_pixmapsdir}/icewm
%dir %{_datadir}/icewm
%{_datadir}/icewm/icons
%{_datadir}/icewm/keys
%{_datadir}/icewm/menu
%{_datadir}/icewm/ledclock
%{_datadir}/icewm/mailbox
%{_datadir}/icewm/preferences
%{_datadir}/icewm/programs
%attr(755,root,root) %{_datadir}/icewm/startup
%{_datadir}/icewm/toolbar
%{_datadir}/icewm/taskbar
%{_datadir}/icewm/winoptions
%dir %{_datadir}/icewm/themes
%{_datadir}/icewm/themes/Infadel2
%{_datadir}/icewm/themes/default
%{_datadir}/icewm/themes/icedesert
%{_datadir}/xsessions/icewm.desktop
%{_datadir}/xsessions/icewm-session.desktop
%{?with_gnome2:%{_wmpropsdir}/IceWM.desktop}
%{_mandir}/man1/icewm.1*

%files themes-base
%defattr(644,root,root,755)
%{_datadir}/icewm/themes/CrystalBlue
%{_datadir}/icewm/themes/Helix
%{_datadir}/icewm/themes/NanoBlue
%{_datadir}/icewm/themes/metal2
%{_datadir}/icewm/themes/motif
%{_datadir}/icewm/themes/win95
# old themes, no longer installed in 1.4.x
%{_datadir}/icewm/themes/gtk2
%{_datadir}/icewm/themes/nice
%{_datadir}/icewm/themes/nice2
%{_datadir}/icewm/themes/warp3
%{_datadir}/icewm/themes/warp4
%{_datadir}/icewm/themes/yellowmotif
