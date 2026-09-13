%global hypr_name hyprwayland-scanner

Name:           %{hypr_name}-devel
Version:        0.4.6
Release:        1%{?dist}
Summary:        A Hyprland implementation of wayland-scanner, in and for C++.

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprwayland-scanner/
Source0:        https://github.com/hyprwm/hyprwayland-scanner/archive/refs/tags/v%{version}.tar.gz#/%{hypr_name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pugixml-devel

%description
A Hyprland implementation of wayland-scanner, in and for C++.

%prep
%setup -q -n %{hypr_name}-%{version}

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%cmake_build

%install
%cmake_install

%files
%{_bindir}/hyprwayland-scanner
%{_libdir}/cmake/hyprwayland-scanner/
%{_libdir}/pkgconfig/hyprwayland-scanner.pc

%changelog
* Fri Aug 21 2026 Veldogar v0.4.6
- Initial version
