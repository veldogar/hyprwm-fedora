Name:           hyprlang
Version:        0.6.8
Release:        1%{?dist}
Summary:        The official implementation library for the hypr config language.

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprlang/
Source0:        https://github.com/hyprwm/hyprlang/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  hyprutils-devel
BuildRequires:  gcc-c++

%description
The official implementation library for the hypr config language.

%package devel
Summary:        Development files for hyprlang
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for hyprlang.

%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%cmake_build

%install
%cmake_install

%files
%{_libdir}/libhyprlang.so.*

%license LICENSE
%doc README.md

%files devel
%{_includedir}/hyprlang.hpp
%{_libdir}/libhyprlang.so
%{_libdir}/pkgconfig/hyprlang.pc

%changelog
* Fri Aug 21 2026 Veldogar v0.6.8
- Initial version
