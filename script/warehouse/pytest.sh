### 测试用例整体执行脚本
set -x
# 指定服务端的 WAREHOUSE_ENDPOINT
# 资产仓库服务端 API 地址
export WAREHOUSE_ENDPOINT="http://localhost:8641"
pytest -s --log-cli-level=INFO --show-capture=all -v --durations=0
set +x