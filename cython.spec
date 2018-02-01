%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%define fla		-O3 -funroll-loops -mtune=power9 -mcpu=power8 -maltivec -mvsx -mpower8-fusion -mpower8-vector -mfloat128 -malign-power -fprefetch-loop-arrays -fopenmp  -mveclibabi=mass -lmass -lmassvp8 -lmass_simdp8 -I/opt/oss-mldl/include  -fpeel-loops -fvect-cost-model -mcmodel=medium  -mhtm -L/opt/ibm/xlmass/8.1.6/lib -L/opt/ibm/xlsmp/4.1.6/lib -L/opt/ibm/xlC/13.1.6/lib -L/opt/ibm/xlf/15.1.6/lib -Wl,-rpath=/opt/oss-mldl/lib -lgomp -mpopcntd -mabi=altivec  -mpowerpc-gpopt -lhugetlbfs
%define lb_flags	-L/opt/ibm/xlmass/8.1.6/lib -L/opt/ibm/xlsmp/4.1.6/lib -L/opt/ibm/xlC/13.1.6/lib -L/opt/ibm/xlf/15.1.6/lib -lm -lpthread -lmass -lmass_simdp8 -lmassvp8 -Wl,-rpath=/opt/oss-mldl/lib -lhugetlbfs
%define	lb_list		-lmass -lmass_simdp8 -lmassvp8 -lm -L/opt/ibm/xlmass/8.1.6/lib -L/opt/ibm/xlsmp/4.1.6/lib -L/opt/ibm/xlC/13.1.6/lib -L/opt/ibm/xlf/15.1.6/lib -lhugetlbfs

%define name		Cython
%define release     	pslq_gcc_huge
%define version		0.27.3
%define _topdir		/home/pqueiroz/pacotes/cython-0.27.3
%define buildroot	%{_topdir}/%{name}-%{version}-root

BuildRoot:	%{buildroot}
Summary:        PSLQ Compilation of Cython
Name:           %{name}
License:	APL
Version:        %{version}
Release:        %{release}
Source:         Cython-0.27.3.tar.gz
Prefix:         /opt/oss-mldl
Group:          Development/Tools
Autoreq:	0 
Requires:	advance-toolchain-at10.0-runtime = 10.0 
Requires:	libxlf >= 15.1.6.0
Requires:	Python = 3.6.4-pslq_gcc_huge



 
%description
PSLQ Compilation of Cython on top of Advance Toolchain and IBM mathematical Libraries
For more information about this package, please check: https://github.com/pslq/tools

WARNING:
  This package have been made for educational purposes, there is no support of anykind implicit on it
  For a supported solution it's advisable to look for either the distrivution packages or IBM's Advance Toolchain

%prep
%setup -q
 
 
%build
F77FLAGS="%{fla}" CFLAGS="%{fla}" CXXFLAGS="%{fla}" FCFLAGS="%{fla}" CPPFLAGS="-I/opt/oss-mldl/include " LDFLAGS="%{lb_flags}" LIBS="%{lb_list}" /opt/oss-mldl/bin/python3 setup.py build

%install
rm -rf %{buildroot}
install -d %{buildroot}
/opt/oss-mldl/bin/python3 setup.py install --root %{buildroot}

 
%files
/opt/oss-mldl/*
