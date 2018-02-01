%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%define fla		-O3 -funroll-loops -mtune=power9 -mcpu=power8 -maltivec -mvsx -mpower8-fusion -mpower8-vector -mfloat128 -malign-power -fprefetch-loop-arrays -fopenmp  -mveclibabi=mass -lmass -lmassvp8 -lmass_simdp8 -I/opt/oss-mldl/include  -fpeel-loops -fvect-cost-model -mcmodel=medium  -mhtm -L/opt/ibm/xlmass/8.1.6/lib -L/opt/ibm/xlsmp/4.1.6/lib -L/opt/ibm/xlC/13.1.6/lib -L/opt/ibm/xlf/15.1.6/lib -Wl,-rpath=/opt/oss-mldl/lib -lgomp -mpopcntd -mabi=altivec  -mpowerpc-gpopt -lhugetlbfs
%define lb_flags	-L/opt/ibm/xlmass/8.1.6/lib -L/opt/ibm/xlsmp/4.1.6/lib -L/opt/ibm/xlC/13.1.6/lib -L/opt/ibm/xlf/15.1.6/lib -lm -lpthread -lmass -lmass_simdp8 -lmassvp8 -Wl,-rpath=/opt/oss-mldl/lib -lhugetlbfs
%define	lb_list		-lmass -lmass_simdp8 -lmassvp8 -lm -L/opt/ibm/xlmass/8.1.6/lib -L/opt/ibm/xlsmp/4.1.6/lib -L/opt/ibm/xlC/13.1.6/lib -L/opt/ibm/xlf/15.1.6/lib -lhugetlbfs

%define name		Python
%define release     	pslq_gcc_huge
%define version		3.6.4
%define _topdir		/home/pqueiroz/pacotes/python-3.6.4
%define buildroot	%{_topdir}/%{name}-%{version}-root

BuildRoot:	%{buildroot}
Summary:        PSLQ Compilation of Python 3.6.4
License:        PSF
Name:           %{name}
Version:        %{version}
Release:        %{release}
Source:         Python-3.6.4.tgz
Prefix:         /opt/oss-mldl
Group:          Development/Tools
Provides:       bundled(python3) = %{version}
Autoreq:	0 
Requires:	advance-toolchain-at10.0-runtime = 10.0 
Requires:	libxlf >= 15.1.6.0


 
%description
PSLQ Compilation of Python 3 on top of Advance Toolchain and IBM mathematical Libraries
For more information about this package, please check: https://github.com/pslq/tools

WARNING:
  This package have been made for educational purposes, there is no support of anykind implicit on it
  For a supported solution it's advisable to look for either the distrivution packages or IBM's Advance Toolchain

%prep
%setup -q
 
 
%build
F77FLAGS="%{fla}" CFLAGS="%{fla}" CXXFLAGS="%{fla}" FCFLAGS="%{fla}" CPPFLAGS="-I/opt/OpenBLAS/include " LDFLAGS="%{lb_flags}" LIBS="%{lb_list}" ./configure \
  --with-threads \
  --enable-ipv6 --enable-loadable-sqlite-extensions \
  --enable-optimizations \
  --enable-shared --prefix=/opt/oss-mldl

F77FLAGS="%{fla}" CFLAGS="%{fla}" CXXFLAGS="%{fla}" FCFLAGS="%{fla}" CPPFLAGS="-I/opt/oss-mldl/include " LDFLAGS="%{lb_flags}" LIBS="%{lb_list}" make -j 20
make -j 20
echo 'export PATH="/opt/oss-mldl/bin:${PATH}"' > profile.sh
echo 'export PKG_CONFIG_PATH="${PKG_CONFIG_PATH}:/opt/oss-mldl/lib/pkgconfig"' >> profile.sh

 
%install
rm -rf %{buildroot}
install -d %{buildroot}/etc/profile.d
F77FLAGS="%{fla}" CFLAGS="%{fla}" CXXFLAGS="%{fla}" FCFLAGS="%{fla}" CPPFLAGS="-I/opt/oss-mldl/include " LDFLAGS="%{lb_flags}" LIBS="%{lb_list}" \
make install DESTDIR=%{buildroot}

install -o root -g root -m 555 profile.sh %{buildroot}/etc/profile.d/python-pslq.sh

 
%files
/opt/oss-mldl/*
/etc/profile.d/python-pslq.sh
