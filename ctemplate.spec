%define	major 2
%define	libname %mklibname ctemplate %{major}
%define	develname %mklibname ctemplate -d

Name:		ctemplate
Version:	2.2
Release:	1
Summary:	Simple but powerful template language for C++
Group:		System/Libraries
License:	BSD
URL:		https://code.google.com/p/ctemplate/
Source0:	https://ctemplate.googlecode.com/files/%{name}-%{version}.tar.gz

%description
The ctemplate package contains a library implementing a simple but
powerful template language for C++.  It emphasizes separating logic
from presentation: it is impossible to embed application logic in this
template language.  This limits the power of the template language
without limiting the power of the template *system*.  Indeed, Google's
"main" web search uses this system exclusively for formatting output.

%package -n	%{libname}
Summary:	Simple but powerful template language for C++
Group:		System/Libraries

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
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{version}

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
%__make check

%install
%__rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%{_docdir}/%{name}-%{version}/INSTALL

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc %{_docdir}/%{name}-%{version}
%{_includedir}/ctemplate/*
%{_bindir}/diff_tpl_auto_escape
%{_bindir}/make_tpl_varnames_h
%{_bindir}/template-converter
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%if %{mdvver} < 201200
%{_libdir}/*.la
%endif
