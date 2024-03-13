*Custom Compiler Version U-2023.03-SP2
*Tue Mar  5 22:27:04 2024

*min_inverter.sp
*inversor minimo 2:1
.option scale=90n
.global gnd! vdd!
********************************************************************************
* Library          : basic_cells
* Cell         
* View             : schematic
* View Search List : hspice hspiceD schematic cmos_sch spice veriloga
* View Stop List   : hspice hspiceD
********************************************************************************

.subckt inv in out N=4 P=8
xm0 out in gnd! gnd! ne w='N' l=2
+ as='N*5' ad='N*5' ps='2*N+10' pd='2*N+10'
xm1 out in vdd! vdd! pe w='P' L=2
+ as='P*5' ad='P*5' ps='2*P+10' pd='2*P+10'

.ends
