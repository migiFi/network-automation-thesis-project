import schedule
import subprocess
import time
import os

def start_devices():
    os.chdir('/home/miggy/ansible-network/playbooks')
    command = [
        "nohup",
        "ansible-playbook",
        "-e", '{"outlets":[{"outlet":"1","state":"1"},{"outlet":"2","state":"1"}]}',
        "-i", "inventory",
        "setPowerState.yml",
        "> start_devices.log 2>&1"
    ]
    subprocess.Popen(command)

def shutdown_devices():
    os.chdir('/home/miggy/ansible-network/playbooks')
    command = [
        "nohup",
        "ansible-playbook",
        "-e", '{"outlets":[{"outlet":"1","state":"0"},{"outlet":"2","state":"0"}]}',
        "-i", "inventory",
        "setPowerState.yml",
        "> shutdown_devices.log 2>&1"
    ]
    subprocess.Popen(command)

schedule.every().day.at("09:00").do(start_devices)

schedule.every().day.at("18:00").do(shutdown_devices)

while True:
    schedule.run_pending()
    time.sleep(60)
