#!/bin/bash
source  /etc/profile.d/comp_vars.sh
(
  CURDIR="$(pwd)"
  mkdir -p buildroot/DEBIAN
  cp control buildroot/DEBIAN
  install -d -o root -g root buildroot/opt/oss-mldl/lib

  tar -zxpvf ./SOURCES/v0.2.20.tar.gz
  (
    cd OpenBLAS-0.2.20
    export NMAX="NUM_THREADS=128"
    export USE_THREAD=1 
    export USE_OPENMP=1 
    export USE_MASS=1 
    make
    make install PREFIX=${CURDIR}/buildroot/opt/oss-mldl

  )
  dpkg-deb --build  buildroot openblas-pslq-0.2.20.deb && rm -rf OpenBLAS-0.2.20 buildroot

)
