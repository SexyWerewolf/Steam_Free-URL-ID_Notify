# SteamID Availability Check

<p align="center"><img src="https://socialify.git.ci/SexyWerewolf/Steam_Free-URL-ID_Notify/image?font=Jost&amp;issues=1&amp;language=1&amp;name=1&amp;owner=1&amp;pattern=Solid&amp;stargazers=1&amp;theme=Dark" alt="project-image"></p>

## 📖 Description

The `SteamID Availability Check` script is designed to monitor and notify you about the availability of Steam IDs. By checking a list of Steam profile URLs, the script will determine if a profile is available and send a notification to your Telegram if it is. The script operates in an infinite loop, with a cooldown period between checks to avoid triggering spam protection.

## 🛠️ Installation Steps

1. **Install Repo**

    ```bash
    git clone https://github.com/SexyWerewolf/Steam_Free-URL-ID_Notify.git
    ```

2. **Go To Root Directory**

    ```bash
    cd Steam_Free-URL-ID_Notify
    ```

3. **Install Requests**

    ```bash
    pip install requests
    ```

4. **Edit The Script**

    ```bash
    nano steam_username_check.py
    ```

5. **Run The Script**

    ```bash
    python3 ./steam_username_check.py
    ```

## 📝 Configuration

- **Telegram Bot Token**: Replace `telegram_bot_token` in the script with your Telegram bot token.

- **Telegram Chat ID**: Replace `telegram_chat_id` with your Telegram chat ID.

- **Input File**: Place Steam profile URLs in the `input_list.txt` file. Each URL should be on a new line in the format: `https://steamcommunity.com/id/YourSteamID`.

- **Output File**: Available Steam IDs will be recorded in the `output_list.txt` file.

## 🛠️ Usage

1. **Edit the Script**: Update lines 13 and 16 in `steam_username_check.py` with your Telegram bot token and chat ID.

2. **Run the Script**: The script will continuously check the availability of Steam IDs listed in `input_list.txt`. If an ID is available, you will receive a Telegram notification.

    ```bash
    python3 steam_username_check.py
    ```

## ⚙️ How It Works

- The script reads Steam profile URLs from `input_list.txt`.
- It checks the availability of each URL.
- If an ID is available, it sends a notification to your Telegram chat and writes the available ID to `output_list.txt`.
- The script includes a cooldown period between checks to comply with spam protection rules and avoid overloading the Steam servers.

## 📜 License

This script is provided as-is. Use it at your own risk. The author is not responsible for any issues that may arise from using this script.

## 🛠️ Contact

For any questions or issues, please open an issue on the [GitHub repository](https://github.com/SexyWerewolf/Steam_Free-URL-ID_Notify) or contact the author directly.
