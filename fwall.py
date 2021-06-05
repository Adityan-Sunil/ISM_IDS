#Command to execute python D:\Projects\ISM_Proj\fwall.py
import pydivert # Python
from urllib.parse import urlparse, parse_qs
from rules import verifyString
import datetime
from colorama import init, Fore, Back, Style;

def parseHTTTPPacket(payload, log_file):
    payload_params = {}
    payload_str = str(payload).split("\\n")
    if len(payload_str) > 2:
        payload_cookie = payload_str[-3].split("; ")
    if payload_str[0][2] == "G":
        try:
            payload_params = {**payload_params,**parse_qs(urlparse(payload_str[0][payload_str[0].index(" ")+1:payload_str[0].index(" ",payload_str[0].index(" ")+1)]).query)}
        except:
            payload_params = {**payload_params, **payload_str[0]}
    elif payload_str[0][2] == "P":
        payload_params = {**payload_params, **parse_qs(payload_str[-1][:-2])}
    else:
        return
    payload_params = {**payload_params, **{"Cookie": payload_cookie[-2:]}}
    for param in list(payload_params.values()):
        for string in param:
            if verifyString(string,log_file):
                return True
    return False
    


#  Capture only TCP packets to port 80, i.e. HTTP requests.
print("Intercepting Packets at dstPort 80")
init()

with pydivert.WinDivert("tcp.DstPort == 80 and tcp.PayloadLength > 0") as w:
    print("Waiting for Packet")
    for packet in w:
        try:        
            log_file =  open("D:\Projects\ISM_Proj\IPSLogs.txt", "a+")
            if not log_file or log_file.closed:
                print("Unable to create/open log file. Exiting the Program")
                exit(0)
            timestamp = datetime.datetime.now() 
            print("[" + Fore.BLUE+ timestamp.strftime("%c") +Style.RESET_ALL+"]" , end=' ')
            log_file.write("["+timestamp.strftime("%c")+"] ")
            log_file.write(str(packet.src_addr)+":"+str(packet.src_port)+" ")
            print(str(packet.src_addr)+":"+str(packet.src_port)+" ")
            result = parseHTTTPPacket(packet.payload, log_file)
            if not result:
                print(Fore.GREEN, "Safe", Style.RESET_ALL)
                w.send(packet)
            else: 
                print(Fore.RED,result, Style.RESET_ALL)    
            log_file.write("****************************\n")  
            log_file.flush()
            log_file.close()  
            if log_file.closed:
                print("File Closed")
            print(w)    
        except:
            print("Error Occured")
            break
        finally:
            log_file.close()
        
