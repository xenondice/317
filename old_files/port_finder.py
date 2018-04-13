
import serial.tools.list_ports

def find_arduino_port():
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        if("arduino" in str(port).lower()):
            return str(port).split(" -")[0]
    return None

def main():
    print(find_arduino_port())

if __name__ == '__main__':
    main()
