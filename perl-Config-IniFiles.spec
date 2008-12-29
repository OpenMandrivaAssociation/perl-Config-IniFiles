%define		module	Config-IniFiles

Name:		perl-%module
Version:	2.45
Release:	%mkrel 1
Summary:	A module for reading .ini-style configuration files
License: 	GPL
Group: 		Development/Perl
URL:		http://search.cpan.org/dist/%module/
Source:     http://www.cpan.org/modules/by-module/Config/%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:  perl(Module::Build)
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This perl module allows you to access to config files written in the
.ini style.

%prep
%setup -q -n Config-IniFiles-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean
rm -rf %{buildroot}
%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Config
%{_mandir}/*/*
