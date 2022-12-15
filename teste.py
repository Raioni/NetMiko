from netmiko import ConnectHandler
from snmp import getOctets
import time

R1 = {
	" device_type " : "cisco_ios" ,
	" host " : "192.168.1.101" ,
	" username " : "raioni" ,
	" password " : "dantas" ,
	" community " : "Roteador1"
}
R2 = {
	" device_type " : "cisco_ios" ,
	" host " : "192.168.1.102" ,
	" username " : "raioni" ,
	" password " : "dantas" ,
	" community " : "Roteador2"
}
R3 = {
	" device_type " : "cisco_ios" ,
	" host " : "192.168.1.103" ,
	" username " : "raioni" ,
	" password " : "dantas" ,
	" community " : "Roteador3"
}



routers = dict()
routers['R1'] = R1
routers['R2'] = R2
routers['R3'] = R3

for i in routers:
    connect = ConnectHandler(**i)
    connect.send_command(f"snmp-server community {i[' community ']} RO")
	connect.save_config()

while(True):
	print('R1 = in: ', getOctets(R1[community], R1[host], "ifInOctets"), 'out: ', getOctets(R1[community], R1[host], "ifOutOctets"))
	print('R2 = in: ', getOctets(R2[community], R2[host], "ifInOctets"), 'out: ', getOctets(R2[community], R2[host], "ifOutOctets"))
	print('R3 = in: ', getOctets(R3[community], R3[host], "ifInOctets"), 'out: ', getOctets(R3[community], R3[host], "ifOutOctets"))
	print('---------------------------------------------------------------------')
	time.sleep(10)
