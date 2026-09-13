%global glaze_version	7.2.0

Name:           Hyprland
Version:        0.56.2
Release:        2%{?dist}
Summary:        Hyprland is an independent, highly customizable, dynamic tiling Wayland compositor.

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprland/
Source0:        https://github.com/hyprwm/hyprland/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source10:       https://github.com/stephenberry/glaze/archive/refs/tags/v%{glaze_version}.tar.gz#/glaze-%{glaze_version}.tar.gz
Patch0:         hyprland-local-glaze.patch

BuildRequires:  git
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  udis86-devel
BuildRequires:  libglvnd-devel
BuildRequires:  glslang-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libuuid-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  cairo-devel
BuildRequires:  pango-devel
BuildRequires:  pixman-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libdrm-devel
BuildRequires:  libinput-devel
BuildRequires:  libeis-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  glib2-devel
BuildRequires:  re2-devel
BuildRequires:  muParser-devel
BuildRequires:  lcms2-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  xcb-util-errors-devel
BuildRequires:  readline-devel
BuildRequires:  tomlplusplus-devel
BuildRequires:  lua-devel

BuildRequires:  aquamarine-devel
BuildRequires:  hyprlang-devel
BuildRequires:  hyprcursor-devel
BuildRequires:  hyprgraphics-devel
BuildRequires:  hyprutils-devel
BuildRequires:  hyprwayland-scanner-devel
BuildRequires:  hyprwire-devel
BuildRequires:	hyprland-protocols-devel

%description
Hyprland is an independent, highly customizable, dynamic tiling Wayland compositor that doesn't sacrifice on its looks.

%package devel
Summary:        Development files for Hyprland
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for Hyprland.

# CMakeLists.txt will be patched to use glaze-src in the subprojects folder
%prep
%autosetup -p1

# glaze -> subprojects
tar xzf %{SOURCE10} -C subprojects --transform='s,^glaze-%{glaze_version},glaze-src,'

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%cmake_build

%install
%cmake_install

rm %{buildroot}%{_bindir}/hyprland
ln -s Hyprland %{buildroot}%{_bindir}/hyprland

%files
%{_bindir}/hyprctl
%{_bindir}/hyprland
%{_bindir}/Hyprland
%{_bindir}/hyprpm
%{_bindir}/start-hyprland

%{_datadir}/hypr/
%{_datadir}/bash-completion/completions/hyprctl
%{_datadir}/bash-completion/completions/hyprpm
%{_datadir}/fish/vendor_completions.d/hyprctl.fish
%{_datadir}/fish/vendor_completions.d/hyprpm.fish
%{_datadir}/zsh/site-functions/_hyprctl
%{_datadir}/zsh/site-functions/_hyprpm
%{_datadir}/man/man1/Hyprland.1.gz
%{_datadir}/man/man1/hyprctl.1.gz
%{_datadir}/wayland-sessions/hyprland-uwsm.desktop
%{_datadir}/wayland-sessions/hyprland.desktop
%{_datadir}/xdg-desktop-portal/hyprland-portals.conf

%license LICENSE
%doc README.md

%files devel
%{_includedir}/hyprland/
%{_datadir}/pkgconfig/hyprland.pc

%changelog
* Fri Aug 21 2026 Veldogar v0.56.2
- Initial version 
