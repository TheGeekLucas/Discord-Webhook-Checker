import os
import time
import requests
from discord import SyncWebhook
import pytz

def print_animated(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_animation(duration=3):
    for _ in range(duration * 10):
        print(".", end='', flush=True)
        time.sleep(0.05)
    print()

def check_webhook(webhook_url):
    response = requests.get(webhook_url)
    return response.status_code == 200

def delete_webhook(webhook_url):
    response = requests.delete(webhook_url)
    return response.status_code == 204

def show_webhook_info(webhook_url):
    webhook = SyncWebhook.from_url(webhook_url)
    print("\033[1;36m")
    print(f"Webhook ID: {webhook.id}")

    print(f"Webhook Creation Date (UTC): {webhook.created_at.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print("\033[0m")
    input("\nPress any key to continue...")

def edit_webhook(webhook_url):
    webhook = SyncWebhook.from_url(webhook_url)
    print("\033[1;33m")
    print("[1] Change Webhook Name\n[3] Exit")
    print("\033[0m")
    
    choice = input("\n> ")

    if choice == "1":
        new_name = input("[INPUT] ENTER THE NEW NAME FOR THE WEBHOOK: ")
        webhook.edit(name=new_name)
        print("Webhook name has been changed successfully.")
        time.sleep(2)
    elif choice == "2":
        show_webhook_info(webhook_url)
    elif choice == "3":
        pass
    else:
        print("Invalid choice.")
        time.sleep(2)

def send_message(webhook_url, message):
    webhook = SyncWebhook.from_url(webhook_url)
    webhook.send(content=message)

def main_menu(first_time):
    webhook_url = None

    while True:
        if first_time:
            clear_screen()
            os.system('title Discord Webhook Checker')
            print("\033[1;31m")
            ascii_art = """
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝     ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗     ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ 
            """
            print_animated(ascii_art, delay=1e-300)
            print("\033[0m")
            first_time = False
            loading_animation()

        clear_screen()
        os.system('title Discord Webhook Checker')
        print("\033[1;31m")
        ascii_art = """
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝     ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗     ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ 
            """
        print(ascii_art)
        print("\033[0m")

        if webhook_url:
            print("\033[1;32m")
            print("[1] Delete Webhook\n[2] Send a Message\n[3] Edit Webhook\n[4] Show Webhook Information\n[5] Exit")
            print("\033[0m")
        else:
            print("\033[1;34m")
            print("[1] Check Webhook Status\n[2] Exit")
            print("\033[0m")

        try:
            q = input("\n> ")
        except KeyboardInterrupt:
            continue

        clear_screen()

        if not webhook_url:
            if q == "1":
                webhook_url = input("[INPUT] ENTER THE WEBHOOK TO CHECK: ")
                if check_webhook(webhook_url):
                    print("Specified webhook does exist.")
                else:
                    print("Specified webhook does not exist.")
                    webhook_url = None
                time.sleep(1)
            elif q == "2":
                break
            else:
                print("Invalid choice.")
                time.sleep(2)
        else:
            if q == "1":
                if delete_webhook(webhook_url):
                    print("Webhook has been deleted successfully.")
                else:
                    print("Unknown error has occurred.")
                time.sleep(2)
                webhook_url = None
            elif q == "2":
                message = input("[INPUT] ENTER THE MESSAGE TO SEND: ")
                send_message(webhook_url, message)
                print("Your message has been sent successfully.")
                time.sleep(2)
            elif q == "3":
                edit_webhook(webhook_url)
            elif q == "4":
                show_webhook_info(webhook_url)
            elif q == "5":
                break
            else:
                print("Invalid choice.")
                time.sleep(2)

if __name__ == "__main__":
    first_time = True
    main_menu(first_time)
