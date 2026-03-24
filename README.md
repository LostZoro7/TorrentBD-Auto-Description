# 🎬 TorrentBD Description Generator
<div align="center">
  
<a href="https://github.com/LostZoro7/TorrentBD-Auto-Description/raw/refs/heads/main/tbd_desc.py" download="tbd_desc.py">
  <img src="https://img.shields.io/badge/Download-Script-green?style=for-the-badge&logo=python" alt="Download Script">
</a>

> **💡 Note:** If the code opens as text, just press **Ctrl + S** to save it as `tbd_desc.py`. you may need to add the `.py` extension by yourself after `tbd_desc`.

</div>

---
A Python-based tool to automate the creation of high-quality movie/TV show descriptions for TorrentBD. This script extracts MediaInfo, captures 3 random high-quality screenshots, uploads them to ImgBB, and generates a formatted BBCode template ready for posting.

## ✨ Features
* 📂 **File Selector:** Opens a standard Windows dialog to pick any video file.
* 📊 **MediaInfo Integration:** Automatically extracts technical specs into a `[mediainfo]` block.
* 📸 **Smart Screenshots:** Uses FFmpeg to grab 3 random frames from different parts of the video.
* ☁️ **Auto-Upload:** Uploads screenshots to ImgBB and returns direct `[img]` links.
* 📜 **Custom Template:** Includes "MediaInfo" , "ScreenShots" & "Thank You" banner.

---

## 🛠️ Prerequisites

Before running the script, ensure you have the following installed:

1. **Python 3.10+**: [Download here](https://www.python.org/downloads/) (Make sure to check "Add Python to PATH").
2. **External Tools (CLI Versions):**
    * [FFmpeg & FFprobe](https://ffmpeg.org/download.html)
    * [MediaInfo CLI](https://mediaarea.net/en/MediaInfo/Download/Windows)
3. **Python Library:**
    ```cmd
    pip install requests
    ```

---

## ⚙️ Configuration

1. Download the CLI tools mentioned above and place them in a folder of your choice.
2. Open `tbd_desc.py` in a text editor (like Notepad or VS Code).
3. **Set your tool paths**: Update the `PATHS CONFIGURATION` section with the location of your `.exe` files:
    ```python
    FFMPEG_PATH    = r"C:\Your\Path\To\ffmpeg.exe"
    FFPROBE_PATH   = r"C:\Your\Path\To\ffprobe.exe"
    MEDIAINFO_PATH = r"C:\Your\Path\To\MediaInfo.exe"
    ```
4. **Add your API Key**: Insert your [ImgBB API Key](https://api.imgbb.com/):
    ```python
    IMGBB_API_KEY = "your_api_key_here"
    ```

---

## 🚀 Usage

1. Run CMD from the script directory.

   Run the script:
    ```cmd
    python tbd_desc.py
    ```
    or 
    you can directly run `tbd_desc.py` by making .bat file (copy and save it as `tbd_desc.bat`):
    ```cmd
   @echo off
   python tbd_desc.py
   pause
   ```
3. Select your video file from the pop-up window.
4. Wait for the "Processing..." message to finish.
5. The script will automatically open `tbd_description.txt` in your script's folder. 
6. **Copy all contents** and paste them into the TorrentBD description box.

---

## 📝 Output Preview
The script generates a text file in the **same folder where the script is located**.

---

## ⚖️ License
This project is for personal use.
