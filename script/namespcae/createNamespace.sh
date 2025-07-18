set -x
rm -rf build
rm -rf dist
rm -rf yeying_client.egg-info

current_path=$(pwd)
file_path=$current_path/yeying/version.py
# 获取版本号
version=$(awk -F"['\"]" '/__version__/{print $2; exit}' "$file_path")

python setup.py bdist_wheel

pip uninstall -y yeying_client && pip install "dist/yeying_client-$version-py3-none-any.whl"

# 指定服务端 WAREHOUSE_ENDPOINT
# 资产仓库服务端 API 地址
export WAREHOUSE_ENDPOINT="http://localhost:8641"
# 创建 namespace
# yeying_cmd createNamespace ${空间名称} ${空间描述} ${身份文件-warehouse.id} ${password}
yeying_cmd createNamespace test_namespace11 testData1 /Users/youxuehu/Downloads/warehouse.id 123456

rm -rf build
rm -rf dist
rm -rf yeying_client.egg-info

set +x
