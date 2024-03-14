*nmos_test.sp

.option post

*Parametros
.temp 70
.param SUPPLY=1.8
.option scale=90n

*librerias
.lib '/mnt/vol_NFS_rh003/Est_VLSI_I_2024/Medina_Mayorga_I_2024_vlsi/VLSI/Tareas/Tarea1/Hspice/lp5mos/xt018.lib' tm
.lib '/mnt/vol_NFS_rh003/Est_VLSI_I_2024/Medina_Mayorga_I_2024_vlsi/VLSI/Tareas/Tarea1/Hspice/lp5mos/param.lib' 3s
.lib '/mnt/vol_NFS_rh003/Est_VLSI_I_2024/Medina_Mayorga_I_2024_vlsi/VLSI/Tareas/Tarea1/Hspice/lp5mos/config.lib' default

*Se invoca al nmos
.include 'min_nmos.sp'

*Circuito de prueba
.global gnd!

*nmos
Vgs  g gnd! SUPPLY
Vds  d gnd! 0 
X0   g d nmos 
*----------------------------------------------------------------------
* Stimulus
*----------------------------------------------------------------------
.dc Vds 0 2  0.05 SWEEP Vgs 0 SUPPLY 0.3
.plot I(Vds) V(d)
.probe
.end

