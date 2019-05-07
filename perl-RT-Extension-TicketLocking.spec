#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	RT
%define		pnam	Extension-TicketLocking
%include	/usr/lib/rpm/macros.perl
Summary:	RT::Extension::TicketLocking - Enables users to place advisory locks on tickets
Name:		perl-RT-Extension-TicketLocking
Version:	1.07
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/RT/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8a174769fae34c3b762f0cfb9991af40
URL:		https://metacpan.org/release/RT-Extension-TicketLocking/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rt
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Locks can be of several different types. Current types are:

Locks are advisory: if a ticket is locked by one user, other users
will be given a notification (in red) that another user has locked
the ticket, with the locking user's name and how long he has had
it locked for, but they will still be allowed to edit and submit
changes on the ticket.

When a user locks a ticket (auto lock or hard lock), they are given
a notification informing them of their lock and how long they have
had the ticket locked (in some other color - currently green).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLVENDORLIB=%{perl_vendorlib} \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/RT/Extension/TicketLocking.pm
%{_mandir}/man3/*
