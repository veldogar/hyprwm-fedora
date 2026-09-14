Name:           hyprutils
Version:        0.14.2
Release:        1%{?dist}
Summary:        Hyprland utilities library used across the ecosystem

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprutils/
Source0:        https://github.com/hyprwm/hyprutils/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pixman-devel

%description
Hyprland utilities library used across the ecosystem.

%package devel
Summary:        Development files for hyprutils
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for hyprutils.

%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%cmake_build

%install
%cmake_install

%files

%license LICENSE
%doc README.md

%{_libdir}/libhyprutils.so.*

%files devel
%{_libdir}/libhyprutils.so
%{_libdir}/pkgconfig/hyprutils.pc
%{_includedir}/hyprutils/

%changelog

* Thu Sep 10 2026 Veldogar v0.14.2
- Regular Update

* Fri Aug 21 2026 Veldogar v0.14.1
- Initial version
