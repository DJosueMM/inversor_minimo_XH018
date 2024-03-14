*  Generated for: FineSimPro
*  Design library name: basic_cells
*  Design cell name: min_inverter
*  Design view name: schematic

.option finesim_output=wdf

.option post
.option scale=90n
.parameter N=4
.parameter Ra=1

.temp 70 
.lib '/mnt/vol_NFS_rh003/Est_VLSI_I_2024/Medina_Mayorga_I_2024_vlsi/VLSI/Tareas/Tarea1/Hspice/lp5mos/xt018.lib' tm
.lib '/mnt/vol_NFS_rh003/Est_VLSI_I_2024/Medina_Mayorga_I_2024_vlsi/VLSI/Tareas/Tarea1/Hspice/lp5mos/param.lib' 3s
.lib '/mnt/vol_NFS_rh003/Est_VLSI_I_2024/Medina_Mayorga_I_2024_vlsi/VLSI/Tareas/Tarea1/Hspice/lp5mos/config.lib' default


.include 'min_inverter.sp'

v18 vdd! gnd! dc=1.8
v17 in gnd! dc=1.8
X1  in out inv P='N*Ra'



.tran 10p 10n start=0 simStart=0
.dc v17 0 1.8 0.01 sweep Ra 1 6 0.5
.measure DC Isc when V(out)=0.9v
.plot V(out) V(in)
.probe dc v(in) v(out)
.probe
.option PARHIER = LOCAL
.option runlvl = 5
.option s_elem_cache_dir = "/home/Medina_Mayorga_I_2024_vlsi/.synopsys_custom/sparam_dir"
.option pva_output_dir = "/home/Medina_Mayorga_I_2024_vlsi/.synopsys_custom/pva_dir"
.option finesim_mode = spicead

.option measform=3




.end
