%define	modname	Crypt-OpenSSL-RSA
%define modver	0.28

Version:	%perl_convert_version %{modver}
Name:		perl-%{modname}
Release:	14
Summary:	%{modname} module for perl 
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Crypt/%{modname}-%{modver}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl-Crypt-OpenSSL-Random
BuildRequires:	pkgconfig(openssl)

%description
%{modname} module for perl

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorarch}/auto/Crypt
%{perl_vendorarch}/Crypt
%{_mandir}/man3/*

