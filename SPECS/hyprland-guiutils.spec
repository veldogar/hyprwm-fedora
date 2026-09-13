Name:           hyprland-guiutils
Version:        0.2.2
Release:        2%{?dist}
Summary:        Hyprland GUI utilities (successor to hyprland-qtutils)

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprland-guiutils/
Source0:        https://github.com/hyprwm/hyprland-guiutils/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  aquamarine-devel
BuildRequires:  hyprgraphics-devel
BuildRequires:  hyprutils-devel
BuildRequires:  hyprlang-devel
BuildRequires:  hyprtoolkit-devel
BuildRequires:  libdrm-devel
BuildRequires:  pixman-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  cairo-devel

%description
Hyprland GUI utilities (successor to hyprland-qtutils)

%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%cmake_build

%install
%cmake_install

%files
%{_bindir}/hyprland-dialog
%{_bindir}/hyprland-donate-screen
%{_bindir}/hyprland-run
%{_bindir}/hyprland-update-screen
%{_bindir}/hyprland-welcome

%license LICENSE
%doc README.md

%changelog

* Thu Sep 10 2026 Veldogar v0.2.2-2
- ABI change in hyprtoolkit v0.5.4 -> v0.6.0

* Fri Aug 21 2026 Veldogar v0.2.2
- Initial version
