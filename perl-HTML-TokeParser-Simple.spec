%define module	HTML-TokeParser-Simple
%define name	perl-%{module}
%define version 3.15
%define release %mkrel 3


Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Easy to use HTML::TokeParser interface
License: 	GPL or Artistic
Group: 		Development/Perl
Source: 	http://search.cpan.org/CPAN/authors/id/O/OV/OVID/%{module}-%{version}.tar.bz2
Url: 		http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl-HTML-Parser => 3.35
BuildRequires:	perl-Sub-Override
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
HTML::TokeParser::Simple is a subclass of HTML::TokeParser that uses
easy-to-remember method calls to work with the tokens.  Rather than
try to remember a bunch of array indices or try to write a bunch of
constants for them, you can now do something like:

 $token->is_start_tag( 'form' )

instead of 

 $token->[0] eq 'S' and $token->[1] eq 'form'

%prep
%setup -q -n %{module}-%{version}
perl -pi -e 'tr/\r//d;' Changes README

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

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
%{perl_vendorlib}/HTML
%{_mandir}/*/*


