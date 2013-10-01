Summary:	Framework providing Desktop activity awareness
Name:		zeitgeist
Version:	0.9.14
Release:	2
License:	LGPL v2
Group:		Daemons
Source0:	http://launchpad.net/zeitgeist/0.9/%{version}/+download/%{name}-%{version}.tar.xz
# Source0-md5:	92371b864515389ffe7d70569f0bc9ed
URL:		http://launchpad.net/zeitgeist
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	python-rdflib
BuildRequires:	raptor2-rapper
BuildRequires:	xapian-core-devel
BuildRequires:	sqlite3-devel
BuildRequires:	telepathy-glib-devel
BuildRequires:	json-glib-devel
BuildRequires:	glib-gio-devel
Requires:	%{name}-libs = %{version}-%{release}
Requires:	python-dbus
Requires:	python-modules
Requires:	python-modules-sqlite
Requires:	python-pygobject
Requires:	python-pyxdg
Provides:	zeitgeist-datahub = %{version}-%{release}
Obsoletes:	zeitgeist-datahub < %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
Zeitgeist is a service which logs the users's activities and events
(files opened, websites visites, conversations hold with other people,
etc.) and makes relevant information available to other applications.
It is able to establish relationships between items based on
similarity and usage patterns.

%package libs
Summary:	Zeitgeist library
Group:		Libraries

%description libs
Zeitgeist library.

%package devel
Summary:	Header files for Zeitgeist library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the package containing the header files for Zeitgeist library.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

#%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/zeitgeist-daemon
%attr(755,root,root) %{_bindir}/zeitgeist-datahub
%{_datadir}/dbus-1/services/org.gnome.zeitgeist.service
%{_datadir}/zeitgeist
%{_sysconfdir}/xdg/autostart/zeitgeist-datahub.desktop
%{_mandir}/man1/zeitgeist-daemon.1*
%{_mandir}/man1/zeitgeist-datahub.1*
%{py_sitescriptdir}/zeitgeist

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libzeitgeist-2.0.so.0
%attr(755,root,root) %{_libdir}/libzeitgeist-2.0.so.*.*.*
%{_libdir}/girepository-1.0/Zeitgeist-2.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libzeitgeist-2.0.so
%{_includedir}/zeitgeist-2.0
%{_pkgconfigdir}/zeitgeist-2.0.pc
%{_datadir}/gir-1.0/Zeitgeist-2.0.gir
%{_datadir}/vala/vapi/zeitgeist-*

