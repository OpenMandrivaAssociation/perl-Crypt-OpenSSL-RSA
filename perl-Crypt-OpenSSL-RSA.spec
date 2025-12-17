%define modname Crypt-OpenSSL-RSA

Version:	0.35
Name:		perl-%{modname}
Release:	2
Summary:	%{modname} module for perl 
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Crypt/%{modname}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl-Crypt-OpenSSL-Random
BuildRequires:  perl(Crypt::OpenSSL::Guess)
BuildRequires:	pkgconfig(openssl)

%description
%{modname} module for perl.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build CFLAGS="%{optflags}"

%install
%make_install

%files
%doc Changes README
%{perl_vendorarch}/auto/Crypt
%{perl_vendorarch}/Crypt
%doc %{_mandir}/man3/*
