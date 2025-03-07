import os
import sys
import subprocess
import time
from onelib import *

def run(filename):
        with open(filename, 'r') as file:
            script = file.read()

        exec("from onelib import *\n" + script)

shexec = input("OneRun $ ")

run(shexec)