import socket
import time

# ANSI escape code for green color
GREEN = "\033[92m"
RESET = "\033[0m"

print(GREEN+ """
                        
                         
  __ _  ___  _ __| |_| |__   ___  ___| ___   __| |
 / _` |/ _ \| '__| __| '_ \ / _ \ |  _ / _ \ / _` |
| (_| | (_) | |  | |_| | | |  __/ |_| | (_) | (_| |
 \__, |\___/|_|   \__|_| |_|\___|\____|\___/ \__,_|
 |___/




""" + RESET)

time.sleep(1)
print(GREEN + 'Please wait...Loading\n' + RESET)
time.sleep(2)

def port_scanner():
    try:
        target_host = input("Enter the target IP you want to scan: ")
        socket.inet_aton(target_host)  # Check if the input is a valid IP address
    except socket.error:
        print ('\n')
        print(GREEN + "Please enter a valid IP address." + RESET)
        return

    print("\n")
    time.sleep(2)
    print(GREEN + 'Scanning ports 1-65535\n' + RESET)
    
    time.sleep(2)
    print(GREEN + 'Please wait while scanning' + RESET)
    
    target_ports = range(1, 65536)  # Scan ports from 1 to 65535

    def scan_port(target_host, port):
        try:
            socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = socket_obj.connect_ex((target_host, port))
            if result == 0:
                print(GREEN + f"Port {port} is open" + RESET)
            socket_obj.close()
        except KeyboardInterrupt:
            print(GREEN + "Scanning stopped by user." + RESET)
            exit()
        except:
            pass

    for port in target_ports:
        scan_port(target_host, port)

port_scanner()
