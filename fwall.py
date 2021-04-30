#Command to execute python D:\Projects\ISM_Proj\fwall.py
import pydivert # Python
from urllib.parse import urlparse, parse_qs
from rules import verifyString


def parsePacketPayload(payload,connected):
    parseList = []
    payload_str = str(payload)
    payload_str = payload_str + "`"
    i=2
    while i < len(payload_str):
        if payload_str[i] == "\\" and i+1 < len(payload_str) and payload_str[i+1] == "x":
            k=0
            sstr = ""
            sstr = sstr +"0x"
            i = i+2
            while i < len(payload_str) and k < 2:
                sstr = sstr+ payload_str[i]
                k = k + 1
                i = i+1
            parseList.append(sstr)
        else:
            sstr = ""
            if payload_str[i] == "\\":
                if payload_str[i+1] == "t":
                    sstr = sstr + '\t'
                elif payload_str[i+1] == "r":
                    sstr = sstr + '\r'
                else:
                    sstr = sstr + '\n'
                i = i+2
            while i < len(payload_str) and payload_str[i] != "\\":
                sstr = sstr + payload_str[i]
                i = i+1
            parseList.append(sstr)
    try:
        parseList[0] = ord(parseList[0])
    except:
        parseList[0] = int(str(parseList[0]),16)
    for i in range(1,len(parseList)):
        try:
            parseList[i] = int(str(parseList[i]),16)
        except:
            continue
    packetDetails = {}
    packetDetails['Length'] = parseList[0] + parseList[1] + parseList[2]
    packetDetails['Number'] = parseList[3]

    if not connected :
        packetDetails['ConnectionDetails'] = {}
        packetDetails['ClientInfo'] = parseList[4:35]
        packetDetails['ConnectionDetails']['Username'] = parseList[36]
        packetDetails['ConnectionDetails']['Schema'] = parseList[39]
        packetDetails['ConnectionDetails']['Password'] = parseList[41]
        packetDetails['ConnectionDetails']['ClientName'] = parseList[47]
        packetDetails['ConnectionDetails']['ServerHost'] = parseList[50]
        connected = True
    else:
       packetDetails['Query'] = parseList[5]

    return packetDetails

def parseHTTTPPacket(payload):
    payload_str = str(payload).split("\\n")
    payload_cookie = payload_str[-3].split("; ")
    if payload_str[0][2] == "G":
        try:
            payload_params = parse_qs(urlparse(payload_str[0][payload_str[0].index(" ")+1:payload_str[0].index(" ",payload_str[0].index(" ")+1)]).query)
        except:
            payload_params = payload_str[0]
    elif payload_str[0][2] == "P":
        payload_params = parse_qs(payload_str[-1][:-2])
    else:
        return
    for param in list(payload_params.values()):
        for string in param:
            print(string)
            if verifyString(string):
                return True
    return False
    


#  Capture only TCP packets to port 80, i.e. HTTP requests.
print("Intercepting Packets at dstPort 80")

with pydivert.WinDivert("tcp.DstPort == 80 and tcp.PayloadLength > 0") as w:
    for packet in w:
        result = parseHTTTPPacket(packet.payload) 
        print(result)    
        if not result:
            w.send(packet)
#
