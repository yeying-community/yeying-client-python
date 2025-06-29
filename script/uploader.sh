set -x
rm -rf build
rm -rf dist
rm -rf yeying_client.egg-info

python setup.py bdist_wheel

pip uninstall -y yeying_client && pip install dist/yeying_client-0.1.0-py3-none-any.whl

# 文件上传
# yeying_cmd put ${本地目录/本地文件} ${资产仓库空间 ID} ${身份文件-warehouse.id} ${password}
yeying_cmd put /Users/youxuehu/SDK/yeying-apps/yeying-client-python/script/generate.sh 96274d7e-0aae-4736-8f34-940a26f2f92a /Users/youxuehu/Downloads/warehouse.id 123456

rm -rf build
rm -rf dist
rm -rf yeying_client.egg-info

set +x
