# Note that this is NOT a relocatable package
%define ver      0.8.1
%define rel      1
%define prefix   /usr

Summary: a simple money management application for GNOME
Name: gnofin
Version: %ver
Release: %rel
Copyright: GPL
Group: X11/Applications
Source: ftp://gnofin.sourceforge.net/pub/gnofin/gnofin-%{ver}.tar.gz
BuildRoot: /var/tmp/gnofin-%{PACKAGE_VERSION}-root
Packager: Darin Fisher <darinf@users.sourceforge.net>
URL: http://gnofin.sourceforge.net
Docdir: %{prefix}/doc

Requires: gnome-libs >= 1.0.0

%description
Gnofin is a light-weight personal finance application for GNOME well-suited for
helping you keep your checkbook and savings accounts up-to-date.

%changelog

* Sat Jan 29 2000 Darin Fisher <darinf@users.sourceforge.net>
- Updated description blurb

* Mon Jan 24 2000 Darin Fisher <darinf@users.sourceforge.net>
- Updates to reflect project move to sourceforge.net

* Tue Nov 23 1999 Darin Fisher <darinf@users.sourceforge.net>
- Updates to include po files and plugins in the rpm

* Mon May 17 1999 Darin Fisher <darinf@users.sourceforge.net>
- Initial spec file copied from electric eyes

%prep
%setup

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix
if [ "$SMP" != "" ]; then
  make -j $SMP
else
  make
fi

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README README.*

%{prefix}/bin/*
%{prefix}/lib/gnofin/plugins/*
%{prefix}/man/*
%{prefix}/share/gnome/apps/Applications/gnofin.desktop
%{prefix}/share/locale/*/*
