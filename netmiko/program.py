#!/usr/bin/env python3

from base64 import b64encode, b64decode
from getpass import getpass
from hashlib import sha256
from random import randint
import sys

# netmiko
from netmiko import ConnectHandler
# pycryptodome
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def readpass(path: str, key: str):
    with open(path, "r") as f:
        iv = b64decode(f.readline().removesuffix("\n"))
        ct = b64decode(f.readline().removesuffix("\n"))
    cipher = AES.new(pad(key.encode(), AES.block_size), AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ct), AES.block_size).decode()


def writepass(path: str, key: str, sshpass: str):
    cipher = AES.new(pad(key.encode(), AES.block_size), AES.MODE_CBC)
    bytes = cipher.encrypt(pad(sshpass.encode(), AES.block_size))
    iv = b64encode(cipher.iv).decode("utf-8")
    ct = b64encode(bytes).decode("utf-8")
    with open(path, "w") as f:
        f.writelines([iv, '\n', ct])


with open("ips.txt", "r") as f:
    iplist = [x.removesuffix("\n") for x in f.readlines()]

key = getpass()
with open("hash.txt", "r") as f:
    if sha256(key.encode()).hexdigest() != f.readline().removesuffix("\n"):
        print("Wrong password!", file=sys.stderr)
        sys.exit(1)

sshpass = readpass("pass.txt", key)
enapass = readpass("enable.txt", key)

newsshpass = sha256(str(randint(0, 0xFFFFFFFF)).encode()).hexdigest()[:16]
print("New passord: " + newsshpass)
writepass("pass.txt", key, newsshpass)

for ip in iplist:
    args = {
        "device_type": "cisco_ios",
        "ip": ip,
        "username": "user",
        "password": sshpass,
        "secret": enapass,
    }

    commands = [
        "username user secret " + newsshpass,
        "do write"
    ]

    print("Trying " + ip)
    try:
        nc = ConnectHandler(**args)
        nc.enable()
        nc.send_config_set(commands)
        nc.disconnect()
        print("Successfully set password for " + ip)
    except:
        print("Failed to set password for " + ip, file=sys.stderr)
