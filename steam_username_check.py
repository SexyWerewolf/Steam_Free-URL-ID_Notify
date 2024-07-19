#Edit The Line: 13, 16

#Checks if a SteamID is Available
#if it is Available You Get a Notification on Your Telegram
#Put the SteamID's on Input.txt File Like That: https://steamcommunity.com/id/SexyWerewolf
#This Program Has Unlimited Loop With 60s Cooldown To Avoid Spam Protection


import requests
import time

#Telegram Bot Token e.g: 987654321:ABCDEFGHIJKLMNOPQRSTUVWXYZ0987654321
telegram_bot_token = ''

# Chat ID του group e.g: -100987654
telegram_chat_id = ''

def check_steam_id_availability(url):
    response = requests.get(url)
    if '<h3>The specified profile could not be found.</h3>' in response.text:
        return False
    else:
        return True

def send_telegram_message(message):
    try:
        telegram_api_url = f'https://api.telegram.org/bot{telegram_bot_token}/sendMessage'
        params = {
            'chat_id': telegram_chat_id,
            'text': message
        }
        response = requests.post(telegram_api_url, params=params)
        response.raise_for_status()  # Checks for Connection Problems
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error Sending Message to Telegram: {e}")
        return None

def process_links(links):
    cooldown_time = 5  # 5 Seconds Cooldown
    with open('output_list.txt', 'w') as output_file:
        for link in links:
            is_available = check_steam_id_availability(link)
            if not is_available:
                message = f"The Steam ID link {link} is Available!"
                print(message)
                send_telegram_message(message)
                # Save The non-available Links To output_list.txt
                output_file.write(f"{link}\n")

            # Wait for The Cooldown Before The Next Request
            time.sleep(cooldown_time)

def main():
    total_cooldown_time = 60  # 1 Minute Cooldown
    cooldown_interval = 5  # 5 Seconds Cooldown Before Starting Again
    current_cooldown_time = total_cooldown_time
    
    while current_cooldown_time > 0:
        print(f"Waiting for Cooldown: {current_cooldown_time} Seconds Remaining...")
        time.sleep(cooldown_interval)
        current_cooldown_time -= cooldown_interval

    while True:
        with open('input_list.txt', 'r') as input_file:
            links = input_file.read().splitlines()
            process_links(links)
        
        print("Cooldown After Processing all Links...")
        time.sleep(total_cooldown_time)

if __name__ == "__main__":
    main()
