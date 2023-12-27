#!/bin/bash
set -e # 如果任何命令執行失敗則立即終止腳本

# 檢查系統上是否已安裝 pipenv
if ! command -v pipenv &> /dev/null
then
    echo "系統未安裝 pipenv，現在開始安裝..."
    sudo apt-get update
    sudo apt-get install -y python3.8 python3-pip

    # 安裝 pipenv
    pip3 install pipenv

    # 設置環境變數
    echo "設置 PIPENV_VENV_IN_PROJECT 環境變數為enabled..."
    export PIPENV_VENV_IN_PROJECT="enabled"
    echo 'export PIPENV_VENV_IN_PROJECT="enabled"' >> ~/.bashrc

    # 將 pipenv 安裝路徑添加到當前會話的 PATH 中
    PIPENV_PATH=$(python3 -m site --user-base)/bin
    echo "export PATH=\"$PIPENV_PATH:\$PATH\"" >> ~/.bashrc
    export PATH="$PIPENV_PATH:$PATH"
    echo "pipenv設置完成。如果要手動重啟遊戲，請關閉並重新開啟您的終端機，或執行 'source ~/.bashrc' 來應用 PATH 變更。"
else
    echo "pipenv 已經安裝"
    echo "設置 PIPENV_VENV_IN_PROJECT 環境變數為enabled..."
    export PIPENV_VENV_IN_PROJECT="enabled"
    echo 'export PIPENV_VENV_IN_PROJECT="enabled"' >> ~/.bashrc
    echo "執行 'source ~/.bashrc' 套用環境變數變更。"
fi


# 使用 pipenv 和 Python 3.8 創建虛擬環境
echo "正在使用 Python 3.8 創建虛擬環境..."
pipenv --python 3.8


# 從 Pipfile 安裝依賴
echo "正在從 Pipfile 安裝依賴..."
pipenv install


# 在虛擬環境中啟動並運行 tic-tac-toe-AI.py
echo "在虛擬環境中運行 tic-tac-toe-AI.py..."
pipenv run python tic-tac-toe-AI.py

