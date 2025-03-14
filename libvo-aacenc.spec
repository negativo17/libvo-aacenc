%define real_name vo-aacenc

Name:           lib%{real_name}
Version:        0.1.3
Release:        3%{?dist}
Summary:        VisualOn AAC encoder library
License:        ASL 2.0
URL:            http://sourceforge.net/projects/opencore-amr/

Source0:        http://downloads.sourceforge.net/opencore-amr/%{real_name}/%{real_name}-%{version}.tar.gz

BuildRequires:  gcc

%description
This library contains an encoder implementation of the Advanced Audio
Coding (AAC) audio codec. The library is based on a codec implementation
by VisualOn as part of the Stagefright framework from the Google
Android project.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{real_name}-%{version}

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

%files
%license COPYING NOTICE
%doc ChangeLog
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{real_name}.pc

%changelog
* Fri Mar 14 2025 Simone Caronni <negativo17@gmail.com> - 0.1.3-3
- Clean up SPEC file.

* Thu Sep 20 2018 Simone Caronni <negativo17@gmail.com> - 0.1.3-2
- Add GCC build requirement.

* Fri Nov 20 2015 Simone Caronni <negativo17@gmail.com> - 0.1.3-1
- First build.
