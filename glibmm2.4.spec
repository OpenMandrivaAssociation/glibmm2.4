%define	pkgname	glibmm
%define	api_version 2.4
%define major	1
%define	libname	%mklibname %{pkgname} %{api_version} %{major}
%define	devname	%mklibname -d %{pkgname} %{api_version}

Name:		%{pkgname}%{api_version}
Summary:	C++ interface for glib
Version:	2.32.0
Release:	1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://gtkmm.sourceforge.net/

Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.xz
BuildRequires:	glib2-devel >= 2.30
BuildRequires:	mm-common >= 0.9.4
BuildRequires:	libsigc++2.0-devel >= 2.2.10
BuildRequires:	doxygen libxslt-proc

%description
Gtkmm provides a C++ interface to the GTK+ GUI library.
%{pkgname} originally belongs to gtkmm, but is now separated,
for use with non-GUI software written in C++.


%package -n	%{libname}
Summary:	C++ interface for glib
Group:		System/Libraries

%description -n	%{libname}
Gtkmm provides a C++ interface to the GTK+ GUI library.
%{pkgname} originally belongs to gtkmm, but is now separated,
for use with non-GUI software written in C++.

This package contains the library needed to run programs dynamically
linked with %{pkgname}.


%package -n	%{devname}
Summary:	Headers and development files of %{pkgname}
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}
Provides:	%{pkgname}%{api_version}-devel = %{version}-%{release}
Requires:	mm-common >= 0.9.4
Obsoletes:	%mklibname -d %{pkgname} %{api_version} 1

%description -n	%{devname}
This package contains the headers and development files that are needed,
when trying to develop or compile applications which need %{pkgname}.


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
%configure2_5x \
    --enable-shared \
    --disable-static
%make

# make check does nothing

%install
%makeinstall_std

%files -n %{libname}
%doc COPYING NEWS README
%{_libdir}/libglibmm*%{api_version}.so.%{major}*
%{_libdir}/libgiomm*%{api_version}.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/giomm-%{api_version}/
%{_libdir}/glibmm-%{api_version}/
%{_libdir}/pkgconfig/*.pc

%files doc
%doc %{_datadir}/doc/glibmm-%{api_version}
%{_datadir}/devhelp/books/glibmm-2.4/
