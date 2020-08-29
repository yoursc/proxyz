#### 打包

    python setup.py bdist_wheel

#### 安装

    pip install dist/flaskr-1.0.0-py3-none-any.whl

#### 配置环境变量

    export FLASK_APP=flaskr

#### 数据库初始化

    flask init-db

#### 快速生成随机秘钥

    python -c 'import os; print(os.urandom(16))'

#### 使用 WSGI 启动

    waitress-serve --call flaskr:create_app
