import os
import shutil

# Specify the directory to organize
directory = input("Enter the path of the directory to organize: ")

# Define file categories and corresponding extensions
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Music": [".mp3", ".wav", ".flac", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".php", ".html", ".css", ".java"],
    "Executables": [".exe", ".bat", ".sh"],
    "Others": []
}

def create_category_folders(base_directory):
    for category in file_categories:
        folder_path = os.path.join(base_directory, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def get_file_category(file_name):
    extension = os.path.splitext(file_name)[1].lower()
    for category, extensions in file_categories.items():
        if extension in extensions:
            return category
    return "Others"

def organize_files(base_directory):
    for file_name in os.listdir(base_directory):
        file_path = os.path.join(base_directory, file_name)
        
        if os.path.isfile(file_path):
            category = get_file_category(file_name)
            destination_folder = os.path.join(base_directory, category)
            shutil.move(file_path, destination_folder)
            print(f"Moved '{file_name}' to '{category}' folder.")

if __name__ == "__main__":
    if os.path.exists(directory):
        create_category_folders(directory)
        organize_files(directory)
        print("File organization complete.")
    else:
        print("The specified directory does not exist.")
