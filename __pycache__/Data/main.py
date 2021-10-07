import subprocess
import os
import time
import sys
import glob

requirements = open("req.txt").read().splitlines()
log = open("./content/install.log", "w")
for package in requirements:
    print("Atualizando dados...")
    p = subprocess.call([sys.executable, "-m", "pip", "install", package],stdout=log, stderr=subprocess.STDOUT)
