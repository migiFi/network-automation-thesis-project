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
            # if prompted, it skips the initial config dialog
            ser.write(b"\r\n")
            time.sleep(0.05)
            ser.write(b"no\n")
            time.sleep(0.05)
            
            print("Pushing config files...")
            time.sleep(0.05)
            
            ser.write(b"\r\n")
            time.sleep(0.05)
            ser.write(b"enable\n")
            time.sleep(0.05)
            ser.write(b"configure terminal\n")
            time.sleep(0.05)
            
            with open(config_file, 'r') as file:
                for line in file:
                    ser.write((line + '\n').encode())
                    time.sleep(0.55) 
                    output = ser.read(ser.inWaiting())
                    print(output.decode(), end='') 
                    
            ser.write(b"end\n")
            time.sleep(0.05)
  
            print(f"Successfully pushed config to device on {device_port}.")
    except Exception as e:
        print(f"Failed to push configuration to device on {device_port}: {e}")

start_time = time.time()

playbook_path =  '/home/miggy/ansible-network/setPowerState.yml'
run_ansible_playbook(playbook_path)

print("Waiting for devices to boot up...")
time.sleep(150) 

push_config('/dev/ttyUSB2', '/home/miggy/ansible-network/config_files/cisco_switchTwo.txt')

time.sleep(30)

push_config('/dev/ttyUSB3', '/home/miggy/ansible-network/config_files/cisco_switchThree.txt')

end_time = time.time()

total_time = round(end_time - start_time, 2)
print(f"Execution time: {total_time} seconds")