#!/usr/bin/env python3

import subprocess

subprocess.run(["date"])
subprocess.run(["sleep", "2"])
resultado = subprocess.run(["ls", "este_archivo_no_existe.txt"])
print(resultado.returncode)