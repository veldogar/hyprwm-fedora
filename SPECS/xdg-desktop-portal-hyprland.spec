Name:           xdg-desktop-portal-hyprland
Version:        1.4.1
Release:        1%{?dist}
Summary:        xdg-desktop-portal backend for Hyprland

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/xdg-desktop-portal-hyprland/
Source0:        https://github.com/hyprwm/xdg-desktop-portal-hyprland/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hyprutils-devel
BuildRequires:  hyprlang-devel
BuildRequires:  hyprwayland-scanner-devel
BuildRequires:  libdrm-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  pipewire-devel
BuildRequires:  sdbus-cpp-devel
BuildRequires:  hyprland-protocols-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  libuuid-devel
BuildRequires:  mesa-libgbm-devel

%description
xdg-desktop-portal backend for Hyprland

%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%cmake_build

%install
%cmake_install

%files
%{_bindir}/hyprland-share-picker
%{_prefix}/lib/systemd/user/xdg-desktop-portal-hyprland.service
%{_libexecdir}/xdg-desktop-portal-hyprland
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.hyprland.service
%{_datadir}/xdg-desktop-portal/portals/hyprland.portal

%license LICENSE
%doc README.md

%changelog
* Fri Aug 21 2026 Veldogar v1.4.1
- Initial version
