# 本次实验目的是批量修改文件名称

import os


def change_file_name(dir_path):
    # 拿到所有文件列表
    file_list = os.listdir(dir_path)
    # 遍历文件列表
    for file in file_list:
        # 拿到原先的文件名
        old_file_name = os.path.join(dir_path, file)
        # 设置新的文件名
        new_file_name = os.path.join(dir_path, f"xwwwb_{file}")
        # 执行重命名
        os.rename(old_file_name, new_file_name)
        print(f"文件\t{old_file_name} 重命名为\t{new_file_name}")


if __name__ == '__main__':
    change_file_name('data')
    print('重命名完成！')
