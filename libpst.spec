Summary:	Tools for conversion of Outlook files to mailbox and other formats
Summary(pl):	Narz�dzia do konwersji plik�w Outlooka do formatu mailbox i innych
Name:		libpst
Version:	0.5.1
Release:	1
License:	GPL
Group:		Applications/Files
Source0:	http://alioth.debian.org/download.php/844/%{name}-%{version}.tgz
# Source0-md5:	0a80562bf7c503f9d3fdd96e0de10408
URL:		http://alioth.debian.org/projects/libpst/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libpst converts Outlook PST files to mailbox and others formats:
kmail, its own recursive format or separate each email into its own
file. It currently handles EMails, Folders and mostly Contacts.

%description -l pl
libpst konwertuje pliki PST z Outlooka do standardowego formatu
skrzynek (mailbox) lub innych format�w: kmaila, w�asnego formatu
rekurencyjnego lub oddziela ka�dy list do osobnego pliku. Aktualnie
obs�uguje listy, foldery i w wi�kszo�ci kontakty.

%prep
%setup -q

%build
%{__make} \
	GCC_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install lspst readpst readpstlog $RPM_BUILD_ROOT%{_bindir}
install readpst.1 readpstlog.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog CREDITS FILE-FORMAT TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
