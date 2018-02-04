#coding: utf-8
import zipfile, os

def backup_to_zip(file):
    zipf = os.path.basename(file)
    if os.path.exists(zipf):
        zipfile.ZipFile(zipf + ".zip", "w")
    else:
        raise ("zipfile元がない。")


if __name__ == "__main__":
    try:
        backup_to_zip("test")
    except Exception as e:
        print(e)
    
