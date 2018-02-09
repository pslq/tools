#!/bin/bash
source  /etc/profile.d/comp_vars.sh

(
  CURDIR="$(pwd)"
  mkdir -p buildroot/DEBIAN
  cp control buildroot/DEBIAN
  tar -zxpvf hdf5-1.10.1.tar.gz

  (
    cd hdf5-1.10.1
    ./configure --with-zlib=/opt/at10.0 --with-pthread --enable-deprecated-symbols --enable-parallel --enable-optimization=high   --prefix=/opt/oss-mldl
    make -j 20
    make install DESTDIR=${CURDIR}/buildroot

  )
  dpkg-deb --build  buildroot hdf5-pslq-1.10.1.deb && rm -rf hdf5-1.10.1 buildroot

)

