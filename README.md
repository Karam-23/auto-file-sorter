# Auto File Sorter – Organize Downloads Folder by File Type

## Auto File Sorter – Organize Your Downloads Folder

This script automatically sorts files from a "Before" folder into categorized subfolders (Documents, Images, Videos, etc.) and moves them to a structured "After" folder.

## Features
- Detects file types based on extensions
- Automatically creates destination folders
- Moves files cleanly and safely
- Cross-platform ready (Windows/Linux/Mac with small path tweaks)

## Real Use Case
Ideal for freelancers, students, and professionals who:
- Want to keep their downloads clean
- Work with many file types
- Need to save time on manual sorting

## Demo

### Before Sorting
![Before](Before)

### The Script in Action
![Code](code)

### After Sorting
![After](After1)
![After](After2)

---

##  How It Works

The script scans a target folder and moves files into subfolders based on their type:
- `.jpg`, `.png`, `.svg` → `Images/`
- `.mp4`, `.mkv`, `.mov` → `Videos/`
- `.pdf`, `.docx`, `.txt` → `Documents/`
- And so on...

It also creates the `After/` folder for the sorted structure.
