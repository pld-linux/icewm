#
# Conditional build:
# _with_antialiasing - enable antialiasing
# _with_gradients - enable gradients (implies _with_antialiasing)
#
# TODO:
# - make a PLD-theme - default :]
# - bigger menu-file
#
Summary:	IceWM X11 Window Manager
Summary(es):	Administrador de Ventanas X11
Summary(pl):	IceWM - mened©er okienek X11
Summary(pt_BR):	Gerenciador de Janelas X11
Summary(ru):	Оконный менеджер для X11
Summary(uk):	В╕конний менеджер для X11
Name:		icewm
Version:	1.2.0
Release:	1
Epoch:    1
License:	LGPL
Group:		X11/Window Managers
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/icewm/%{name}-%{version}.tar.gz
Source1:	IceWM.desktop
Source2:	%{name}.directory
Source3:	ftp://ftp.sourceforge.net/pub/sourceforge/icewm/iceicons-0.6.tar.gz
Source4:	IceWM.RunWM
Source5:	IceWM.wm_style
Source6:	%{name}-menu
Source7:	ftp://ftp.sourceforge.net/pub/sourceforge/icewm/netscapeicons-0.2.tar.gz
URL:		http://www.icewm.org/
BuildRequires:	XFree86-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	imlib-devel
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
Mened©er okienek pod X11. Mo©e emulowaФ wygl╠d Windows'95, OS/2 Warp
3,4, MWM. Mened©er ten prСbuje wybraФ najlepsze cechy dostЙpne w
powy©szych ╤rodowiskach, jak: wiele jednocze╤nie obecnych przestrzeni
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
Marko Macek: gtk2, metal2, motif, nice, warp3, warp4, win95.

%description themes-base -l pl
Standardowy zestaw tematСw dla IceWM-a, dostarczany wraz z nim.
Wszystkie stworzone przez Marko Macka: gtk2, metal2, motif, nice,
warp3, warp4, win95.

%prep
%setup -q

cd lib/icons
tar -xzf %{SOURCE3}
tar -xzf %{SOURCE7}
cd ../..

%build
%configure \
	--with-docdir=%{_docdir} \
	--enable-i18n \
	--enable-guievents \
	--enable-xfreetype \
	--with-gnome-menus \
	--with-imlib \
	%{?_with_antialiasing:--enable-antialiasing} \
	%{?_with_gradients:--enable-gradients}
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

ln -s %{_libdir}/X11/icewm/icons $RPM_BUILD_ROOT%{_pixmapsdir}/icewm

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
%dir %{_libdir}/X11/icewm
%{_libdir}/X11/icewm/icons
%{_libdir}/X11/icewm/ledclock
%{_libdir}/X11/icewm/mailbox
%{_libdir}/X11/icewm/taskbar
%dir %{_libdir}/X11/icewm/themes
%{_libdir}/X11/icewm/themes/Infadel2
%dir %{_applnkdir}/Settings/IceWM
%{_applnkdir}/Settings/IceWM/.directory
%{_wmpropsdir}/*
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
