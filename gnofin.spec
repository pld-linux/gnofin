# Note that this is NOT a relocatable package
%define ver      0.5.4
%define rel      1
%define prefix   /usr

Summary: GNOME financial manager
Name: gnofin
Version: %ver
Release: %rel
Copyright: GPL
Group: X11/Applications
Source: ftp://jagger.berkeley.edu/pub/darin/gnofin/gnofin-%{ver}.tar.gz
BuildRoot: /var/tmp/gnofin-%{PACKAGE_VERSION}-root
Packager: Darin Fisher <dfisher@jagger.berkeley.edu>
URL: http://jagger.berkeley.edu/~dfisher/gnofin
Docdir: %{prefix}/doc
# Requires: imlib >= 1.8.1

%description
Gnofin is a light-weight financial management program well-suited for 
helping you keep your checkbook and savings accounts up-to-date.

%changelog

* Mon May 17 1999 Darin Fisher <dfisher@jagger.me.berkeley.edu>
- Initial spec file copied from electric eyes

%prep
%setup

%build
libtoolize --copy --force
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix
make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README
%{prefix}/bin/*
%{prefix}/man/*
