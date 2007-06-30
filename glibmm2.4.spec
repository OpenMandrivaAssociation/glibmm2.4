%define version 2.13.7
%define release %mkrel 1

%define pkgname	glibmm
%define api_version 2.4
%define major 1
%define libname_orig %mklibname %{pkgname} %{api_version}
%define libname %mklibname %{pkgname} %{api_version} %{major}

Name:		%{pkgname}%{api_version}
Summary:	C++ interface for glib
Version:	%{version}
Release:	%{release}
License:	LGPL
Group:		System/Libraries
URL:		http://gtkmm.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:		http://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.bz2
BuildRequires:	glib2-devel >= 2.10
BuildRequires:	libsigc++2.0-devel

%description
Gtkmm provides a C++ interface to the GTK+ GUI library.
%{pkgname} originally belongs to gtkmm, but is now separated,
for use with non-GUI software written in C++.


%package	-n %{libname}
Summary:	C++ interface for glib
Group:		System/Libraries
Provides:	%{libname_orig} = %{version}-%{release}
Provides:	%{pkgname}%{api_version} = %{version}-%{release}

%description	-n %{libname}
Gtkmm provides a C++ interface to the GTK+ GUI library.
%{pkgname} originally belongs to gtkmm, but is now separated,
for use with non-GUI software written in C++.

This package contains the library needed to run programs dynamically
linked with %{pkgname}.


%package	-n %{libname}-devel
Summary:	Headers and development files of %{pkgname}
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}
Provides:	%{pkgname}%{api_version}-devel = %{version}-%{release}
Provides:	%{libname_orig}-devel = %{version}-%{release}

%description	-n %{libname}-devel
This package contains the headers and development files that are needed,
when trying to develop or compile applications which need %{pkgname}.


%package	-n %{libname}-static-devel
Summary:	Static libraries of %{pkgname}
Group:		Development/GNOME and GTK+
Requires:	%{libname}-devel = %{version}
Provides:	%{libname_orig}-static-devel = %{version}-%{release}

%description	-n %{libname}-static-devel
Gtkmm provides a C++ interface to the GTK+ GUI library.
%{pkgname} originally belongs to gtkmm, but is now separated,
for use with non-GUI software written in C++.

This package contains the static libraries of %{pkgname}.


%package	doc
Summary:	Glibmm documentation
Group:		Books/Other

%description	doc
Gtkmm provides a C++ interface to the GTK+ GUI library.
%{pkgname} originally belongs to gtkmm, but is now separated,
for use with non-GUI software written in C++.

This package contains all API documentation for %{pkgname}.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# mdk does not have libtool 1.5 yet
%define __libtoolize /bin/true
%configure2_5x --enable-static --enable-shared
%make

# make check does nothing

%install
rm -rf %{buildroot}
%makeinstall_std
find %buildroot -name \*.la|xargs chmod 644

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-, root, root)
%doc COPYING NEWS README
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-, root, root)
%doc AUTHORS CHANGES ChangeLog
%{_includedir}/*
%attr(644,root,root) %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/glibmm-%{api_version}
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4

%files -n %{libname}-static-devel
%defattr(-, root, root)
%{_libdir}/*.a

%files doc
%defattr(-, root, root)
%doc %{_datadir}/doc/glibmm-%{api_version}


