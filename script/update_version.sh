#!/bin/bash
current_path=$(pwd)
file_path=$current_path/yeying/version.py
# 获取当前时间（格式：YYYYMMDDHHMMSS）
current_time=$(date +"%Y%m%d%H%M%S")

# 使用sed进行替换（兼容Linux和macOS）
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS系统
    sed -i '' "s/__version__[[:space:]]*=[[:space:]]*\"[^\"]*\"/__version__ = \"$current_time\"/" "$file_path"
else
    # Linux及其他系统
    sed -i "s/__version__[[:space:]]*=[[:space:]]*\"[^\"]*\"/__version__ = \"$current_time\"/" "$file_path"
fi

# 验证修改
echo "版本号已更新为："
grep '__version__' "$file_path"