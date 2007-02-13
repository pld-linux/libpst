Summary:	Utility for converting Microsoft Outlook mail files
Summary(pl.UTF-8):	Narzędzie do konwertowania plików wiadomości Microsoft Outlooka
Name:		libpst
Version:	0.5.1
Release:	2
License:	GPL
Group:		Applications
Source0:	http://alioth.debian.org/download.php/844/%{name}-%{version}.tar.gz
# Source0-md5:	0a80562bf7c503f9d3fdd96e0de10408
Patch0:		readpst-install.patch
URL:		http://alioth.debian.org/projects/libpst/
Obsoletes:	readpst
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
readpst is a utility for converting Microsoft Outlook mail files
(personal folders) to standard UNIX mbox format.

This is a fork of the libpst project at sourceforge.

%description -l pl.UTF-8
readpst to narzędzie do konwertowania plików wiadomości programu
Microsoft Outlook (osobistych katalogów) do standardowego formatu Unix
mbox.

Jest to odgałęzienie projektu libpst na sourceforge.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog FILE-FORMAT TODO
%attr(755,root,root) %{_bindir}/readpst
%attr(755,root,root) %{_bindir}/readpstlog
%{_mandir}/man1/readpst.1*
%{_mandir}/man1/readpstlog.1*
