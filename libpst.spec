Summary:	Library for reading .pst files
Summary(pl.UTF-8):	Biblioteka do czytania plików .pst
Name:		libpst
Version:	0.6.34
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://www.five-ten-sg.com/libpst/packages/%{name}-%{version}.tar.gz
# Source0-md5:	092067121a7f8c5f8bea8b3cdc31f5e6
URL:		http://www.five-ten-sg.com/libpst/
BuildRequires:	ImageMagick
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	gd-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for reading .pst files.

%description -l pl.UTF-8
Biblioteka do czytania plików .pst.

%package devel
Summary:	Header files for libpst library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libpst
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libpst library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libpst.

%package static
Summary:	Static libpst library
Summary(pl.UTF-8):	Statyczna biblioteka libpst
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libpst library.

%description static -l pl.UTF-8
Statyczna biblioteka libpst.

%package tools
Summary:	Utilities for converting Microsoft Outlook .pst files
Summary(pl.UTF-8):	Narzędzia do konwertowania plików .pst Microsoft Outlooka
Group:		Applications
Requires:	%{name} = %{version}-%{release}
Requires:	ImageMagick
Obsoletes:	readpst

%description tools
Utilities for converting Microsoft Outlook .pst files.

%description tools -l pl.UTF-8
Narzędzia do konwertowania plików .pst Microsoft Outlooka.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-dii \
	--enable-libpst-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libpst.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpst.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpst.so
%{_libdir}/libpst.la
%{_includedir}/libpst
%{_pkgconfigdir}/libpst.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libpst.a

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lspst
%attr(755,root,root) %{_bindir}/pst2dii
%attr(755,root,root) %{_bindir}/pst2ldif
%attr(755,root,root) %{_bindir}/readpst
%attr(755,root,root) %{_bindir}/readpstlog
%{_mandir}/man1/lspst.1*
%{_mandir}/man1/pst2dii.1*
%{_mandir}/man1/pst2ldif.1*
%{_mandir}/man1/readpst.1*
%{_mandir}/man1/readpstlog.1*
%{_mandir}/man5/outlook.pst.5*
