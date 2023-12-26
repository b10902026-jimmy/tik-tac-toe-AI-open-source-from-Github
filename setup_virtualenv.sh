#!/bin/bash
set -e # 如果任何語句的執行結果不是true則立即退出腳本

# 檢查是否已安裝 pipenv
if ! command -v pipenv &> /dev/null
then
    echo "pipenv could not be found on the system, now installing pipenv..."
    sudo apt-get update
    sudo apt-get install -y python3.8 python3-pip

    # 安裝 pipenv
    pip3 install pipenv

    # 將 pipenv 安裝路徑添加到當前 session 的 PATH
    PIPENV_PATH=$(python3 -m site --user-base)/bin
    export PATH="$PIPENV_PATH:$PATH"
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



echo "export PATH=\"$HOME/.local/bin:$PATH\"" >> ~/.bashrc

echo "Setup is complete. Please close and reopen your terminal or run 'source ~/.bashrc' to apply PATH changes."
