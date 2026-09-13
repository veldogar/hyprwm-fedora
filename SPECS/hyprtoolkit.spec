Name:           hyprtoolkit
Version:        0.6.0
Release:        1%{?dist}
Summary:        A modern C++ Wayland-native GUI toolkit

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprtoolkit/
Source0:        https://github.com/hyprwm/hyprtoolkit/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libglvnd-devel
BuildRequires:  hyprutils-devel
BuildRequires:  aquamarine-devel
BuildRequires:  hyprgraphics-devel
BuildRequires:  hyprwayland-scanner-devel
BuildRequires:  hyprlang-devel
BuildRequires:  cairo-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  pixman-devel
BuildRequires:  libdrm-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  pango-devel
BuildRequires:  iniparser-devel
BuildRequires:  abseil-cpp-devel

%description
A modern C++ Wayland-native GUI toolkit

%package devel
Summary:        Development files for hyprtoolkit
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for hyprtoolkit.

%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%cmake_build

%install
%cmake_install

%files
%{_libdir}/libhyprtoolkit.so.*

%license LICENSE
%doc README.md

%files devel
%{_includedir}/hyprtoolkit/
%{_libdir}/libhyprtoolkit.so
%{_libdir}/pkgconfig/hyprtoolkit.pc

%changelog

* Thu Sep 10 2026 Veldogar v0.6.0
- Regular Update

* Fri Aug 21 2026 Veldogar v0.5.4
- Initial version
