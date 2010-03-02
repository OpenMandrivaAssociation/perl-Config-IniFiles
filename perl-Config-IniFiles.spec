%define upstream_name	 Config-IniFiles
%define upstream_version 2.57

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	A module for reading .ini-style configuration files
License: 	GPL
Group: 		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Module::Build)
BuildRoot: %{_tmppath}/%{name}-%{version}-%{relase}
BuildArch: noarch

%description
This perl module allows you to access to config files written in the
.ini style.

%prep
%setup -q -n Config-IniFiles-%{upstream_version}

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
