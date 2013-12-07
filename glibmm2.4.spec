%define url_ver %(echo %{version}|cut -d. -f1,2)

%define	pkgname	glibmm
%define	api	2.4
%define major	1
%define	libname		%mklibname %{pkgname} %{api} %{major}
%define	libdefs		%mklibname %{pkgname}_generate_extra_defs %{api} %{major}
%define	libgiomm	%mklibname giomm %{api} %{major}
%define	devname		%mklibname -d %{pkgname} %{api}

Summary:	C++ interface for glib
Name:		%{pkgname}%{api}
Version:	2.36.2
Release:	4
License:	LGPLv2+
Group:		System/Libraries
Url:		http://gtkmm.sourceforge.net/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/glibmm/%{url_ver}/%{pkgname}-%{version}.tar.xz

BuildRequires:	doxygen
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(mm-common-util)
BuildRequires:	pkgconfig(sigc++-2.0)

%description
Gtkmm provides a C++ interface to the GTK+ GUI library.
%{pkgname} originally belongs to gtkmm, but is now separated,
for use with non-GUI software written in C++.

%package -n	%{libname}
Summary:	C++ interface for glib
Group:		System/Libraries

%description -n	%{libname}
This package contains a library needed to run programs dynamically
linked with %{pkgname}.

%package -n	%{libdefs}
Summary:	C++ interface for glib
Group:		System/Libraries
Conflicts:	%{_lib}glibmm2.4_1 < 2.34.1-3

%description -n	%{libdefs}
This package contains a library needed to run programs dynamically
linked with %{pkgname}.

%package -n	%{libgiomm}
Summary:	C++ interface for glib
Group:		System/Libraries
Conflicts:	%{_lib}glibmm2.4_1 < 2.34.1-3

%description -n	%{libgiomm}
This package contains a library needed to run programs dynamically
linked with %{pkgname}.

%package -n	%{devname}
Summary:	Headers and development files of %{pkgname}
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libdefs} = %{version}-%{release}
Requires:	%{libgiomm} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	mm-common >= 0.9.4
Obsoletes:	%{name}-doc < 2.34.1-3

%description -n	%{devname}
This package contains the headers and development files that are needed,
when trying to develop or compile applications which need %{pkgname}.

%prep
%setup -qn %{pkgname}-%{version}

%build
%configure2_5x \
    --enable-shared \
    --disable-static
%make

# make check does nothing

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libglibmm-%{api}.so.%{major}*

%files -n %{libdefs}
%{_libdir}/libglibmm_generate_extra_defs-%{api}.so.%{major}*

%files -n %{libgiomm}
%{_libdir}/libgiomm-%{api}.so.%{major}*

%files -n %{devname}
%doc COPYING NEWS README AUTHORS ChangeLog
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/giomm-%{api}/
%{_libdir}/glibmm-%{api}/
%{_libdir}/pkgconfig/*.pc
%doc %{_datadir}/doc/glibmm-%{api}
%doc %{_datadir}/devhelp/books/glibmm-2.4/

