# tik-tac-toe-AI-open-source-from-Github-

This project contains a simple tic-tac-toe game with an AI component that runs in the terminal. Below are the instructions to set up and run the game.
It's an opensource project from github.com

## Prerequisites

Make sure you running all the command below on `bash` shell. This project uses `pipenv` for dependency management.

## Setup Instructions

1. Clone the repository to your local machine:

    ```sh
    git clone https://github.com/<your-username>/tik-tac-toe-AI-from-Github.git
    ```

    Replace `<your-username>` with your actual GitHub username.

2. Change into the project directory:

    ```sh
    cd tik-tac-toe-AI-from-Github
    ```

3. Run the setup script to install `pipenv`, create a virtual environment, and install dependencies:

    ```sh
    bash setup_virtualenv.sh
    ```

    This script will automatically set up everything required to run the game.

## Running the Game

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