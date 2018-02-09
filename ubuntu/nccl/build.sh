#!/bin/bash
source  /etc/profile.d/comp_vars.sh
(
  CURDIR="$(pwd)"
  mkdir -p buildroot/DEBIAN ${CURDIR}/buildroot/opt/oss-mldl/lib
  cp control buildroot/DEBIAN
  install -d -o root -g root buildroot/opt/oss-mldl/lib
  git clone https://github.com/NVIDIA/nccl.git
  (
    cd nccl
    make CUDA_HOME=/usr/local/cuda
    make install PREFIX=${CURDIR}/buildroot/opt/oss-mldl/lib

  )
  dpkg-deb --build  buildroot nccl-pslq-1git.deb && rm -rf nccl buildroot

)

