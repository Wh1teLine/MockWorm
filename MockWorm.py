import os
import shutil

def duplicate_files_recursive(folder):
    try:
        items = os.listdir(folder)
        
        for item in items:
            path = os.path.join(folder, item)
            
            if os.path.isfile(path):
                new_name = item + "_copy"
                new_path = os.path.join(folder, new_name)
                if not os.path.exists(new_path):
                    shutil.copy2(path, new_path)
            
            elif os.path.isdir(path):
                new_folder = path + "_copy"
                if not os.path.exists(new_folder):
                    shutil.copytree(path, new_folder)
                duplicate_files_recursive(path)

    except Exception as e:
        print(f"Error di folder {folder}: {e}")

duplicate_files_recursive(os.getcwd())
