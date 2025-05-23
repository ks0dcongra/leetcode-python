import os
import random
import glob

if __name__ == '__main__':
    # 確保 'python' 資料夾存在
    dir_name = 'Python'
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    # 刪除所有 'test_' 開頭的檔案
    existing_files = glob.glob(os.path.join(dir_name, 'test_*.py'))
    for file_path in existing_files:
        os.remove(file_path)
        print(f"Deleted: {file_path}")

    # 生成隨機4位數字
    random_number = random.randint(1000, 9999)
    file_name = f"test_{random_number}.py"
    file_path = os.path.join(dir_name, file_name)

    # 建立新檔案
    # with open(file_path, 'w'):
        # passq

    print(f"Created: {file_path}")


    # import sys

# if __name__ == '__main__':
#     file_name = 'test'
#     try:
#         file_name = sys.argv[1]
#     except IndexError:
#         print("Usage: python create_empty_file [filename]")
#     print("Creating " + file_name + "in python dir...")
#     with open("python/" + file_name + ".py", 'w'):
#         pass
  
#     print("Done!")