from pysnmp.hlapi import *

def getOctets(community,ipaddress,octets):

    iterator = getCmd(
        SnmpEngine(),
        CommunityData(community),
        UdpTransportTarget((ipaddress, 161)),
        ContextData(),
        ObjectType(ObjectIdentity('IF-MIB', octets, 1)),
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        print(errorIndication)

    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

    else:
        for varBind in varBinds:
            return varBind[1]
