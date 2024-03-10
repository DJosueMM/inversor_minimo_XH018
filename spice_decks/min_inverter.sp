*Custom Compiler Version U-2023.03-SP2
*Tue Mar  5 22:27:04 2024

*min_inverter.sp
*inversor minimo 2:1

.global gnd! vdd!
********************************************************************************
* Library          : basic_cells
* Cell             : min_inverter
* View             : schematic
* View Search List : hspice hspiceD schematic cmos_sch spice veriloga
* View Stop List   : hspice hspiceD
********************************************************************************

.subckt inv in out N = 360n P = 720n
xm0 out in gnd! gnd! ne w=360n l=180n as=1.728e-13 ad=1.728e-13 ps=1.68e-06 pd=1.68e-06
+ nrs=0.75 nrd=0.75 m='1*1' par1='1*1' xf_subext=0
xm1 out in vdd! vdd! pe w=720n l=180n as=3.456e-13 ad=3.456e-13 ps=2.4e-06 pd=2.4e-06
+ nrs=0.375 nrd=0.375 m='1*1' par1='1*1' xf_subext=0
.ends

