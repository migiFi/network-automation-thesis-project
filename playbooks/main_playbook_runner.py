import serial
import time
import subprocess

def run_ansible_playbook(playbook_path):
    try:
        result = subprocess.run(['ansible-playbook', playbook_path], check=True)
        print(f"Playbook was executed successfully: {playbook_path}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute the playbook {playbook_path}: {e}")

def push_config(device_port, config_file):
    try:
        with serial.Serial(device_port, baudrate=9600, timeout=1) as ser:
            ser.write(b"\r\n")
            time.sleep(1)
            ser.write(b"enable\n")
            time.sleep(1)
            ser.write(b"configure terminal\n")
            time.sleep(1)
            
            with open(config_file, 'r') as file:
                for line in file:
                    ser.write((line + '\n').encode())
                    time.sleep(0.25) 
                    output = ser.read(ser.inWaiting())
                    print(output.decode(), end='')  #
                    
            ser.write(b"end\n")
            time.sleep(1)
  
            print(f"Configuration pushed to device on {device_port}.")
    except Exception as e:
        print(f"Failed to push configuration to device on {device_port}: {e}")

playbook_path =  ' '# need ansible playbook path from master node
run_ansible_playbook(playbook_path)

print("Waiting for devices to boot up...")
time.sleep(180) # the time it takes for devices to boot up <<<--- needs a more accurate time 

push_config('/dev/ttyUSB1', '/home/miggy/network-automation-thesis-project/config_files/cisco-router-simple.txt')

time.sleep(8)

push_config('/dev/ttyUSB0', '/home/miggy/network-automation-thesis-project/config_files/cisco-switch-simple.txt')
