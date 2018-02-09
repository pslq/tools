### AT10
export PATH="/opt/at10.0/bin:/opt/at10.0/sbin:${PATH}"
export PATH="${PATH}:/opt/ibm/xlf/15.1.5/bin:/opt/ibm/xlC/13.1.5/bin"
###
FL=" -O3 -funroll-loops -mtune=power9 -mcpu=power8 -maltivec -mvsx -mpower8-fusion -mpower8-vector -mfloat128 -malign-power -fprefetch-loop-arrays -fopenmp  -mveclibabi=mass -lmass -lmassvp8 -lmass_simdp8 -I/opt/oss-mldl/include  -fpeel-loops -fvect-cost-model -mcmodel=medium  -mhtm -L/opt/ibm/xlmass/8.1.5/lib -L/opt/ibm/xlsmp/4.1.5/lib -L/opt/ibm/xlC/13.1.5/lib -L/opt/ibm/xlf/15.1.5/lib -Wl,-rpath=/opt/oss-mldl/lib -lgomp -mpopcntd -mabi=altivec  -mpowerpc-gpopt "
###
####
#export CXX="c++ -shared"
export F77FLAGS="${FL}"
export CFLAGS="${FL} "
export CXXFLAGS="${FL}"
export FCFLAGS="${FL}"
export CPPFLAGS="-I/opt/oss-mldl/include"
export LDFLAGS="-L/opt/ibm/xlmass/8.1.5/lib -L/opt/ibm/xlsmp/4.1.5/lib -L/opt/ibm/xlC/13.1.5/lib -L/opt/ibm/xlf/15.1.5/lib -lm -lpthread -lmass -lmass_simdp8 -lmassvp8 -Wl,-rpath=/opt/oss-mldl/lib -lgomp "
export LIBS=" -lmass -lmass_simdp8 -lmassvp8 -lm -L/opt/ibm/xlmass/8.1.5/lib -L/opt/ibm/xlsmp/4.1.5/lib -L/opt/ibm/xlC/13.1.5/lib -L/opt/ibm/xlf/15.1.5/lib  -Wl,-rpath=/opt/python-at-3.6.4/lib -lgomp "
