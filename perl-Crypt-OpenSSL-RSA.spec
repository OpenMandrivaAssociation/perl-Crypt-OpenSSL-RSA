%define	module	Crypt-OpenSSL-RSA
%define name	perl-%{module}
%define version	0.25
%define release %mkrel 3

Summary:	%{module} module for perl 
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Crypt/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
Requires:	openssl
Buildrequires:	perl-devel
BuildRequires:	perl-Crypt-OpenSSL-Random
Buildrequires:	openssl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
%{module} module for perl

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%{__make} test

%install
rm -rf %{buildroot} 
%makeinstall_std

%clean 
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorarch}/auto/Crypt
%{perl_vendorarch}/Crypt
%{_mandir}/man*/*


