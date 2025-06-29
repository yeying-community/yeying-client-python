set -x
rm -rf build
rm -rf dist
rm -rf yeying_client.egg-info

python setup.py bdist_wheel

pip uninstall -y yeying_client && pip install dist/yeying_client-0.1.0-py3-none-any.whl

yeying_cmd put /Users/youxuehu/SDK/yeying-apps/yeying-client-python/.idea/ 96274d7e-0aae-4736-8f34-940a26f2f92a

rm -rf build
rm -rf dist
rm -rf yeying_client.egg-info

set +x
