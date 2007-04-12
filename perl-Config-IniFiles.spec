%define		realname	Config-IniFiles
Summary:	Config-IniFiles module for perl
Name:		perl-%realname
Version:	2.39
Release:	%mkrel 2
License: 	GPL
Group: 		Development/Perl
Source: 	%realname-%version.tar.bz2
URL:		http://search.cpan.org/dist/%realname/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root/
BuildArch:	noarch

%description
This perl module allows you to access to config files written in the
.ini style.

%prep
%setup -q -n Config-IniFiles-%{version}

%build
chmod 644 README IniFiles.pm
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%files
%defattr(-,root,root)
%{perl_vendorlib}/Config
%{_mandir}/*/*
%doc README


