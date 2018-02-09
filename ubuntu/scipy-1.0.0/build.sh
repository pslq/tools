#!/bin/bash
source  /etc/profile.d/comp_vars.sh
export F77FLAGS="${F77FLAGS} -shared"
export CFLAGS="${CFLAGS} -shared"
export CXXFLAGS="${CXXFLAGS} -shared"
export FCFLAGS="${CFLAGS} -shared"
export CPPFLAGS="-I/opt/oss-mldl/include"
export LDFLAGS="${LDFLAGS} -shared"
export LIBS="${LIBS} -shared"

(
  CURDIR="$(pwd)"
  mkdir -p buildroot/DEBIAN
  cp control buildroot/DEBIAN
  tar -zxpvf SOURCES/scipy-1.0.0.tar.gz 

  (
    cd scipy-1.0.0
    /opt/oss-mldl/bin/python3 setup.py build
    /opt/oss-mldl/bin/python3 setup.py install --root ${CURDIR}/buildroot
  )
  dpkg-deb --build  buildroot scipy-pslq-1.0.0.deb && rm -rf scipy-1.0.0 buildroot

)

