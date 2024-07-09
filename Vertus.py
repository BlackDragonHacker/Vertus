import requests
import json
import time
import os

# Function to read tokens from token.txt
def read_tokens(filename):
    with open(filename, 'r') as f:
        tokens = f.read().strip().splitlines()
    return tokens

# Function to display countdown
def display_countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"\rWait {i} seconds...", end="", flush=True)
        time.sleep(1)
    print("\n")

# Function to print ASCII art
def print_ascii_art1():
    print("\033[1;91m" + r""" ______  _               _    
 | ___ \| |             | |   
 | |_/ /| |  __ _   ___ | | __
 | ___ \| | / _` | / __|| |/ /
 | |_/ /| || (_| || (__ |   < 
 \____/ |_| \__,_| \___||_|\_\
""" + "\033[0m" + "\033[1;92m" + r""" ______                                   
 |  _  \                                  
 | | | | _ __   __ _   __ _   ___   _ __  
 | | | || '__| / _` | / _` | / _ \ | '_ \ 
 | |/ / | |   | (_| || (_| || (_) || | | |
 |___/  |_|    \__,_| \__, | \___/ |_| |_|
                       __/ |              
                      |___/               
""" + "\033[0m" + "\033[1;93m" + r"""  _   _               _                
 | | | |             | |               
 | |_| |  __ _   ___ | | __  ___  _ __ 
 |  _  | / _` | / __|| |/ / / _ \| '__|
 | | | || (_| || (__ |   < |  __/| |   
 \_| |_/ \__,_| \___||_|\_\ \___||_| 
""" + "\033[0m")


def print_ascii_art2():
    print("\033[1;96m----------------------------------\033[0m")


def print_ascii_art3():
    print("\033[1;93mScript created by: Black Dragon Hacker\033[0m")


def print_ascii_art4():
 print("\033[1;92mJoin Telegram: \nhttps://t.me/BlackDragonHacker007\033[0m")


def print_ascii_art5():
 print("\033[1;91mVisit my GitHub: \nhttps://github.com/BlackDragonHacker\033[0m")


def print_ascii_art6():
 print("\033[1;96m----------------------------------\033[0m")


def print_ascii_art7():
 print("\033[1;38;2;139;69;19;48;2;173;216;230m--------[Vertus Bot]--------\033[0m")


def print_ascii_art8():
 print("\033[1;96m----------------------------------\033[0m")

# Function to fetch initial data
def fetch_initial_data(token):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {token}',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site'
    }
    
    url = 'https://api.thevertus.app/users/get-data'
    payload = {}

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        data = json.loads(response.text)
        return data
    else:
        print(f'Error fetching initial data: HTTP {response.status_code} - {response.text}')
        return None

# Function to claim daily bonus
def claim_daily_bonus(token):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {token}',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site'
    }
    
    url = 'https://api.thevertus.app/users/claim-daily'
    payload = {}

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        print(f'\033[92m Daily Bonus claimed successful\033[0m')
    elif response.status_code == 409:
        print(f'\033[93m Daily Bonus already claimed\033[0m')
    else:
        print(f'\033[1;91mError claiming Daily Bonus: HTTP {response.status_code} - {response.text}\033[0m')

# Main function to claim tokens for each account
def claim_tokens():
    while True:  # Loop to continuously claim tokens
        tokens = read_tokens('token.txt')  # Read tokens from file
        
        initial_data_list = []
        for token in tokens:
            initial_data = fetch_initial_data(token)
            if initial_data:
                initial_data_list.append(initial_data)
            else:
                initial_data_list.append(None)

        # Clear the terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')

        # Print ASCII art
        print_ascii_art1()
        print_ascii_art2()
        print_ascii_art3()
        print_ascii_art4()
        print_ascii_art5()
        print_ascii_art6()
        print_ascii_art7()
        print_ascii_art8()

        # Print the number of accounts
        print(f"\033[1;94mTotal number of accounts: {len(tokens)}\033[0m")

        for index, token in enumerate(tokens, start=1):
            headers = {
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9',
                'authorization': f'Bearer {token}',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                'pragma': 'no-cache',
                'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site'
            }
            
            url = 'https://api.thevertus.app/game-service/collect'
            payload = {}

            # Making POST request to claim tokens
            response = requests.post(url, headers=headers, json=payload)

            # Print response for each account
            print(f'\033[96m\033[1m------Account {index}------\033[0m')

            if response.status_code == 201:
                try:
                    data = json.loads(response.text)
                    new_balance = data.get('newBalance', '')

                    # Calculate balance as per your requirement
                    if new_balance:
                        balance = float(new_balance) / 1e18  # Divide by 10^18 as per your requirement
                        print(f'\033[1;95m VERT Balance: {balance}\033[0m')
                        print(f'\033[92m VERT Claimed Successful\033[0m')  # Print "Claimed Successful" upon success
                    else:
                        print(f'\033[1;91mError: No newBalance in response\033[0m')
                except json.JSONDecodeError:
                    print(f'\033[1;91mError: Invalid JSON response\033[0m')
            else:
                print(f'\033[1;91mError: HTTP {response.status_code} - {response.text}\033[0m')

            # Claim the daily bonus for the current account
            claim_daily_bonus(token)

            # Display countdown before processing next account
            if index < len(tokens):
                display_countdown(5)  # Wait for 5 seconds before processing next account

        # After processing all accounts, wait before claiming tokens again
        print("\nWaiting before claiming tokens again...\n")
        display_countdown(300)  # Wait for 60 seconds before claiming tokens again

# Print ASCII art before running the main function
        print_ascii_art1()
        print_ascii_art2()
        print_ascii_art3()
        print_ascii_art4()
        print_ascii_art5()
        print_ascii_art6()
        print_ascii_art7()
        print_ascii_art8()

# Run the main function
if __name__ == '__main__':
    claim_tokens()
