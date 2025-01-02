import socket
import sys

def scan (host, ports):
    try:
        for port in ports:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.5)
            code = client.connect_ex((host, int(port)))
            if code == 0:
                print("[x] {} open".format(port))
    except:
        print("Erro, something is wrong.")


if __name__ ==  "__main__":
    if len(sys.argv)>= 2:
        host = sys.argv[1]
        if len(sys.argv)>=3:
            ports = sys.argv[2].split(",")
        else:
            ports =[21,22,23,25,65,80,135,443,8080,8443,3306,139,445]
        scan(host,ports)
    else:
        print("Usage: python portScan.py examplo.com ports (examplo: 80)") 