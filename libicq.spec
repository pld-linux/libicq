Summary:	libicq library
Summary(pl):	Biblioteka libicq
Name:		libicq
Version:	0.33
Release:	7
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libicq/%{name}-%{version}.tar.gz
# Source0-md5:	3717d4b08dfdd9af9a57f5d17d04529d
URL:		http://sourceforge.net/projects/libicq/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
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
Requires:	%{name} = %{version}

%description devel
Header files etc you can use to develop libicq applications.

%description devel -l pl
Pakiet ten zawiera pliki nag³ówkowe i inne do libicq niezbêdne przy
tworzeniu aplikacji opartych o tê bibliotekê.

%package static
Summary:	Static libicq libraries
Summary(pl):	Biblioteka statyczna libicq
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libicq libraries.

%description static -l pl
Biblioteka statyczna libicq.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
