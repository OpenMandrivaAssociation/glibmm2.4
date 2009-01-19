%define version 2.19.2
%define release %mkrel 1

%define pkgname	glibmm
%define api_version 2.4
%define major 1
%define libname_orig %mklibname %{pkgname} %{api_version}
%define libname %mklibname %{pkgname} %{api_version} %{major}
%define libnamedev %mklibname -d %{pkgname} %{api_version}
%define libnamestaticdev %mklibname -s -d %{pkgname} %{api_version}

Name:		%{pkgname}%{api_version}
Summary:	C++ interface for glib
Version:	%{version}
Release:	%{release}
License:	LGPLv2+
Group:		System/Libraries
URL:		http://gtkmm.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:		http://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.bz2
BuildRequires:	glib2-devel >= 2.17.4
BuildRequires:	libsigc++2.0-devel
BuildRequires:	doxygen libxslt-proc

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


%package	-n %{libnamedev}
Summary:	Headers and development files of %{pkgname}
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}
Provides:	%{pkgname}%{api_version}-devel = %{version}-%{release}
Provides:	%{libname_orig}-devel = %{version}-%{release}
Obsoletes: %mklibname -d %{pkgname} %{api_version} 1

%description	-n %{libnamedev}
This package contains the headers and development files that are needed,
when trying to develop or compile applications which need %{pkgname}.


%package	-n %{libnamestaticdev}
Summary:	Static libraries of %{pkgname}
Group:		Development/GNOME and GTK+
Requires:	%{libnamedev} = %{version}
Provides:	%{libname_orig}-static-devel = %{version}-%{release}
Obsoletes: %mklibname -s -d %{pkgname} %{api_version} 1

%description	-n %{libnamestaticdev}
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

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-, root, root)
%doc COPYING NEWS README
%{_libdir}/libglibmm*%{api_version}.so.%{major}*
%{_libdir}/libgiomm*%{api_version}.so.%{major}*

%files -n %{libnamedev}
%defattr(-, root, root)
%doc AUTHORS ChangeLog
%{_includedir}/*
%attr(644,root,root) %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/giomm-%api_version
%{_libdir}/glibmm-%{api_version}
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4
%_datadir/devhelp/books/glibmm-2.4

%files -n %{libnamestaticdev}
%defattr(-, root, root)
%{_libdir}/*.a

%files doc
%defattr(-, root, root)
%doc %{_datadir}/doc/glibmm-%{api_version}


