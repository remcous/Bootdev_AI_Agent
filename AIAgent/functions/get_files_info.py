import os

def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        
        if not os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        file_info = []
        
        for file_name in os.listdir(target_dir):
            file_path = f"{target_dir}/{file_name}"
            file_info.append(f'- {file_name}: {os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}')
            
        return "\n".join(file_info)
    except Exception as e:
        return f"Error listing files: {e}"
    
if __name__ == "__main__":
    print(get_files_info("calculator"))