Summary: 	Remember your birthdays and anniversaries
Summary(pl):	Przypomina twoje urodzinay i rocznice
Name:	 	kbirthday
Version:	0.7.3
Release: 	1
Group:	 	Application
License: 	GPL
URL:	 	http://www.gfai.de/~jaham/
Source0: 	http://www.gfai.de/~jaham/download/%{name}-%{version}.tar.gz	
# Source0-md5:	997b6003772a67042cfdf9a45bdb2b19
BuildRoot: 	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	kdelibs-devel
Requires: 	kdelibs
Requires:	kdebase-desktop
Requires:	kdebase-kaddressbook

%description
KBirthday reminds you of birthdays and anniversaries from your KDE 
addressbook.

%description -l pl
KBirthday przypomina ci o urodzinach i rocznicach osСb ktСrych dane
s╠ w twojej ksi╠©ce adresowej KDE.

%description -l de
KBirthday erinnert an Geburtstage und JubilО©╫n aus dem KDE Adressbuch.

%description -l fr
KBirthday vous rappelle la date des anniversaires О©╫partir de votre 
carnet d'adresses de KDE.

%description -l es
KBirthday le recuerda los cumpleaц╠os y aniversarios de su libreta 
de direcciones de KDE.

%description -l ru_RU.KOI8-R
KBirthday напоминает о днях рождениях и годовщинах из адресной книги KDE.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build

%configure
%{__make}

%install
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang kbirthday

%clean
rm -rf $RPM_BUILD_ROOT

%files -f kbirthday.lang
%defattr(-,root,root,0755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{_libdir}/libkbirthday.la
%{_libdir}/libkbirthday.so
%{_datadir}/apps/kicker/applets/kbirthday.desktop
%{_iconsdir}/hicolor/16x16/apps/kbirthday.png
%{_iconsdir}/hicolor/32x32/apps/kbirthday.png
