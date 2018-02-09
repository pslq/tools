#!/bin/bash
source  /etc/profile.d/comp_vars.sh
(
  CURDIR="$(pwd)"
  mkdir -p buildroot/DEBIAN
  cp control buildroot/DEBIAN
  tar -zxpvf fftw-3.3.7.tar.gz
  (
    cd fftw-3.3.7
    ./configure --with-g77-wrappers --enable-threads --enable-threads --enable-openmp --enable-mpi --enable-altivec --enable-vsx --enable-single --prefix=/opt/oss-mldl
    make -j 20
    make install DESTDIR="${CURDIR}/buildroot"
  )
  dpkg-deb --build  buildroot fftw-pslq-3.3.7.deb && rm -rf fftw-3.3.7 buildroot

)

