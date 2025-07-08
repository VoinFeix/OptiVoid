# modules/system_cleanup.py

import os
import subprocess
import shutil
from modules.logger import write_log

def clean_package_cache():
    print("[*] Cleaning XBPS package cache...")
    try:
        subprocess.run(["xbps-remove", "-Oo"], check=True)
        write_log("Cleaned XBPS package cache.")
    except Exception as e:
        print(f"[!] Failed to clean XBPS cache: {e}")
        write_log(f"Failed to clean XBPS cache: {e}")


def clean_orphan_packages():
    print("[*] Removing orphan packages...")
    try:
        subprocess.run(["xbps-remove", "-oO"], check=True)
        write_log("Cleaned Orphan packages.")
    except Exception as e:
        print(f"[!] Failed to remove orphan packages: {e}")
        write_log(f"[!] Failed to remove orphan packages: {e}")



def clean_thumbnails():
    print("[*] Cleaning user thumbnail cache...")
    thumb_path = os.path.expanduser("~/.cache/thumbnails")
    try:
        if os.path.exists(thumb_path):
            shutil.rmtree(thumb_path)
            print("[+] Thumbnail cache cleaned.")
            write_log("[+] Thumbnail cache cleaned.")
        else:
            print("[~] No thumbnail cache found.")
            write_log("[~] No thumbnail cache found.")
    except Exception as e:
        print(f"[!] Failed to clean thumbnails: {e}")
        write_log(f"[!] Failed to clean thumbnails: {e}")

def clean_trash():
    print("[*] Emptying user Trash...")
    trash_path = os.path.expanduser("~/.local/share/Trash")
    try:
        if os.path.exists(trash_path):
            shutil.rmtree(trash_path)
            print("[+] Trash emptied.")
            write_log("[+] Trash emptied.")
        else:
            print("[~] Trash is already clean.")
            write_log("[~] Trash is already clean.")
    except Exception as e:
        print(f"[!] Failed to clean Trash: {e}")
        write_log(f"[!] Failed to clean Trash: {e}")


def clean_logs():
    print("[*] Cleaning log files...")
    log_dirs = ["/var/log", "/var/tmp"]
    for log_dir in log_dirs:
        try:
            subprocess.run(["find", log_dir, "-type", "f", "-name", "*.log", "-delete"])
            print(f"[+] Logs in {log_dir} cleaned.")
            write_log(f"[+] Logs in {log_dir} cleaned.")
        except Exception as e:
            print(f"[!] Failed to clean logs in {log_dir}: {e}")
            write_log(f"[!] Failed to clean logs in {log_dir}: {e}")

def run_cleanup():
    print("\n[OptiVoid] Running full system cleanup...\n")
    clean_package_cache()
    clean_orphan_packages()
    clean_thumbnails()
    clean_trash()
    clean_logs()
    print("\n✅ System cleanup completed!\n")
    write_log("\n✅ System cleanup completed!\n")