import os
import sys
import subprocess

def decompress_lz4_files(folder):
    if not os.path.isdir(folder):
        print(f"Error: {folder} is not a valid directory")
        return
    
    for filename in os.listdir(folder):
        if filename.endswith(".lz4"):
            file_path = os.path.join(folder, filename)
            output_file = os.path.splitext(file_path)[0]  # Remove .lz4 extension
            subprocess.run(["lz4", "-d", file_path, output_file])
            print(f"Decompressed {file_path} to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python decompress_lz4.py <folder_path>")
        sys.exit(1)
    
    folder_path = sys.argv[1]
    decompress_lz4_files(folder_path)