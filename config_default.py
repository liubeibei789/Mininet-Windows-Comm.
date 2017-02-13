# config_default.py

# ************* comm_win_power.py *****************
# *********************************************
configs_power = {

	# === parameters in receive()===
	'ip_windows1' : '127.0.0.1',    # listen to its localhost addr (waiting for mininet1)
	'port_windows1' : 2222,
	'file_recv' : 'powerInFile',  # file name: please put 'bbb' for 'bbb_17.txt'
								 # ignoring the underline, number and extension

	# === parameters in transmit()===
	'ip_mininiet1' : '10.206.201.201',  # transmit files to mininet1
	'port_mininet1' : 4444,       # mininet1 and mininet2 share ip addr '10.206.201.201'
	'file_trans' : 'powerOutFile'  # mininet1: port 4444, mininet2: port 5555
	
	# note:last item without comma
}



# ************* mininet1.py *******************
# *********************************************
configs_mininet1 = {

	# === parameters in receive()===
	'ip_mininet1' : '10.206.201.201',  # listen to its own addr, waiting for power_windows(trans_recv.py)
	'port_mininet1' : 4444,
	'file_recv' : 'h1toWater',      # files received from power_windows, named 'h1toWater'
	
	# === parameters in transmit()===
	'ip_windows1' : '10.144.154.181',    # '10.144.154.181': ip addr of the laptop(windows)
	'port_windows1' : 2222,           # mininet1 only sends files to power_windows(trans_recv.py), 
	'file_trans' : 'h1toPower'         # 'h1toPower' is the name on mininet1 side, (take file by this name)
								  # when windows1 receives the file, he names it 'powerInFile'
}

# ************* host1.py **********************
# *********************************************
configs_host1 = {

	# === parameters in receive()===
	'ip_host1' : '10.0.0.1',       
	'port_host1' : 6666,
	'file_recv' : 'h1toPower',   # 'mininet1Rcv' is not received by host1, but by mininet1
									# here host1 only fetches it 						
	# === parameters in transmit()===
	'ip_host2' : '10.0.0.2',   
	'port_host2' : 6666,
	'file_trans' : 'h1toWater'     # host1 sends file to host2

}

# ************* host2.py **********************
# *********************************************
configs_host2 = {

	# === parameters in receive()===
	'ip_host2' : '10.0.0.2',        
	'port_host2' : 6666,
	'file_recv' : 'h2toWater',  
									
	# === parameters in transmit()===
	'ip_host1' : '10.0.0.1',
	'port_host1' : 6666,
	'file_trans' : 'h2toPower'      # host2 sends file to host1

}

# ************* mininet2.py *******************
# *********************************************
configs_mininet2 = {

	# === parameters in receive()===
	'ip_mininet2' : '10.206.201.201', # mininet1 and mininet2 share ip addr '10.206.201.201'
	'port_mininet2' : 5555,           # mininet1: port 4444, mininet2: port 5555
	'file_recv' : 'h2toPower',
	
	# === parameters in transmit()===
	'ip_windows2' : '10.144.154.181',    # power_windows and water_windows share ip addr '10.144.154.181'
	'port_windows2' : 3333,           # power_windows: port 2222, water_windows: port 3333
	'file_trans' : 'h2toWater'        # 'h2toWater' is the name on mininet2 side, (take file by this name)
								  # when windows2 receives the file, he names it 'waterInFile'
}

# ************* comm_win_water.py ****************
# *********************************************
configs_water = {

	# === parameters in receive()===
	'ip_windows2' : '127.0.0.1',   
	'port_windows2' : 3333,         
	'file_recv' : 'waterInFile',
	
	# === parameters in transmit()===
	'ip_mininiet2' : '10.206.201.201',  
	'port_mininet2' : 5555,
	'file_trans' : 'waterOutFile'   
	
}

