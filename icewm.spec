#
# Conditional build:
# _with_gradients	- enable gradients (implies _with_antialiasing)
# _with_antialiasing	- enable antialiasing (implies _with_freetype)
# _without_freetype	- disable xfreetype support
# _without_guievents	- disable guievents
# _without_gnome	- disable GNOME support
# _without_imlib	- disable imlib support
#
# TODO:
# - make a PLD-theme - default :]
# - bigger menu-file
#

Summary:	IceWM X11 Window Manager
Summary(es):	Administrador de Ventanas X11
Summary(pl):	IceWM - zarz╠dca okienek X11
Summary(pt_BR):	Gerenciador de Janelas X11
Summary(ru):	Оконный менеджер для X11
Summary(uk):	В╕конний менеджер для X11
Name:		icewm
Version:	1.2.3
Release:	1
Epoch:		1
License:	LGPL
Group:		X11/Window Managers
Source0:	http://cesnet.dl.sourceforge.net/sourceforge/icewm/%{name}-%{version}.tar.gz
Source1:	IceWM.desktop
Source2:	%{name}.directory
Source3:	http://cesnet.dl.sourceforge.net/sourceforge/icewm/iceicons-0.6.tar.gz
Source4:	IceWM.RunWM
Source5:	IceWM.wm_style
Source6:	%{name}-menu
Source7:	http://cesnet.dl.sourceforge.net/sourceforge/icewm/netscapeicons-0.2.tar.gz
Patch0:		%{name}-menu.patch
Patch1:		%{name}-compile-fixes.patch
URL:		http://www.icewm.org/
BuildRequires:	XFree86-devel
%{!?_without_guievents:BuildRequires:	esound-devel}
%{!?_without_gnome:BuildRequires:	gnome-libs-devel}
%{!?_without_imlib:BuildRequires:	imlib-devel}
BuildRequires:	libstdc++-devel
Requires(pre):	fileutils
Requires(pre):	sh-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_wmstyledir	/etc/sysconfig/wmstyle
%define		_wmpropsdir	%{_datadir}/wm-properties

%description
Window Manager for X Window System. Can emulate the look of
Windows'95, OS/2 Warp 3,4, Motif. Tries to take the best features of
the above systems. Features multiple workspaces, opaque move/resize,
task bar, window list, mailbox status, digital clock. Fast and small.

%description -l es
Administrador de Ventanas para el X Window. Puede emular la apariencia
del Windows'95, OS/2 Warp 3 y 4 y el Motif. Intenta usar las mejores
caracterМsticas de los sistemas citados. CaracterМsticas: varios
ambientes de trabajo, movimiento/ redimensionamiento opaco, barra de
tareas, lista de ventanas, estado de la caja de entrada del correo y
reloj digital. RАpido y pequeЯo.

%description -l pl
Zarz╠dca okienek pod X11. Mo©e emulowaФ wygl╠d Windows'95, OS/2 Warp
3, 4, MWM. Zarz╠dca ten prСbuje przej╠Ф z powy©szych ╤rodowisk ich
najlepsze cechy, takie jak: wiele jednocze╤nie obecnych przestrzeni
roboczych, paski narzЙdziowe, status skrzynki z poczt╠, cyfrowy zegar.
Jest przy tym maЁy i szybki.

%description -l pt_BR
Gerenciador de Janelas para o X Window. Pode emular a aparЙncia do
Windows'95, OS/2 Warp 3 e 4 e o Motif. Tenta usar as melhores
caracterМsticas dos sistemas citados. CaracterМsticas: vАrios
ambientes de trabalho, movimentaГЦo/ redimensionamento opaco, barra de
tarefas, lista de janelas, status da caixa de entrada do correio e
relСgio digital. и rАpido e pequeno.

%description -l ru
Оконный менеджер для X Window System. Может эмулировать внешний вид
Windows'95, OS/2 Warp 3,4, Motif. Старается взять лучшее из упомянутых
систем. Поддерживает несколько рабочих поверхностей, непрозрачное
перемещение окон, полоску заданий, список окон, статус почтового
ящика, цифровые часы. Быстрый и компактный.

%description -l uk
В╕конний менеджер для X Window System. Може емулювати зовн╕шн╕й вигляд
Windows'95, OS/2 Warp 3,4, Motif. Намага╓ться взяти найкраще ╕з
згаданих систем. П╕дтриму╓ к╕лька робочих площин, непрозоре
перем╕щення в╕кон, смужку завдань, список в╕кон, стан поштово╖
скриньки, цифровий годинник. Швидкий та компактний.

%package themes-base
Summary:	Pack of themes for IceWM
Summary(pl):	Zestaw tematСw dla IceWM-a
Group:		Themes
Requires:	icewm

%description themes-base
Standard pack of themes delivered with IceWM. All of them made by
Marko Macek: gtk2, metal2, motif, nice, nice2, warp3, warp4, win95.

%description themes-base -l pl
Standardowy zestaw tematСw dla IceWM-a, dostarczany wraz z nim.
Wszystkie stworzone przez Marko Macka: gtk2, metal2, motif, nice,
nice2, warp3, warp4, win95.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

cd lib/icons
tar -xzf %{SOURCE3}
tar -xzf %{SOURCE7}
cd ../..

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%configure \
	%{?_with_gradients:--enable-gradients} \
	%{?_with_antialiasing:--enable-antialiasing} \
	%{!?_without_freetype:--enable-xfreetype} \
	%{!?_without_guievents:--enable-guievents} \
	%{!?_without_gnome:--with-gnome-menus} \
	%{?_without_imlib:--without-imlib} \
	--with-cfgdir=%{_sysconfdir}/X11/{name} \
	--with-docdir=%{_docdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_wmstyledir}} \
	$RPM_BUILD_ROOT{%{_applnkdir}/Settings/IceWM,%{_wmpropsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Settings/IceWM/.directory
install %{SOURCE4} $RPM_BUILD_ROOT%{_wmstyledir}/IceWM.sh
install %{SOURCE5} $RPM_BUILD_ROOT%{_wmstyledir}/IceWM.names
install %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/X11/icewm/menu
install lib/keys $RPM_BUILD_ROOT%{_sysconfdir}/X11/icewm/keys
install lib/preferences $RPM_BUILD_ROOT%{_sysconfdir}/X11/icewm/preferences
install lib/toolbar $RPM_BUILD_ROOT%{_sysconfdir}/X11/icewm/toolbar
install lib/winoptions $RPM_BUILD_ROOT%{_sysconfdir}/X11/icewm/winoptions

ln -s %{_datadir}/icewm/icons $RPM_BUILD_ROOT%{_pixmapsdir}/icewm

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%pre
test -h %{_pixmapsdir}/icewm || rm -rf %{_pixmapsdir}/icewm

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS CHANGES FAQ PLATFORMS README* TODO icewm.lsm doc/*.html
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}/X11/icewm
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/X11/icewm/*
%{_pixmapsdir}/icewm
%dir %{_datadir}/icewm
%{_datadir}/icewm/icons
%{_datadir}/icewm/ledclock
%{_datadir}/icewm/mailbox
%{_datadir}/icewm/taskbar
%dir %{_datadir}/icewm/themes
%{_datadir}/icewm/themes/Infadel2
%dir %{_applnkdir}/Settings/IceWM
%{_applnkdir}/Settings/IceWM/.directory
%{_wmpropsdir}/*
%attr(755,root,root) %{_wmstyledir}/IceWM.sh
%attr(644,root,root) %{_wmstyledir}/IceWM.names

%files themes-base
%defattr(644,root,root,755)
%{_datadir}/icewm/themes/gtk2
%{_datadir}/icewm/themes/metal2
%{_datadir}/icewm/themes/motif
%{_datadir}/icewm/themes/nice
%{_datadir}/icewm/themes/nice2
%{_datadir}/icewm/themes/warp3
%{_datadir}/icewm/themes/warp4
%{_datadir}/icewm/themes/win95
