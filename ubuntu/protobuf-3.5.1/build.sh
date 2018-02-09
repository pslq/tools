#!/bin/bash
source  /etc/profile.d/comp_vars.sh
(
  CURDIR="$(pwd)"
  mkdir -p buildroot/DEBIAN
  cp control buildroot/DEBIAN
  tar -zxpvf SOURCES/protobuf-3.5.1.tar.gz
  (
    cd protobuf-3.5.1
    ./configure --prefix=/opt/oss-mldl --with-zlib --enable-shared --enable-static
    make -j 20
    make install DESTDIR=${CURDIR}/buildroot
    (
      cd python
      /opt/oss-mldl/bin/python3 setup.py build
      /opt/oss-mldl/bin/python3 setup.py install --root ${CURDIR}/buildroot
    )

  )
  dpkg-deb --build  buildroot protobuf-pslq-3.5.1.deb && rm -rf protobuf-3.5.1 buildroot

)

