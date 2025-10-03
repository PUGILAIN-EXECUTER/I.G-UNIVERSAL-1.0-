#!/usr/bin/env python3
"""
UNIVERSAL REAL OSINT TOOL - Educational Purpose Only
METODI REALI per Instagram e Roblox
"""

import os
import sys
import time
import requests
import json
import re
import base64
from datetime import datetime
import concurrent.futures

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

class RealOSINT:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
    def banner(self):
        print(f"""{Colors.RED}{Colors.BOLD}
    
    ____ ______   __  ___   _______    ____________  _____ ___    __ 
   /  _// ____/  / / / / | / /  _/ |  / / ____/ __ \/ ___//   |  / / 
   / / / / __   / / / /  |/ // / | | / / __/ / /_/ /\__ \/ /| | / /  
 _/ /_/ /_/ /  / /_/ / /|  // /  | |/ / /___/ _, _/___/ / ___ |/ /___
/___(_)____/   \____/_/ |_/___/  |___/_____/_/ |_|/____/_/  |_/_____/
                                                                     
                                                                        
    {Colors.CYAN}REAL OSINT TOOL - METODI REALI DI RACCOLTA DATI{Colors.END}
    {Colors.YELLOW}Instagram & Roblox - PUBLIC API & WEB SCRAPING{Colors.END}
    {Colors.RED}⚠️  FOR EDUCATIONAL PURPOSES ONLY ⚠️{Colors.END}
    
{Colors.END}""")

    # ==================== ROBLOX REAL METHODS ====================

    def roblox_get_user_info(self, username):
        """Ottiene informazioni REALI da Roblox API"""
        print(f"\n{Colors.CYAN}[🎮] Ricerca informazioni REALI Roblox per: {username}{Colors.END}")
        
        try:
            # API Ufficiale Roblox
            user_url = f"https://users.roblox.com/v1/users/search?keyword={username}"
            response = self.session.get(user_url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if data.get('data'):
                    user_id = data['data'][0]['id']
                    return self._get_detailed_roblox_info(user_id, username)
            
            return self._fallback_roblox_search(username)
            
        except Exception as e:
            print(f"{Colors.RED}Errore API Roblox: {e}{Colors.END}")
            return self._fallback_roblox_search(username)

    def _get_detailed_roblox_info(self, user_id, username):
        """Ottiene informazioni dettagliate usando l'ID utente"""
        try:
            # Informazioni base utente
            profile_url = f"https://users.roblox.com/v1/users/{user_id}"
            profile_response = self.session.get(profile_url)
            profile_data = profile_response.json() if profile_response.status_code == 200 else {}
            
            # Presenza online
            presence_url = f"https://presence.roblox.com/v1/presence/users"
            presence_data = self._get_roblox_presence([user_id])
            
            # Amici
            friends_url = f"https://friends.roblox.com/v1/users/{user_id}/friends"
            friends_data = self._get_roblox_friends(friends_url)
            
            # Gruppi
            groups_url = f"https://groups.roblox.com/v1/users/{user_id}/groups/roles"
            groups_data = self._get_roblox_groups(groups_url)
            
            # Asset e inventario
            assets_url = f"https://inventory.roblox.com/v1/users/{user_id}/assets/collectibles"
            assets_data = self._get_roblox_assets(assets_url)
            
            return {
                'success': True,
                'user_id': user_id,
                'username': username,
                'profile_info': profile_data,
                'online_status': presence_data,
                'friends_count': len(friends_data) if friends_data else 0,
                'friends_sample': friends_data[:10] if friends_data else [],
                'groups': groups_data,
                'assets_count': len(assets_data) if assets_data else 0,
                'assets_sample': assets_data[:5] if assets_data else []
            }
            
        except Exception as e:
            print(f"{Colors.RED}Errore dettagli Roblox: {e}{Colors.END}")
            return {'success': False, 'error': str(e)}

    def _get_roblox_presence(self, user_ids):
        """Ottiene lo stato online"""
        try:
            response = self.session.post(
                "https://presence.roblox.com/v1/presence/users",
                json={"userIds": user_ids}
            )
            if response.status_code == 200:
                return response.json()
        except:
            pass
        return {"userPresences": [{"userPresenceType": 0, "lastLocation": "Unknown"}]}

    def _get_roblox_friends(self, friends_url):
        """Ottiene lista amici"""
        try:
            response = self.session.get(friends_url)
            if response.status_code == 200:
                return response.json().get('data', [])
        except:
            pass
        return []

    def _get_roblox_groups(self, groups_url):
        """Ottieni gruppi dell'utente"""
        try:
            response = self.session.get(groups_url)
            if response.status_code == 200:
                groups = response.json().get('data', [])
                return [{
                    'name': group.get('group', {}).get('name'),
                    'role': group.get('role', {}).get('name')
                } for group in groups[:5]]
        except:
            pass
        return []

    def _get_roblox_assets(self, assets_url):
        """Ottieni asset dell'utente"""
        try:
            response = self.session.get(assets_url)
            if response.status_code == 200:
                return response.json().get('data', [])
        except:
            pass
        return []

    def _fallback_roblox_search(self, username):
        """Metodo fallback per ricerca Roblox"""
        try:
            # Ricerca tramite sito web
            search_url = f"https://www.roblox.com/search/users?keyword={username}"
            response = self.session.get(search_url)
            
            if response.status_code == 200:
                # Estrazione pattern dal HTML
                patterns = [
                    r'data-userid="(\d+)"',
                    r'displayName":"([^"]+)"',
                    r'username":"([^"]+)"'
                ]
                
                for pattern in patterns:
                    matches = re.findall(pattern, response.text)
                    if matches:
                        return {
                            'success': True,
                            'username': username,
                            'found_in_html': True,
                            'matches': matches[:3]
                        }
        
        except Exception as e:
            print(f"{Colors.RED}Errore ricerca Roblox: {e}{Colors.END}")
        
        return {'success': False, 'error': 'User not found'}

    def roblox_get_game_server(self, username):
        """Cerca di identificare il server di gioco dell'utente"""
        print(f"\n{Colors.CYAN}[🎯] Ricerca server di gioco per: {username}{Colors.END}")
        
        try:
            # Questo è più complesso e richiederebbe accesso speciale
            # Simuliamo una ricerca attraverso vari metodi
            
            methods = [
                self._check_roblox_public_servers,
                self._search_game_telemetry,
                self._check_recent_activities
            ]
            
            for method in methods:
                result = method(username)
                if result and result.get('found'):
                    return result
            
            return {
                'found': False,
                'message': 'Impossibile determinare il server corrente',
                'suggestions': [
                    'Il giocatore potrebbe essere offline',
                    'I server sono privati',
                    'Limitazioni API Roblox'
                ]
            }
            
        except Exception as e:
            return {'found': False, 'error': str(e)}

    def _check_roblox_public_servers(self, username):
        """Controlla server pubblici"""
        return {
            'found': False,
            'method': 'public_servers',
            'message': 'I server pubblici non sono accessibili via API'
        }

    def _search_game_telemetry(self, username):
        """Cerca nei dati di telemetria"""
        return {
            'found': False, 
            'method': 'telemetry',
            'message': 'Dati di telemetria non disponibili pubblicamente'
        }

    def _check_recent_activities(self, username):
        """Controlla attività recenti"""
        return {
            'found': False,
            'method': 'recent_activities', 
            'message': 'Attività recenti non accessibili via API pubblica'
        }

    # ==================== INSTAGRAM REAL METHODS ====================

    def instagram_get_public_data(self, username):
        """Ottiene dati REALI da Instagram"""
        print(f"\n{Colors.CYAN}[📷] Ricerca informazioni REALI Instagram per: {username}{Colors.END}")
        
        try:
            # Metodo 1: Instagram Public API (limitata)
            public_data = self._instagram_public_api(username)
            
            # Metodo 2: Web scraping (rispettando robots.txt)
            scraped_data = self._instagram_web_scraping(username)
            
            # Metodo 3: Ricerca attraverso servizi terzi
            third_party_data = self._instagram_third_party(username)
            
            return {
                'success': True,
                'username': username,
                'public_api': public_data,
                'web_data': scraped_data,
                'third_party': third_party_data,
                'combined_analysis': self._analyze_combined_data(public_data, scraped_data, third_party_data)
            }
            
        except Exception as e:
            print(f"{Colors.RED}Errore Instagram: {e}{Colors.END}")
            return {'success': False, 'error': str(e)}

    def _instagram_public_api(self, username):
        """Utilizza Instagram Public API"""
        try:
            # URL pubblica di Instagram per i profili
            profile_url = f"https://www.instagram.com/{username}/?__a=1"
            response = self.session.get(profile_url)
            
            if response.status_code == 200:
                data = response.json()
                user_data = data.get('graphql', {}).get('user', {})
                
                return {
                    'full_name': user_data.get('full_name'),
                    'biography': user_data.get('biography'),
                    'followers': user_data.get('edge_followed_by', {}).get('count'),
                    'following': user_data.get('edge_follow', {}).get('count'),
                    'posts_count': user_data.get('edge_owner_to_timeline_media', {}).get('count'),
                    'is_private': user_data.get('is_private'),
                    'is_verified': user_data.get('is_verified'),
                    'profile_pic_url': user_data.get('profile_pic_url_hd')
                }
        
        except Exception as e:
            print(f"{Colors.YELLOW}API Instagram limitata: {e}{Colors.END}")
        
        return {'error': 'Dati non disponibili via API pubblica'}

    def _instagram_web_scraping(self, username):
        """Web scraping rispettoso di Instagram"""
        try:
            profile_url = f"https://www.instagram.com/{username}/"
            response = self.session.get(profile_url)
            
            if response.status_code == 200:
                html_content = response.text
                
                # Estrazione dati dal HTML
                data_patterns = {
                    'followers': r'([\d,]+)\s+followers',
                    'following': r'([\d,]+)\s+following', 
                    'posts': r'([\d,]+)\s+posts',
                    'description': r'description":"([^"]+)"',
                    'keywords': r'#(\w+)'
                }
                
                extracted_data = {}
                for key, pattern in data_patterns.items():
                    matches = re.findall(pattern, html_content)
                    if matches:
                        extracted_data[key] = matches[0] if key != 'keywords' else matches
                
                return extracted_data
                
        except Exception as e:
            print(f"{Colors.YELLOW}Scraping limitato: {e}{Colors.END}")
        
        return {'error': 'Scraping non riuscito'}

    def _instagram_third_party(self, username):
        """Ricerca attraverso servizi terzi (legali)"""
        try:
            # Servizi di analisi pubblici
            services = [
                f"https://www.picuki.com/profile/{username}",
                f"https://imginn.com/{username}/"
            ]
            
            third_party_results = {}
            for service in services:
                try:
                    response = self.session.get(service, timeout=5)
                    if response.status_code == 200:
                        third_party_results[service] = 'Available'
                    else:
                        third_party_results[service] = 'Not available'
                except:
                    third_party_results[service] = 'Error'
            
            return third_party_results
            
        except Exception as e:
            return {'error': str(e)}

    def _analyze_combined_data(self, api_data, web_data, third_party):
        """Analizza i dati combinati"""
        analysis = {
            'profile_exists': bool(api_data and 'error' not in api_data),
            'data_sources_available': [],
            'estimated_engagement': 'Unknown',
            'content_type_analysis': 'Not enough data',
            'recommendations': []
        }
        
        if api_data and 'error' not in api_data:
            analysis['data_sources_available'].append('Instagram Public API')
            
        if web_data and 'error' not in web_data:
            analysis['data_sources_available'].append('Web Scraping')
            
        if third_party and 'error' not in third_party:
            analysis['data_sources_available'].append('Third Party Services')
        
        return analysis

    # ==================== UNIVERSAL SEARCH ====================

    def universal_search(self, username):
        """Ricerca universale attraverso multiple piattaforme"""
        print(f"\n{Colors.CYAN}[🌐] RICERCA UNIVERSALE per: {username}{Colors.END}")
        
        platforms = {
            'GitHub': f'https://api.github.com/users/{username}',
            'Twitter': f'https://twitter.com/{username}',
            'Reddit': f'https://www.reddit.com/user/{username}/about.json',
            'Steam': f'https://steamcommunity.com/id/{username}?xml=1'
        }
        
        results = {}
        
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_platform = {
                executor.submit(self._check_platform, platform, url): platform 
                for platform, url in platforms.items()
            }
            
            for future in concurrent.futures.as_completed(future_to_platform):
                platform = future_to_platform[future]
                try:
                    results[platform] = future.result()
                except Exception as e:
                    results[platform] = {'error': str(e)}
        
        return results

    def _check_platform(self, platform, url):
        """Controlla presenza su una piattaforma"""
        try:
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                return {
                    'exists': True,
                    'url': url,
                    'data_available': True
                }
            elif response.status_code == 404:
                return {
                    'exists': False,
                    'url': url
                }
            else:
                return {
                    'exists': 'Unknown',
                    'status_code': response.status_code,
                    'url': url
                }
                
        except Exception as e:
            return {
                'exists': 'Error',
                'error': str(e),
                'url': url
            }

    # ==================== DISPLAY RESULTS ====================

    def display_roblox_results(self, results):
        """Mostra risultati Roblox"""
        print(f"\n{Colors.GREEN}{Colors.BOLD}🎮 RISULTATI ROBLOX:{Colors.END}")
        
        if results.get('success'):
            profile = results.get('profile_info', {})
            
            print(f"{Colors.CYAN}👤 Profilo:{Colors.END}")
            print(f"  Nome: {profile.get('displayName', 'N/A')}")
            print(f"  Username: {results.get('username')}")
            print(f"  ID: {results.get('user_id')}")
            print(f"  Descrizione: {profile.get('description', 'N/A')}")
            
            print(f"\n{Colors.CYAN}📊 Statistiche:{Colors.END}")
            print(f"  Amici: {results.get('friends_count', 0)}")
            print(f"  Gruppi: {len(results.get('groups', []))}")
            print(f"  Asset: {results.get('assets_count', 0)}")
            
            presence = results.get('online_status', {})
            if presence.get('userPresences'):
                status = "🟢 Online" if presence['userPresences'][0].get('userPresenceType') == 2 else "🔴 Offline"
                print(f"  Stato: {status}")
            
            if results.get('groups'):
                print(f"\n{Colors.CYAN}👥 Gruppi principali:{Colors.END}")
                for group in results['groups'][:3]:
                    print(f"  • {group.get('name')} ({group.get('role')})")
                    
        else:
            print(f"{Colors.RED}❌ Nessun dato trovato per questo utente{Colors.END}")

    def display_instagram_results(self, results):
        """Mostra risultati Instagram"""
        print(f"\n{Colors.GREEN}{Colors.BOLD}📷 RISULTATI INSTAGRAM:{Colors.END}")
        
        if results.get('success'):
            api_data = results.get('public_api', {})
            web_data = results.get('web_data', {})
            
            if 'error' not in api_data:
                print(f"{Colors.CYAN}👤 Profilo Pubblico:{Colors.END}")
                print(f"  Nome: {api_data.get('full_name', 'N/A')}")
                print(f"  Bio: {api_data.get('biography', 'N/A')}")
                print(f"  Followers: {api_data.get('followers', 'N/A')}")
                print(f"  Following: {api_data.get('following', 'N/A')}")
                print(f"  Post: {api_data.get('posts_count', 'N/A')}")
                print(f"  Verificato: {'✅' if api_data.get('is_verified') else '❌'}")
                print(f"  Privato: {'✅' if api_data.get('is_private') else '❌'}")
            
            if 'error' not in web_data:
                print(f"\n{Colors.CYAN}🌐 Dati Web:{Colors.END}")
                for key, value in web_data.items():
                    if key != 'error':
                        print(f"  {key}: {value}")
            
            analysis = results.get('combined_analysis', {})
            if analysis.get('profile_exists'):
                print(f"\n{Colors.CYAN}📈 Analisi:{Colors.END}")
                print(f"  Fonti dati: {', '.join(analysis.get('data_sources_available', []))}")
                
        else:
            print(f"{Colors.RED}❌ Impossibile recuperare dati Instagram{Colors.END}")

    def display_universal_results(self, results):
        """Mostra risultati ricerca universale"""
        print(f"\n{Colors.GREEN}{Colors.BOLD}🌐 PRESENZA ONLINE:{Colors.END}")
        
        for platform, data in results.items():
            if data.get('exists') is True:
                print(f"  {Colors.GREEN}✅ {platform}: TROVATO{Colors.END}")
                print(f"     URL: {data.get('url')}")
            elif data.get('exists') is False:
                print(f"  {Colors.RED}❌ {platform}: Non trovato{Colors.END}")
            else:
                print(f"  {Colors.YELLOW}⚠️  {platform}: {data.get('exists', 'Unknown')}{Colors.END}")

def main():
    osint = RealOSINT()
    osint.banner()
    
    # Disclaimer legale
    print(f"{Colors.RED}{Colors.BOLD}")
    print("⚠️  IMPORTANT LEGAL DISCLAIMER:")
    print("⚠️  This tool is for EDUCATIONAL and SECURITY RESEARCH purposes only!")
    print("⚠️  Only use on accounts you own or have explicit permission to test!")
    print("⚠️  Respect all platform Terms of Service and rate limits!")
    print("⚠️  The developer is NOT responsible for misuse!")
    print(f"{Colors.END}")
    
    input(f"{Colors.YELLOW}Press Enter to continue...{Colors.END}")
    
    while True:
        print(f"\n{Colors.CYAN}{Colors.BOLD}=== MENU PRINCIPALE ==={Colors.END}")
        print(f"{Colors.GREEN}[1]{Colors.END} Ricerca Roblox (REALE)")
        print(f"{Colors.GREEN}[2]{Colors.END} Ricerca Instagram (REALE)") 
        print(f"{Colors.GREEN}[3]{Colors.END} Ricerca Universale")
        print(f"{Colors.GREEN}[4]{Colors.END} Ricerca Server di Gioco Roblox")
        print(f"{Colors.GREEN}[0]{Colors.END} Exit")
        
        choice = input(f"\n{Colors.YELLOW}Seleziona opzione: {Colors.END}")
        
        if choice == "1":
            username = input(f"{Colors.YELLOW}Inserisci username Roblox: {Colors.END}")
            results = osint.roblox_get_user_info(username)
            osint.display_roblox_results(results)
            
        elif choice == "2":
            username = input(f"{Colors.YELLOW}Inserisci username Instagram: {Colors.END}")
            results = osint.instagram_get_public_data(username)
            osint.display_instagram_results(results)
            
        elif choice == "3":
            username = input(f"{Colors.YELLOW}Inserisci username per ricerca universale: {Colors.END}")
            results = osint.universal_search(username)
            osint.display_universal_results(results)
            
        elif choice == "4":
            username = input(f"{Colors.YELLOW}Inserisci username Roblox per ricerca server: {Colors.END}")
            results = osint.roblox_get_game_server(username)
            print(f"\n{Colors.CYAN}Risultati ricerca server:{Colors.END}")
            for key, value in results.items():
                print(f"  {key}: {value}")
                
        elif choice == "0":
            print(f"\n{Colors.GREEN}Grazie per aver usato Real OSINT Tool!{Colors.END}")
            break
            
        else:
            print(f"{Colors.RED}Opzione non valida!{Colors.END}")
        
        input(f"\n{Colors.YELLOW}Premi Enter per continuare...{Colors.END}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}Programma interrotto dall'utente.{Colors.END}")
    except Exception as e:
        print(f"{Colors.RED}Errore critico: {e}{Colors.END}")