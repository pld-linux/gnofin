Summary:	GNOME financial manager
Name:		gnofin
Version:	0.5.6
Release:	1
Copyright:	GPL
Group:		X11/Applications
Source:		ftp://jagger.berkeley.edu/pub/darin/gnofin/%{name}-%{version}.tar.gz
URL:		http://jagger.berkeley.edu/~dfisher/gnofin
Requires: imlib >= 1.8.1
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix /usr/X11R6

%description
Gnofin is a simple checkbook application for Linux (and other UNIX
variants). Gnofin aims to provide a convenient way to keep track of your
checking and savings accounts (or any other monetary-type accounts). It is
designed to be light-weight, fast, and extremely easy to use.

%prep
%setup -q

%build
libtoolize --copy --force
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=%{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{_prefix} install

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	AUTHORS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%doc *gz
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Sat May 29 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.5.6-1]
- rewited spec to PLD coding style.

* Mon May 17 1999 Darin Fisher <dfisher@jagger.me.berkeley.edu>
- Initial spec file copied from electric eyes
