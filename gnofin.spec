Summary:	GNOME financial manager
Summary(pl):	Zarz±dca finansów dla GNOME
Name:		gnofin
Version:	0.8.4
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gnofin/%{name}-%{version}.tar.gz
URL:		http://gnofin.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	imlib-devel >= 1.8.1
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnofin is a simple checkbook application for Linux (and other UNIX
variants). Gnofin aims to provide a convenient way to keep track of
your checking and savings accounts (or any other monetary-type
accounts). It is designed to be light-weight, fast, and extremely easy
to use.

%description -l pl
Gnofin jest prost± aplikacj± rachunkow± dla Linuksa oraz innych
uniksów. Pozwala na zarz±dzanie twoimi rachunkami oraz kontami
(wszystkimi rodzajami kont walutowych). Program jest zaprojektowany z
my¶l±, aby byæ ma³ym, szybkim oraz bardzo prostym w obs³udze.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Office/PIMs

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/gnofin
%dir %{_libdir}/gnofin/plugins
%attr(755,root,root) %{_libdir}/gnofin/plugins/*
%{_applnkdir}/Office/PIMs/*
%{_mandir}/man?/*
