import subprocess
import os
import time
import sys
import glob

clear = lambda: os.system("cls")

clear()

requirements = open("req.txt").read().splitlines()
log = open("./content/install.log", "w")
for package in requirements:
    print("Atualizando dados...")
    time.sleep(1)
    print("Conectando com o servidor...")
    p = subprocess.call([sys.executable, "-m", "pip", "install", package],stdout=log, stderr=subprocess.STDOUT)

clear()

import dotExec