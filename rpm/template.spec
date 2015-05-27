Name:           ros-indigo-kobuki-core
Version:        0.6.1
Release:        0%{?dist}
Summary:        ROS kobuki_core package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/kobuki_core
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-kobuki-dock-drive
Requires:       ros-indigo-kobuki-driver
Requires:       ros-indigo-kobuki-ftdi
BuildRequires:  ros-indigo-catkin

%description
Non-ROS software for Kobuki, Yujin Robot's mobile research base.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed May 27 2015 Daniel Stonier <stonier@yujinrobot.com> - 0.6.1-0
- Autogenerated by Bloom

* Mon Aug 04 2014 Daniel Stonier <stonier@yujinrobot.com> - 0.6.0-0
- Autogenerated by Bloom

* Mon Aug 04 2014 Daniel Stonier <stonier@yujinrobot.com> - 0.5.3-0
- Autogenerated by Bloom

