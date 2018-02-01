# This is a sample spec file for wget


%define fla             -O3 -funroll-loops -mtune=power9 -mcpu=power8 -maltivec -mvsx -mpower8-fusion -mpower8-vector -mfloat128 -malign-power -fprefetch-loop-arrays -fopenmp  -mveclibabi=mass -lmass -lmassvp8 -lmass_simdp8 -I/opt/oss-mldl/include  -fpeel-loops -fvect-cost-model -mcmodel=medium  -mhtm -L/opt/ibm/xlmass/8.1.6/lib -L/opt/ibm/xlsmp/4.1.6/lib -L/opt/ibm/xlC/13.1.6/lib -L/opt/ibm/xlf/15.1.6/lib -Wl,-rpath=/opt/oss-mldl/lib -Wl,-rpath=/opt/openBLAS/lib -lgomp -mpopcntd -mabi=altivec  -mpowerpc-gpopt 
%define lb_flags        -L/opt/ibm/xlmass/8.1.6/lib -L/opt/ibm/xlsmp/4.1.6/lib -L/opt/ibm/xlC/13.1.6/lib -L/opt/ibm/xlf/15.1.6/lib -lm -lpthread -lmass -lmass_simdp8 -lmassvp8 -Wl,-rpath=/opt/oss-mldl/lib -Wl,-rpath=/opt/openBLAS/lib
%define lb_list         -lmass -lmass_simdp8 -lmassvp8 -lm -L/opt/ibm/xlmass/8.1.6/lib -L/opt/ibm/xlsmp/4.1.6/lib -L/opt/ibm/xlC/13.1.6/lib -L/opt/ibm/xlf/15.1.6/lib 
 
%define name		OpenBLAS
%define release     	pslq
%define version		0.2.20
%define lapackver	3.7.0
%define _topdir		/home/pqueiroz/pacotes/openblas
%define buildroot	%{_topdir}/%{name}-%{version}-root
 
BuildRoot:	%{buildroot}
Summary:        PSLQ OpenBlas
License:        GPL
Name:           %{name}
Version:        %{version}
Release:        %{release}
Source:         v0.2.20.tar.gz
Prefix:         /opt/openBLAS
Group:          Development/Libraries
Provides:       bundled(lapack) = %{lapackver}
Requires:	advance-toolchain-at10.0-runtime = 10.0

%description
PSLQ Compilation of OpenBLAS on top of Advance Toolchain and IBM mathematical Libraries
For more information about this package, please check: https://github.com/pslq/tools

WARNING:
  This package have been made for educational purposes, there is no support of anykind implicit on it
  For a supported solution it's advisable to look for either the distrivution packages or IBM's Advance Toolchain
 
%prep
%setup -q
 
 
%build
F77FLAGS="%{fla}" CFLAGS="%{fla}" CXXFLAGS="%{fla}" FCFLAGS="%{fla}" CPPFLAGS="-I/opt/oss-mldl/include " LDFLAGS="%{lb_flags}" LIBS="%{lb_list}" NMAX="NUM_THREADS=128" USE_THREAD=1 USE_OPENMP=1 USE_MASS=1 make
echo 'export LD_LIBRARY_PATH="/opt/openBLAS/lib:${LD_LIBRARY_PATH}"' > profile.sh
echo 'export PKG_CONFIG_PATH="${PKG_CONFIG_PATH}:/opt/openBLAS/lib/pkgconfig"' >> profile.sh

 
%install
rm -rf %{buildroot}
install -d %{buildroot}/opt/openBLAS/doc
install -d %{buildroot}/etc/profile.d

make install PREFIX=%{buildroot}/opt/openBLAS
install -o root -g root -m 644 *txt *md LICENSE  %{buildroot}/opt/openBLAS/doc
install -o root -g root -m 555 profile.sh %{buildroot}/etc/profile.d/OpenBlas-pslq.sh

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

 
%files
/opt/openBLAS/lib/*
/opt/openBLAS/include/*
/etc/profile.d/OpenBlas-pslq.sh

%doc %attr(0444,root,root) /opt/openBLAS/doc/LICENSE
%doc %attr(0444,root,root) /opt/openBLAS/doc/*txt
%doc %attr(0444,root,root) /opt/openBLAS/doc/*md
