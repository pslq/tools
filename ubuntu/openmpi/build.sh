#!/bin/bash
source  /etc/profile.d/comp_vars.sh
(
  CURDIR="$(pwd)"
  mkdir -p buildroot/DEBIAN
  cp control buildroot/DEBIAN
  tar -zxpvf SOURCES/openmpi-3.0.0.tar.gz
  (
    cd openmpi-3.0.0
    ./configure \
      --with-slurm --with-zlib=/opt/at10.0 --with-cuda=/usr/local/cuda \
      --enable-cxx-exceptions --enable-static \
      --enable-mpi-cxx --enable-mpi-cxx-seek --prefix=/opt/oss-mldl
    make -j 20
    make
    make install DESTDIR=${CURDIR}/buildroot


  )
  dpkg-deb --build  buildroot openmpi-pslq-3.0.0.deb && rm -rf openmpi-3.0.0 buildroot

)

