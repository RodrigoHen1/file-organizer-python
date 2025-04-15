# file-organizer-python

# 🗂️ Python File Organizer

A simple Python script that organizes files in a directory into categorized folders based on file extensions. Ideal for cleaning up messy download folders or desktops.

## ✅ Features

- Automatically creates folders for:
  - Images
  - Documents
  - Videos
  - Music
  - Archives
  - Scripts
  - Others
- Moves files into their respective folders
- Easy to customize and expand

## 🛠 Requirements

- Python 3.x

No additional packages needed—uses only built-in libraries.

## 📁 How to Use

1. Clone the repo or download the script:

```bash
git clone https://github.com/yourusername/file-organizer.git
Open the script in a code editor and change the TARGET_FOLDER to the directory you want to organize.

python
Copiar
Editar
TARGET_FOLDER = r'C:\Users\YourUsername\Downloads'  # example for Windows
Run the script:

bash
Copiar
Editar
python file_organizer.py
Done! Check the folder for newly created subdirectories.

📸 Screenshots
Before: Messy folder with various files

After: Organized folder with categorized subfolders

✏️ Customization
Want to support more file types or change the folder names? Just edit the FILE_TYPES dictionary in the script.

python
Copiar
Editar
FILE_TYPES = {
    'Images': ['.jpg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx'],
    # Add more types as needed
}
