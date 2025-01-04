# Beatz 🎵  
**A compact MP3 music player built using IoT Technology.**  

## Features  
- Lightweight and efficient.  
- Easy to set up and run.  
- Built with FastAPI and Python for seamless integration.  

---

## Installation and Running Instructions  

1. **Set up the application:**  
   ```bash
   # Create a Python virtual environment
   python -m venv ./

   # Activate the environment
   source bin/activate

   # Install required modules
   pip install fastapi requests uvicorn "fastapi[standard]"

2. **Run the application**
   ```bash
   #Activate the environment
   source bin/activate

   # navigate to the server director and start the app
   cd server && fastapi dev main.py

   # Open a new terminal window and navigate to the client directory and start main.py
   cd client && python3 main.py
