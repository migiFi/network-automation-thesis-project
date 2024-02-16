import serial
import time

def push_config(device_port, config_file):
    try:
        with serial.Serial(device_port, baudrate=9600, timeout=1) as ser:
            ser.write(b"\r\n")
            time.sleep(0.5)
            ser.write(b"enable\n")
            time.sleep(0.5)
            ser.write(b"configure terminal\n")
            time.sleep(0.5)
            
            with open(config_file, 'r') as file:
                for line in file:
                    ser.write((line + '\n').encode())
                    time.sleep(0.75)  # Wait for the command to be executed
                    output = ser.read(ser.inWaiting()) 
                    print(output.decode(), end='')  #
                    
            ser.write(b"end\n")
            time.sleep(0.5)
  
            print(f"Configuration pushed to device on {device_port}.")
    except Exception as e:
        print(f"Failed to push configuration to device on {device_port}: {e}")

push_config('/dev/ttyUSB0', '/home/miggy/network-automation-thesis-project/config_files/cisco_switch_simple.txt')
time.sleep(7)
push_config('/dev/ttyUSB1', '/home/miggy/network-automation-thesis-project/config_files/cisco_router_simple.txt')
