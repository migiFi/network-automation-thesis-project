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
curl 'http://admin:12345678@192.168.0.5/Set.cmd?CMD=GetPower'
```

```shell
[syspimp@localhost ansible-ippower9258]$ ansible-playbook -i inventory ippower-getstate.yml 

PLAY [Get the power state of the IP Power 9258 unit] *****************************************************************

TASK [Get the state of all of the ports] *****************************************************************************
[WARNING]: The value ******** (type int) in a string field was converted to '********' (type string). If this does not look like what you expect, quote the entire value to ensure it does not change.

ok: [192.168.0.5 -> localhost]

TASK [Creating dictionary from the output] ***************************************************************************
ok: [192.168.0.5] => (item=<html>p61=1)
ok: [192.168.0.5] => (item=p62=1)
ok: [192.168.0.5] => (item=p63=1)
ok: [192.168.0.5] => (item=p64=1</html>
)

TASK [Show the Parsed Output] ****************************************************************************************
ok: [192.168.0.5] => {
    "result": {
        "port1": "On",
        "port2": "On",
        "port3": "On",
        "port4": "On"
    }
}

PLAY RECAP ***********************************************************************************************************
192.168.0.5   : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```



```shell
[syspimp@localhost ansible-ippower9258]$ ansible-playbook -e '{"outlets":[{"outlet":"1","state":"0"},{"outlet":"2","state":"0"}]}' -i inventory ippower-setstate.yml 

PLAY [Set the power state of the IP Power 9258 outlets] **************************************************************

TASK [Set the state of the Outlets being changed] ********************************************************************
ok: [192.168.0.5 -> localhost] => (item={'outlet': '1', 'state': '0'})
ok: [192.168.0.5 -> localhost] => (item={'outlet': '2', 'state': '0'})
[WARNING]: The value ******** (type int) in a string field was converted to '********' (type string). If this does
not look like what you expect, quote the entire value to ensure it does not change.


TASK [Get the state of the Outlets] **********************************************************************************
ok: [192.168.0.5 -> localhost]

TASK [Creating dictionary from the output] ***************************************************************************
ok: [192.168.0.5] => (item=<html>p61=0)
ok: [192.168.0.5] => (item=p62=0)
ok: [192.168.0.5] => (item=p63=1)
ok: [192.168.0.5] => (item=p64=1</html>
)

TASK [Show the Final State of Outlets] *******************************************************************************
ok: [192.168.0.5] => {
    "result": {
        "port1": "Off",
        "port2": "Off",
        "port3": "On",
        "port4": "On"
    }
}

PLAY RECAP ***********************************************************************************************************
192.168.0.5   : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

[syspimp@localhost ansible-ippower9258]$
```
