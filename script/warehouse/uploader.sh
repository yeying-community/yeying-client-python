set -x
rm -rf build
rm -rf dist
rm -rf yeying_client.egg-info

python setup.py bdist_wheel

pip uninstall -y yeying_client && pip install dist/yeying_client-0.1.0-py3-none-any.whl

# 指定服务端 WAREHOUSE_ENDPOINT
# 资产仓库服务端 API 地址
export WAREHOUSE_ENDPOINT="http://localhost:8641"
# 文件上传
# yeying_cmd put ${本地目录/本地文件} ${资产仓库空间 ID} ${是否加密 True/False} ${身份文件-warehouse.id} ${password}
yeying_cmd put /Users/youxuehu/SDK/yeying-apps/yeying-client-python/script/delete.sh 96274d7e-0aae-4736-8f34-940a26f2f92a True /Users/youxuehu/Downloads/warehouse.id 123456

rm -rf build
rm -rf dist
rm -rf yeying_client.egg-info

set +x
