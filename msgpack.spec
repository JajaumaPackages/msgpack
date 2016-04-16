Name:		msgpack
Version:	1.4.1
Release:	1%{?dist}
Summary:	Binary-based efficient object serialization library
Group:		System Environment/Libraries

License:	Boost
URL:		http://msgpack.org
Source0:	https://github.com/msgpack/msgpack-c/releases/download/cpp-%{version}/%{name}-%{version}.tar.gz

# for regenerating configure
BuildRequires:	libtool
# for %%check
BuildRequires:	gtest-devel
BuildRequires:	zlib-devel

%description
MessagePack is a binary-based efficient object serialization
library. It enables to exchange structured objects between many
languages like JSON. But unlike JSON, it is very fast and small.


%package devel
Summary:	Libraries and header files for %{name}
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Libraries and header files for %{name}


%prep
%setup -q


%build
autoreconf -f -i
%configure --disable-static
make %{?_smp_mflags}


%check
make check


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f '{}' ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%{!?_licensedir:%global license %doc}
%license LICENSE_1_0.txt COPYING
%doc AUTHORS ChangeLog NOTICE README README.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/msgpack.pc


%changelog
* Thu Apr  7 2016 Daiki Ueno <dueno@redhat.com> - 1.4.1-1
- new upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 10 2015 Neal Gompa <ngompa13{%}gmail{*}com> - 1.3.0-1
- Upgrade to 1.3.0 upstream release
- Drop unneeded patch

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.9-3
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 11 2014 Daiki Ueno <dueno@redhat.com> - 0.5.9-1
- new upstream release
- apply patch to fix int->float test failure

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan  9 2014 Daiki Ueno <dueno@redhat.com> - 0.5.8-1
- new upstream release
- remove patches that are no longer needed

* Tue Aug 27 2013 Dan Horák <dan[at]danny.cz> - 0.5.7-5
- apply upstream fix for big endians

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 15 2012 Daiki Ueno <dueno@redhat.com> - 0.5.7-1
- initial packaging for Fedora

