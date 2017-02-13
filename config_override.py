# config_override.py

# ************* comm_win_power.py *****************
# *********************************************
configs_power = {
	# === parameters in receive()===    
	'ip_windows1' : '127.0.0.1',    # listen to its localhost addr (waiting for mininet1) 
	# === parameters in transmit()===
	'ip_mininiet1' : '10.206.201.201'  # transmit files to mininet1
}

# ************* mininet1.py *******************
# *********************************************
configs_mininet1 = {
	# === parameters in receive()===
	'ip_mininet1' : '10.206.201.201',  # listen to its own addr (waiting for power_windows)
	# === parameters in transmit()===
	'ip_windows1' : '10.140.219.96'    # '10.144.154.181': ip addr of the laptop(windows)
	
}

# ************* host1.py **********************
# *********************************************
configs_host1 = {
	# === parameters in receive()===
	'ip_host1' : '10.0.0.1',
	# === parameters in transmit()===
	'ip_host2' : '10.0.0.2'  	
}

# ************* host2.py **********************
# *********************************************
configs_host2 = {
	# === parameters in receive()===
	'ip_host2' : '10.0.0.2',   
	# === parameters in transmit()===
	'ip_host1' : '10.0.0.1'
}

# ************* mininet2.py *******************
# *********************************************
configs_mininet2 = {
	# === parameters in receive()===
	'ip_mininet2' : '10.206.201.201', # mininet1 and mininet2 share ip addr '10.206.201.201'
	# === parameters in transmit()===
	'ip_windows2' : '10.140.219.96'    # power_windows and water_windows share ip addr '10.144.154.181'
	
}

# ************* comm_win_water.py ****************
# *********************************************
configs_water = {
	# === parameters in receive()===
	'ip_windows2' : '127.0.0.1', 
	# === parameters in transmit()===
	'ip_mininiet2' : '10.206.201.201'
}


