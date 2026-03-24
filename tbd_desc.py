import os
import subprocess
import requests
import random
import base64
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

# --- 1. PATHS CONFIGURATION ---
# Paste the FULL location of your .exe files here. 
# Use 'r' before the quotes to handle Windows backslashes correctly.
FFMPEG_PATH    = r"C:\Your\Path\To\ffmpeg.exe"
FFPROBE_PATH   = r"C:\Your\Path\To\ffprobe.exe"
MEDIAINFO_PATH = r"C:\Your\Path\To\MediaInfo.exe"

# --- 2. API CONFIGURATION ---
IMGBB_API_KEY = "your_api_key_here"

def get_startupinfo():
    if os.name == 'nt':
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        return si
    return None

def check_tools():
    """Verify all .exe files exist before starting"""
    tools = {
        "FFmpeg": FFMPEG_PATH,
        "FFprobe": FFPROBE_PATH,
        "MediaInfo": MEDIAINFO_PATH
    }
    for name, path in tools.items():
        if not os.path.exists(path):
            messagebox.showerror("Tool Missing", f"Could not find {name} at:\n{path}\n\nPlease check your folder and update the script paths.")
            return False
    return True

def get_video_duration(path):
    cmd = [FFPROBE_PATH, "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", path]
    res = subprocess.run(cmd, capture_output=True, text=True, startupinfo=get_startupinfo())
    return float(res.stdout.strip()) if res.returncode == 0 else None

def get_mediainfo(path):
    res = subprocess.run([MEDIAINFO_PATH, path], capture_output=True, text=True, startupinfo=get_startupinfo())
    return res.stdout.strip()

def upload_to_imgbb(img_path):
    try:
        with open(img_path, "rb") as f:
            data = {"key": IMGBB_API_KEY, "image": base64.b64encode(f.read())}
            r = requests.post("https://api.imgbb.com/1/upload", data=data)
            return r.json()['data']['url'] if r.status_code == 200 else None
    except:
        return None

def select_file_manually():
    root = tk.Tk()
    root.withdraw() 
    root.attributes("-topmost", True)
    file_path = filedialog.askopenfilename(
        title="Select Video File for TorrentBD",
        filetypes=[("Video files", "*.mkv *.mp4 *.avi *.ts"), ("All files", "*.*")]
    )
    root.destroy()
    return file_path

def process_video():
    if not check_tools(): return # Stop if tools are missing
    
    video = select_file_manually()
    if not video: return
    
    print(f"\n🎬 Processing: {video}")
    mi_text = get_mediainfo(video)
    duration = get_video_duration(video)
    uploaded_urls = []
    
    print("📸 Generating 3 random screenshots & uploading...")
    for i in range(3):
        ts = random.uniform(duration * (0.1 + i*0.25), duration * (0.3 + i*0.25))
        temp_img = f"temp_ss_{i}.jpg"
        
        cmd = [FFMPEG_PATH, "-y", "-ss", str(ts), "-i", video, "-frames:v", "1", "-q:v", "2", temp_img]
        subprocess.run(cmd, capture_output=True, startupinfo=get_startupinfo())
        
        url = upload_to_imgbb(temp_img)
        if url:
            uploaded_urls.append(url)
            print(f" ✅ Screenshot {i+1} uploaded.")
        
        if os.path.exists(temp_img): 
            os.remove(temp_img)

    # --- BBCODE BUILDING ---
    bb = (
        f"[hr][center][img]https://i.ibb.co.com/Rq0gWF5/Media-Info.png[/img][/center][hr]\n"
        f"[b][size=2][font=consolas][mediainfo]\n{mi_text}\n[/mediainfo][/font][/size][/b]\n\n"
        f"[hr][center][img]https://i.ibb.co.com/KxTxH45D/screenshots.png[/img][/center][hr]\n"
        f"[center]\n"
    )
    
    for url in uploaded_urls: 
        bb += f"[img]{url}[/img]\n"
    
    bb += (
        f"[/center]\n"
        f"[hr][center][img]https://i.ibb.co.com/FkPr6XyR/Thank-You.png[/img][/center][hr]\n"
    )

    output_path = "tbd_description.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(bb)
    
    print(f"\n✨ Success! Opening the description now...")
    os.startfile(output_path)

if __name__ == "__main__":
    process_video()
