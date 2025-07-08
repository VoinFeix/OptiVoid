# Author = Manoj Meghwal

import os
import platform
import socket

from modules import system_updater
import time
from modules import preset_installer
from modules import system_cleanup
from modules.logger import LOG_FILE

def is_connected():
    try:
        socket.create_connection(("8.8.8.8", 53))
        return True
    except OSError:
        return False

clear = "clear" if platform.system().lower() != "windows" else "cls"


def logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            print("\n===== OptiVoid Logs =====\n")
            os.system(f"less {LOG_FILE}")

    else:
        print("\n[!] No logs found yet.\n")

def main():
    # Checking if the OptiVoid is running with sudo or not

    if os.getuid() != 0:
        print("❌ OptiVoid must be run with sudo/root privileges.")
        return

    if not is_connected():
        print("❌ No internet connection. Please connect to WiFi and try again.")
        return

    
    while True:

        print("===== Welcome to OptiVoid =====")
        print()
        print("Note: OptiVoid requires a higher amount of Internet, Only Proced when connected to Wifi.")
        print("1) Start")
        print("2) Logs")
        print("3) Exit")

        try:
            choice = int(input("Enter your choice: "))

        except ValueError:
            print("Invalid option, please try again.")
            continue
            
        if choice == "1":
            system_updater.run_updater()
            os.system(clear)

            time.sleep(1)

            while True:                    
                print("\n=== Select preset ===")
                print("1) Minimal")
                print("2) Normal")
                print("3) Developer")
                print("4) Full")
                print("5) Help")
                print("6) Back")

                preset = input("Preset choice: ")

                if preset == "1":
                    preset_installer.minimal_preset()
                    break

                elif preset == "2":
                    preset_installer.normal_preset()
                    break

                elif preset == "3":
                    preset_installer.developer_preset()
                    break

                elif preset == "4":
                    preset_installer.full_preset()
                    break

                elif preset == "5":
                    os.system(clear)
                    preset_help = """
                    <=== PRESET HELP MENU ===>

                    1) Minimal:
                    🛠 Lightweight apps, core utilities, Openbox setup. No bloat.
                    🔧 Desktop: Openbox

                    2) Normal:
                    📦 Tools for daily use: browser, file manager, system utilities, editors.
                    🖥 Desktop: Xfce4, Fluxbox

                    3) Developer:
                    👨‍💻 Includes code editors, compilers, Git, and dev tools.
                    🖥 Desktop: Xfce4, KDE Plasma, Fluxbox

                    4) Full:
                    🚀 Combines Minimal + Normal + Developer + Extra tools.
                    🖥 Desktop: Xfce4, KDE Plasma, Fluxbox, Mate

                    """
                    print(preset_help)
                
                elif preset == "6":
                    break

                else:
                    print("Invalid option, please try again.")
                    continue
                    
            
            system_cleanup.run_cleanup()
            

        elif choice == "2":
            os.system(clear)
            logs()

        elif choice == "3":
            print("Thank You for using OptiVoid. GoodBye!")
            break

        else:
            print("Invalid option, please try again.")

       

if __name__ == '__main__':
    main()