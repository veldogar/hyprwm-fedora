Name:           hypridle
Version:        0.1.8
Release:        1%{?dist}
Summary:        Hyprland's idle daemon

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hypridle/
Source0:        https://github.com/hyprwm/hypridle/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hyprland-protocols-devel
BuildRequires:  hyprlang-devel
BuildRequires:  hyprutils-devel
BuildRequires:  hyprwayland-scanner-devel
BuildRequires:  sdbus-cpp-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel

%description
A fast and consistent wire protocol for IPC

%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%cmake_build

%install
%cmake_install

%files
%{_bindir}/hypridle
%{_prefix}/lib/systemd/user/hypridle.service
%{_datadir}/hypr/hypridle.conf

%license LICENSE
%doc README.md

%changelog
* Fri Aug 21 2026 Veldogar v0.1.8
- Initial version
