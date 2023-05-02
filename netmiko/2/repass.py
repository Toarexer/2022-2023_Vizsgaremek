#!/usr/bin/env python3

from hashlib import sha256
from netmiko import ConnectHandler
from os import chdir, rename
from os.path import dirname, exists
from random import randint
import sys


def readcsv(path: str, errpath: str):
    arr = []
    with open(path, "r") as f:
        with open(errpath, "a") as e:
            for line in [x.removesuffix("\n") for x in f.readlines()]:
                args = line.split(";")
                try:
                    arr.append(
                        {
                            "ip": args[0],
                            "port": int(args[1]),
                            "user": args[2],
                            "pass": args[3],
                            "secret": args[4],
                            "success": bool(args[5])
                        }
                    )
                except:
                    print("Failed to parse: " + line, file=sys.stderr)
                    e.write(line + "\n")
    return arr


def writecsv(path: str, hosts: list):
    open(path, "w").close()
    with open(path, "a") as f:
        for host in hosts:
            print(host["ip"],
                  host["port"],
                  host["user"],
                  host["pass"],
                  host["secret"],
                  host["success"],
                  sep=";", file=f)


chdir(dirname(__file__))

csvfile = "hosts.csv"
errfile = "errors.txt"

if not exists(csvfile):
    open(csvfile, "w").close()
if not exists(errfile):
    open(errfile, "w").close()

hosts = readcsv(csvfile, errfile)

for host in filter(lambda h: (len(sys.argv) == 1) or (h["ip"] in sys.argv[1:]), hosts):
    args = {
        "device_type": "cisco_ios",
        "ip": host["ip"],
        "port": host["port"],
        "username": host["user"],
        "password": host["pass"],
        "secret": host["secret"],
    }

    newpass = sha256(str(randint(0, 0xFFFFFFFF)).encode()).hexdigest()[:16]

    commands = [
        "username " + host["user"] + " secret " + newpass,
        "do write"
    ]

    print("Trying " + host["ip"])
    try:
        with ConnectHandler(**args) as nc:
            nc.enable()
            nc.send_config_set(commands)
        print("Successfully set password for " + host["ip"])
        host["pass"] = newpass
        host["success"] = True
    except:
        print("Failed to set password for " + host["ip"], file=sys.stderr)
        host["success"] = False

rename(csvfile, csvfile.replace(".csv", ".prev.csv"))
writecsv(csvfile, hosts)
