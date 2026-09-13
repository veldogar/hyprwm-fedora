Name:           hyprpaper
Version:        0.8.4
Release:        2%{?dist}
Summary:        Hyprpaper is a wayland wallpaper utility with IPC controls

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprpaper/
Source0:        https://github.com/hyprwm/hyprpaper/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  git
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  aquamarine-devel
BuildRequires:  hyprwayland-scanner-devel
BuildRequires:  hyprutils-devel
BuildRequires:  hyprgraphics-devel
BuildRequires:  hyprtoolkit-devel
BuildRequires:  hyprlang-devel
BuildRequires:  hyprwire-devel
BuildRequires:  pixman-devel
BuildRequires:  libdrm-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  file-devel
BuildRequires:  cairo-devel
BuildRequires:  libglvnd-devel

%description
Hyprpaper is a wayland wallpaper utility with IPC controls.

%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%cmake_build

%install
%cmake_install

%files
%{_bindir}/hyprpaper
%{_prefix}/lib/systemd/user/hyprpaper.service

%license LICENSE
%doc README.md

%changelog
* Thu Sep 10 2026 Veldogar v0.8.4-2
- Recompile: ABI change in hyprtoolkit v0.5.4 -> v0.6.0

* Fri Aug 21 2026 Veldogar v0.8.4
- Initial version
