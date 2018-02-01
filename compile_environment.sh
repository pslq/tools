export PATH="/opt/at10.0/bin:/opt/at10.0/sbin:${PATH}"
export PATH="${PATH}:/opt/ibm/xlf/15.1.6/bin:/opt/ibm/xlC/13.1.6/bin"

FL=" -O3 -funroll-loops -mtune=power9 -mcpu=power8 -maltivec -mvsx -mpower8-fusion -mpower8-vector -mfloat128 -malign-power -fprefetch-loop-arrays -fopenmp  -mveclibabi=mass -lmass -lmassvp8 -lmass_simdp8 -I/opt/OpenBLAS/include  -fpeel-loops -fvect-cost-model -mcmodel=medium  -mhtm -L/opt/ibm/xlmass/8.1.6/lib -L/opt/ibm/xlsmp/4.1.6/lib -L/opt/ibm/xlC/13.1.6/lib -L/opt/ibm/xlf/15.1.6/lib -Wl,-rpath=/opt/python-at-3.6.4/lib -lgomp -mpopcntd -mabi=altivec  -mpowerpc-gpopt -lhugetlbfs"


export F77FLAGS="${FL}"
export CFLAGS="${FL} "
export CXXFLAGS="${FL}"
export FCFLAGS="${FL}"
export CPPFLAGS="-I/opt/OpenBLAS/include "
export LDFLAGS="-L/opt/ibm/xlmass/8.1.6/lib -L/opt/ibm/xlsmp/4.1.6/lib -L/opt/ibm/xlC/13.1.6/lib -L/opt/ibm/xlf/15.1.6/lib -lm -lpthread -lmass -lmass_simdp8 -lmassvp8 -Wl,-rpath=/opt/python-at-3.6.4/lib -lgomp "
export LIBS=" -lmass -lmass_simdp8 -lmassvp8 -lm -L/opt/ibm/xlmass/8.1.6/lib -L/opt/ibm/xlsmp/4.1.6/lib -L/opt/ibm/xlC/13.1.6/lib -L/opt/ibm/xlf/15.1.6/lib  -Wl,-rpath=/opt/python-at-3.6.4/lib -lgomp "
