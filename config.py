import os
from pathlib import Path

# --- SYSTEM IDENTITY ---
# You can change this string at any time to instantly rename your system
SYSTEM_NAME = "Silent"

# --- DIRECTORY PATHS ---
# Automatically resolves the root path where main.py sits
BASE_DIR = Path(__file__).resolve().parent

DB_DIR = BASE_DIR / "database"
BACKGROUND_DIR = BASE_DIR / "background"
ROUTER_DIR = BASE_DIR / "router"
MODULES_DIR = BASE_DIR / "modules"

# Ensure all necessary local directories exist on the laptop automatically
for directory in [DB_DIR, BACKGROUND_DIR, ROUTER_DIR, MODULES_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

    # --- LOCAL OLLAMA BACKEND CONFIGURATION ---
    OLLAMA_API_URL = "http://localhost:11434/api"

    # Free Local Model Registry Defaults (Based on optimal laptop sizing)
    ROUTER_MODEL = "llama3.2:3b"       # Fast, lightweight model for choosing the right AI
    CODING_MODEL = "qwen2.5-coder:7b"  # High-accuracy model for coding/OS execution tasks
    GENERAL_MODEL = "llama3.3:8b"     # Rich context model for chatting in regional dialects
    