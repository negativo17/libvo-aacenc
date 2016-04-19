Name:           libvo-aacenc
Version:        0.1.3
Release:        1%{?dist}
Summary:        VisualOn AAC encoder library
License:        ASL 2.0
URL:            http://sourceforge.net/projects/opencore-amr/

Source0:        http://downloads.sourceforge.net/opencore-amr/vo-aacenc/vo-aacenc-%{version}.tar.gz

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
%setup -qn vo-aacenc-%{version}

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name '*.la' -delete


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%{!?_licensedir:%global license %%doc}
%license COPYING NOTICE
%doc ChangeLog
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/vo-aacenc.pc


%changelog
* Fri Nov 20 2015 Simone Caronni <negativo17@gmail.com> - 0.1.3-1
- First build.
