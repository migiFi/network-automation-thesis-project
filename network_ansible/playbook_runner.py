import ansible_runner
import serial
import time

devices = {
    'master': '/dev/ttyUSB1',
    'nodeOne': '/dev/ttyUSB0',
}

commands = {
    'master': [
        b'enable\n',
        b'confifure terminal\n',
        b'hostname master\n'
        b'crypto key generate rsa\n',
        b'line vty 0 15\n',
        b'login local\n',
        b'transport input ssh\n',
        b'exit\n'
        b'username cisco privilege 15 secret cisco123\n',
        b'ip ssh version 2\n',
        b'write memory\n'
    ],
    'nodeOne': [
        b'enable\n',
        b'confifure terminal\n',
        b'hostname nodeOne\n'
        b'ip domain-name cisco.com'
        b'crypto key generate rsa\n',
        b'line vty 0 15\n',
        b'login local\n',
        b'transport input ssh\n',
        b'exit\n'
        b'username cisco privilege 15 secret cisco123\n',
        b'ip ssh version 2\n',
        b'write memory\n'
        
    ],
    
}

runner = ansible_runner.run(
    private_data_dir='/home/miggy/network-automation-thesis-project/network_ansible', 
    playbook='rollback-playbook.yml'
)

while "Reloading device" not in runner.events:
    time.sleep(1)

for device, port in devices.items():
    print(f"Configuring {device}...")
    connection = serial.Serial(port, 9600)
    for command in commands[device]:
        connection.write(command)
        time.sleep(4)
    print(f"{device} configuration completed.")
    connection.close()

while True:
    output = connection.readline().decode('utf-8')
    if "SSH connectivity restored" in output:
        break

runner.wait()
