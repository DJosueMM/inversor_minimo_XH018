*nmos_test.sp

.option post

*Parametros
.temp 70
.param SUPPLY=1.8

*librerias
.lib '/mnt/vol_NFS_rh003/Est_VLSI_I_2024/Medina_Mayorga_I_2024_vlsi/VLSI/Tareas/Tarea1/Hspice/lp5mos/xt018.lib' tm
.lib '/mnt/vol_NFS_rh003/Est_VLSI_I_2024/Medina_Mayorga_I_2024_vlsi/VLSI/Tareas/Tarea1/Hspice/lp5mos/param.lib' 3s
.lib '/mnt/vol_NFS_rh003/Est_VLSI_I_2024/Medina_Mayorga_I_2024_vlsi/VLSI/Tareas/Tarea1/Hspice/lp5mos/config.lib' default

*Se invoca al nmos
*.include 'min_nmos.sp'

*Circuito de prueba
.global gnd!

*nmos
Vgs  g gnd! SUPPLY
Vds  d gnd! 0 
xm0  d g gnd! gnd! ne w=360n l=180n as=1.728e-13 ad=1.728e-13 ps=1.68e-06 pd=1.68e-06
+ nrs=0.75 nrd=0.75 m='1*1' par1='1*1' xf_subext=0

*----------------------------------------------------------------------
* Stimulus
*----------------------------------------------------------------------
.dc Vds 0 2  0.05 SWEEP Vgs 0 SUPPLY 0.3
.plot I(Vds) V(d)
.probe
.end

