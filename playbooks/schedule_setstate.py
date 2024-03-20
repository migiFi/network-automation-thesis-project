import schedule
import subprocess
import time

def shutdown_devices():
    command = [
        "ansible-playbook",
        "-e", '{"outlets":[{"outlet":"1","state":"0"},{"outlet":"2","state":"0"}]}',
        "-i", "inventory",
        "ippower-setstate.yml"
    ]
    subprocess.run(command)

def start_devices():
    command = [
        "ansible-playbook",
        "-e", '{"outlets":[{"outlet":"1","state":"1"},{"outlet":"2","state":"1"}]}',
        "-i", "inventory",
        "ippower-setstate.yml"
    ]
    subprocess.run(command)

schedule.every().day.at("18:00").do(shutdown_devices)

schedule.every().day.at("09:00").do(start_devices)

while True:
    schedule.run_pending()
    time.sleep(60)
