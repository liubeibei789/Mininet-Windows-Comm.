# config.py

import config_default

cfp = config_default.configs_power
cfw = config_default.configs_water

try:
	import config_override
	cfp.update(config_override.configs_power)
	cfw.update(config_override.configs_water)
	
except ImportError:
	pass