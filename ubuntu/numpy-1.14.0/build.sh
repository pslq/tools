#!/bin/bash
source  /etc/profile.d/comp_vars.sh
(
  CURDIR="$(pwd)"
  mkdir -p buildroot/DEBIAN
  cp control buildroot/DEBIAN
  unzip ./SOURCES/numpy-1.14.0.zip
  (
    cd numpy-1.14.0
    /opt/oss-mldl/bin/python3 setup.py build
    /opt/oss-mldl/bin/python3 setup.py install --root ${CURDIR}/buildroot
  )
  dpkg-deb --build  buildroot numpy-pslq-1.14.0.deb && rm -rf numpy-1.14.0 buildroot

)

