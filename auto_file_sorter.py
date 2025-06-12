import os
import shutil

folder_path = "C:/Users/abdel/OneDrive/Bureau/Python Automation/auto_file_sorter/Before"  


for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    

    if os.path.isfile(file_path):
        print(f"Fichier trouvé : {filename}")




folder_path = "C:/Users/abdel/OneDrive/Bureau/Python Automation/auto_file_sorter/Before"

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):
        _, extension = os.path.splitext(filename)
        extension = extension[1:]  

        if extension == "":
            extension = "no_extension"

        target_folder = os.path.join(folder_path, extension.upper())

       
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        
        shutil.move(file_path, os.path.join(target_folder, filename))
        print(f" {filename} déplacé dans {extension.upper()}/")

