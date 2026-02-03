import os

def get_files_info(working_directory, directory="."):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_dir,directory))
        valid_target_dir = os.path.commonpath([abs_working_dir, target_dir]) == abs_working_dir

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        output = []
        for item in sorted(os.listdir(target_dir)):
            item_path = os.path.join(target_dir, item)
            size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)

            output.append(f"  - {item}: file_size={size} bytes, is_dir={is_dir}")

        return "\n".join(output)
    
    except Exception as e:
        return f"Error: {str(e)}"