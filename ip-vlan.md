# TH VLAN TABLE

|Vlan|Name|Network|Default Router|DHCP|DHCP Server|DNS Server|
|:---:|:---|:---|:---|:---:|:---|:---|
|10|SZERVERTEREM|192.168.10.0/24|192.168.10.1|||8.8.8.8|
|20|IRODA|192.168.20.0/24|192.168.20.1|100-200|192.168.10.22 (windows)|192.168.10.22 (windows)|
|30|WIFI|192.168.30.0/24|192.168.30.1|10-254|192.168.10.22 (windows)|192.168.10.22 (windows)|
|40|TERMINAL|192.168.40.0/24|192.168.40.1|||192.168.10.22 (windows)|
|50|WEB|192.168.50.0/24|192.168.50.1|||8.8.8.8|
|99|MANAGEMENT|192.168.99.0/24|192.168.99.1|10-254|192.168.10.22 (windows)|192.168.10.22 (windows)|

# Devices

|Name|Internal IP|Translated IP|
|:---|:---|:---|
|Linux Server|192.168.10.9||
|Win Server|192.168.10.22||
|Exchange Server|192.168.10.19||
|Kertész Web Server|192.168.10.12|12.0.0.12|
