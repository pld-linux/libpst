Summary:	Tools for conversion of Outlook files to mailbox and other formats
Summary(pl):	Narzêdzia do konwersji plików Outlooka do formatu mailbox i innych
Name:		libpst
Version:	0.5
Release:	1
License:	GPL
Group:		Applications/Files
Source0:	http://dl.sourceforge.net/ol2mbox/%{name}_%{version}.tgz
# Source0-md5:	aebe0033b3a3fb9afc6ae948d767a684
#http://dl.sourceforge.net/ol2mbox/kdbx-0.7.1.tar.gz
URL:		http://sourceforge.net/projects/ol2mbox/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libpst converts Outlook PST files to mailbox and others formats:
kmail, its own recursive format or separate each email into its own
file. It currently handles EMails, Folders and mostly Contacts.

%description -l pl
libpst konwertuje pliki PST z Outlooka do standardowego formatu
skrzynek (mailbox) lub innych formatów: kmaila, w³asnego formatu
rekurencyjnego lub oddziela ka¿dy list do osobnego pliku. Aktualnie
obs³uguje listy, foldery i w wiêkszo¶ci kontakty.

%prep
%setup -q -n %{name}_%{version}

%build
%{__make} \
	GCC_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install readpst readpstlog $RPM_BUILD_ROOT%{_bindir}
install debian/readpst.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS FILE-FORMAT README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
