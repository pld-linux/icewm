#
# Conditional build:
# _with_gradients	- enable gradients (implies _with_antialiasing)
# _without_antialiasing	- disable antialiasing
# _without_freetype	- disable xfreetype support (implies _without_antialiasing)
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
Summary(pl):	IceWM - zarz�dca okienek X11
Summary(pt_BR):	Gerenciador de Janelas X11
Summary(ru):	������� �������� ��� X11
Summary(uk):	�������� �������� ��� X11
Name:		icewm
Version:	1.2.6
Release:	4
Epoch:		2
License:	LGPL
Group:		X11/Window Managers
Source0:	http://dl.sourceforge.net/icewm/%{name}-%{version}.tar.gz
Source1:	IceWM.desktop
Source2:	%{name}.directory
Source3:	http://dl.sourceforge.net/icewm/iceicons-0.6.tar.gz
Source4:	IceWM.RunWM
Source5:	IceWM.wm_style
Source6:	http://dl.sourceforge.net/icewm/netscapeicons-0.2.tar.gz
URL:		http://www.icewm.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
%{!?_without_guievents:BuildRequires:	esound-devel}
BuildRequires:	gettext-devel
%{!?_without_gnome:BuildRequires:	gnome-libs-devel}
%{!?_without_imlib:BuildRequires:	imlib-devel}
BuildRequires:	libstdc++-devel
%{!?_without_freetype:BuildRequires:	Xft-devel >= 2.1}
Requires(pre):	fileutils
Requires(pre):	sh-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wmstyledir	/etc/sysconfig/wmstyle
%define		_wmpropsdir	/usr/share/wm-properties

%description
Window Manager for X Window System. Can emulate the look of
Windows'95, OS/2 Warp 3,4, Motif. Tries to take the best features of
the above systems. Features multiple workspaces, opaque move/resize,
task bar, window list, mailbox status, digital clock. Fast and small.

%description -l es
Administrador de Ventanas para el X Window. Puede emular la apariencia
del Windows'95, OS/2 Warp 3 y 4 y el Motif. Intenta usar las mejores
caracter�sticas de los sistemas citados. Caracter�sticas: varios
ambientes de trabajo, movimiento/ redimensionamiento opaco, barra de
tareas, lista de ventanas, estado de la caja de entrada del correo y
reloj digital. R�pido y peque�o.

%description -l pl
Zarz�dca okienek pod X11. Mo�e emulowa� wygl�d Windows'95, OS/2 Warp
3, 4, MWM. Zarz�dca ten pr�buje przej�� z powy�szych �rodowisk ich
najlepsze cechy, takie jak: wiele jednocze�nie obecnych przestrzeni
roboczych, paski narz�dziowe, status skrzynki z poczt�, cyfrowy zegar.
Jest przy tym ma�y i szybki.

%description -l pt_BR
Gerenciador de Janelas para o X Window. Pode emular a apar�ncia do
Windows'95, OS/2 Warp 3 e 4 e o Motif. Tenta usar as melhores
caracter�sticas dos sistemas citados. Caracter�sticas: v�rios
ambientes de trabalho, movimenta��o/ redimensionamento opaco, barra de
tarefas, lista de janelas, status da caixa de entrada do correio e
rel�gio digital. � r�pido e pequeno.

%description -l ru
������� �������� ��� X Window System. ����� ����������� ������� ���
Windows'95, OS/2 Warp 3,4, Motif. ��������� ����� ������ �� ����������
������. ������������ ��������� ������� ������������, ������������
����������� ����, ������� �������, ������ ����, ������ ���������
�����, �������� ����. ������� � ����������.

%description -l uk
�������� �������� ��� X Window System. ���� ��������� ���Φ�Φ� ������
Windows'95, OS/2 Warp 3,4, Motif. ����������� ����� �������� ��
�������� ������. ������դ ˦���� ������� ������, ���������
����ͦ����� צ���, ������ �������, ������ צ���, ���� ������ϧ
��������, �������� ��������. ������� �� ����������.

%package themes-base
Summary:	Pack of themes for IceWM
Summary(pl):	Zestaw motyw�w dla IceWM-a
Group:		Themes
Requires:	icewm

%description themes-base
Standard pack of themes delivered with IceWM. All of them made by
Marko Macek: gtk2, metal2, motif, nice, nice2, warp3, warp4, win95.

%description themes-base -l pl
Standardowy zestaw motyw�w dla IceWM-a, dostarczany wraz z nim.
Wszystkie stworzone przez Marko Macka: gtk2, metal2, motif, nice,
nice2, warp3, warp4, win95.

%prep
%setup -q

cd lib/icons
tar -xzf %{SOURCE3}
tar -xzf %{SOURCE6}
cd ../..

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure \
	%{?_with_gradients:--enable-gradients} \
	%{!?_without_antialiasing:--enable-antialiasing} \
	%{?_without_freetype:--disable-xfreetype} \
	%{!?_without_guievents:--enable-guievents} \
	%{!?_without_gnome:--with-gnome-menus} \
	%{?_without_imlib:--without-imlib} \
	--enable-shaped-decorations \
	--with-cfgdir=%{_sysconfdir}/X11/%{name} \
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
install lib/keys $RPM_BUILD_ROOT%{_sysconfdir}/X11/%{name}/keys
install lib/preferences $RPM_BUILD_ROOT%{_sysconfdir}/X11/%{name}/preferences
install lib/toolbar $RPM_BUILD_ROOT%{_sysconfdir}/X11/%{name}/toolbar
install lib/winoptions $RPM_BUILD_ROOT%{_sysconfdir}/X11/%{name}/winoptions

ln -s %{_datadir}/icewm/icons $RPM_BUILD_ROOT%{_pixmapsdir}/icewm

echo "menuprog \"Programs\" %{_datadir}/icewm/icons/folder_16x16.xpm icewm-menu-gnome1 --list \"%{_applnkdir}\"" > $RPM_BUILD_ROOT%{_sysconfdir}/X11/%{name}/menu

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%pre
test -h %{_pixmapsdir}/icewm || rm -rf %{_pixmapsdir}/icewm

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS CHANGES FAQ PLATFORMS README* TODO icewm.lsm doc/*.html
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}/X11/%{name}
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/X11/%{name}/*
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
