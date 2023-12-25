#!/bin/bash
set -e # 如果任何語句的執行結果不是true則立即退出腳本

# 檢查是否已安裝 pipenv
if ! command -v pipenv &> /dev/null
then
    echo "pipenv could not be found on the system, now installing pipenv..."
    sudo apt-get update
    sudo apt-get install -y python3.8 python3-pip
    pip3 install pipenv
else
    echo "pipenv is already installed"
fi

# 使用 pipenv 和 Python 3.8 創建虛擬環境
echo "Using Python 3.8 to create virtual environment..."
pipenv --python 3.8

# 安裝依賴項
echo "Installing dependencies from Pipfile..."
pipenv install

# 啟動虛擬環境並運行 tic-tac-toe-AI.py
echo "Running tic-tac-toe-AI.py inside virtual environment..."
pipenv run python tic-tac-toe-AI.py


