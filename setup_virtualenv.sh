#!/bin/bash

# 安裝 pipenv
echo " installing pipenv..."
sudo apt-get update
sudo apt-get install -y python3.8 python3-pip
pip3 install pipenv

# 使用 pipenv 和 Python 3.8 創建虛擬環境
# pipenv 會自動在專案根目錄下創建一個 .venv 資料夾來存放虛擬環境
echo " Using Python 3.8 to create virtual enviroment..."
pipenv --python 3.8

echo " Virtual enviroment has been created in .venv director"

# 啟動虛擬環境的 shell
# 使用 'pipenv shell' 進入虛擬環境
# 在這個 shell 中運行的所有命令都將在虛擬環境中執行
echo " Entering shell of the virtual enviroment..."
pipenv shell

echo " Enter 'exit' to quit the virtual enviroment "

python tic-tac-toe-AI.py
