Name:           hyprcursor
Version:        0.1.13
Release:        1%{?dist}
Summary:        The hyprland cursor format, library and utilities.

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprcursor/
Source0:        https://github.com/hyprwm/hyprcursor/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hyprlang-devel
BuildRequires:  libzip-devel
BuildRequires:  librsvg2-devel
BuildRequires:  tomlplusplus-devel
BuildRequires:  cairo-devel

%description
The hyprland cursor format, library and utilities.

%package devel
Summary:        Development files for hyprcursor
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for hyprcursor.

%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%cmake_build

%install
%cmake_install

%files
%{_bindir}/hyprcursor-util
%{_libdir}/libhyprcursor.so.*

%license LICENSE
%doc README.md

%files devel
%{_includedir}/hyprcursor.hpp
%{_includedir}/hyprcursor/
%{_libdir}/libhyprcursor.so
%{_libdir}/pkgconfig/hyprcursor.pc

%changelog
* Fri Aug 21 2026 Veldogar v0.1.13
- Initial version
