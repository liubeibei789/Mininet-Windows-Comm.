# config.py

import config_default

cfp = config_default.configs_power
cfw = config_default.configs_water
cfm1 = config_default.configs_mininet1
cfm2 = config_default.configs_mininet2
cfh1 = config_default.configs_host1
cfh2 = config_default.configs_host2


try:
	import config_override
	cfp.update(config_override.configs_power)
	cfw.update(config_override.configs_water)
	cfm1.update(config_override.configs_mininet1)
	cfm2.update(config_override.configs_mininet2)
	cfh1.update(config_override.configs_host1)
	cfh2.update(config_override.configs_host2)
	
except ImportError:
	pass