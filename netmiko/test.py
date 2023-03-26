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


def readpass(key: str):
    with open("pass.txt", "r") as f:
        iv = b64decode(f.readline().removesuffix("\n"))
        ct = b64decode(f.readline().removesuffix("\n"))
    cipher = AES.new(pad(key.encode(), AES.block_size), AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ct), AES.block_size).decode()

with open("ips.txt", "r") as f:
    iplist = [x.removesuffix("\n") for x in f.readlines()]

key = getpass()
with open("hash.txt", "r") as f:
    if sha256(key.encode()).hexdigest() != f.readline().removesuffix("\n"):
        print("wrong pasword!", file=sys.stderr)
        sys.exit(1)

sshpass = readpass(key)

for ip in iplist:
    args = {
        "device_type": "cisco_ios",
        "ip": ip,
        "username": "user",
        "password": sshpass,
    }

    print("trying " + ip)
    try:
        ConnectHandler(**args).disconnect()
        print("successfully connected to " + ip)
    except:
        print("failed to connect to " + ip, file=sys.stderr)
