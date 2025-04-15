import os
import shutil

# === Define folder categories ===
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.html', '.css'],
    'Others': []
}

# === Customize this path ===
TARGET_FOLDER = r'C:\Users\YourUsername\Downloads'  # Change to your target directory

def get_category(file_extension):
    for category, extensions in FILE_TYPES.items():
        if file_extension.lower() in extensions:
            return category
    return 'Others'

def organize_files():
    for filename in os.listdir(TARGET_FOLDER):
        filepath = os.path.join(TARGET_FOLDER, filename)

        if os.path.isfile(filepath):
            _, ext = os.path.splitext(filename)
            category = get_category(ext)

            category_path = os.path.join(TARGET_FOLDER, category)
            if not os.path.exists(category_path):
                os.makedirs(category_path)

            new_path = os.path.join(category_path, filename)
            shutil.move(filepath, new_path)
            print(f"Moved: {filename} → {category}/")

if __name__ == '__main__':
    organize_files()
    print("✅ Done organizing!")
