#!/bin/bash
source  /etc/profile.d/comp_vars.sh
(
  CURDIR="$(pwd)"
  mkdir -p buildroot/DEBIAN
  cp control buildroot/DEBIAN
  tar -zxpvf SOURCES/Cython-0.27.3.tar.gz
  (
    cd Cython-0.27.3
    /opt/oss-mldl/bin/python3 setup.py build
    /opt/oss-mldl/bin/python3 setup.py install --root ${CURDIR}/buildroot
  )
  dpkg-deb --build  buildroot cython-pslq-0.27.3.deb && rm -rf Cython-0.27.3 buildroot

)

