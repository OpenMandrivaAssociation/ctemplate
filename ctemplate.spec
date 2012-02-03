%define	major 0
%define libname %mklibname ctemplate %{major}
%define develname %mklibname ctemplate -d

Summary:	Simple but powerful template language for C++
Name:		ctemplate
Version:	1.0
Release:	%mkrel 2
Group:		System/Libraries
License:	BSD
URL:		http://code.google.com/p/google-ctemplate/
Source0:		http://google-ctemplate.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	autoconf

%description
The ctemplate package contains a library implementing a simple but
powerful template language for C++.  It emphasizes separating logic
from presentation: it is impossible to embed application logic in this
template language.  This limits the power of the template language
without limiting the power of the template *system*.  Indeed, Google's
"main" web search uses this system exclusively for formatting output.

%package -n	%{libname}
Summary:	Simple but powerful template language for C++
Group:          System/Libraries

%description -n	%{libname}
The ctemplate package contains a library implementing a simple but
powerful template language for C++.  It emphasizes separating logic
from presentation: it is impossible to embed application logic in this
template language.  This limits the power of the template language
without limiting the power of the template *system*.  Indeed, Google's
"main" web search uses this system exclusively for formatting output.

%package -n	%{develname}
Summary:	Development files for the %{name} library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Provides:	lib%{name}-devel = %{version}
Requires:	%{libname} = %{version}
Obsoletes:	%{mklibname ctemplate 0 -d}

%description -n	%{develname}
The ctemplate-devel package contains static and debug libraries and header
files for developing applications that use the ctemplate package.

%prep

%setup -q

%build
export PTHREAD_LIBS="-lpthread"
%configure2_5x -enable-static=no

%make

%check
make check

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

# cleanup
rm -rf %{buildroot}%{_docdir}/ctemplate-*

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL README doc/*
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/ctemplate/*
%{_bindir}/diff_tpl_auto_escape
%{_bindir}/make_tpl_varnames_h
%{_bindir}/template-converter
%{_libdir}/*.so
#%{_libdir}/*.a
#%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
