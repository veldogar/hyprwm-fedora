Name:           hyprwire
Version:        0.3.1
Release:        1%{?dist}
Summary:        Hyprland utilities library used across the ecosystem

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprwire/
Source0:        https://github.com/hyprwm/hyprwire/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pugixml-devel
BuildRequires:  hyprutils-devel
BuildRequires:  libffi-devel

%description
A fast and consistent wire protocol for IPC

%package devel
Summary:        Development files for hyprwire
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for hyprwire.

%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%cmake_build

%install
%cmake_install

%files
%{_libdir}/libhyprwire.so.*

%license LICENSE
%doc README.md

%files devel
%{_bindir}/hyprwire-scanner
%{_includedir}/hyprwire/
%{_libdir}/libhyprwire.so
%{_libdir}/pkgconfig/hyprwire.pc
%{_libdir}/pkgconfig/hyprwire-scanner.pc
%{_libdir}/cmake/hyprwire-scanner/

%changelog
* Fri Aug 21 2026 Veldogar v0.3.1
- Initial version
