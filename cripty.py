import os 
import sys
import winreg as reg

cwd = os.getcwd()

python_exe = sys.executable

key_path = r"*\\shell\\Cripty" 
key = reg.CreateKeyEx(reg.HKEY_CLASSES_ROOT, key_path)

reg.SetValue(key, '', reg.REG_,"&Cripty")

key1 = reg.CreateKeyEx(key, r"command")

reg.SetValue(key1,'', reg.REG_SZ, python_exe + f'"{cwd}\\app.py"')