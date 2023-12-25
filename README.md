# 井字遊戲 AI - 從 GitHub 開源專案

這個專案包含一個簡單的井字遊戲，配備 AI 對手，可以在終端機中運行。以下是設置和運行遊戲的指示。
這是一個來自 github.com 的開源專案。

## 先決條件

確保您在 `bash` shell 中運行以下所有命令。這個專案使用 `pipenv` 進行依賴管理。

## 設置指南

1. 克隆儲存庫到您的本地機器：

    ```sh
    git clone https://github.com/<your-username>/tik-tac-toe-AI-from-Github.git
    ```

    將 `<your-username>` 替換為您的實際 GitHub 用戶名。

2. 切換到專案目錄：

    ```sh
    cd tik-tac-toe-AI-from-Github
    ```

3. 運行設置腳本以安裝 `pipenv`、創建虛擬環境並安裝依賴：

    ```sh
    bash setup_virtualenv.sh
    ```

    這個腳本將自動設置運行遊戲所需的一切。

## 運行遊戲(手動)

設置完成後，遊戲將自動啟動。不過如果您需要手動啟動遊戲，可以使用以下命令：

```sh
pipenv run python tic-tac-toe-AI.py
```

## 額外資訊
- 如果您希望在虛擬環境中執行其他命令，可以通過運行以下命令來啟動環境 shell：

```sh
pipenv shell
```
要退出虛擬環境，請輸入 exit 或按 Ctrl+D。

- 也為那些不喜歡使用 pipenv 的人提供了 requirements.txt 檔案。可以使用以下命令安裝依賴：

```sh
pip install -r requirements.txt
```
### 感謝你的閱讀與使用！


# tik-tac-toe-AI-open-source-from-Github-

This project contains a simple tic-tac-toe game with an AI component that runs in the terminal. Below are the instructions to set up and run the game.
It's an opensource project from github.com

## Prerequisites

Make sure you running all the command below on `bash` shell. This project uses `pipenv` for dependency management.

## Setup Instructions

1. Clone the repository to your local machine:

    ```sh
    https://github.com/b10902026-jimmy/tik-tac-toe-AI-open-source-from-Github-
    ```

2. Change into the project directory:

    ```sh
    cd tik-tac-toe-AI-from-Github
    ```

3. Run the setup script to install `pipenv`, create a virtual environment, and install dependencies:

    ```sh
    bash setup_virtualenv.sh
    ```

    This script will automatically set up everything required to run the game.

## Running the Game（manually）

After the setup is complete, the game will start automatically. If you need to start the game manually, you can do so with the following command:

```sh
pipenv run python tic-tac-toe-AI.py
```

## Additional Information
- If you wish to run other commands within the virtual environment, you can activate the environment shell by running:

```sh
pipenv shell
```

 To exit the virtual environment, type exit or press Ctrl+D.

- The requirements.txt file is also provided for those who prefer not to use pipenv. Dependencies can be installed using:

```sh
pip install -r requirements.txt
```
### Thank you for trying out Tic-Tac-Toe AI. Enjoy the game!