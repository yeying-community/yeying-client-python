set -x
rm -rf build
rm -rf dist
rm -rf yeying_client.egg-info

python setup.py bdist_wheel

pip uninstall -y yeying_client && pip install dist/yeying_client-0.0.2-py3-none-any.whl

# 指定服务端 WAREHOUSE_ENDPOINT
# 资产仓库服务端 API 地址
export WAREHOUSE_ENDPOINT="http://localhost:8641"
# 文件下载
# yeying_cmd get ${资产仓库空间 ID} ${文件上传返回的 hash} ${本地文件输出路径}  ${身份文件-warehouse.id} ${password}
yeying_cmd get 96274d7e-0aae-4736-8f34-940a26f2f92a febf138d839ac3ef18ee33cc81e2ea766e918045ce09c25e573d0c8e4385915d delete.sh /Users/youxuehu/Downloads/warehouse.id 123456

rm -rf build
rm -rf dist
rm -rf yeying_client.egg-info

set +x
