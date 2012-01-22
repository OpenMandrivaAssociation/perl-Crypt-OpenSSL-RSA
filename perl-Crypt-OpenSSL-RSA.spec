%define	upstream_name	 Crypt-OpenSSL-RSA
%define upstream_version 0.28

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3
Summary:	%{upstream_name} module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.gz

Buildrequires:	perl-devel
BuildRequires:	perl-Crypt-OpenSSL-Random
Buildrequires:	openssl-devel

%description
%{upstream_name} module for perl

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%{__make} test

%install
rm -rf %{buildroot} 
%makeinstall_std

%files
%doc Changes README
%{perl_vendorarch}/auto/Crypt
%{perl_vendorarch}/Crypt
%{_mandir}/man*/*

