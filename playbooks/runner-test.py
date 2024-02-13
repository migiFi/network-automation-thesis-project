import ansible_runner
import serial
import time

devices = {
    'nodeOne': '/dev/ttyUSB0',
}

commands = {
    'nodeOne': [
        b'enable\n',
        b'confifure terminal\n',
        b'hostname nodeOne\n',
        b'ip domain-name cisco.com',
        b'crypto key generate rsa\n',
        b'line vty 0 15\n',
        b'transport input ssh\n',
        b'login local\n',
        b'exit\n',
        b'username cisco privilege 15 secret cisco123\n',
        b'ip ssh version 2\n',
        b'write memory\n'
    ],
    
}

runner = ansible_runner.run(
    private_data_dir='/home/miggy/network-automation-thesis-project/network_ansible/', 
    playbook='testing.yml'
)

while "Reloading device" not in runner.events:
    time.sleep(3)

for device, port in devices.items():
    print(f"Configuring {device}...")
    connection = serial.Serial(port, 9600)
    for command in commands[device]:
        connection.write(command)
        time.sleep(6)
    print(f"{device} configuration completed.")
    connection.close()

while True:
    output = connection.readline().decode('utf-8')
    if "SSH connectivity restored" in output:
        break

runner.wait()
