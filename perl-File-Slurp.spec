%define	upstream_name	 File-Slurp
%define	upstream_version 9999.19

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Efficient Reading/Writing of Complete Files
Group:		Development/Perl
License:	GPL+ or Artistic
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:		http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl-JSON-PP
BuildArch:	noarch


%description
This module provides subs that allow you to read or write entire files with one
simple call. They are designed to be simple to use, have flexible ways to pass
in or get the file contents and to be very efficient. There is also a sub to
read in all the files in a directory other than . and ..

These slurp/spew subs work for files, pipes and sockets, and stdio,
pseudo-files, and DATA.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 644 lib/File/Slurp.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std
find %{buildroot} -name "perllocal.pod" | xargs -i rm -f {}

%files
%doc README Changes
%{_mandir}/man3*/*
%{perl_vendorlib}/File


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 9999.190.0-4mdv2012.0
+ Revision: 765250
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 9999.190.0-3
+ Revision: 763764
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 9999.190.0-2
+ Revision: 763064
- rebuild

* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 9999.190.0-1
+ Revision: 684744
- update to new version 9999.19

* Sat May 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 9999.180.0-1
+ Revision: 674660
- update to new version 9999.18

* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 9999.160.0-1
+ Revision: 659933
- update to new version 9999.16

* Sat Mar 26 2011 Guillaume Rousse <guillomovitch@mandriva.org> 9999.150.0-1
+ Revision: 648574
- update to new version 9999.15

* Wed Mar 23 2011 Guillaume Rousse <guillomovitch@mandriva.org> 9999.140.0-1
+ Revision: 648087
- update to new version 9999.14

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 9999.130.0-1mdv2010.1
+ Revision: 403180
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 9999.13-3mdv2009.1
+ Revision: 351753
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 9999.13-2mdv2009.0
+ Revision: 223754
- rebuild

* Sat Jan 26 2008 Guillaume Rousse <guillomovitch@mandriva.org> 9999.13-1mdv2008.1
+ Revision: 158255
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 17 2007 Thierry Vignaud <tv@mandriva.org> 9999.12-3mdv2008.0
+ Revision: 64751
- rebuild

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 9999.12-2mdv2008.0
+ Revision: 23408
- rebuild


* Tue Mar 07 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 9999.12-1mdk
- 9999.12

* Wed Jan 25 2006 Guillaume Rousse <guillomovitch@mandriva.org> 9999.11-1mdk
- new version
- spec cleanup
- rpmbuildupdate aware
- fix directory ownership
- better summary and description

* Mon May 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 9999.09-1mdk
- 9999.09

* Mon Jan 31 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 9999.07-1mdk
- 9999.07

* Tue Nov 16 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 9999.06-1mdk
- 9999.06

* Wed Apr 21 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 9999.04-1mdk
- 9999.04
- correct license
- spec cosmetics

* Thu Aug 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2002.1031-3mdk
- rebuild for new perl
- macroize
- drop $RPM_OPT_FLAGS, noarch..
- use %%makeinstall_std macro

* Fri Jul 18 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 2002.1031-2mdk
- buildrequires

* Thu Jun 26 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 2002.1031-1mdk
- Initial build.

