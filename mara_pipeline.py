# -*- coding:utf-8 -*-
from mara_pipelines.pipelines import Pipeline, Task
from mara_pipelines.commands.bash import RunBash
from mara_pipelines.commands.python import RunFunction
import os
import subprocess

# 数据库配置 (使用环境变量)
import mara_db.config
import mara_db.dbs

mara_db.config.databases = lambda: {
    'mara': mara_db.dbs.PostgreSQLDB(
        host=os.getenv('DB_HOST', '47.96.175.91'),
        port=os.getenv('DB_PORT', 5432),
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASSWORD', "8uhb$RFV"),
        database=os.getenv('DB_NAME', 'postgres')
    )
}

# 主流水线
pipeline = Pipeline(id='sdk_release', description='SDK发布流水线')

# 任务1: 运行测试
pipeline.add(Task(
    id='run_tests',
    description='运行单元测试',
    commands=[RunBash('bash script/pytest.sh')]
))

# 任务2: 构建SDK
def build_sdk_package():
    # 清理旧构建
    if os.path.exists('dist'):
        for f in os.listdir('dist'):
            os.remove(os.path.join('dist', f))

    # 构建新包
    subprocess.run(['python', 'setup.py', 'sdist', 'bdist_wheel'], check=True)


pipeline.add(Task(
    id='build_sdk',
    description='构建SDK包',
    commands=[RunFunction(build_sdk_package)],
), upstreams=['run_tests'])


# 任务3: 构建文档
def build_docs():
    # 安装文档依赖
    subprocess.run(['pip', 'install', 'sphinx', 'sphinx_rtd_theme'], check=True)

    # 创建构建目录
    os.makedirs('_build/docs', exist_ok=True)

    # 生成HTML文档
    subprocess.run([
        'sphinx-build',
        '-b', 'html',
        'docs/',
        '_build/docs'
    ], check=True)


pipeline.add(Task(
    id='build_docs',
    description='构建文档',
    commands=[RunFunction(build_docs)],
), upstreams=['run_tests'])

# 可选：添加版本更新任务
def bump_version():
    # 这里使用bump2version工具，需提前安装
    subprocess.run(['bump2version', 'patch'], check=True)


pipeline.add(Task(
    id='bump_version',
    description='更新版本号',
    commands=[RunFunction(bump_version)],
), upstreams=['run_tests'])


from mara_pipelines.cli import run_pipeline
run_pipeline(pipeline)