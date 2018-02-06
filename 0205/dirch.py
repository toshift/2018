import os
import glob


def main_os(path):
    # 現在のディレクトリの情報を取得する
    for d in os.listdir(path):
        # ディレクトリのファイルを取得する
        try:
            for f in os.listdir(path + "\\" + d):
                print(f)
        except Exception as e:
            continue


def main_glob(path):
    files = []
    # ディレクトリのファイルを取得する
    files = glob.glob(path + "*\\*\\*.txt")
    print(files)


if __name__ == "__main__":
    path = os.getcwd()
    main_os(path)
    main_glob(path)
