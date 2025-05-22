import os
import shutil

def duplicate_files_recursive(folder):
    try:
        # List isi folder sekarang
        items = os.listdir(folder)
        
        for item in items:
            path = os.path.join(folder, item)
            
            if os.path.isfile(path):
                # File: buat duplikat dengan nama file_copy
                new_name = item + "_copy"
                new_path = os.path.join(folder, new_name)
                if not os.path.exists(new_path):
                    shutil.copy2(path, new_path)
            
            elif os.path.isdir(path):
                # Folder: duplikasi folder baru dengan _copy
                new_folder = path + "_copy"
                if not os.path.exists(new_folder):
                    shutil.copytree(path, new_folder)
                
                # Lakukan rekursi ke folder asli (bukan ke duplikat)
                duplicate_files_recursive(path)

    except Exception as e:
        print(f"Error di folder {folder}: {e}")

if __name__ == "__main__":
    target_folder = os.getcwd()
    duplicate_files_recursive(target_folder)
