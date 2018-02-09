#!/bin/bash
source  /etc/profile.d/comp_vars.sh

(
  CURDIR="$(pwd)"
  mkdir -p buildroot/DEBIAN
  install -d -o root -g root -m 0755 buildroot/opt/oss-mldl/bin
  cp control buildroot/DEBIAN
  mkdir -p bazel-0.9.0
  (
    cd bazel-0.9.0
    unzip ../SOURCES/bazel-0.9.0-dist.zip
    PATH="/opt/oss-mldl/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin:/opt/ibm/xlf/15.1.6/bin:/opt/ibm/xlC/13.1.6/bin:/opt/ibm/xlf/15.1.5/bin:/opt/ibm/xlC/13.1.5/bin" ./compile.sh
    cp output/bazel ${CURDIR}/buildroot/opt/oss-mldl/bin
  )
  dpkg-deb --build  buildroot bazel-pslq-0.9.0.deb && rm -rf bazel-0.9.0 buildroot

)

