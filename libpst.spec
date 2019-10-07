#
# Conditional build:
%bcond_without	python2		# CPython 2.x module
%bcond_without	python3		# CPython 3.x module
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Library for reading .pst files
Summary(pl.UTF-8):	Biblioteka do czytania plików .pst
Name:		libpst
Version:	0.6.72
Release:	2
License:	GPL v2+
Group:		Libraries
Source0:	https://www.five-ten-sg.com/libpst/packages/%{name}-%{version}.tar.gz
# Source0-md5:	0085c9769a163e7ac59dba6518e0cc1e
Patch0:		%{name}-link.patch
URL:		https://www.five-ten-sg.com/libpst/
BuildRequires:	ImageMagick
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	gd-devel
BuildRequires:	libgsf-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
%if %{with python2}
BuildRequires:	boost-python-devel
BuildRequires:	python-devel >= 2
BuildRequires:	python-modules >= 2
%endif
%if %{with python3}
BuildRequires:	boost-python3-devel
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for reading PST (MS Outlook Personal Folders) files.

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

%package -n python-libpst
Summary:	libpst Python 2 bindings
Summary(pl.UTF-8):	Wiązania libpst dla Pythona 2
Group:		Development/Languages/Python

%description -n python-libpst
libpst Python 2 bindings.

%description -n python-libpst -l pl.UTF-8
Wiązania libpst dla Pythona 2.

%package -n python3-libpst
Summary:	libpst Python 3 bindings
Summary(pl.UTF-8):	Wiązania libpst dla Pythona 3
Group:		Development/Languages/Python

%description -n python3-libpst
libpst Python 3 bindings.

%description -n python3-libpst -l pl.UTF-8
Wiązania libpst dla Pythona 3.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static} \
	--enable-dii \
	--enable-libpst-shared \
	%{!?with_python3:--disable-python}

%{__make}

%if %{with python2}
install -d build-py2
./libtool --mode=compile %{__cxx} %{rpmcxxflags} %{rpmcppflags} -I. -Isrc -I%{py_incdir} -o build-py2/python-libpst.lo -c python/python-libpst.cpp
./libtool --mode=link %{__cxx} -shared -module -avoid-version -rpath %{py_sitedir} %{rpmldflags} %{rpmcxxflags} -o build-py2/_libpst.la build-py2/python-libpst.lo src/libpst.la -lboost_python%(echo %{py_ver} | tr -d .)
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/_libpst.la
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/_libpst.a
%endif

%if %{with python2}
install -d $RPM_BUILD_ROOT%{py_sitedir}
./libtool --mode=install install build-py2/_libpst.la $RPM_BUILD_ROOT%{py_sitedir}
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/_libpst.la
%endif

# packaged as %doc (split into base and -devel)
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libpst.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpst.so.4

%files devel
%defattr(644,root,root,755)
%doc html/*.html html/devel
%attr(755,root,root) %{_libdir}/libpst.so
%{_libdir}/libpst.la
%{_includedir}/libpst-4
%{_pkgconfigdir}/libpst.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libpst.a
%endif

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lspst
%attr(755,root,root) %{_bindir}/nick2ldif
%attr(755,root,root) %{_bindir}/pst2dii
%attr(755,root,root) %{_bindir}/pst2ldif
%attr(755,root,root) %{_bindir}/readpst
%{_mandir}/man1/lspst.1*
%{_mandir}/man1/pst2dii.1*
%{_mandir}/man1/pst2ldif.1*
%{_mandir}/man1/readpst.1*
%{_mandir}/man5/outlook.pst.5*

%if %{with python2}
%files -n python-libpst
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_libpst.so
%endif

%if %{with python3}
%files -n python3-libpst
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/_libpst.so
%endif
