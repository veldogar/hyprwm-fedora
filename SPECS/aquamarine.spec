Name:           aquamarine
Version:        0.15.0
Release:        1%{?dist}
Summary:        Aquamarine is a very light linux rendering backend library

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/aquamarine/
Source0:        https://github.com/hyprwm/aquamarine/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  hyprutils-devel
BuildRequires:  hyprwayland-scanner-devel
BuildRequires:  gcc-c++
BuildRequires:  pixman-devel
BuildRequires:  libseat-devel
BuildRequires:  libinput-devel
BuildRequires:  libdrm-devel
BuildRequires:  libudev-devel
BuildRequires:  hwdata-devel
BuildRequires:  libglvnd-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  libdisplay-info-devel

%description
Aquamarine is a very light linux rendering backend library

%package devel
Summary:        Development files for aquamarine
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for aquamarine.

%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%cmake_build

%install
%cmake_install

%files
%{_libdir}/libaquamarine.so.*

%license LICENSE
%doc README.md

%files devel
%{_includedir}/aquamarine/
%{_libdir}/libaquamarine.so
%{_libdir}/pkgconfig/aquamarine.pc

%changelog
* Fri Aug 21 2026 Veldogar v0.15.0
- Initial version
