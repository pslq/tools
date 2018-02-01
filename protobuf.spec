%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%define fla             -O3 -funroll-loops -mtune=power9 -mcpu=power8 -maltivec -mvsx -mpower8-fusion -mpower8-vector -mfloat128 -malign-power -fprefetch-loop-arrays -fopenmp  -mveclibabi=mass -lmass -lmassvp8 -lmass_simdp8 -I/opt/oss-mldl/include  -fpeel-loops -fvect-cost-model -mcmodel=medium  -mhtm -L/opt/ibm/xlmass/8.1.6/lib -L/opt/ibm/xlsmp/4.1.6/lib -L/opt/ibm/xlC/13.1.6/lib -L/opt/ibm/xlf/15.1.6/lib -Wl,-rpath=/opt/oss-mldl/lib -lgomp -mpopcntd -mabi=altivec  -mpowerpc-gpopt 
%define lb_flags        -L/opt/ibm/xlmass/8.1.6/lib -L/opt/ibm/xlsmp/4.1.6/lib -L/opt/ibm/xlC/13.1.6/lib -L/opt/ibm/xlf/15.1.6/lib -lm -lpthread -lmass -lmass_simdp8 -lmassvp8 -Wl,-rpath=/opt/oss-mldl/lib 
%define lb_list         -lmass -lmass_simdp8 -lmassvp8 -lm -L/opt/ibm/xlmass/8.1.6/lib -L/opt/ibm/xlsmp/4.1.6/lib -L/opt/ibm/xlC/13.1.6/lib -L/opt/ibm/xlf/15.1.6/lib 

# This is a sample spec file for bazel

%define name		protobuf
%define release     	pslq
%define version		3.5.1
%define _topdir		/home/pqueiroz/pacotes/protobuf-3.5.1
%define buildroot	%{_topdir}/%{name}-%{version}-root
 
BuildRoot:	%{buildroot}
Summary:        PSLQ protobuf
License:        Open Source
Name:           %{name}
Version:        %{version}
Release:        %{release}
Source:         protobuf-3.5.1.tar.gz
Prefix:         /opt/oss-mldl
Group:          Development/Tools
Autoreq:	0
Requires:	advance-toolchain-at11.0-runtime	>= 11.0


 
%description
PSLQ Compilation of protobuf

%prep
%setup -q 
 
 
%build
F77FLAGS="%{fla}" CFLAGS="%{fla}" CXXFLAGS="%{fla}" FCFLAGS="%{fla}" CPPFLAGS="-I/opt/OpenBLAS/include " LDFLAGS="%{lb_flags}" LIBS="%{lb_list}" \
./configure --prefix=/opt/oss-mldl --with-zlib --enable-shared --enable-static
F77FLAGS="%{fla}" CFLAGS="%{fla}" CXXFLAGS="%{fla}" FCFLAGS="%{fla}" CPPFLAGS="-I/opt/OpenBLAS/include " LDFLAGS="%{lb_flags}" LIBS="%{lb_list}"  make -j 20
( cd python ; /opt/oss-mldl/bin/python3 setup.py build )

 
%install
make install DESTDIR=%{buildroot}
( cd python ; /opt/oss-mldl/bin/python3 setup.py install --root %{buildroot} )


%files
/opt/oss-mldl/*
