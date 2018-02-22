
import serial.tools.list_ports

def find_arduino_port():
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        if("arduino" in str(port.product.lower())):
            return port
    return Null

#	for p in ports:
#        if("arduino" in str(p).lower()):
#            return str(p).split(" -")[0]

def main():
    print(find_arduino_port())

if __name__ == '__main__':
    main()
