# Network Automation Thesis Project

This is my implementation of using Ansible and Python for my bachelor's thesis to automate the network lab at `Metropolia University of Applied Sciences`. In this project, you can find the Ansible playbooks, inventory, and Python Scripts that made it possible.  

# Goal

The main goal for this project was to be able to automate the network's lab since it is still being manually managed for updates, lab/exams configurations, and power management, and to provide a road map of playbook and scripts to help the lectures introduce network automation for network management and educational purposes.

# Devices

PC:
    - Ubuntu 23.10

Router & Switches:
    - Cisco 2801 router
    - Cisco Catalyst 3560 Switch 

Web controller:
    - IP Power 9258

# Topology

Below is an image of the topology used for testing the Ansible playbooks and Python scripts. The topology consists of a Linux machine as the control node to a web controller, and 4 network devices.

![Getting Started](./images/Thesis_topology.png)


# How to use the IP Power 9258 playbooks

Credits for the web controller playbooks go to [syspimp](https://github.com/syspimp) for his straightforward but great example of how to automate and manage the IP Power 9258 using Ansible.

To use, curl or visit this URL to test if this will work on your IP Power. The default user is admin, and the default password is '12345678'. Change it if needed and change the IP address as needed. I used use 192.168.1.10 in this example:

```shell
curl 'http://admin:12345678@192.168.1.10/Set.cmd?CMD=GetPower'
```
If you get something like this back 'p61=1,p62=1,p63=1,p64=1', you are all set. Otherwise, you will need to enable HTTP commands in the Web Console for your IP Power 9258 unit. Visit http://192.168.1.10/system.htm to enable HTTP commands. Your device may reboot and cut the power to anything connected when you change a setting!!

```shell
$ ansible-playbook -i inventory getPowerState.yml 

PLAY [Get the power state of the IP Power 9258 unit] *****************************

TASK [Get the state of all of the ports] *****************************************
ok: [192.168.1.10 -> localhost]

TASK [Creating dictionary from the output] ***************************************
ok: [192.168.1.10] => (item=<html>p61=0)
ok: [192.168.1.10] => (item=p62=0)
ok: [192.168.1.10] => (item=p63=0)
ok: [192.168.1.10] => (item=p64=0</html>
)

TASK [Show the Parsed Output] ****************************************************
ok: [192.168.1.10] => {
    "result": {
        "port1": "Off",
        "port2": "Off",
        "port3": "Off",
        "port4": "Off"
    }
}

PLAY RECAP ***********************************************************************
192.168.1.10               : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0     

```

You can also pass in extra-vars to the playbook using the -e flag on the command line:

```shell
$ ansible-playbook -e '{"outlets":[{"outlet":"1","state":"1"},{"outlet":"2","state":"1"}]}' -i inventory setPowerState.yml 

$ ansible-playbook -i inventory setPowerState.yml 

PLAY [Set the power state of the IP Power 9258 outlets] **************************

TASK [Set the state of the Outlets being changed] ********************************
ok: [192.168.1.10 -> localhost] => (item={'outlet': 1, 'state': 1})
ok: [192.168.1.10 -> localhost] => (item={'outlet': 2, 'state': 1})

TASK [Get the state of the Outlets] **********************************************
ok: [192.168.1.10 -> localhost]

TASK [Creating dictionary from the output] ***************************************
ok: [192.168.1.10] => (item=<html>p61=1)
ok: [192.168.1.10] => (item=p62=1)
ok: [192.168.1.10] => (item=p63=0)
ok: [192.168.1.10] => (item=p64=0</html>
)

TASK [Show the Final State of Outlets] *******************************************
ok: [192.168.1.10] => {
    "result": {
        "port1": "On",
        "port2": "On",
        "port3": "Off",
        "port4": "Off"
    }
}

PLAY RECAP ***********************************************************************
192.168.1.10               : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   



```
