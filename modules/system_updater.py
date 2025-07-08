# system_updater.py
import os
import subprocess
from modules.logger import write_log

def run_updater():
    print("\n[OptiVoid] Updating system and installing essential tools...\n")

    try:
        print("\n[*] Updating system packages...")
        subprocess.run(["xbps-install", "-Syu"], check=True)

        tools = [
            "sudo", "curl", "wget", "rsync", "openssh", "ca-certificates", "gnupg", "htop", "btop", "neofetch", "lsd", "psmisc", "xclip", "which", "nano", "vim", "micro", "bash-completion", "man-pages", "less", "git", "gcc", "make", "cmake", "binutils", "pkg-config", "xorg", "xorg-minimal", "grub", "xinit", "dbus"
        ]
        

        print("\n[*] Installing essential tools...")

        # Install all tools
        for i, t in enumerate(sorted(set(tools)), 1):
            try:
                print(f"[{i}/{len(tools)}] Installing: {t}")
                write_log(f"[~] Installing: {t}")
                result = subprocess.run(["xbps-install", "-Sy", t], capture_output=True, text=True)

                if result.returncode != 0:
                    print(f"[!] Failed to install {t}. Reason:\n{result.stderr}")
                    write_log(f"[!] Failed to install {t}. Reason:\n{result.stderr}")
                else:
                    print(f"[✓] Installed: {t}")
                    write_log(f"[✓] Installed: {t}")

            except Exception as e:
                print(f"[X] Error installing {t}: {e}")
                write_log(f"[X] Error installing {t}: {e}")
                continue

 
        print("\n✅ All essential tools installed successfully!\n")

    except subprocess.CalledProcessError as e:
        print(f"\n[!] Command failed: {e}")
    except Exception as e:
        print(f"\n!] Unexpected error: {e}")

    try:
        if not os.path.exists("/var/service/dbus"):
            subprocess.run(["ln", "-s", "/etc/sv/dbus", "/var/service"], check=True)
    except Exception as e:
        print(f"[!] Failed to enable Dbus: {e}")