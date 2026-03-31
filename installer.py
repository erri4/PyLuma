from typing import Callable, Any
import ctypes
import sys
import urllib.request
import zipfile
import os
import io
import shutil
import stat
import json
import time
import subprocess
import requests

"""
compile:
nuitka --follow-imports --standalone --windows-console-mode=force --onefile .\installer.py
"""

try:
    import winreg
    import win32con
    import win32gui
except:
    if os.name == "nt":
        print('please install win32. use `pip install pywin32`')
        sys.exit()

dest_folder = "C:/PyLuma"

def remove_readonly(func: Callable[..., Any], path: str, exc_info: BaseException):
    os.chmod(path, stat.S_IWRITE)
    func(path)

if os.name == "nt":
    dest_folder = "C:/PyLuma"
elif os.name == "posix":
    import pwd
    sudo_user = os.environ.get("SUDO_USER")
    if sudo_user:
        dest_folder = os.path.join(pwd.getpwnam(sudo_user).pw_dir, 'PyLuma')
    else:
        dest_folder = os.path.expanduser("~/PyLuma")

def get_files():
    global dest_folder
    time.sleep(2)
    url = "https://github.com/Erri4/PyLuma/archive/refs/heads/main.zip"
    try:
        if os.path.exists(dest_folder):
            if os.name == 'nt':
                shutil.rmtree(dest_folder, onexc=remove_readonly)
            elif os.name == "posix":
                shutil.rmtree(dest_folder)
        os.makedirs(dest_folder)
    except Exception as e:
        print(e)
        input()
    with urllib.request.urlopen(url) as response:
        zip_data = response.read()
    
    with zipfile.ZipFile(io.BytesIO(zip_data)) as zip_ref:
        for member in zip_ref.namelist():
            filename = "/".join(member.split("/")[1:])
            if not filename:
                continue
            target_path = os.path.join(dest_folder, filename)
            if member.endswith("/"):
                os.makedirs(target_path, exist_ok=True)
            else:
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                with open(target_path, "wb") as f:
                    f.write(zip_ref.read(member))
    
    file_path = os.path.join(dest_folder, "bin/luma" + (".exe" if os.name != "nt" else ''))
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
        except Exception as e:
            print(e, file_path)
            input()
    repo = "Erri4/PyLuma"

    url = f"https://api.github.com/repos/{repo}/commits/main"

    with urllib.request.urlopen(url) as response:
        data = json.load(response)

    commit = data["sha"]
    jsonpth = os.path.join(dest_folder, "version.json")
    with open(jsonpth, 'r') as f:
        version = json.load(f)
        version['commit'] = commit
        with open(jsonpth, 'w') as w:
            json.dump(version, w)
    process_folder(os.path.join(dest_folder, 'bin'))
    if os.name == "posix":
        current_permissions = os.stat(os.path.join(dest_folder, 'bin', 'luma')).st_mode
        os.chmod(os.path.join(dest_folder, 'bin', 'luma'), current_permissions | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

        current_permissions = os.stat(os.path.join(dest_folder, 'bin', 'luma.bin')).st_mode
        os.chmod(os.path.join(dest_folder, 'bin', 'luma.bin'), current_permissions | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    else:
        win32gui.SendMessageTimeout(
            win32con.HWND_BROADCAST,
            win32con.WM_SETTINGCHANGE,
            0,
            "Environment",
            win32con.SMTO_ABORTIFHUNG,
            5000
        )
    if os.name == "nt":
        installer_src = os.path.join(dest_folder, "installer.exe")
        subprocess.Popen(['luma', '--aptins-internal', installer_src])
        sys.exit()
    elif os.name == "posix":
        installer_src = os.path.join(dest_folder, "installer.bin")
        subprocess.Popen([os.path.join(dest_folder, 'bin', 'luma'), '--aptins-internal', installer_src])
        sys.exit()
        


def add_to_PATH(path: str):
    if os.name == "nt":
        key = r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment"
        with winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE) as hklm:
            with winreg.OpenKey(hklm, key, 0, winreg.KEY_READ | winreg.KEY_WRITE) as env_key:
                current_path: str = winreg.QueryValueEx(env_key, "Path")[0]
                if path.lower() in current_path.lower():
                    print("Already in PATH.")
                    return
                new_path_value = current_path.rstrip(';') + ";" + path
                winreg.SetValueEx(env_key, "Path", 0, winreg.REG_EXPAND_SZ, new_path_value)
    elif os.name == "posix":
        bashrc = os.path.expanduser("~/.bashrc")
        with open(bashrc, "a") as f:
            f.write(f'\nexport PATH="{path}:$PATH"\n')

def parse_pointer(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()

    oid = None
    size = None

    for line in lines:
        if line.startswith("oid sha256:"):
            oid = line.strip().split(":")[1]
        elif line.startswith("size"):
            size = int(line.strip().split()[1])

    return oid, size


def download_lfs_file(oid, size, filepath):
    batch_url = f"https://github.com/Erri4/PyLuma.git/info/lfs/objects/batch"

    headers = {
        "Accept": "application/vnd.git-lfs+json",
        "Content-Type": "application/json",
    }

    data = {
        "operation": "download",
        "objects": [{"oid": oid, "size": size}],
    }

    r = requests.post(batch_url, json=data, headers=headers)
    r.raise_for_status()

    obj = r.json()["objects"][0]
    download_url = obj["actions"]["download"]["href"]

    file_data = requests.get(download_url).content

    with open(filepath, "wb") as f:
        f.write(file_data)



def is_lfs_pointer(path):
    try:
        with open(path, "r") as f:
            return "git-lfs" in f.readline()
    except:
        return False


def process_folder(folder):
    for root, _, files in os.walk(folder):
        for name in files:
            path = os.path.join(root, name)

            if is_lfs_pointer(path):
                print(f"Downloading real file for: {path}")

                oid, size = parse_pointer(path)
                if oid and size:
                    download_lfs_file(oid, size, path)

def is_admin():
    if os.name == "posix":
        return os.geteuid() == 0
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    add_to_PATH(dest_folder)
    add_to_PATH(os.path.join(dest_folder, 'bin'))
    get_files()
else:
    if os.name == "posix":
        print("please use sudo.")
        sys.exit()
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)