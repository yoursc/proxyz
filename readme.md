#### 打包

    python setup.py bdist_wheel

#### 安装

    pip install dist/flaskr-1.0.0-py3-none-any.whl

#### 快速生成随机秘钥

    python -c 'import os; print(os.urandom(16))'

# 启动应用

#### Windows 开发环境（直接启动）

    set FLASK_ENV=development
    set FLASK_APP=flaskr
    flask init-db
    flask run

#### Linux 生产环境（使用 WSGI 启动）

    export FLASK_ENV=production
    waitress-serve --call flaskr:create_app
