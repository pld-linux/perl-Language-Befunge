%include	/usr/lib/rpm/macros.perl
%define	pdir	Language
%define	pnam	Befunge
Summary:	Language::Befunge perl module - a Befunge 98 interpreter
Summary(pl):	Modu� perla Language::Befunge - interpreter Befunge 98
Name:		perl-Language-Befunge
Version:	0.38
Release:	2
# same as perl
License:	GPL v1+ Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	10671a349e1f1e5e6599d0cb980db4cd
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Storable
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(v5.6)'

%description
Language::Befunge is an interpreter of Befunge 98 topological
language. This module implements the Funge-98 specifications on a 2D
field (also called Befunge). In particular, be aware that this is not
a Trefunge implementation (3D).

%description -l pl
Language::Befunge to interpreter j�zyka topologicznego Befunge 98. Ten
modu� jest implementacj� specyfikacji Funge-98 dla przestrzeni 2D
(nazywanego tak�e Befunge). Nie jest to implementacja Trefunge (3D).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo "y" | perl Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install Befunge/{examples,lib}/* \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README Befunge/doc/*.{txt,html}
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Language/Befunge.pm
%dir %{perl_vendorlib}/Language/Befunge
%{perl_vendorlib}/Language/Befunge/*.pm
%{_mandir}/man1/*
%{_mandir}/man3/Language::Befunge.3pm*
%{_mandir}/man3/Language::Befunge::[^l]*
%{_examplesdir}/%{name}-%{version}
