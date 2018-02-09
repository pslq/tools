#!/bin/bash
source  /etc/profile.d/comp_vars.sh
(
  CURDIR="$(pwd)"
  mkdir -p buildroot/DEBIAN
  cp control buildroot/DEBIAN
  tar -zxpvf ./SOURCES/pillow-git_current_02042018.tgz
  (
    cd pillow-git_current_02042018
    /opt/oss-mldl/bin/python3 setup.py build
    /opt/oss-mldl/bin/python3 setup.py install --root ${CURDIR}/buildroot
  )
  dpkg-deb --build  buildroot pillow-pslq-git_current_02042018.deb && rm -rf pillow-git_current_02042018 buildroot

)

