set -x
rm -rf build
rm -rf dist
rm -rf yeying_client.egg-info

python setup.py bdist_wheel

pip uninstall -y yeying_client && pip install dist/yeying_client-0.1.0-py3-none-any.whl

# 文件下载
# yeying_cmd get ${资产仓库空间 ID} ${文件上传返回的 hash} ${本地文件输出路径}  ${身份文件-warehouse.id} ${password}
yeying_cmd get 96274d7e-0aae-4736-8f34-940a26f2f92a c8c2ec2db6048d916045ba0450a1fc642fabf62c1d64ca93f40cc96609c31695 generate.sh /Users/youxuehu/Downloads/warehouse.id 123456

rm -rf build
rm -rf dist
rm -rf yeying_client.egg-info

set +x
