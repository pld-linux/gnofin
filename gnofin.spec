Summary:	GNOME financial manager
Name:		gnofin
Version:	0.5.6
Release:	1
Copyright:	GPL
Group:		X11/Applications
Source:		ftp://jagger.berkeley.edu/pub/darin/gnofin/%{name}-%{version}.tar.gz
URL:		http://jagger.berkeley.edu/~dfisher/gnofin
BuildPrereq:	gnome-libs-devel
BuildPrereq:	XFree86-devel
BuildPrereq:	imlib-devel >= 1.8.1
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix /usr/X11R6
%define		_mandir /usr/X11R6/man

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
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	AUTHORS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
