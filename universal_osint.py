#!/usr/bin/env python3
"""
UNIVERSAL OSINT TOOL - REAL WORKING VERSION
Combines Instagram OSINT + Real Roblox API + Universal Search
EDUCATIONAL PURPOSE ONLY
"""

import requests
import json
import time
import re
import sys
from datetime import datetime

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

class UniversalOSINT:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
            'Accept': 'application/json'
        })
    
    def banner(self):
        print(f"""{Colors.RED}{Colors.BOLD}
    
    ____ ______   __  ___   _______    ____________  _____ ___    __ 
   /  _// ____/  / / / / | / /  _/ |  / / ____/ __ \/ ___//   |  / / 
   / / / / __   / / / /  |/ // / | | / / __/ / /_/ /\__ \/ /| | / /  
 _/ /_/ /_/ /  / /_/ / /|  // /  | |/ / /___/ _, _/___/ / ___ |/ /___
/___(_)____/   \____/_/ |_/___/  |___/_____/_/ |_|/____/_/  |_/_____/
                                                                     
                                   
    {Colors.CYAN}UNIVERSAL OSINT TOOL - REAL WORKING VERSION{Colors.END}
    {Colors.YELLOW}Instagram + Roblox Real API + Universal Search{Colors.END}
    {Colors.RED}⚠️  FOR EDUCATIONAL PURPOSES ONLY ⚠️{Colors.END}
    
{Colors.END}""")

    # ==================== REAL ROBLOX OSINT ====================
    
    def get_roblox_user_id(self, username):
        """Get Roblox user ID from username"""
        try:
            url = f"https://api.roblox.com/users/get-by-username?username={username}"
            response = self.session.get(url)
            
            if response.status_code == 200:
                data = response.json()
                if 'Id' in data:
                    return data['Id']
            return None
        except Exception as e:
            print(f"{Colors.RED}Error getting user ID: {e}{Colors.END}")
            return None

    def get_roblox_user_info(self, user_id):
        """Get complete Roblox user information"""
        try:
            url = f"https://users.roblox.com/v1/users/{user_id}"
            response = self.session.get(url)
            
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"{Colors.RED}Error getting user info: {e}{Colors.END}")
            return None

    def get_roblox_friends(self, user_id):
        """Get user's friends list"""
        try:
            url = f"https://friends.roblox.com/v1/users/{user_id}/friends"
            response = self.session.get(url)
            
            if response.status_code == 200:
                data = response.json()
                return data.get('data', [])
            return []
        except Exception as e:
            print(f"{Colors.RED}Error getting friends: {e}{Colors.END}")
            return []

    def get_roblox_groups(self, user_id):
        """Get user's groups"""
        try:
            url = f"https://groups.roblox.com/v1/users/{user_id}/groups/roles"
            response = self.session.get(url)
            
            if response.status_code == 200:
                data = response.json()
                return data.get('data', [])
            return []
        except Exception as e:
            print(f"{Colors.RED}Error getting groups: {e}{Colors.END}")
            return []

    def get_roblox_assets(self, user_id):
        """Get user's owned assets"""
        try:
            url = f"https://inventory.roblox.com/v1/users/{user_id}/assets/collectibles?limit=10"
            response = self.session.get(url)
            
            if response.status_code == 200:
                data = response.json()
                return data.get('data', [])
            return []
        except Exception as e:
            print(f"{Colors.RED}Error getting assets: {e}{Colors.END}")
            return []

    def get_roblox_badges(self, user_id):
        """Get user's badges"""
        try:
            url = f"https://badges.roblox.com/v1/users/{user_id}/badges?limit=10"
            response = self.session.get(url)
            
            if response.status_code == 200:
                data = response.json()
                return data.get('data', [])
            return []
        except Exception as e:
            print(f"{Colors.RED}Error getting badges: {e}{Colors.END}")
            return []

    def roblox_osint(self, username):
        """COMPLETE Roblox OSINT - WORKING"""
        print(f"\n{Colors.CYAN}[🎮] STARTING ROBLOX ANALYSIS FOR: {username}{Colors.END}")
        
        # Get user ID
        user_id = self.get_roblox_user_id(username)
        if not user_id:
            print(f"{Colors.RED}❌ Roblox user not found: {username}{Colors.END}")
            return None
        
        print(f"{Colors.GREEN}✅ User ID found: {user_id}{Colors.END}")
        
        # Collect all data
        user_info = self.get_roblox_user_info(user_id)
        friends = self.get_roblox_friends(user_id)
        groups = self.get_roblox_groups(user_id)
        assets = self.get_roblox_assets(user_id)
        badges = self.get_roblox_badges(user_id)
        
        # Compile results
        results = {
            'success': True,
            'user_id': user_id,
            'username': username,
            'user_info': user_info,
            'friends_count': len(friends),
            'friends_sample': friends[:5],
            'groups_count': len(groups),
            'groups_sample': groups[:5],
            'assets_count': len(assets),
            'assets_sample': assets[:3],
            'badges_count': len(badges),
            'badges_sample': badges[:3]
        }
        
        return results

    def display_roblox_results(self, results):
        """Display Roblox results in readable format"""
        if not results or not results.get('success'):
            print(f"{Colors.RED}❌ No data found{Colors.END}")
            return
        
        user_info = results.get('user_info', {})
        
        print(f"\n{Colors.GREEN}{Colors.BOLD}🎮 ROBLOX RESULTS - REAL DATA{Colors.END}")
        print(f"{Colors.CYAN}═" * 50 + Colors.END)
        
        # Basic info
        print(f"{Colors.BOLD}👤 PROFILE INFORMATION:{Colors.END}")
        print(f"  Display Name: {user_info.get('displayName', 'N/A')}")
        print(f"  Username: {results.get('username')}")
        print(f"  User ID: {results.get('user_id')}")
        print(f"  Description: {user_info.get('description', 'No description')}")
        print(f"  Account Created: {user_info.get('created', 'N/A')}")
        print(f"  Verified: {'✅' if user_info.get('isVerified', False) else '❌'}")
        
        # Statistics
        print(f"\n{Colors.BOLD}📊 STATISTICS:{Colors.END}")
        print(f"  Friends Count: {results.get('friends_count', 0)}")
        print(f"  Groups Count: {results.get('groups_count', 0)}")
        print(f"  Assets Owned: {results.get('assets_count', 0)}")
        print(f"  Badges Earned: {results.get('badges_count', 0)}")
        
        # Friends sample
        if results.get('friends_sample'):
            print(f"\n{Colors.BOLD}👥 FRIENDS (FIRST 5):{Colors.END}")
            for friend in results['friends_sample']:
                print(f"  • {friend.get('name', 'N/A')} (ID: {friend.get('id')})")
        
        # Groups sample
        if results.get('groups_sample'):
            print(f"\n{Colors.BOLD}👥 GROUPS (FIRST 5):{Colors.END}")
            for group in results['groups_sample']:
                group_info = group.get('group', {})
                role = group.get('role', {})
                print(f"  • {group_info.get('name', 'N/A')} - {role.get('name', 'Member')}")
        
        # Assets sample
        if results.get('assets_sample'):
            print(f"\n{Colors.BOLD}💎 ASSETS (FIRST 3):{Colors.END}")
            for asset in results['assets_sample']:
                print(f"  • {asset.get('name', 'N/A')}")
        
        print(f"{Colors.CYAN}═" * 50 + Colors.END)

    # ==================== INSTAGRAM REAL OSINT ====================

    def instagram_osint(self, username):
        """Instagram OSINT using real methods"""
        print(f"\n{Colors.CYAN}[📷] STARTING INSTAGRAM ANALYSIS FOR: {username}{Colors.END}")
        
        try:
            # Try to get public data
            profile_url = f"https://www.instagram.com/{username}/"
            response = self.session.get(profile_url)
            
            if response.status_code == 200:
                html_content = response.text
                
                # Extract data from HTML
                data_patterns = {
                    'followers': r'([\d,]+)\s+followers',
                    'following': r'([\d,]+)\s+following',
                    'posts': r'([\d,]+)\s+posts',
                    'description': r'"description":"([^"]+)"',
                    'is_private': r'"is_private":(true|false)',
                    'full_name': r'"full_name":"([^"]+)"'
                }
                
                extracted_data = {'success': True, 'username': username}
                for key, pattern in data_patterns.items():
                    matches = re.findall(pattern, html_content)
                    if matches:
                        extracted_data[key] = matches[0]
                
                return extracted_data
            else:
                return {'success': False, 'error': 'Profile not accessible'}
                
        except Exception as e:
            return {'success': False, 'error': str(e)}

    def display_instagram_results(self, results):
        """Display Instagram results"""
        if not results or not results.get('success'):
            print(f"{Colors.RED}❌ Cannot retrieve Instagram data{Colors.END}")
            return
        
        print(f"\n{Colors.GREEN}{Colors.BOLD}📷 INSTAGRAM RESULTS{Colors.END}")
        print(f"{Colors.CYAN}═" * 50 + Colors.END)
        
        if results.get('full_name'):
            print(f"{Colors.BOLD}👤 PROFILE INFORMATION:{Colors.END}")
            print(f"  Full Name: {results.get('full_name')}")
            print(f"  Username: {results.get('username')}")
            print(f"  Bio: {results.get('description', 'No bio')}")
            print(f"  Followers: {results.get('followers', 'N/A')}")
            print(f"  Following: {results.get('following', 'N/A')}")
            print(f"  Posts: {results.get('posts', 'N/A')}")
            print(f"  Private: {'✅' if results.get('is_private') == 'true' else '❌'}")
        else:
            # Fallback display
            print(f"{Colors.BOLD}👤 BASIC INFORMATION:{Colors.END}")
            print(f"  Username: {results.get('username')}")
            for key, value in results.items():
                if key not in ['success', 'username', 'error']:
                    print(f"  {key.replace('_', ' ').title()}: {value}")
        
        print(f"{Colors.CYAN}═" * 50 + Colors.END)

    # ==================== UNIVERSAL SEARCH ====================

    def universal_search(self, username):
        """Search across multiple platforms"""
        print(f"\n{Colors.CYAN}[🌐] STARTING UNIVERSAL SEARCH FOR: {username}{Colors.END}")
        
        platforms = {
            'GitHub': f'https://api.github.com/users/{username}',
            'Reddit': f'https://www.reddit.com/user/{username}/about.json',
            'Twitter': f'https://twitter.com/{username}',
            'Steam': f'https://steamcommunity.com/id/{username}'
        }
        
        results = {}
        
        for platform, url in platforms.items():
            try:
                response = self.session.get(url, timeout=10)
                
                if response.status_code == 200:
                    results[platform] = {
                        'exists': True,
                        'url': url,
                        'status': 'Found'
                    }
                elif response.status_code == 404:
                    results[platform] = {
                        'exists': False,
                        'url': url,
                        'status': 'Not found'
                    }
                else:
                    results[platform] = {
                        'exists': 'Unknown',
                        'url': url,
                        'status_code': response.status_code
                    }
                    
            except Exception as e:
                results[platform] = {
                    'exists': 'Error',
                    'url': url,
                    'error': str(e)
                }
        
        return results

    def display_universal_results(self, results):
        """Display universal search results"""
        print(f"\n{Colors.GREEN}{Colors.Bold}🌐 ONLINE PRESENCE RESULTS{Colors.END}")
        print(f"{Colors.CYAN}═" * 50 + Colors.END)
        
        for platform, data in results.items():
            if data.get('exists') is True:
                print(f"  {Colors.GREEN}✅ {platform}: FOUND{Colors.END}")
                print(f"     URL: {data.get('url')}")
            elif data.get('exists') is False:
                print(f"  {Colors.RED}❌ {platform}: Not found{Colors.END}")
            else:
                print(f"  {Colors.YELLOW}⚠️  {platform}: {data.get('exists', 'Unknown')}{Colors.END}")
        
        print(f"{Colors.CYAN}═" * 50 + Colors.END)

    # ==================== MAIN MENU ====================

    def main_menu(self):
        """Display main menu"""
        print(f"\n{Colors.BOLD}{Colors.CYAN}=== MAIN MENU ==={Colors.END}")
        print(f"{Colors.GREEN}[1]{Colors.END} Roblox OSINT (Real API)")
        print(f"{Colors.GREEN}[2]{Colors.END} Instagram OSINT (Web Scraping)")
        print(f"{Colors.GREEN}[3]{Colors.END} Universal Platform Search")
        print(f"{Colors.GREEN}[4]{Colors.END} Quick All-in-One Search")
        print(f"{Colors.GREEN}[0]{Colors.END} Exit")
        
        choice = input(f"\n{Colors.YELLOW}Select option: {Colors.END}")
        return choice

    def quick_search(self, username):
        """Perform quick search across all platforms"""
        print(f"\n{Colors.CYAN}[🚀] QUICK SEARCH INITIATED FOR: {username}{Colors.END}")
        
        results = {}
        
        # Roblox search
        print(f"{Colors.YELLOW}[1/3] Searching Roblox...{Colors.END}")
        results['Roblox'] = self.roblox_osint(username)
        
        # Instagram search
        print(f"{Colors.YELLOW}[2/3] Searching Instagram...{Colors.END}")
        results['Instagram'] = self.instagram_osint(username)
        
        # Universal search
        print(f"{Colors.YELLOW}[3/3] Searching other platforms...{Colors.END}")
        results['Universal'] = self.universal_search(username)
        
        return results

    def display_quick_results(self, results):
        """Display quick search results"""
        print(f"\n{Colors.GREEN}{Colors.BOLD}🚀 QUICK SEARCH RESULTS{Colors.END}")
        print(f"{Colors.CYAN}═" * 60 + Colors.END)
        
        if results.get('Roblox'):
            self.display_roblox_results(results['Roblox'])
        
        if results.get('Instagram'):
            self.display_instagram_results(results['Instagram'])
        
        if results.get('Universal'):
            self.display_universal_results(results['Universal'])

def main():
    osint = UniversalOSINT()
    osint.banner()
    
    # Legal disclaimer
    print(f"{Colors.RED}{Colors.BOLD}")
    print("⚠️  IMPORTANT LEGAL DISCLAIMER:")
    print("⚠️  This tool is for EDUCATIONAL and SECURITY RESEARCH purposes only!")
    print("⚠️  Only use on accounts you own or have explicit permission to test!")
    print("⚠️  Respect all platform Terms of Service and rate limits!")
    print("⚠️  The developer is NOT responsible for misuse!")
    print(f"{Colors.END}")
    
    input(f"{Colors.YELLOW}Press Enter to continue...{Colors.END}")
    
    while True:
        choice = osint.main_menu()
        
        if choice == "1":
            username = input(f"{Colors.YELLOW}Enter Roblox username: {Colors.END}")
            results = osint.roblox_osint(username)
            osint.display_roblox_results(results)
            
        elif choice == "2":
            username = input(f"{Colors.Yellow}Enter Instagram username: {Colors.END}")
            results = osint.instagram_osint(username)
            osint.display_instagram_results(results)
            
        elif choice == "3":
            username = input(f"{Colors.YELLOW}Enter username for universal search: {Colors.END}")
            results = osint.universal_search(username)
            osint.display_universal_results(results)
            
        elif choice == "4":
            username = input(f"{Colors.YELLOW}Enter username for quick search: {Colors.END}")
            results = osint.quick_search(username)
            osint.display_quick_results(results)
            
        elif choice == "0":
            print(f"\n{Colors.GREEN}Thank you for using Universal OSINT Tool!{Colors.END}")
            break
            
        else:
            print(f"{Colors.RED}Invalid option!{Colors.END}")
        
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}Program interrupted by user.{Colors.END}")
    except Exception as e:
        print(f"{Colors.RED}Critical error: {e}{Colors.END}")
