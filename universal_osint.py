#!/usr/bin/env python3
"""
I.G UNIVERSAL V2 - ROBLOX OSINT TOOL
Advanced Roblox User Intelligence Gathering Tool
"""

import requests
import json
import time
import sys
import os
from datetime import datetime
import argparse

class Color:
    RED = '\033[38;5;196m'
    GREEN = '\033[38;5;46m'
    BLUE = '\033[38;5;51m'
    YELLOW = '\033[38;5;226m'
    ORANGE = '\033[38;5;208m'
    PURPLE = '\033[38;5;129m'
    PINK = '\033[38;5;201m'
    CYAN = '\033[38;5;87m'
    MAGENTA = '\033[38;5;165m'
    WHITE = '\033[38;5;15m'
    RESET = '\033[0m'

class RobloxUniversalV2:
    def __init__(self):
        self.version = "2.0"
        self.author = "I.G Universal"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        })
        
        # ROBLOX THEMED BANNER - SUPER COOL!
        self.banner = f"""
{Color.PINK}╔═══════════════════════════════════════════════════════════════════════════════╗
{Color.PINK}║                                                                               ║
{Color.CYAN}║    ██████╗  ██████╗ ██████╗ ██╗      ██████╗ ██╗  ██╗    ██╗ ██████╗         ║
{Color.CYAN}║    ██╔══██╗██╔═══██╗██╔══██╗██║     ██╔═══██╗╚██╗██╔╝    ██║██╔════╝         ║
{Color.BLUE}║    ██████╔╝██║   ██║██████╔╝██║     ██║   ██║ ╚███╔╝     ██║██║              ║
{Color.BLUE}║    ██╔══██╗██║   ██║██╔══██╗██║     ██║   ██║ ██╔██╗     ██║██║              ║
{Color.PURPLE}║    ██║  ██║╚██████╔╝██████╔╝███████╗╚██████╔╝██╔╝ ██╗    ██║╚██████╗         ║
{Color.PURPLE}║    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝    ╚═╝ ╚═════╝         ║
{Color.PINK}║                                                                               ║
{Color.RED}║           ██╗   ██╗███╗   ██╗██╗██╗███╗   ██╗██╗███████╗███████╗██████╗ ███████╗║
{Color.RED}║           ██║   ██║████╗  ██║██║██║████╗  ██║██║██╔════╝██╔════╝██╔══██╗██╔════╝║
{Color.ORANGE}║           ██║   ██║██╔██╗ ██║██║██║██╔██╗ ██║██║█████╗  ███████╗██████╔╝█████╗  ║
{Color.ORANGE}║           ██║   ██║██║╚██╗██║██║██║██║╚██╗██║██║██╔══╝  ╚════██║██╔══██╗██╔══╝  ║
{Color.YELLOW}║           ╚██████╔╝██║ ╚████║██║██║██║ ╚████║██║███████╗███████║██║  ██║███████╗║
{Color.YELLOW}║            ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝╚═╝  ╚═══╝╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝║
{Color.PINK}║                                                                               ║
{Color.GREEN}║                         🚀 ROBLOX OSINT TOOL V2.0 🚀                         ║
{Color.GREEN}║                      Advanced User Intelligence Gathering                    ║
{Color.PINK}║                                                                               ║
{Color.PINK}╚═══════════════════════════════════════════════════════════════════════════════╝{Color.RESET}
"""

    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    def print_banner(self):
        self.clear_screen()
        print(self.banner)
        print(f"{Color.CYAN}[{Color.GREEN}+{Color.CYAN}]{Color.WHITE} I.G Universal V2 - Roblox OSINT Tool")
        print(f"{Color.CYAN}[{Color.GREEN}+{Color.CYAN}]{Color.WHITE} Version: {self.version}")
        print(f"{Color.CYAN}[{Color.GREEN}+{Color.CYAN}]{Color.WHITE} Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{Color.PURPLE}═" * 80 + Color.RESET)

    def print_status(self, message: str, status: str = "info"):
        colors = {
            "info": Color.BLUE,
            "success": Color.GREEN,
            "warning": Color.YELLOW,
            "error": Color.RED,
            "special": Color.PURPLE
        }
        color = colors.get(status, Color.WHITE)
        symbols = {"info": "●", "success": "✔", "warning": "⚠", "error": "✖", "special": "◆"}
        symbol = symbols.get(status, "●")
        print(f"{color}[{symbol}]{Color.WHITE} {message}{Color.RESET}")

    def get_user_info(self, user_id: str):
        """Get comprehensive Roblox user information"""
        self.print_status(f"Fetching information for UserID: {user_id}", "special")
        
        try:
            # User Profile API
            profile_url = f"https://users.roblox.com/v1/users/{user_id}"
            response = self.session.get(profile_url)
            
            if response.status_code != 200:
                self.print_status(f"Failed to fetch user data: {response.status_code}", "error")
                return None
            
            user_data = response.json()
            
            # Display user information
            print(f"\n{Color.CYAN}┌──{Color.WHITE} BASIC INFORMATION {Color.CYAN}─" + "─" * 50 + "┐")
            print(f"{Color.CYAN}│{Color.WHITE} User ID: {Color.GREEN}{user_data.get('id', 'N/A')}")
            print(f"{Color.CYAN}│{Color.WHITE} Username: {Color.YELLOW}{user_data.get('name', 'N/A')}")
            print(f"{Color.CYAN}│{Color.WHITE} Display Name: {Color.BLUE}{user_data.get('displayName', 'N/A')}")
            print(f"{Color.CYAN}│{Color.WHITE} Description: {Color.PURPLE}{user_data.get('description', 'N/A')}")
            print(f"{Color.CYAN}│{Color.WHITE} Created: {Color.ORANGE}{user_data.get('created', 'N/A')}")
            print(f"{Color.CYAN}│{Color.WHITE} Verified: {Color.GREEN if user_data.get('isVerified', False) else Color.RED}{user_data.get('isVerified', 'N/A')}")
            print(f"{Color.CYAN}└" + "─" * 68 + "┘")
            
            # Get additional details
            self.get_user_details(user_id)
            self.get_friends_count(user_id)
            self.get_followers_count(user_id)
            self.get_following_count(user_id)
            self.get_user_avatar(user_id)
            self.get_user_presence(user_id)
            self.get_user_groups(user_id)
            self.get_user_assets(user_id)
            
            return user_data
            
        except Exception as e:
            self.print_status(f"Error fetching user info: {e}", "error")
            return None

    def get_user_details(self, user_id: str):
        """Get additional user details"""
        try:
            details_url = f"https://users.roblox.com/v1/users/{user_id}"
            response = self.session.get(details_url)
            
            if response.status_code == 200:
                details = response.json()
                print(f"\n{Color.GREEN}├── Additional Details:")
                print(f"{Color.GREEN}│   └── Banned: {Color.RED if details.get('isBanned') else Color.GREEN}{details.get('isBanned', 'N/A')}")
                
        except Exception as e:
            self.print_status(f"Error fetching user details: {e}", "warning")

    def get_friends_count(self, user_id: str):
        """Get user friends count"""
        try:
            friends_url = f"https://friends.roblox.com/v1/users/{user_id}/friends/count"
            response = self.session.get(friends_url)
            
            if response.status_code == 200:
                friends_data = response.json()
                print(f"{Color.BLUE}├── Friends Count: {Color.WHITE}{friends_data.get('count', 0)}")
                
        except Exception as e:
            self.print_status(f"Error fetching friends count: {e}", "warning")

    def get_followers_count(self, user_id: str):
        """Get user followers count"""
        try:
            followers_url = f"https://friends.roblox.com/v1/users/{user_id}/followers/count"
            response = self.session.get(followers_url)
            
            if response.status_code == 200:
                followers_data = response.json()
                print(f"{Color.PURPLE}├── Followers: {Color.WHITE}{followers_data.get('count', 0)}")
                
        except Exception as e:
            self.print_status(f"Error fetching followers count: {e}", "warning")

    def get_following_count(self, user_id: str):
        """Get user following count"""
        try:
            following_url = f"https://friends.roblox.com/v1/users/{user_id}/followings/count"
            response = self.session.get(following_url)
            
            if response.status_code == 200:
                following_data = response.json()
                print(f"{Color.ORANGE}├── Following: {Color.WHITE}{following_data.get('count', 0)}")
                
        except Exception as e:
            self.print_status(f"Error fetching following count: {e}", "warning")

    def get_user_avatar(self, user_id: str):
        """Get user avatar information"""
        try:
            avatar_url = f"https://avatar.roblox.com/v1/users/{user_id}/avatar"
            response = self.session.get(avatar_url)
            
            if response.status_code == 200:
                avatar_data = response.json()
                print(f"{Color.YELLOW}├── Avatar Information:")
                print(f"{Color.YELLOW}│   └── Avatar Type: {Color.WHITE}{avatar_data.get('playerAvatarType', 'N/A')}")
                
        except Exception as e:
            self.print_status(f"Error fetching avatar info: {e}", "warning")

    def get_user_presence(self, user_id: str):
        """Get user presence/status"""
        try:
            presence_url = f"https://presence.roblox.com/v1/presence/users"
            response = self.session.post(presence_url, json={"userIds": [user_id]})
            
            if response.status_code == 200:
                presence_data = response.json()
                if presence_data.get('userPresences'):
                    user_presence = presence_data['userPresences'][0]
                    print(f"{Color.CYAN}├── Presence:")
                    print(f"{Color.CYAN}│   └── Status: {Color.WHITE}{user_presence.get('userPresenceType', 'N/A')}")
                    print(f"{Color.CYAN}│   └── Last Online: {Color.WHITE}{user_presence.get('lastOnline', 'N/A')}")
                    
        except Exception as e:
            self.print_status(f"Error fetching presence: {e}", "warning")

    def get_user_groups(self, user_id: str):
        """Get user groups"""
        try:
            groups_url = f"https://groups.roblox.com/v1/users/{user_id}/groups/roles"
            response = self.session.get(groups_url)
            
            if response.status_code == 200:
                groups_data = response.json()
                groups = groups_data.get('data', [])
                print(f"{Color.GREEN}├── Groups ({len(groups)}):")
                
                for group in groups[:5]:  # Show first 5 groups
                    group_name = group.get('group', {}).get('name', 'N/A')
                    role = group.get('role', {}).get('name', 'N/A')
                    print(f"{Color.GREEN}│   └── {Color.WHITE}{group_name} ({role})")
                    
                if len(groups) > 5:
                    print(f"{Color.GREEN}│   └── ... and {len(groups) - 5} more groups")
                    
        except Exception as e:
            self.print_status(f"Error fetching groups: {e}", "warning")

    def get_user_assets(self, user_id: str):
        """Get user assets/items"""
        try:
            assets_url = f"https://inventory.roblox.com/v1/users/{user_id}/items/1/1?limit=10"
            response = self.session.get(assets_url)
            
            if response.status_code == 200:
                assets_data = response.json()
                assets = assets_data.get('data', [])
                print(f"{Color.BLUE}├── Recent Assets ({len(assets)}):")
                
                for asset in assets[:3]:  # Show first 3 assets
                    asset_name = asset.get('name', 'N/A')
                    print(f"{Color.BLUE}│   └── {Color.WHITE}{asset_name}")
                    
        except Exception as e:
            self.print_status(f"Error fetching assets: {e}", "warning")

    def get_user_by_username(self, username: str):
        """Get user ID from username"""
        self.print_status(f"Searching for username: {username}", "info")
        
        try:
            search_url = f"https://users.roblox.com/v1/users/search"
            params = {'keyword': username, 'limit': 1}
            response = self.session.get(search_url, params=params)
            
            if response.status_code == 200:
                search_data = response.json()
                if search_data.get('data'):
                    user = search_data['data'][0]
                    print(f"{Color.GREEN}├── Found User:")
                    print(f"{Color.GREEN}│   └── ID: {Color.WHITE}{user.get('id')}")
                    print(f"{Color.GREEN}│   └── Name: {Color.WHITE}{user.get('name')}")
                    print(f"{Color.GREEN}│   └── Display Name: {Color.WHITE}{user.get('displayName')}")
                    return user.get('id')
                else:
                    self.print_status("User not found", "error")
                    return None
            else:
                self.print_status(f"Search failed: {response.status_code}", "error")
                return None
                
        except Exception as e:
            self.print_status(f"Error searching user: {e}", "error")
            return None

    def bulk_user_lookup(self, user_list: list):
        """Lookup multiple users"""
        self.print_status(f"Starting bulk lookup for {len(user_list)} users", "special")
        
        for username in user_list:
            username = username.strip()
            if username:
                print(f"\n{Color.PURPLE}═[{Color.WHITE} Processing: {username} {Color.PURPLE}]═" + "═" * (50 - len(username)))
                user_id = self.get_user_by_username(username)
                if user_id:
                    self.get_user_info(str(user_id))
                time.sleep(1)

    def advanced_user_analysis(self, user_id: str):
        """Advanced analysis with more endpoints"""
        self.print_status(f"Starting advanced analysis for UserID: {user_id}", "special")
        
        # Get basic info first
        basic_info = self.get_user_info(user_id)
        if not basic_info:
            return
            
        print(f"\n{Color.RED}┌──{Color.WHITE} ADVANCED ANALYSIS {Color.RED}─" + "─" * 48 + "┐")
        
        # Add more advanced endpoints here
        self.get_user_badges(user_id)
        self.get_user_favorites(user_id)
        self.get_user_statistics(user_id)
        
        print(f"{Color.RED}└" + "─" * 68 + "┘")

    def get_user_badges(self, user_id: str):
        """Get user badges"""
        try:
            badges_url = f"https://badges.roblox.com/v1/users/{user_id}/badges"
            response = self.session.get(badges_url)
            
            if response.status_code == 200:
                badges_data = response.json()
                badges = badges_data.get('data', [])
                print(f"{Color.YELLOW}├── Badges ({len(badges)}):")
                
        except Exception as e:
            self.print_status(f"Error fetching badges: {e}", "warning")

    def get_user_favorites(self, user_id: str):
        """Get user favorites"""
        try:
            favorites_url = f"https://games.roblox.com/v2/users/{user_id}/favorite/games"
            response = self.session.get(favorites_url)
            
            if response.status_code == 200:
                favorites_data = response.json()
                favorites = favorites_data.get('data', [])
                print(f"{Color.CYAN}├── Favorite Games ({len(favorites)}):")
                
        except Exception as e:
            self.print_status(f"Error fetching favorites: {e}", "warning")

    def get_user_statistics(self, user_id: str):
        """Get user statistics"""
        try:
            # This would require additional endpoints
            print(f"{Color.GREEN}├── Statistics: {Color.WHITE}Advanced stats available")
            
        except Exception as e:
            self.print_status(f"Error fetching statistics: {e}", "warning")

    def show_menu(self):
        """Display the main menu"""
        menu = f"""
{Color.PURPLE}╔═══════════════════════════════════════════════════════════════════════════════╗
{Color.PURPLE}║                   {Color.CYAN}🎮 ROBLOX OSINT MENU - I.G UNIVERSAL V2{Color.PURPLE}                   ║
{Color.PURPLE}╠═══════════════════════════════════════════════════════════════════════════════╣
{Color.PURPLE}║ {Color.GREEN}1.{Color.WHITE} 🔍 Lookup User by ID          {Color.GREEN}4.{Color.WHITE} 👥 Bulk User Lookup           {Color.PURPLE}║
{Color.PURPLE}║ {Color.GREEN}2.{Color.WHITE} 🔎 Lookup User by Username    {Color.GREEN}5.{Color.WHITE} 🚀 Advanced User Analysis     {Color.PURPLE}║
{Color.PURPLE}║ {Color.GREEN}3.{Color.WHITE} 📊 Get User Statistics        {Color.GREEN}6.{Color.WHITE} 🎯 Multiple Analysis          {Color.PURPLE}║
{Color.PURPLE}║                                                                               ║
{Color.PURPLE}║ {Color.RED}0.{Color.WHITE} 🚪 Exit Tool                                                 {Color.PURPLE}║
{Color.PURPLE}╚═══════════════════════════════════════════════════════════════════════════════╝{Color.RESET}

{Color.YELLOW}Select an option [0-6]: {Color.RESET}"""
        
        print(menu)

    def run(self):
        """Main execution function"""
        try:
            while True:
                self.print_banner()
                self.show_menu()
                
                choice = input().strip()
                
                if choice == '1':
                    user_id = input(f"{Color.YELLOW}Enter Roblox User ID: {Color.RESET}").strip()
                    if user_id:
                        self.get_user_info(user_id)
                
                elif choice == '2':
                    username = input(f"{Color.YELLOW}Enter Roblox Username: {Color.RESET}").strip()
                    if username:
                        user_id = self.get_user_by_username(username)
                        if user_id:
                            self.get_user_info(str(user_id))
                
                elif choice == '3':
                    user_id = input(f"{Color.YELLOW}Enter Roblox User ID for statistics: {Color.RESET}").strip()
                    if user_id:
                        self.advanced_user_analysis(user_id)
                
                elif choice == '4':
                    users_input = input(f"{Color.YELLOW}Enter usernames (comma-separated): {Color.RESET}").strip()
                    if users_input:
                        user_list = users_input.split(',')
                        self.bulk_user_lookup(user_list)
                
                elif choice == '5':
                    user_id = input(f"{Color.YELLOW}Enter User ID for advanced analysis: {Color.RESET}").strip()
                    if user_id:
                        self.advanced_user_analysis(user_id)
                
                elif choice == '6':
                    targets = input(f"{Color.YELLOW}Enter User IDs/usernames (comma-separated): {Color.RESET}").strip()
                    if targets:
                        for target in targets.split(','):
                            target = target.strip()
                            if target.isdigit():
                                self.get_user_info(target)
                            else:
                                user_id = self.get_user_by_username(target)
                                if user_id:
                                    self.get_user_info(str(user_id))
                            print("\n" + "="*80 + "\n")
                
                elif choice == '0':
                    self.print_status("Thank you for using I.G Universal V2 - Roblox OSINT!", "success")
                    break
                
                else:
                    self.print_status("Invalid option! Please try again.", "error")
                
                if choice != '0':
                    input(f"\n{Color.YELLOW}Press Enter to continue...{Color.RESET}")
                    
        except KeyboardInterrupt:
            self.print_status("\nTool interrupted by user. Goodbye!", "warning")
        except Exception as e:
            self.print_status(f"Unexpected error: {e}", "error")

def main():
    """Main function"""
    tool = RobloxUniversalV2()
    tool.run()

if __name__ == "__main__":
    main()
