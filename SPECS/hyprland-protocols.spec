%global hypr_name hyprland-protocols
%global debug_package %{nil}

Name:           %{hypr_name}-devel
Version:        0.7.0
Release:        1%{?dist}
Summary:        Wayland protocol extensions for Hyprland.

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprland-protocols/
Source0:        https://github.com/hyprwm/hyprland-protocols/archive/refs/tags/v%{version}.tar.gz#/%{hypr_name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc-c++

%description
Wayland protocol extensions for Hyprland.

%prep
%setup -q -n %{hypr_name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%{_datadir}/hyprland-protocols/
%{_datadir}/pkgconfig/hyprland-protocols.pc

%changelog
* Fri Aug 21 2026 Veldogar v0.7.0
- Initial version
