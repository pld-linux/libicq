Summary:	libicq library
Summary(pl):	Biblioteka libicq
Name:		libicq
Version:	0.33
Release:	3
Copyright:	GPL
Group:		Libraries
Group(pl):	Biblioteki
Source:		%{name}-%{version}.tar.gz
#URL:		
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Libicq library needed by some ICQ clients

%description -l pl
Biblioteka u¿ywana przez niektóre programy ICQ

%package devel
Summary:	Header files etc to develop libicq applications
Summary(pl):	Pliki nag³ówkowe i inne do libicq
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files etc you can use to develop libicq applications.

%description -l pl devel
Pakiet ten zaziewra pliki nag³ówkowe i inne do libicq niezbêdne przy
tworzeniu aplikacji opartych o t± bibliotekê.

%package static
Summary:	Static libicq libraries
Summary(pl):	Biblioteka statyczna libicq
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libicq libraries.

%description -l pl static
Biblioteka statyczna libicq.

%prep
%setup -q

%build
#automake
LDFLAGS="-s"; export LDFLAGS
%configure 
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README,TODO}.gz 
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
