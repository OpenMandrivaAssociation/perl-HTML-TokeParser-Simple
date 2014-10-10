%define upstream_name	 HTML-TokeParser-Simple
%define upstream_version 3.16

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 3.16
Release:	2

Summary:	Easy to use HTML::TokeParser interface
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/authors/id/O/OV/OVID/HTML-TokeParser-Simple-3.16.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(HTML::Parser)
BuildRequires:	perl(Sub::Override)
BuildArch:	noarch

%description
HTML::TokeParser::Simple is a subclass of HTML::TokeParser that uses
easy-to-remember method calls to work with the tokens.  Rather than
try to remember a bunch of array indices or try to write a bunch of
constants for them, you can now do something like:

 $token->is_start_tag( 'form' )

instead of 

 $token->[0] eq 'S' and $token->[1] eq 'form'

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
perl -pi -e 'tr/\r//d;' Changes README

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/HTML
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 3.150.0-1mdv2010.0
+ Revision: 403264
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 3.15-3mdv2009.0
+ Revision: 257240
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 3.15-1mdv2008.1
+ Revision: 135847
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Jan 03 2007 Stefan van der Eijk <stefan@mandriva.org> 3.15-1mdv2007.0
+ Revision: 103808
- Import perl-HTML-TokeParser-Simple

* Mon Dec 19 2005 Guillaume Rousse <guillomovitch@mandriva.org> 3.15-1mdk
- New release 3.15

* Thu Oct 13 2005 Guillaume Rousse <guillomovitch@mandriva.org> 3.14-1mdk
- New release 3.14
- spec cleanup
- fix directory ownership
- fix source url
- %%mkrel
- fix doc encoding

* Tue Jan 11 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 3.13-1mdk
- 3.13
- Remove MANIFEST, change summary and URL; de-PREFIXify

* Tue Apr 20 2004 Stefan van der Eijk <stefan@eijk.nu> 2.2-1mdk
- initial package


