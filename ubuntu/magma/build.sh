#!/bin/bash
export PATH="/opt/oss-mldl/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin:/opt/bazel/output:/opt/ibm/xlf/15.1.5/bin:/opt/ibm/xlC/13.1.5/bin"
(
  CURDIR="$(pwd)"
  mkdir -p buildroot/DEBIAN
  cp control buildroot/DEBIAN
  tar -zxpvf magma-2.3.0.tar.gz
  (
    cd magma-2.3.0
    make -j 20
    make install DESTDIR="${CURDIR}/buildroot"
  )
  dpkg-deb --build buildroot magma-pslq-2.3.0.deb && rm -rf buildroot magma-2.3.0

)
