import os
import time
from datetime import datetime
from PIL import ImageGrab

def main():
    folder = "screenshots"
    if not os.path.exists(folder):
        os.makedirs(folder)

    print("Starting screenshot capture... (1 per minute)")
    
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = os.path.join(folder, f"screenshot_{timestamp}.png")
        
        try:
            img = ImageGrab.grab()
            img.save(filename)
            print(f"Saved: {filename}")
        except Exception as e:
            print(f"Screenshot failed: {e}")

        time.sleep(60)

if __name__ == "__main__":
    main()

# Open powershell and run:
# python -m venv venv

# venv\Scripts\activate

# Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

# pip install pillow

# Deactivate when done
# deactivate
