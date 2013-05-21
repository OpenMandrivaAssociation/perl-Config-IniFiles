%define upstream_name	 Config-IniFiles
%define upstream_version 2.68

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	A module for reading .ini-style configuration files
License: 	GPL
Group: 		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Module::Build)
BuildRequires: perl-devel
BuildArch: noarch

%description
This perl module allows you to access to config files written in the
.ini style.

%prep
%setup -q -n Config-IniFiles-%{upstream_version}

%build
%__perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc README
%{perl_vendorlib}/Config
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.680.0-4mdv2012.0
+ Revision: 765106
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 2.680.0-2
+ Revision: 763047
- rebuild

* Fri Jun 24 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.680.0-1
+ Revision: 686972
- update to new version 2.68

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.660.0-2
+ Revision: 667051
- mass rebuild

* Sun Jan 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.660.0-1
+ Revision: 634216
- update to new version 2.66

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.650.0-1mdv2011.0
+ Revision: 601862
- update to new version 2.65

* Sun Nov 21 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.640.0-1mdv2011.0
+ Revision: 599548
- update to new version 2.64

* Tue Nov 16 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.610.0-1mdv2011.0
+ Revision: 598079
- update to new version 2.61

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 2.580.0-2mdv2011.0
+ Revision: 564731
- rebuild for perl 5.12.1

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 2.580.0-1mdv2011.0
+ Revision: 553076
- update to 2.58

* Tue Mar 02 2010 Jérôme Quelin <jquelin@mandriva.org> 2.570.0-1mdv2010.1
+ Revision: 513472
- update to 2.57

* Thu Dec 31 2009 Jérôme Quelin <jquelin@mandriva.org> 2.560.0-1mdv2010.1
+ Revision: 484371
- update to 2.56

* Wed Dec 23 2009 Jérôme Quelin <jquelin@mandriva.org> 2.550.0-1mdv2010.1
+ Revision: 481708
- update to 2.55

* Thu Nov 19 2009 Jérôme Quelin <jquelin@mandriva.org> 2.540.0-1mdv2010.1
+ Revision: 467358
- update to 2.54

* Sat Nov 14 2009 Jérôme Quelin <jquelin@mandriva.org> 2.530.0-1mdv2010.1
+ Revision: 465997
- update to 2.53

* Fri Jul 17 2009 Jérôme Quelin <jquelin@mandriva.org> 2.520.0-1mdv2010.0
+ Revision: 396841
- rebuild for new automatic procides extraction
- using %%perl_convert_version

* Mon Jun 29 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.52-1mdv2010.0
+ Revision: 390521
- update to new version 2.52

* Tue Jun 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.51-1mdv2010.0
+ Revision: 384239
- update to new version 2.51

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.50-1mdv2010.0
+ Revision: 383475
- update to new version 2.50

* Tue May 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.49-1mdv2010.0
+ Revision: 372089
- update to new version 2.49

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.48-1mdv2010.0
+ Revision: 370044
- update to new version 2.48

* Fri Jan 23 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.47-1mdv2009.1
+ Revision: 332845
- update to new version 2.47

* Sun Jan 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.46-1mdv2009.1
+ Revision: 330907
- update to new version 2.46

* Mon Dec 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.45-1mdv2009.1
+ Revision: 320944
- new version

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.39-4mdv2009.0
+ Revision: 223575
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 2.39-3mdv2008.1
+ Revision: 136690
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 17 2007 Thierry Vignaud <tv@mandriva.org> 2.39-3mdv2008.0
+ Revision: 64793
- rebuild


* Sat Feb 03 2007 Olivier Thauvin <nanardon@mandriva.org> 2.39-2mdv2007.0
+ Revision: 116052
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Config-IniFiles

* Tue Jan 31 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.39-1mdk
- 2.39
- spec cleanup
- Add tests

* Tue Feb 15 2005 Michael Scherer <misc@mandrake.org> 2.38-3mdk
- Rebuild
- Fix description, and rpmlint warning.

* Wed Feb 25 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.38-2mdk
- rebuild
- fix url
- own dir
- cosmetic

