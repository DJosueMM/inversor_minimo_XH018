*pmos_test.sp

.option post

*Parametros
.temp 70
.param SUPPLY=1.8
.option scale=90n

*librerias
.lib '/mnt/vol_NFS_rh003/Est_VLSI_I_2024/Medina_Mayorga_I_2024_vlsi/VLSI/Tareas/Tarea1/Hspice/lp5mos/xt018.lib' tm
.lib '/mnt/vol_NFS_rh003/Est_VLSI_I_2024/Medina_Mayorga_I_2024_vlsi/VLSI/Tareas/Tarea1/Hspice/lp5mos/param.lib' 3s
.lib '/mnt/vol_NFS_rh003/Est_VLSI_I_2024/Medina_Mayorga_I_2024_vlsi/VLSI/Tareas/Tarea1/Hspice/lp5mos/config.lib' default

*Se invoca al pmos
.include 'min_pmos.sp'

*Circuito de prueba
.global vdd! gnd!

*nmos
Vgs  vdd! g SUPPLY
Vds  vdd! gnd! 0 
X1   g gnd! pmos 
*----------------------------------------------------------------------
* Stimulus
*----------------------------------------------------------------------
.dc Vds 0 2  0.05 SWEEP Vgs 0 SUPPLY 0.3
.plot I(Vds) V(gnd!)
.probe
.end

