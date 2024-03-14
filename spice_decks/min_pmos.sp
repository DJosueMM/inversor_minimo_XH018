*nmos minimo.sp

.option scale=90n

.global vdd!

.subckt pmos g d P=8

xm1 d g vdd! vdd! pe w='P' L=2
+ as='P*5' ad='P*5' ps='2*P+10' pd='2*P+10'

.ends
