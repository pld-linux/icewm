# TODO:
# - make a PLD-theme - default:]
#
# Conditional build:
%bcond_without	freetype	# xfreetype support (implies no antialiasing)
%bcond_without	alsa		# ALSA sound for GUI events
%bcond_without	ao		# AO sound for GUI events

Summary:	IceWM X11 Window Manager
Summary(de.UTF-8):	IceWM ist ein Window Manager für X
Summary(es.UTF-8):	Administrador de Ventanas X11
Summary(pl.UTF-8):	IceWM - zarządca okienek X11
Summary(pt_BR.UTF-8):	Gerenciador de Janelas X11
Summary(ru.UTF-8):	Оконный менеджер для X11
Summary(uk.UTF-8):	Віконний менеджер для X11
Name:		icewm
Version:	3.3.2
Release:	1
Epoch:		2
License:	LGPL v2
Group:		X11/Window Managers
#Source0Download: https://github.com/ice-wm/icewm/releases
Source0:	https://github.com/ice-wm/icewm/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	505150fa7b544c86c56f1016fcc220d7
Source1:	%{name}-startup.sh
Patch0:		desktop-files.patch
URL:		https://ice-wm.org/
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	cmake
BuildRequires:	discount
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	fribidi-devel >= 0.10.4
BuildRequires:	gettext >= 0.19.6
BuildRequires:	gettext-tools >= 0.19.6
BuildRequires:	git-core
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	imlib2-devel
%{?with_ao:BuildRequires:	libao-devel}
BuildRequires:	librsvg-devel
%{?with_alsa:BuildRequires:	libsndfile-devel}
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2.4.2
BuildRequires:	pkgconfig
BuildRequires:	ruby-asciidoctor
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
%{?with_freetype:BuildRequires:	xorg-lib-libXft-devel >= 2.1}
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXrender-devel
Requires(pre):	/bin/rm
Requires(pre):	/usr/bin/test
Requires:	shared-mime-info
Requires:	xinitrc-ng
Requires:	xorg-app-xrandr
Conflicts:	filesystem < 3.0-20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires:	%{name} = %{epoch}:%{version}
BuildArch:	noarch

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

%build
%cmake -B build \
	-DCONFIG_LIBRSVG=ON \
	-DCFGDIR=%{_sysconfdir}/X11/%{name} \
	-DDOCDIR=%{_docdir}/%{name}-%{version} \
	%{?with_alsa:-DENABLE_ALSA=ON} \
	%{?with_ao:-DENABLE_AO=ON} \
	%{!?with_freetype:-DCONFIG_XFREETYPE=OFF -DCONFIG_COREFONTS=ON}

cd build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/%{name}

cd build
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd ..

cd build/man
%{__ln} -s icewm.1.html icewm.html
cd -

%{__sed} -e 's|^# IconPath=.*|IconPath="%{_pixmapsdir}:%{_iconsdir}:"|' -i $RPM_BUILD_ROOT%{_datadir}/icewm/preferences

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/icewm/startup
cp -p $RPM_BUILD_ROOT%{_datadir}/icewm/keys $RPM_BUILD_ROOT%{_sysconfdir}/X11/%{name}/keys
cp -p $RPM_BUILD_ROOT%{_datadir}/icewm/menu $RPM_BUILD_ROOT%{_sysconfdir}/X11/%{name}/menu
cp -p $RPM_BUILD_ROOT%{_datadir}/icewm/preferences $RPM_BUILD_ROOT%{_sysconfdir}/X11/%{name}/preferences
cp -p $RPM_BUILD_ROOT%{_datadir}/icewm/programs $RPM_BUILD_ROOT%{_sysconfdir}/X11/%{name}/programs
cp -p $RPM_BUILD_ROOT%{_datadir}/icewm/startup $RPM_BUILD_ROOT%{_sysconfdir}/X11/%{name}/startup
cp -p $RPM_BUILD_ROOT%{_datadir}/icewm/toolbar $RPM_BUILD_ROOT%{_sysconfdir}/X11/%{name}/toolbar
cp -p $RPM_BUILD_ROOT%{_datadir}/icewm/winoptions $RPM_BUILD_ROOT%{_sysconfdir}/X11/%{name}/winoptions
:> $RPM_BUILD_ROOT%{_sysconfdir}/X11/%{name}/restart

# old themes, no longer installed
cp -pr lib/themes/{gtk2,nice,nice2,warp3,warp4,yellowmotif} $RPM_BUILD_ROOT%{_datadir}/icewm/themes

# duplicate locale
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/no
# unsupported locale
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS CHANGES ChangeLog NEWS PLATFORMS README.md THANKS TODO build/man/*.html
%attr(755,root,root) %{_bindir}/icehelp
%attr(755,root,root) %{_bindir}/icesh
%attr(755,root,root) %{_bindir}/icesound
%attr(755,root,root) %{_bindir}/icewm
%attr(755,root,root) %{_bindir}/icewm-menu-fdo
%attr(755,root,root) %{_bindir}/icewm-session
%attr(755,root,root) %{_bindir}/icewm-set-gnomewm
%attr(755,root,root) %{_bindir}/icewmbg
%attr(755,root,root) %{_bindir}/icewmhint
%attr(755,root,root) %{_bindir}/icewm-menu-xrandr
%{_mandir}/man1/icehelp.1*
%{_mandir}/man1/icesh.1*
%{_mandir}/man1/icesound.1*
%{_mandir}/man1/icewm-menu-fdo.1*
%{_mandir}/man1/icewm-menu-xrandr.1*
%{_mandir}/man1/icewm-session.1*
%{_mandir}/man1/icewm-set-gnomewm.1*
%{_mandir}/man1/icewmbg.1*
%{_mandir}/man1/icewmhint.1*
%{_mandir}/man5/icewm-env.5*
%{_mandir}/man5/icewm-focus_mode.5*
%{_mandir}/man5/icewm-keys.5*
%{_mandir}/man5/icewm-menu.5*
%{_mandir}/man5/icewm-preferences.5*
%{_mandir}/man5/icewm-prefoverride.5*
%{_mandir}/man5/icewm-programs.5*
%{_mandir}/man5/icewm-shutdown.5*
%{_mandir}/man5/icewm-startup.5*
%{_mandir}/man5/icewm-theme.5*
%{_mandir}/man5/icewm-toolbar.5*
%{_mandir}/man5/icewm-winoptions.5*
%dir %{_sysconfdir}/X11/%{name}
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/X11/%{name}/keys
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/X11/%{name}/menu
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/X11/%{name}/preferences
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/X11/%{name}/programs
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/X11/%{name}/toolbar
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/X11/%{name}/winoptions
%config(noreplace,missingok) %verify(not md5 mtime size) %attr(755,root,root) %{_sysconfdir}/X11/%{name}/restart
%config(noreplace,missingok) %verify(not md5 mtime size) %attr(755,root,root) %{_sysconfdir}/X11/%{name}/startup
%dir %{_datadir}/icewm
%{_datadir}/icewm/IceWM.jpg
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
