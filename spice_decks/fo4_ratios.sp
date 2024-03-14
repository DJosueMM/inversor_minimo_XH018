*fo4_ratios.sp


*  Generated for: FineSimPro
*  Design library name: basic_cells
*  Design cell name: min_inverter
*  Design view name: schematic

*opcion para generar el .tr0 y simular despues
.option post

*Parametros
.temp 70 
.param SUPPLY=1.8
.param H=4
.param N1=4
.param Ra=2
.option scale=90n

*librerias
.lib '/mnt/vol_NFS_rh003/Est_VLSI_I_2024/Medina_Mayorga_I_2024_vlsi/VLSI/Tareas/Tarea1/Hspice/lp5mos/xt018.lib' tm
.lib '/mnt/vol_NFS_rh003/Est_VLSI_I_2024/Medina_Mayorga_I_2024_vlsi/VLSI/Tareas/Tarea1/Hspice/lp5mos/param.lib' 3s
.lib '/mnt/vol_NFS_rh003/Est_VLSI_I_2024/Medina_Mayorga_I_2024_vlsi/VLSI/Tareas/Tarea1/Hspice/lp5mos/config.lib' default


.global vdd! gnd!

*Se invoca al inversor 
.include 'min_inverter.sp'


*Netlist para simular el fo4

Vdd vdd! gnd! 'SUPPLY'
Vin a gnd! PULSE 0 'SUPPLY' 0ps 50ps 50ps 450ps 1000ps
X1 a b inv N='N1'  P='N1*Ra'                
X2 b c inv N='N1'  P='N1*Ra'  M='H'          
X3 c d inv N='N1'  P='N1*Ra'  M='H**2'      
X4 d e inv N='N1'  P='N1*Ra'  M='H**3'      
X5 e f inv N='N1'  P='N1*Ra'  M='H**4'      

*Configuraciones de simulacion
.tran 0.1ps 1ns sweep Ra 1 6 0.1 

*Obtener delays
.measure tpdr * rising prop delay
+ TRIG v(c) VAL='SUPPLY/2' FALL=1 
+ TARG v(d) VAL='SUPPLY/2' RISE=1
.measure tpdf * falling prop delay
+ TRIG v(c) VAL='SUPPLY/2' RISE=1
+ TARG v(d) VAL='SUPPLY/2' FALL=1 
.measure tpd param='(tpdr+tpdf)/2' * average prop delay
.measure trise * rise time
+ TRIG v(d) VAL='0.2*SUPPLY' RISE=1
+ TARG v(d) VAL='0.8*SUPPLY' RISE=1
.measure tfall * fall time
+ TRIG v(d) VAL='0.8*SUPPLY' FALL=1
+ TARG v(d) VAL='0.2*SUPPLY' FALL=1
.measure diff param='tpdr-tpdf'

.probe tran v(c) v(d)
.measure pwr AVG 'P(Vdd)*-1' FROM=0ns TO=1ns
.option measform=3
.end
