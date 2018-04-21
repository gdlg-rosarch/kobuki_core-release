# Script generated with Bloom
pkgdesc="ROS - Utilities for flashing and enabling Kobuki's USB connection. This package contains tools for flashing the Kobuki's FTDI chip (usually done at the factory). The special firmware for the FTDI chip (USB to serial converter) enables it to appear as /dev/kobuki on the user's PC."
url='http://ros.org/wiki/kobuki_ftdi'

pkgname='ros-kinetic-kobuki-ftdi'
pkgver='0.7.8_2'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('libftdi'
'libusb-compat'
'pkg-config'
'ros-kinetic-catkin'
'ros-kinetic-ecl-command-line'
)

depends=('libftdi'
'libusb-compat'
'ros-kinetic-ecl-command-line'
)

conflicts=()
replaces=()

_dir=kobuki_ftdi
source=()
md5sums=()

prepare() {
    cp -R $startdir/kobuki_ftdi $srcdir/kobuki_ftdi
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

