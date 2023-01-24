import serial.tools.list_ports

portList = []
serialInst = serial.Serial()
ports = serial.tools.list_ports.comports()

def find_ports():
    for port in ports:
        portList.append(str(port))

def print_ports():
    for port in portList:
        print(port)

def main():
    find_ports()
    print_ports()

if __name__ == '__main__':
    main()