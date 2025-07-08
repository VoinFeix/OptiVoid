#!/usr/bin/env python3

import enum
import time
import subprocess
import os
from modules.logger import write_log

    
def minimal_preset():
    # Openbox Desktop
    print("\n[~] Installing Minimal Preset...")
    time.sleep(1)

    tools = [
        "falkon", "pcmanfm", "gvfs", "mpv", "pavucontrol", "ristretto", "pulseaudio", "alsa-utils", "mousepad", "lxterminal", "lxappearance", "xterm", "openbox", "obconf", "lxrandr", "tint2" ,"tint2conf" ,"volumeicon", "NetworkManager", "network-manager-applet", "xfce4-notifyd", "sddm", "feh", "obmenu-generator", "breeze-snow-cursor-theme"
    ]
    
        
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

    print("[*] Minimal preset tools installed.")
    write_log("[*] Minimal preset tools installed.")
            
    # Setup .xinitrc and .xsession
    home = os.path.expanduser("~/")

    session_cmd = "exec openbox-session\n"

    with open(os.path.join(home, ".xinitrc"), "w") as f:
        f.write(session_cmd)

    with open(os.path.join(home, ".xsession"), "w") as f:
        f.write(session_cmd)

    # Enable Sddm login manager
    try:
        if not os.path.islink("/var/service/sddm"):
            subprocess.run(["ln", "-s", "/etc/sv/sddm", "/var/service"], check=True)
            write_log("Enabled Sddm login manager.")
    except Exception as e:
        print(f"[!] Failed to enable Sddm: {e}")
        write_log(f"[!] Failed to enable Sddm: {e}")
    
    # Configuring openbox
    ob_config_path = os.path.expanduser("~/.config/openbox")
    os.makedirs(ob_config_path, exist_ok=True)
        
    file = os.path.expanduser("~/.config/openbox/autostart")
    os.makedirs(os.path.dirname(file), exist_ok=True)

    autostart = """obmenu-generator -i -p &
    tint2 &
    nm-applet &
    volumeicon &
    xfce4-notifyd &
    feh --bg-scale ~/wallpaper.png &
    """

    with open(file, "w") as f:
        f.write(autostart)

    
    print("\n✅ Minimal preset applied successfully!\n")
    write_log("\n✅ Minimal preset applied successfully!\n")
    time.sleep(1)

    print("👉 You can now reboot and login via your selected desktop.")
    print("👉 Or type `startx` if you're using `.xinitrc` without display manager.")




def normal_preset():
    # Xfce4 and Fluxbox Desktop
    print("\n[~] Installing Normal Preset...")
    time.sleep(1)

    tools = [
        "libreoffice", "gimp", "vlc", "firefox", "Thunar", "file-roller", "galculator", "xfce4-screenshooter", "evince", "pavucontrol", "xscreensaver", "xfce4", "htop", "cmatrix", "xf86-video-amdgpu", "xf86-video-intel", "xf86-video-nouveau", "sddm", "blueman", "bluez", "bluez-alsa" , "fluxbox", "xdgmenumaker", "openvpn", "ksnip", "lxterminal", "alacritty", "ranger", "NetworkManager", "network-manager-applet", "pa-applet", "chromium", "gvfs", "udisk2", "simple-scan", "papirus-icon-theme", "picom", "acpid", "upower", "xfce4-power-manager", "breeze-snow-cursor-theme"
    ]

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

    print("[*] Normal preset tools installed.")
    write_log("[*] Normal preset tools installed.")

    # Enable Sddm login manager
    try:
        if not os.path.islink("/var/service/sddm"):
            subprocess.run(["ln", "-s", "/etc/sv/sddm", "/var/service"], check=True)
            write_log("Enabled Sddm login manager.")
    except Exception as e:
        print(f"[!] Failed to enable Sddm: {e}")
        write_log(f"[!] Failed to enable Sddm: {e}") 

    # Setup .xinitrc and .xsession
    home = os.path.expanduser("~")
    
    options = {
        "1": ("xfce4-session", "Xfce4"),
        "2": ("fluxbox-session", "Fluxbox"),
    }

    while True:
        print("<=== Default Desktop Environment ===>")
        for key, (_, name) in options.items():
            print(f"{key}) {name}")

        choice = input("Enter your choice: ").strip()

        if choice in options:
            session_cmd, name = options[choice]
            session_cmd = f"exec {session_cmd}\n"
            write_log(f"Selected {name} Desktop Environment.")
            break

        else:
            print("Invalid input, defaulting to Xfce4.")
            session_cmd = "exec xfce4-session\n"
            write_log("Selected Default Xfce4 Desktop Environment.")
            break

    with open(os.path.join(home, ".xinitrc"), "w") as f:
        f.write(session_cmd)

    with open(os.path.join(home, ".xsession"), "w") as f:
        f.write(session_cmd)

    print("\n✅ Normal preset applied successfully!\n")
    write_log("\n✅ Normal preset applied successfully!\n")
    time.sleep(1)

    print("👉 You can now reboot and login via your selected desktop.")
    print("👉 Or type `startx` if you're using `.xinitrc` without display manager.")

   


def developer_preset():
        # Xfce4 ,Fluxbox and KDE Plasma Desktop
    print("\n[~] Installing Developer Preset...")
    time.sleep(1)

    tools = [
        "gimp", "vlc", "firefox", "Thunar", "file-roller", "galculator", "xfce4-screenshooter", "evince", "pavucontrol", "xscreensaver", "xfce4", "htop", "cmatrix", "xf86-video-amdgpu", "xf86-video-intel", "xf86-video-nouveau", "sddm", "blueman", "bluez", "bluez-alsa" , "fluxbox", "xdgmenumaker", "openvpn", "ksnip", "lxterminal", "alacritty", "ranger", "NetworkManager", "network-manager-applet", "pa-applet", "chromium", "gvfs", "udisk2", "simple-scan", "papirus-icon-theme", "picom", "acpid", "upower", "xfce4-power-manager", "breeze-snow-cursor-theme", "git", "make", "gcc", "python3", "python3-pip", "python3-setuptools", "neovim", "micro", "helix", "tmux", "curl", "wget", "zip", "unzip", "cmake", "man-pages", "bash-completion", "geany", "meld", "vscode", "sqlite", "sqlitebrowser", "nodejs", "flatpak", "ark", "dolphin", "kde5", "kde-plasma", "kde5-baseapps","kde-connect", "konsole", "qt5-svg", "breeze", "sddm-kcm"
    ]

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

    print("[*] Developer preset tools installed.")
    write_log("[*] Developer preset tools installed.")
                    
    # Enable Sddm login manager
    try:
        if not os.path.islink("/var/service/sddm"):
            subprocess.run(["ln", "-s", "/etc/sv/sddm", "/var/service"], check=True)
            write_log("Enabled Sddm login manager.")
    except Exception as e:
        print(f"[!] Failed to enable Sddm: {e}")
        write_log(f"[!] Failed to enable Sddm: {e}") 

    # Setup .xinitrc and .xsession
    home = os.path.expanduser("~")
    
    options = {
        "1": ("xfce4-session", "Xfce4"),
        "2": ("fluxbox-session", "Fluxbox"),
        "3": ("startplasma-x11", "KDE Plasma")
    }

    while True:
        print("<=== Default Desktop Environment ===>")
        for key, (_, name) in options.items():
            print(f"{key}) {name}")

        choice = input("Enter your choice: ").strip()

        if choice in options:
            session_cmd, name = options[choice]
            session_cmd = f"exec {session_cmd}\n"
            write_log(f"Selected {name} Desktop Environment.")
            break

        else:
            print("Invalid input, defaulting to Xfce4.")
            session_cmd = "exec xfce4-session\n"
            write_log("Selected Default Xfce4 Desktop Environment.")
            break


    with open(os.path.join(home, ".xinitrc"), "w") as f:
        f.write(session_cmd)

    with open(os.path.join(home, ".xsession"), "w") as f:
        f.write(session_cmd) 


    print("\n✅ Developer preset applied successfully!\n")
    write_log("\n✅ Developer preset applied successfully!\n")
    time.sleep(1)

    print("👉 You can now reboot and login via your selected desktop.")
    print("👉 Or type `startx` if you're using `.xinitrc` without display manager.")



def full_preset():
    # Xfce4, Fluxbox, KDE Plasma and Mate Desktop

    print("\n[~] Installing Full Preset...")
    time.sleep(1)

    tools = [
        "gimp", "vlc", "firefox", "Thunar", "file-roller", "galculator", "xfce4-screenshooter", "evince", "pavucontrol", "xscreensaver", "xfce4", "htop", "cmatrix", "xf86-video-amdgpu", "xf86-video-intel", "xf86-video-nouveau", "sddm", "blueman", "bluez", "bluez-alsa" , "fluxbox", "xdgmenumaker", "openvpn", "ksnip", "lxterminal", "alacritty", "ranger", "NetworkManager", "network-manager-applet", "pa-applet", "chromium", "gvfs", "udisk2", "simple-scan", "papirus-icon-theme", "picom", "acpid", "upower", "xfce4-power-manager", "breeze-snow-cursor-theme", "git", "make", "gcc", "python3", "python3-pip", "python3-setuptools", "neovim", "micro", "helix", "tmux", "curl", "wget", "zip", "unzip", "cmake", "man-pages", "bash-completion", "geany", "meld", "vscode", "sqlite", "sqlitebrowser", "nodejs", "flatpak", "ark", "dolphin", "kde5", "kde-plasma", "kde5-baseapps","kde-connect", "konsole", "qt5-svg", "breeze", "sddm-kcm", "mate", "mate-extra"
    ]

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

    print("[*] Full preset tools installed.")
    write_log("[*] Full preset tools installed.")

    # Enable Sddm login manager
    try:
        if not os.path.islink("/var/service/sddm"):
            subprocess.run(["ln", "-s", "/etc/sv/sddm", "/var/service"], check=True)
            write_log("Enabled Sddm login manager.")
    except Exception as e:
        print(f"[!] Failed to enable Sddm: {e}")
        write_log(f"[!] Failed to enable Sddm: {e}") 


    # Setup .xinitrc and .xsession
    home = os.path.expanduser("~")
    
    options = {
        "1": ("xfce4-session", "Xfce4"),
        "2": ("fluxbox-session", "Fluxbox"),
        "3": ("startplasma-x11", "KDE Plasma"),
        "4": ("mate-session", "Mate")
    }

    while True:
        print("<=== Default Desktop Environment ===>")
        for key, (_, name) in options.items():
            print(f"{key}) {name}")

        choice = input("Enter your choice: ").strip()

        if choice in options:
            session_cmd, name = options[choice]
            session_cmd = f"exec {session_cmd}\n"
            write_log(f"Selected {name} Desktop Environment.")
            break

        else:
            print("Invalid input, defaulting to Plasma desktop.")
            session_cmd = "exec startplasma-x11\n"
            write_log("Selected Default Plasma Desktop Environment.")
            break


    with open(os.path.join(home, ".xinitrc"), "w") as f:
        f.write(session_cmd)

    with open(os.path.join(home, ".xsession"), "w") as f:
        f.write(session_cmd)


    print("\n✅ Full preset applied successfully!\n")
    write_log("\n✅ Full preset applied successfully!\n")
    time.sleep(1)

    print("👉 You can now reboot and login via your selected desktop.")
    print("👉 Or type `startx` if you're using `.xinitrc` without display manager.")
    