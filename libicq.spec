Summary:	libicq library
Summary(pl):	Biblioteka libicq
Name:		libicq
Version:	0.33
Release:	4
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	%{name}-%{version}.tar.gz
#URL:		
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libicq is based on micq and is intended to make it easy to add ICQ
communication support to your software.

%description -l pl
libicq bazuje na ¼ród³ach micq i umo¿liwia ³atwe dodanie do ró¿nych
plikacji komunikacji bazyuj±cej na priotokole ICQ.

%package devel
Summary:	Header files etc to develop libicq applications
Summary(pl):	Pliki nag³ówkowe i inne do libicq
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
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
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libicq libraries.

%description -l pl static
Biblioteka statyczna libicq.

%prep
%setup -q

%build
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
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
