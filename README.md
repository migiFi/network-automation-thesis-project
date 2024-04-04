# Ansible Network Automation Thesis Project

This my implematantion of using Ansible to automate some of the network devices at `Metropolia University of Applied Sciences` lab. Bellow you can find the Ansible playbooks, inventories, configurations (used fortesting) and a Python Script that puts it all together.  

# Why? 



# Device

Cisco:
    - Cisco router
    - Cisco Switch 

HP:
    - HP Switch

AVIOSYS:
    - IP Power 9258

# Topology

The idea for this project was to be able to automate the network's lab since its still being manually manage for updates, lab/exams configs and power, below is an image of the topogy used for testing the devices. The topoly consist of a Linux machine (Ubuntu 23.10) as the control node and 4 network devices as the remote host.


# how to use to use the Network-Ansible playbook







# how to use the IP Power 9258 playbooks

Credits go to @syspimp (https://github.com/syspimp) for this straightforward but great example of how to automate and manage the the IP Power 9258 using Ansible.


```shell
curl 'http://admin:12345678@192.168.1.10/Set.cmd?CMD=GetPower'
```

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
output.content looks like this: <html>p61=1,p62=1,p63=1,p64=1</html>, 
where P61 thru P64 are the 4 outlets and
1 is outlet on, 0 is outlet off
we create a dictionary by splitting on the comma in output.content,
reate an index variable outlet_index to track the outlet number in a dictionary named 'result'if 'result' is not set, default to empty {} and combine with local vars: 'key' and 'value'
local vars: 'value' is set by removing all content except the outlet state using regex_replace
replace '0' to be 'Off'
create an if/then by searching for Off and if not found output On
result = {"Port1": "On", "Port2": "Off" ...}


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
