# Script generated with Bloom
pkgdesc="ROS - C++ driver library for Kobuki: Pure C++ driver library for Kobuki. This is for those who do not wish to use ROS on their systems."
url='http://ros.org/wiki/kobuki_driver'

pkgname='ros-kinetic-kobuki-driver'
pkgver='0.7.8_2'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-ecl-build'
'ros-kinetic-ecl-command-line'
'ros-kinetic-ecl-converters'
'ros-kinetic-ecl-devices'
'ros-kinetic-ecl-geometry'
'ros-kinetic-ecl-mobile-robot'
'ros-kinetic-ecl-sigslots'
'ros-kinetic-ecl-time'
)

depends=('ros-kinetic-ecl-command-line'
'ros-kinetic-ecl-converters'
'ros-kinetic-ecl-devices'
'ros-kinetic-ecl-geometry'
'ros-kinetic-ecl-mobile-robot'
'ros-kinetic-ecl-sigslots'
'ros-kinetic-ecl-time'
)

conflicts=()
replaces=()

_dir=kobuki_driver
source=()
md5sums=()

prepare() {
    cp -R $startdir/kobuki_driver $srcdir/kobuki_driver
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

