%define	major 2
%define	libname %mklibname ctemplate %{major}
%define	develname %mklibname ctemplate -d

Name:		ctemplate
Version:	2.2
Release:	2
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



%changelog
* Mon Mar 26 2012 Andrey Bondrov <abondrov@mandriva.org> 2.0-1mdv2012.0
+ Revision: 786981
- New version 2.0

* Fri Feb 03 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.0-2
+ Revision: 770846
- remove .la files
- dont build static libs

* Wed Oct 05 2011 Andrey Bondrov <abondrov@mandriva.org> 1.0-1
+ Revision: 703085
- New version: 1.0

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.96-2mdv2011.0
+ Revision: 610174
- rebuild

* Tue Oct 27 2009 Ahmad Samir <ahmadsamir@mandriva.org> 0.96-1mdv2010.1
+ Revision: 459501
- New release 0.96

* Mon May 18 2009 Oden Eriksson <oeriksson@mandriva.com> 0.94-1mdv2010.0
+ Revision: 376957
- 0.94

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri May 02 2008 Oden Eriksson <oeriksson@mandriva.com> 0.90-1mdv2009.0
+ Revision: 200403
- 0.90

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Oct 11 2007 Oden Eriksson <oeriksson@mandriva.com> 0.8-1mdv2008.1
+ Revision: 96986
- 0.8
- new devel naming

* Sun Jun 24 2007 Oden Eriksson <oeriksson@mandriva.com> 0.6.1-1mdv2008.0
+ Revision: 43639
- Import ctemplate



* Sun Jun 24 2007 Oden Eriksson <oeriksson@mandriva.com> 0.6.1-1mdv2008.0
- 0.6.1

* Fri Jul 28 2006 Oden Eriksson <oeriksson@mandriva.com> 0.2-1mdk
- 0.2

* Tue May 02 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1-1mdk
- initial Mandriva package
