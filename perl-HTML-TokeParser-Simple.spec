%define upstream_name	 HTML-TokeParser-Simple
%define upstream_version 3.15

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary: 	Easy to use HTML::TokeParser interface
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url: 		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/O/OV/OVID/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl-HTML-Parser => 3.35
BuildRequires:	perl-Sub-Override
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

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
