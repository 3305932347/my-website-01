import os

# 设定：你的文件所在的文件夹路径 ('.' 代表当前目录)
path = '.' 
# 设定：新文件名的前缀
prefix = ''
# 设定：起始编号
start_num = 1

# 获取文件列表
files = os.listdir(path)
# 过滤掉脚本自己，防止把 .py 文件也重命名了
files = [f for f in files if f.endswith(('.jpg', '.jpeg', '.png', '.webp'))]

# 排序 (可选：按修改时间排序，这样旧照片在前)
files.sort(key=lambda x: os.path.getmtime(os.path.join(path, x)))

for index, filename in enumerate(files):
    # 获取原文件后缀 (.jpg)
    ext = os.path.splitext(filename)[1]
    
    # 构建新文件名: img_001.jpg (zfill(3) 表示补齐3位，如 001)
    new_name = f"{prefix}{str(start_num + index).zfill(3)}{ext}"
    
    # 重命名
    old_file = os.path.join(path, filename)
    new_file = os.path.join(path, new_name)
    
    print(f"Renaming: {filename} -> {new_name}")
    os.rename(old_file, new_file)

print("✅ 全部完成！")