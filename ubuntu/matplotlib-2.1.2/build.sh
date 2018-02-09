#!/bin/bash                                                                                                                                                                                                                                                                    
source  /etc/profile.d/comp_vars.sh
(
  CURDIR="$(pwd)"
  mkdir -p buildroot/DEBIAN
  cp control buildroot/DEBIAN
  tar -zxpvf ./SOURCES/matplotlib-2.1.2.tar.gz
  (
    cd matplotlib-2.1.2
    /opt/oss-mldl/bin/python3 setup.py build
    /opt/oss-mldl/bin/python3 setup.py install --root ${CURDIR}/buildroot
  )
  dpkg-deb --build  buildroot matplotlib-pslq-2.1.2.deb && rm -rf matplotlib-2.1.2 buildroot

)

