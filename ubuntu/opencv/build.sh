#!/bin/bash
source /etc/profile.d/comp_vars.sh
export OpenBLAS_HOME=/opt/oss-mldl
export CUDA_NVCC_FLAGS="--expt-relaxed-constexpr"


CUR_DIR=$(pwd)
mkdir -p buildroot/DEBIAN
unzip 3.4.0.zip
# git clone --recursive https://github.com/opencv/opencv.git
(
  rm -rf opencv-3.4.0/build
  mkdir opencv-3.4.0/build
  cd opencv-3.4.0/build
  cmake \
    -DAT_PATH=/opt/at10.0  \
    -D BUILD_TESTS=OFF -D BUILD_PERF_TESTS=OFF -D BUILD_opencv_ts=OFF \
    -D CMAKE_BUILD_TYPE=Release \
    -DOpenBLAS_HOME=/opt/oss-mldl \
    -DCUDA_NVCC_FLAGS="--expt-relaxed-constexpr" \
    -DProtobuf_PROTOC_EXECUTABLE='/opt/oss-mldl/bin/protoc' \
    -D CMAKE_INSTALL_PREFIX=/opt/oss-mldl \
    -D PYTHON3_EXECUTABLE=/opt/oss-mldl/bin/python3 \
    -D WITH_CUDA=ON -D ENABLE_FAST_MATH=1 \
    -D CUDA_FAST_MATH=1 -D WITH_CUBLAS=1 \
    -D INSTALL_PYTHON_EXAMPLES=ON  -D BUILD_EXAMPLES=ON .. 
  make DESTDIR=${CUR_DIR}/buildroot -j 8 install
)
dpkg-deb --build  buildroot opencv-pslq-3.4.0.deb && rm -rf opencv-3.4.0 buildroot

