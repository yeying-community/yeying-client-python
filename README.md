# yeying-client-python

## 打 whl 包命令

    python setup.py sdist bdist_wheel

## 发布公网

    # 安装 twine 命令
    pip install --upgrade twine setuptools wheel
    # 执行命令
    twine upload dist/*
    # 输入 token，自己注册 https://pypi.org 的账号，新建一个 token
    

## pytest 执行命令

    pytest -s --log-cli-level=INFO --show-capture=all