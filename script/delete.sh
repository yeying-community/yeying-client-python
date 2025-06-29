set -x
rm -rf build
rm -rf dist
rm -rf yeying_client.egg-info

python setup.py bdist_wheel

pip uninstall -y yeying_client && pip install dist/yeying_client-0.1.0-py3-none-any.whl

# 文件下载
yeying_cmd delete 96274d7e-0aae-4736-8f34-940a26f2f92a 55392b23b75e3a5e039232cce80f8b91ba6bf31d66057085afc6f522349c4281

rm -rf build
rm -rf dist
rm -rf yeying_client.egg-info

set +x
