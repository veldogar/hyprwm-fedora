Name:           hyprgraphics
Version:        0.5.1
Release:        1%{?dist}
Summary:        Hyprland graphics / resource utilities

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprgraphics/
Source0:        https://github.com/hyprwm/hyprgraphics/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libglvnd-devel
BuildRequires:  hyprutils-devel
BuildRequires:  cairo-devel
BuildRequires:  pango-devel
BuildRequires:  pixman-devel
BuildRequires:  libdrm-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libwebp-devel
BuildRequires:  file-devel
BuildRequires:  librsvg2-devel

%description
Hyprland graphics / resource utilities

%package devel
Summary:        Development files for hyprgraphics
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for hyprgraphics.

%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%cmake_build

%install
%cmake_install

%files
%{_libdir}/libhyprgraphics.so.*

%license LICENSE
%doc README.md

%files devel
%{_includedir}/hyprgraphics/
%{_libdir}/libhyprgraphics.so
%{_libdir}/pkgconfig/hyprgraphics.pc

%changelog
* Fri Aug 21 2026 Veldogar v0.5.1
- Initial version
