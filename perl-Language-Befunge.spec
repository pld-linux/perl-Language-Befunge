%include	/usr/lib/rpm/macros.perl
%define		pdir	Language
%define		pnam	Befunge
Summary:	Language::Befunge perl module - a Befunge 98 interpreter
Summary(pl.UTF-8):	Moduł perla Language::Befunge - interpreter Befunge 98
Name:		perl-Language-Befunge
Version:	4.12
Release:	1
# same as perl
License:	GPL v1+ Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c79f4663f7b81dfe532267e803642657
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(v5.6)'

%description
Language::Befunge is an interpreter of Befunge 98 topological
language. This module implements the Funge-98 specifications on a 2D
field (also called Befunge). In particular, be aware that this is not
a Trefunge implementation (3D).

%description -l pl.UTF-8
Language::Befunge to interpreter języka topologicznego Befunge 98. Ten
moduł jest implementacją specyfikacji Funge-98 dla przestrzeni 2D
(nazywanego także Befunge). Nie jest to implementacja Trefunge (3D).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo "y" | perl Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Language/Befunge.pm
%dir %{perl_vendorlib}/Language/Befunge
%{perl_vendorlib}/Language/Befunge/*.pm
%{_mandir}/man1/*
%{_mandir}/man3/Language::Befunge.3pm*
%{_mandir}/man3/Language::Befunge::[!l]*
