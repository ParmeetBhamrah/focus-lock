# Focus Lock 🔒

A simple yet effective Python tool to boost productivity by blocking distracting apps for a set duration.

## 🚀 Features

- Block one or multiple apps by name (e.g., `notepad.exe`, `chrome.exe`)
- Custom duration: choose hours or minutes
- Terminates running instances of selected apps
- Keeps monitoring in the background and blocks app relaunches
- Lightweight and command-line based

## 🛠️ Tech Stack

- [Python](https://www.python.org/)
- [psutil](https://pypi.org/project/psutil/)

## 🧠 How It Works

- The script prompts the user to input names of apps to block and a duration.
- It checks every 2 seconds if any of the selected apps are running.
- If found, it terminates the process.
- The process continues until the specified duration elapses.

## 📦 Installation

```bash
pip install psutil
```

## 🧪 Usage

```bash
python focus_lock.py
```

Follow the on-screen prompts to enter:
1. App names (comma separated)
2. Duration format (minutes or hours)
3. Time to block the apps


## 📄 License

MIT License

---

Built with ❤️ by Parmeet Singh Bhamrah