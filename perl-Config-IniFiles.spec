%define upstream_name	 Config-IniFiles
%define upstream_version 2.98

Summary:	A module for reading .ini-style configuration files
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1
License:	GPLv2
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(IO::Scalar)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
# Workaround for perl-CPAN prior to 5.26.1-2 incorrectly
# providing perl(Module::Build)
BuildRequires:	perl-Module-Build

%description
This perl module allows you to access to config files written in the
.ini style.

%prep
%setup -qn Config-IniFiles-%{upstream_version}

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
%{_mandir}/man3/*
