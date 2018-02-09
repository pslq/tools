#!/bin/bash
source  /etc/profile.d/comp_vars.sh
(
  CURDIR="$(pwd)"
  mkdir -p buildroot/DEBIAN
  install -d -o root -g root -m 755 buildroot/etc/profile.d
  install -d -o root -g root -m 755 buildroot/etc/ld.so.conf.d
  cp control buildroot/DEBIAN
  echo 'export PATH="/opt/oss-mldl/bin:${PATH}"' >> buildroot/etc/profile.d/oss-mldl.sh
  echo 'export PKG_CONFIG_PATH="${PKG_CONFIG_PATH}:/opt/oss-mldl/lib/pkgconfig"' >> buildroot/etc/profile.d/oss-mldl.sh
  echo 'export LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:/opt/oss-mldl/lib"' >> buildroot/etc/profile.d/oss-mldl.sh

  echo '/opt/oss-mldl/lib' > buildroot/etc/ld.so.conf.d/oss-mldl.conf

  tar -zxpvf SOURCES/Python-3.6.4.tgz
  (
    cd Python-3.6.4
    ./configure --with-threads --enable-ipv6 --enable-loadable-sqlite-extensions \
      --enable-optimizations --enable-shared --prefix=/opt/oss-mldl
    make -j 20
    make install DESTDIR="${CURDIR}/buildroot"
  )
  dpkg-deb --build buildroot python3-pslq-3.6.4.deb && rm -rf Python-3.6.4 buildroot

)
