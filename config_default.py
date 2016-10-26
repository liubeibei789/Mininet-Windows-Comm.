# config_default.py

configs_power = {

	# === parameters in receive()===
	'ip_windows' : '127.0.0.1',
	'port_windows' : 2222,
	'file_recv' : 'bbb',    # please put 'bbb' for 'bbb_17.txt'(omit underline, number and extension)
	
	# === parameters in transmit()===
	'ip_mininiet' : '10.206.201.201',
	'port_mininet' : 4444,
	'file_trans' : 'bbb'
	
	# note:last item without comma
}

configs_water = {

	# === parameters in receive()===
	'ip_windows' : '127.0.0.1',
	'port_windows' : 3333,
	'file_recv' : 'bbb2',
	
	# === parameters in transmit()===
	'ip_mininiet' : '10.206.201.201',
	'port_mininet' : 5555,
	'file_trans' : 'bbb2'
	
}
