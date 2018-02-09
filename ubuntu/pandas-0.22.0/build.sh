#!/bin/bash
source  /etc/profile.d/comp_vars.sh

(
  CURDIR="$(pwd)"
  mkdir -p buildroot/DEBIAN
  cp control buildroot/DEBIAN
  tar -zxpvf ./SOURCES/pandas-0.22.0.tar.gz

  (
    cd pandas-0.22.0
    /opt/oss-mldl/bin/python3 setup.py build
    /opt/oss-mldl/bin/python3 setup.py install --root ${CURDIR}/buildroot

  )
  dpkg-deb --build  buildroot pandas-pslq-0.22.0.deb && rm -rf pandas-0.22.0 buildroot

)

