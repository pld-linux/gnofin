Summary:	GNOME financial manager
Name:		gnofin
Version:	0.8.3
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://download.sourceforge.net/pub/sourceforge/gnofin/%{name}-%{version}.tar.gz
URL:		http://gnofin.sourceforge.net/
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	XFree86-devel
BuildRequires:	imlib-devel >= 1.8.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Gnofin is a simple checkbook application for Linux (and other UNIX
variants). Gnofin aims to provide a convenient way to keep track of
your checking and savings accounts (or any other monetary-type
accounts). It is designed to be light-weight, fast, and extremely easy
to use.

%prep
%setup -q

%build
gettextize --copy --force
autoconf
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Office/PIMs

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *gz
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/gnofin
%dir %{_libdir}/gnofin/plugins
%attr(755,root,root) %{_libdir}/gnofin/plugins/*
%{_applnkdir}/Office/PIMs/*
%{_mandir}/man1/*
