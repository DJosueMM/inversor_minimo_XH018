* corner.sp 
* Step response of unloaded inverter across process corners
*----------------------------------------------------------------------
* Parameters and models
*----------------------------------------------------------------------
.option scale=90
.param SUPPLY=1.8 
.lib '/mnt/vol_NFS_rh003/Est_VLSI_I_2024/Medina_Mayorga_I_2024_vlsi/VLSI/Tareas/Tarea1/Hspice/lp5mos/xt018.lib' tm 
.lib '/mnt/vol_NFS_rh003/Est_VLSI_I_2024/Medina_Mayorga_I_2024_vlsi/VLSI/Tareas/Tarea1/Hspice/lp5mos/param.lib' 3s
.lib '/mnt/vol_NFS_rh003/Est_VLSI_I_2024/Medina_Mayorga_I_2024_vlsi/VLSI/Tareas/Tarea1/Hspice/lp5mos/config.lib' default
.option post
*----------------------------------------------------------------------
* Simulation netlist
*----------------------------------------------------------------------
.global vdd! gnd!
.include 'min_inverter.sp'
Vdd vdd! gnd! 'SUPPLY'
Vin in  gnd! PULSE 0s 'SUPPLY' 0s 20ps 20ps 150ps 300ps
X1 in out inv 
*----------------------------------------------------------------------
* Stimulus
*----------------------------------------------------------------------
.tran 0.1ps 400ps

*Obtener delays
.measure tpdr * rising prop delay
+ TRIG v(in) VAL='SUPPLY/2' FALL=1 
+ TARG v(out) VAL='SUPPLY/2' RISE=1
.measure tpdf * falling prop delay
+ TRIG v(in) VAL='SUPPLY/2' RISE=1
+ TARG v(out) VAL='SUPPLY/2' FALL=1 
.measure tpd param='(tpdr+tpdf)/2' * average prop delay
.measure trise * rise time
+ TRIG v(out) VAL='0.2*SUPPLY' RISE=1
+ TARG v(out) VAL='0.8*SUPPLY' RISE=1
.measure tfall * fall time
+ TRIG v(out) VAL='0.8*SUPPLY' FALL=1
+ TARG v(out) VAL='0.2*SUPPLY' FALL=1


.probe tran v(in) v(out)

*Corners

.alter
.lib '/mnt/vol_NFS_rh003/Est_VLSI_I_2024/Medina_Mayorga_I_2024_vlsi/VLSI/Tareas/Tarea1/Hspice/lp5mos/xt018.lib' wo
.alter
.lib '/mnt/vol_NFS_rh003/Est_VLSI_I_2024/Medina_Mayorga_I_2024_vlsi/VLSI/Tareas/Tarea1/Hspice/lp5mos/xt018.lib' wp
.alter
.lib '/mnt/vol_NFS_rh003/Est_VLSI_I_2024/Medina_Mayorga_I_2024_vlsi/VLSI/Tareas/Tarea1/Hspice/lp5mos/xt018.lib' ws
.alter
.lib '/mnt/vol_NFS_rh003/Est_VLSI_I_2024/Medina_Mayorga_I_2024_vlsi/VLSI/Tareas/Tarea1/Hspice/lp5mos/xt018.lib' wz
.end
