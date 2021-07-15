%define	modname	Crypt-OpenSSL-RSA
%define modver	0.31

Version:	%perl_convert_version %{modver}
Name:		perl-%{modname}
Release:	4
Summary:	%{modname} module for perl 
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Crypt/%{modname}-%{modver}.tar.gz
# Remove SSLv2 bits, following OpenSSL upstream suggestion
# https://github.com/openssl/openssl/issues/14216
Patch0:		Crypt-OpenSSL-RSA-openssl-3.0.patch
BuildRequires:	perl-devel
BuildRequires:	perl-Crypt-OpenSSL-Random
BuildRequires:  perl(Crypt::OpenSSL::Guess)
BuildRequires:	pkgconfig(openssl)

%description
%{modname} module for perl

%prep
%autosetup -p1 -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build CFLAGS="%{optflags}"

%install
%make_install

%files
%doc Changes README
%{perl_vendorarch}/auto/Crypt
%{perl_vendorarch}/Crypt
%{_mandir}/man3/*
