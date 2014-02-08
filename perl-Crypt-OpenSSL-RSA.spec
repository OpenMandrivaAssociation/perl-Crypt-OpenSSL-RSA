%define	upstream_name	 Crypt-OpenSSL-RSA
%define upstream_version 0.28

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    6
Summary:	%{upstream_name} module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl-Crypt-OpenSSL-Random
BuildRequires:	pkgconfig(openssl)

%description
%{upstream_name} module for perl

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%__make test

%install
rm -rf %{buildroot} 
%makeinstall_std

%files
%doc Changes README
%{perl_vendorarch}/auto/Crypt
%{perl_vendorarch}/Crypt
%{_mandir}/man*/*



%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.280.0-3
+ Revision: 765130
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.280.0-2
+ Revision: 763633
- rebuilt for perl-5.14.x

* Wed Nov 30 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.280.0-1
+ Revision: 735519
- new version 0.28
- cleaned up spec
- removed defattr, clean section, BuildRoot, mkrel

* Tue Jul 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.270.0-1
+ Revision: 688743
- update to new version 0.27

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.260.0-8
+ Revision: 667059
- mass rebuild

* Mon Aug 02 2010 Funda Wang <fwang@mandriva.org> 0.260.0-7mdv2011.0
+ Revision: 564957
- rebuild for perl 5.12.1
- rebuild for perl 5.12.1

  + JÃ©rÃ´me Quelin <jquelin@mandriva.org>
    - rebuild

  + Sandro Cazzaniga <kharec@mandriva.org>
    - rebuild

* Wed Apr 07 2010 Funda Wang <fwang@mandriva.org> 0.260.0-3mdv2010.1
+ Revision: 532503
- rebuild

* Fri Feb 26 2010 Oden Eriksson <oeriksson@mandriva.com> 0.260.0-2mdv2010.1
+ Revision: 511612
- rebuilt against openssl-0.9.8m

* Tue Nov 24 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.260.0-1mdv2010.1
+ Revision: 469435
- update to 0.26

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.250.0-1mdv2010.0
+ Revision: 403034
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.25-4mdv2009.1
+ Revision: 351696
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.25-3mdv2009.0
+ Revision: 223583
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.25-2mdv2008.1
+ Revision: 152038
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Jul 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.25-1mdv2008.0
+ Revision: 47628
- update to new version 0.25


* Fri Nov 24 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.24-1mdv2007.0
+ Revision: 86940
- new version
- Import perl-Crypt-OpenSSL-RSA

* Fri Sep 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.23-2mdv2007.0
- Rebuild

* Sun Apr 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.23-1mdk
- New release 0.23
- spec cleanup
- correct optimisations

* Wed Nov 30 2005 Oden Eriksson <oeriksson@mandriva.com> 0.22-3mdk
- rebuilt against openssl-0.9.8a

* Tue Oct 11 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.22-2mdk
- Fix buildrequires mistake

* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.22-1mdk
- 0.22

* Tue Feb 08 2005 Sylvie Terjan <erinmargault@mandrake.org> 0.21-2mdk
- rebuild for new perl

* Thu Apr 22 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.21-1mdk
- 0.21

