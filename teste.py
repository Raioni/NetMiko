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



routers = dict()
routers['R1'] = R1
routers['R2'] = R2
routers['R3'] = R3

cont = 0
comm = ["Router1","Router2","Router3"]

for routers in (R1,R2,R3):
    connect = ConnectHandler(**routers)
    output = connect.send_command(f'snmp-server community {comm[cont]} RO')
    print(output)
    cont +=1


#for i in routers:
#    connect = ConnectHandler(**routers[i])
#    connect.send_command(f"snmp-server community {comm[cont]} RO")
#    cont +=1

while(True):
	print('R1 = in: ', getOctets(comm[0], R1['host'], "ifInOctets"), 'out: ', getOctets(comm[0], R1['host'], "ifOutOctets"))
	print('R2 = in: ', getOctets(comm[1], R2['host'], "ifInOctets"), 'out: ', getOctets(comm[1], R2['host'], "ifOutOctets"))
	print('R3 = in: ', getOctets(comm[2], R3['host'], "ifInOctets"), 'out: ', getOctets(comm[2], R3['host'], "ifOutOctets"))
	print('---------------------------------------------------------------------')
	time.sleep(10)
