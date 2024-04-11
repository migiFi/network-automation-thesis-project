import schedule
import subprocess
import time
import os

def start_devices():
    os.chdir('/home/miggy/ansible-network/playbooks')
    command = [
        "ansible-playbook",
        "-e", '{"outlets":[{"outlet":"1","state":"1"},{"outlet":"2","state":"1"}]}',
        "-i", "inventory",
        "setPowerState.yml"
    ]
    with open("start_devices.log", "w") as logfile:
        subprocess.Popen(command, stdout=logfile, stderr=subprocess.STDOUT)

def shutdown_devices():
    os.chdir('/home/miggy/ansible-network/playbooks')
    command = [
        "ansible-playbook",
        "-e", '{"outlets":[{"outlet":"1","state":"0"},{"outlet":"2","state":"0"}]}',
        "-i", "inventory",
        "setPowerState.yml"
    ]
    with open("shutdown_devices.log", "w") as logfile:
        subprocess.Popen(command, stdout=logfile, stderr=subprocess.STDOUT)

schedule.every().day.at("08:30").do(start_devices)
schedule.every().day.at("18:00").do(shutdown_devices)

while True:
    schedule.run_pending()
    time.sleep(60)
