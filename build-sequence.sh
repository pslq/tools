#!/bin/bash
(
  cd python-3.6.4
  rpmbuild -bb --clean SPECS/python.spec 
)
(
  cd openblas
  rpmbuild -bb --clean SPECS/openblas-pq.spec
)
(
  cd cython-0.27.3
  rpmbuild -bb --clean SPECS/cython.spec
)
(
  cd setuptools
  rpmbuild -bb --clean SPECS/setuptools.spec
)
(
  cd pip
  rpmbuild -bb --clean SPECS/pip.spec 
)
(
  cd six
  rpmbuild -bb SPECS/six.spec 
)
(
  cd numpy-1.14.0
  rpmbuild -bb --clean SPECS/numpy.spec 

)
(
  cd pandas-0.22.0
  rpmbuild -bb --clean SPECS/pandas.spec
)
(
  cd scipy-1.0.0
  rpmbuild -bb --clean SPECS/scipy.spec
)
(
  cd h5py-2.7.1
  rpmbuild -bb SPECS/h5py.spec
)
(
  cd matplotlib-2.1.2
  rpmbuild -bb SPECS/matplotlib.spec 
) 
(
  cd protobuf-3.5.1
  rpmbuild -bb SPECS/protobuf.spec
)
(
  cd bazel
  rpmbuild -bb SPECS/bazel.spec 
)
(
  cd pyyaml
  rpmbuild -bb SPECS/pyyaml.spec 
)
(
  cd combo
  pip download wheel Markdown werkzeug bleach
)
  
