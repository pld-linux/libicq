Summary:	libicq library
Summary(pl.UTF-8):	Biblioteka libicq
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

%description -l pl.UTF-8
libicq bazuje na źródłach micq i umożliwia łatwe dodanie do różnych
aplikacji komunikacji bazującej na protokole ICQ.

%package devel
Summary:	Header files etc to develop libicq applications
Summary(pl.UTF-8):	Pliki nagłówkowe i inne do libicq
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files etc you can use to develop libicq applications.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i inne do libicq niezbędne przy
tworzeniu aplikacji opartych o tę bibliotekę.

%package static
Summary:	Static libicq libraries
Summary(pl.UTF-8):	Biblioteka statyczna libicq
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libicq libraries.

%description static -l pl.UTF-8
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
