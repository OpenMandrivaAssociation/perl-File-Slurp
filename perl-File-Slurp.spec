%define	modname	File-Slurp
%define	modver	9999.19

Summary:	Efficient Reading/Writing of Complete Files
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	8
Group:		Development/Perl
License:	GPLv2+ or Artistic
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/File/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl-JSON-PP

%description
This module provides subs that allow you to read or write entire files with one
simple call. They are designed to be simple to use, have flexible ways to pass
in or get the file contents and to be very efficient. There is also a sub to
read in all the files in a directory other than . and ..

These slurp/spew subs work for files, pipes and sockets, and stdio,
pseudo-files, and DATA.

%prep
%setup -qn %{modname}-%{modver}
chmod 644 lib/File/Slurp.pm

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std
find %{buildroot} -name "perllocal.pod" | xargs -i rm -f {}

%files
%doc README Changes
%{perl_vendorlib}/File
%{_mandir}/man3*/*

