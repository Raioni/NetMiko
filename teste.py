from netmiko import ConnectHandler
from snmp import getOctets
import time

R1 = {
	"device_type" : "cisco_ios" ,
	"host" : "192.168.1.101" ,
	"username" : "raioni" ,
	"password" : "dantas" ,
}
R2 = {
	"device_type" : "cisco_ios" ,
	"host" : "192.168.1.102" ,
	"username" : "raioni" ,
	"password" : "dantas" ,
}
R3 = {
	"device_type" : "cisco_ios" ,
	"host" : "192.168.1.103" ,
	"username" : "raioni" ,
	"password" : "dantas" ,
}


cont = 0
comm = ["Router1","Router2","Router3"]

for routers in (R1,R2,R3):
    connect = ConnectHandler(**routers)
    snmp = 'snmp-server community ' + comm[cont] + ' RO'
    array = [snmp, "end"]
    output = connect.send_config_set(array)
    cont +=1

while(True):
	print('---------------------------------------------------------------------')
	print('R1 = in: ', getOctets(comm[0], R1['host'], "ifInOctets"), 'out: ', getOctets(comm[0], R1['host'], "ifOutOctets"))
	print('R2 = in: ', getOctets(comm[1], R2['host'], "ifInOctets"), 'out: ', getOctets(comm[1], R2['host'], "ifOutOctets"))
	print('R3 = in: ', getOctets(comm[2], R3['host'], "ifInOctets"), 'out: ', getOctets(comm[2], R3['host'], "ifOutOctets"))
	print('---------------------------------------------------------------------')
	time.sleep(10)

