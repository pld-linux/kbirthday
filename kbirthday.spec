Summary:	Remember your birthdays and anniversaries
Summary(pl):	Przypomina twoje urodzinay i rocznice
Name:		kbirthday
Version:	0.7.3
Release:	1
Group:		X11/Applications
License:	GPL v2
Source0:	http://www.gfai.de/~jaham/download/%{name}-%{version}.tar.gz
# Source0-md5:	997b6003772a67042cfdf9a45bdb2b19
Patch0:		%{name}-desktop.patch
URL:		http://www.gfai.de/~jaham/
BuildRequires:	automake
BuildRequires:	kdelibs-devel
Requires:	kdebase-desktop
Requires:	kdebase-kaddressbook
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KBirthday reminds you of birthdays and anniversaries from your KDE
addressbook.

%description -l pl
KBirthday przypomina ci o urodzinach i rocznicach osСb ktСrych dane s╠
w twojej ksi╠©ce adresowej KDE.

%description -l de
KBirthday erinnert an Geburtstage und JubilО©╫n aus dem KDE
Adressbuch.

%description -l fr
KBirthday vous rappelle la date des anniversaires О©╫partir de votre
carnet d'adresses de KDE.

%description -l es
KBirthday le recuerda los cumpleaц╠os y aniversarios de su libreta de
direcciones de KDE.

%description -l ru
KBirthday напоминает о днях рождениях и годовщинах из адресной книги
KDE.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/apps/kicker/applets/kbirthday.desktop \
      $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{_libdir}/libkbirthday.la
%{_libdir}/libkbirthday.so
%{_desktopdir}/kbirthday.desktop
%{_iconsdir}/hicolor/16x16/apps/kbirthday.png
%{_iconsdir}/hicolor/32x32/apps/kbirthday.png
