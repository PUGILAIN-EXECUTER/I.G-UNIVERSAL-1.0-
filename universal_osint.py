#OFFICIAL TOOL

import requests
import json
import time
import os
import sys
from datetime import datetime

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def clear_screen():
    os.system('clear')

def print_banner():
    banner = f"""
{Color.CYAN}{Color.BOLD}
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                                                                              ║
║          .---`\~~\                 ____ ______   _    _____                  ║
║        ;       ~~ \               /  _// ____/  | |  / /__\                  ║
║       |  PUGILAIN  ;              / / / / __    | | / /__/ /                 ║
║    ,--------,______|---.       _/ /_/ /_/ /    | |/ // __/                   ║        
║   /          \-----`    \    /___(_)____/     |___//____/                    ║
║   `.__________`-_______-                                                     ║
║                                                                              ║
║                                                                              ║
║                                                                              ║
║                    ROBLOX® OSINT© TOOL - COMPLETE USER INFO℗                 ║
║                                                                              ║
║     TIKTOK: PugilainTeam | GitHub: PUGILAIN-EXECUTER | OFFICIALE TOOL        ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
{Color.END}
    """
    print(banner)

def get_user_info(user_id):
    try:
        url = f"https://users.roblox.com/v1/users/{user_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

def get_presence(user_id):
    try:
        url = "https://presence.roblox.com/v1/presence/users"
        data = {"userIds": [user_id]}
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

def get_friends(user_id):
    try:
        url = f"https://friends.roblox.com/v1/users/{user_id}/friends"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

def get_followers(user_id):
    try:
        url = f"https://friends.roblox.com/v1/users/{user_id}/followers"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

def get_followings(user_id):
    try:
        url = f"https://friends.roblox.com/v1/users/{user_id}/followings"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

def get_groups(user_id):
    try:
        url = f"https://groups.roblox.com/v1/users/{user_id}/groups/roles"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

def get_avatar(user_id):
    try:
        url = f"https://thumbnails.roblox.com/v1/users/avatar?userIds={user_id}&size=420x420&format=Png&isCircular=false"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

def get_badges(user_id):
    try:
        url = f"https://badges.roblox.com/v1/users/{user_id}/badges"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

def get_inventory(user_id):
    try:
        url = f"https://inventory.roblox.com/v1/users/{user_id}/items/All"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

def get_username_by_id(user_id):
    try:
        url = f"https://users.roblox.com/v1/users/{user_id}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get('name', 'Unknown')
        return 'Unknown'
    except:
        return 'Unknown'

def display_user_info(user_id):
    print(f"\n{Color.YELLOW}{Color.BOLD}[🔍] EXTRACTING USER INFORMATION...{Color.END}")
    time.sleep(1)
    
    user_data = get_user_info(user_id)
    if not user_data:
        print(f"{Color.RED}[❌] USER NOT FOUND{Color.END}")
        return
    
    print(f"\n{Color.GREEN}{Color.BOLD}╔══════════════════════════════════════════════════════════════╗{Color.END}")
    print(f"{Color.GREEN}{Color.BOLD}║                      BASIC INFORMATION                       ║{Color.END}")
    print(f"{Color.GREEN}{Color.BOLD}╚══════════════════════════════════════════════════════════════╝{Color.END}")
    
    print(f"{Color.CYAN}👤 Username: {Color.WHITE}{user_data.get('name', 'N/A')}{Color.END}")
    print(f"{Color.CYAN}🆔 User ID: {Color.WHITE}{user_data.get('id', 'N/A')}{Color.END}")
    print(f"{Color.CYAN}📛 Display Name: {Color.WHITE}{user_data.get('displayName', 'N/A')}{Color.END}")
    print(f"{Color.CYAN}📅 Created: {Color.WHITE}{datetime.fromisoformat(user_data.get('created', '')).strftime('%Y-%m-%d %H:%M:%S') if user_data.get('created') else 'N/A'}{Color.END}")
    
    presence_data = get_presence(user_id)
    if presence_data and 'userPresences' in presence_data and presence_data['userPresences']:
        presence = presence_data['userPresences'][0]
        print(f"{Color.CYAN}🟢 Status: {Color.WHITE}{presence.get('lastLocation', 'Offline')}{Color.END}")
        print(f"{Color.CYAN}🎮 Game: {Color.WHITE}{presence.get('placeId', 'Not in game')}{Color.END}")

def display_friends_info(user_id):
    print(f"\n{Color.YELLOW}{Color.BOLD}[👥] EXTRACTING FRIENDS INFORMATION...{Color.END}")
    time.sleep(1)
    
    friends_data = get_friends(user_id)
    if not friends_data or 'data' not in friends_data:
        print(f"{Color.RED}[❌] NO FRIENDS FOUND{Color.END}")
        return
    
    print(f"\n{Color.GREEN}{Color.BOLD}╔══════════════════════════════════════════════════════════════╗{Color.END}")
    print(f"{Color.GREEN}{Color.BOLD}║                         FRIENDS LIST                          ║{Color.END}")
    print(f"{Color.GREEN}{Color.BOLD}╚══════════════════════════════════════════════════════════════╝{Color.END}")
    
    for i, friend in enumerate(friends_data['data'][:20], 1):
        emoji = "👤"
        print(f"{Color.MAGENTA}{emoji} Friend {i}: {Color.WHITE}{friend.get('name', 'Unknown')} {Color.YELLOW}(ID: {friend.get('id', 'N/A')}){Color.END}")

def display_followers_info(user_id):
    print(f"\n{Color.YELLOW}{Color.BOLD}[📋] EXTRACTING FOLLOWERS INFORMATION...{Color.END}")
    time.sleep(1)
    
    followers_data = get_followers(user_id)
    if not followers_data or 'data' not in followers_data:
        print(f"{Color.RED}[❌] NO FOLLOWERS FOUND{Color.END}")
        return
    
    print(f"\n{Color.GREEN}{Color.BOLD}╔══════════════════════════════════════════════════════════════╗{Color.END}")
    print(f"{Color.GREEN}{Color.BOLD}║                        FOLLOWERS LIST                         ║{Color.END}")
    print(f"{Color.GREEN}{Color.BOLD}╚══════════════════════════════════════════════════════════════╝{Color.END}")
    
    for i, follower in enumerate(followers_data['data'][:15], 1):
        emoji = "🌟"
        print(f"{Color.MAGENTA}{emoji} Follower {i}: {Color.WHITE}{follower.get('name', 'Unknown')} {Color.YELLOW}(ID: {follower.get('id', 'N/A')}){Color.END}")

def display_groups_info(user_id):
    print(f"\n{Color.YELLOW}{Color.BOLD}[👥] EXTRACTING GROUPS INFORMATION...{Color.END}")
    time.sleep(1)
    
    groups_data = get_groups(user_id)
    if not groups_data or 'data' not in groups_data:
        print(f"{Color.RED}[❌] NO GROUPS FOUND{Color.END}")
        return
    
    print(f"\n{Color.GREEN}{Color.BOLD}╔══════════════════════════════════════════════════════════════╗{Color.END}")
    print(f"{Color.GREEN}{Color.BOLD}║                         GROUPS LIST                           ║{Color.END}")
    print(f"{Color.GREEN}{Color.BOLD}╚══════════════════════════════════════════════════════════════╝{Color.END}")
    
    for i, group in enumerate(groups_data['data'][:10], 1):
        emoji = "🏢"
        role = group.get('role', {})
        print(f"{Color.MAGENTA}{emoji} Group {i}: {Color.WHITE}{group.get('group', {}).get('name', 'Unknown')} {Color.YELLOW}(Role: {role.get('name', 'N/A')}){Color.END}")

def display_avatar_info(user_id):
    print(f"\n{Color.YELLOW}{Color.BOLD}[🖼️] EXTRACTING AVATAR INFORMATION...{Color.END}")
    time.sleep(1)
    
    avatar_data = get_avatar(user_id)
    if not avatar_data or 'data' not in avatar_data or not avatar_data['data']:
        print(f"{Color.RED}[❌] NO AVATAR DATA FOUND{Color.END}")
        return
    
    print(f"\n{Color.GREEN}{Color.BOLD}╔══════════════════════════════════════════════════════════════╗{Color.END}")
    print(f"{Color.GREEN}{Color.BOLD}║                        AVATAR INFORMATION                     ║{Color.END}")
    print(f"{Color.GREEN}{Color.BOLD}╚══════════════════════════════════════════════════════════════╝{Color.END}")
    
    avatar = avatar_data['data'][0]
    print(f"{Color.CYAN}🖼️ Avatar URL: {Color.WHITE}{avatar.get('imageUrl', 'N/A')}{Color.END}")

def display_badges_info(user_id):
    print(f"\n{Color.YELLOW}{Color.BOLD}[🏅] EXTRACTING BADGES INFORMATION...{Color.END}")
    time.sleep(1)
    
    badges_data = get_badges(user_id)
    if not badges_data or 'data' not in badges_data:
        print(f"{Color.RED}[❌] NO BADGES FOUND{Color.END}")
        return
    
    print(f"\n{Color.GREEN}{Color.BOLD}╔══════════════════════════════════════════════════════════════╗{Color.END}")
    print(f"{Color.GREEN}{Color.BOLD}║                         BADGES LIST                           ║{Color.END}")
    print(f"{Color.GREEN}{Color.BOLD}╚══════════════════════════════════════════════════════════════╝{Color.END}")
    
    for i, badge in enumerate(badges_data['data'][:10], 1):
        emoji = "🏅"
        print(f"{Color.MAGENTA}{emoji} Badge {i}: {Color.WHITE}{badge.get('displayName', 'Unknown')} {Color.YELLOW}({badge.get('displayDescription', 'No description')}){Color.END}")

def display_all_info(user_id):
    display_user_info(user_id)
    display_friends_info(user_id)
    display_followers_info(user_id)
    display_groups_info(user_id)
    display_avatar_info(user_id)
    display_badges_info(user_id)

def main():
    clear_screen()
    print_banner()
    
    while True:
        print(f"\n{Color.CYAN}{Color.BOLD}╔══════════════════════════════════════════════════════════════╗{Color.END}")
        print(f"{Color.CYAN}{Color.BOLD}║                     SELECT AN OPTION                         ║{Color.END}")
        print(f"{Color.CYAN}{Color.BOLD}╚══════════════════════════════════════════════════════════════╝{Color.END}")
        
        print(f"{Color.WHITE}{Color.BOLD}[1] {Color.GREEN}Extract Basic User Info{Color.END}")
        print(f"{Color.WHITE}{Color.BOLD}[2] {Color.GREEN}Extract Friends List{Color.END}")
        print(f"{Color.WHITE}{Color.BOLD}[3] {Color.GREEN}Extract Followers List{Color.END}")
        print(f"{Color.WHITE}{Color.BOLD}[4] {Color.GREEN}Extract Groups Info{Color.END}")
        print(f"{Color.WHITE}{Color.BOLD}[5] {Color.GREEN}Extract Avatar Info{Color.END}")
        print(f"{Color.WHITE}{Color.BOLD}[6] {Color.GREEN}Extract Badges Info{Color.END}")
        print(f"{Color.WHITE}{Color.BOLD}[7] {Color.GREEN}Extract ALL Information{Color.END}")
        print(f"{Color.WHITE}{Color.BOLD}[0] {Color.RED}Exit{Color.END}")
        
        choice = input(f"\n{Color.YELLOW}Select option (0-7): {Color.END}")
        
        if choice == '0':
            print(f"\n{Color.RED}[👋] Goodbye!{Color.END}")
            break
        elif choice in ['1', '2', '3', '4', '5', '6', '7']:
            user_id = input(f"{Color.YELLOW}Enter Roblox User ID: {Color.END}")
            
            if not user_id.isdigit():
                print(f"{Color.RED}[❌] Invalid User ID!{Color.END}")
                continue
            
            if choice == '1':
                display_user_info(user_id)
            elif choice == '2':
                display_friends_info(user_id)
            elif choice == '3':
                display_followers_info(user_id)
            elif choice == '4':
                display_groups_info(user_id)
            elif choice == '5':
                display_avatar_info(user_id)
            elif choice == '6':
                display_badges_info(user_id)
            elif choice == '7':
                display_all_info(user_id)
        else:
            print(f"{Color.RED}[❌] Invalid option!{Color.END}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Color.RED}[👋] Script interrupted by user{Color.END}")
        sys.exit(0)
