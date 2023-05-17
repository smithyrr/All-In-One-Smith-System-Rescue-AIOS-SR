# Importing necessary tools


from Tools.Tool_Scripts.gparted_tool import run_gparted_tool
from Tools.Tool_Scripts.photorec_tool import run_photorec_tool
from Tools.Tool_Scripts.testdisk_tool import run_testdisk_tool
from Tools.Diagnostic_Tools.diagnostics_tool import run_diagnostics_tool
import Tools.Tool_Scripts.system_restore_tool
from Tools.Monitor.cpu_monitor import monitor_cpu_usage
from Tools.Monitor.memory_monitor import monitor_memory_usage
from Tools.Monitor.disk_monitor import monitor_disk_usage
from Tools.Monitor.network_monitor import monitor_network_stats