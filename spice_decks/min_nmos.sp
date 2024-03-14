*nmos minimo.sp

.option scale=90n

.global gnd!

.subckt nmos g d N=4

xm0 d g gnd! gnd! ne w='N' l=2
+ as='N*5' ad='N*5' ps='2*N+10' pd='2*N+10'

.ends
