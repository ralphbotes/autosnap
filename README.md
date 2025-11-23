# **AutoSnap — Automatic Screenshot Capture (Python)**

AutoSnap is a small Python tool that takes a **screenshot every minute** and stores it inside a `screenshots/` folder.  
It uses a PowerShell launcher (`run.ps1`) that **creates a virtual environment automatically** if one doesn’t exist, installs dependencies, activates the venv, and runs the script.

If you can’t follow this, that’s your problem — the steps below are spoon-fed.

---

## **Features**
- Captures a full-screen PNG screenshot every 60 seconds  
- Saves all screenshots to `./screenshots/`  
- Automatically creates a Python virtual environment on first run  
- Installs required dependencies (Pillow)  
- Clean PowerShell launcher script  
- Zero setup once it’s running

---

## **Installation & Usage**

### **1. Get the folder path.**  
**Example:**  
C:\Users\YOU\Downloads\autosnap\


---

### **2. Open PowerShell and run:**  
cd [paste_path_here]

**Example:**  
cd C:\Users\YOU\Downloads\autosnap\

---

### **3. Run the following command to start:**  
.\run.ps1

### **Note:**  
If PowerShell complains about permission issues, fix your user policy:  
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

---

### **4. To stop:**  
Ctrl + C

---

## **Project Structure**
autosnap/
│
├── autosnap.py # Screenshot script
├── run.ps1 # Launcher (creates venv + runs script)
├── .gitignore # Keeps repo clean
└── screenshots/ # Auto-created screenshot output folder

---

## **Requirements**
- Python 3.8+  
- Windows (uses PIL ImageGrab)

---

If you want a version that runs in the background, logs activity, minimizes to tray, or compiles to a single EXE — tell me, and I’ll strip your excuses again.  
