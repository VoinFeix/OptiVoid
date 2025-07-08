# 🧠 OptiVoid - Ultimate Void Linux Post-Install Toolkit

**OptiVoid** is a powerful post-install automation tool tailored for Void Linux users. It helps users install desktop environments, essential tools, developer utilities, and clean up the system in just a few minutes — all from a terminal-based interface.

---

## 🔧 Features

- ✅ **System Updater** — Updates your system and installs essential packages.
- 🎯 **Presets Installer**
  - **Minimal:** Lightweight Openbox setup.
  - **Normal:** Xfce4 + Fluxbox for everyday use.
  - **Developer:** Full programming environment (Xfce4, KDE, dev tools).
  - **Full:** Everything above + Mate Desktop.
- 🧹 **System Cleanup** — Clears package cache, orphan packages, thumbnails, trash, and old logs.
- 📜 **Logging** — All actions are logged to `~/optivoid_logs.txt`.
- 📡 **Internet and Root Check** — Prevents execution without root or active connection.

---

## 🧰 Requirements

- Python 3
- Void Linux (with `xbps-install`)
- Root (sudo) privileges
- Internet connection

---

## 📦 Installation

1. Clone the Repository

```bash
git clone <>
cd
```

2. Run the Program
```bash
sudo python3 optivoid.py
```

---

## 📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Contact
- Created by Manoj Meghwal.
- Feel free to open issues or submit pull requests.
