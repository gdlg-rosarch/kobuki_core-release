Name:           ros-kinetic-kobuki-driver
Version:        0.7.8
Release:        0%{?dist}
Summary:        ROS kobuki_driver package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/kobuki_driver
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-ecl-command-line
Requires:       ros-kinetic-ecl-converters
Requires:       ros-kinetic-ecl-devices
Requires:       ros-kinetic-ecl-geometry
Requires:       ros-kinetic-ecl-mobile-robot
Requires:       ros-kinetic-ecl-sigslots
Requires:       ros-kinetic-ecl-time
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-ecl-build
BuildRequires:  ros-kinetic-ecl-command-line
BuildRequires:  ros-kinetic-ecl-converters
BuildRequires:  ros-kinetic-ecl-devices
BuildRequires:  ros-kinetic-ecl-geometry
BuildRequires:  ros-kinetic-ecl-mobile-robot
BuildRequires:  ros-kinetic-ecl-sigslots
BuildRequires:  ros-kinetic-ecl-time

%description
C++ driver library for Kobuki: Pure C++ driver library for Kobuki. This is for
those who do not wish to use ROS on their systems.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sun Apr 02 2017 Daniel Stonier <stonier@yujinrobot.com> - 0.7.8-0
- Autogenerated by Bloom

* Wed Mar 29 2017 Daniel Stonier <stonier@yujinrobot.com> - 0.7.7-0
- Autogenerated by Bloom

* Mon Mar 27 2017 Daniel Stonier <stonier@yujinrobot.com> - 0.7.6-0
- Autogenerated by Bloom

* Fri Mar 03 2017 Daniel Stonier <stonier@yujinrobot.com> - 0.7.5-0
- Autogenerated by Bloom

* Thu Feb 23 2017 Daniel Stonier <stonier@yujinrobot.com> - 0.7.4-0
- Autogenerated by Bloom

* Thu Feb 23 2017 Daniel Stonier <stonier@yujinrobot.com> - 0.7.3-0
- Autogenerated by Bloom

* Wed Nov 09 2016 Daniel Stonier <stonier@yujinrobot.com> - 0.7.2-0
- Autogenerated by Bloom

* Fri May 06 2016 Daniel Stonier <stonier@yujinrobot.com> - 0.7.1-0
- Autogenerated by Bloom

* Fri May 06 2016 Daniel Stonier <stonier@yujinrobot.com> - 0.7.0-0
- Autogenerated by Bloom

