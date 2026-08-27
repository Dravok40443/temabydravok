import os
import sys
import subprocess
import time
import random

BANNER_HACKER = r""" ███████████  █████ █████    ██████████   ███████████     █████████   █████   █████    ███████    █████   ████
▒▒███▒▒▒▒▒███▒▒███ ▒▒███    ▒▒███▒▒▒▒███ ▒▒███▒▒▒▒▒███   ███▒▒▒▒▒███ ▒▒███   ▒▒███   ███▒▒▒▒▒███ ▒▒███   ███▒ 
 ▒███    ▒███ ▒▒███ ███      ▒███   ▒▒███ ▒███    ▒███  ▒███    ▒███  ▒███    ▒███  ███     ▒▒███ ▒███  ███   
 ▒██████████   ▒▒█████       ▒███    ▒███ ▒██████████   ▒███████████  ▒███    ▒███ ▒███      ▒███ ▒███████    
 ▒███▒▒▒▒▒███   ▒▒███        ▒███    ▒███ ▒███▒▒▒▒▒███  ▒███▒▒▒▒▒███  ▒▒███   ███  ▒███      ▒███ ▒███▒▒███   
 ▒███    ▒███    ▒███        ▒███    ███  ▒███    ▒███  ▒███    ▒███   ▒▒▒█████▒   ▒▒███     ███  ▒███ ▒▒███  
 ███████████     █████       ██████████   █████   █████ █████   █████    ▒▒███      ▒▒▒███████▒   █████ ▒▒████
▒▒▒▒▒▒▒▒▒▒▒     ▒▒▒▒▒       ▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒   ▒▒▒▒▒ ▒▒▒▒▒   ▒▒▒▒▒      ▒▒▒         ▒▒▒▒▒▒▒    ▒▒▒▒▒   ▒▒▒▒ 
                                                                                                              
                                                                                                              
                                                                                                              
                                                                                                              
                                                                                                              
                                                                                                              
                                                                                                              
                                                                                                              
                                                                                                              
                                                                                                              
                                                                                                              
                                                                                                              
                                                                                                              
                                                                                                                                                                                                                   
"""

FRASES_INSTALACAO = [
    "“Injecting packets into the matrix... watch out for the virtual cops.”",
    "“Control is an illusion. Your terminal now belongs to ByDravok.”",
    "“Compiling elite protocols... Zero and One.”",
    "“Decrypting mainframes... Don't blink.”"
]

def animacao_abertura():
    os.system('cls' if os.name == 'nt' else 'clear')
    linhas = BANNER_HACKER.splitlines()
    # Efeito de revelação em cascata suave e rápida de cima para baixo
    for i in range(1, len(linhas) + 1):
        os.system('cls' if os.name == 'nt' else 'clear')
        trecho = "\n".join(linhas[:i])
        print(f"\033[38;5;196m{trecho}\033[0m")
        time.sleep(0.04)
    time.sleep(0.2)

def efeito_digitacao(texto, cor="\033[92m", atraso=0.015):
    for char in texto:
        sys.stdout.write(cor + char + "\033[0m")
        sys.stdout.flush()
        time.sleep(atraso)
    print()

def main():
    animacao_abertura()
    
    # Exibe o banner completo em vermelho sangue
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\033[38;5;196m{BANNER_HACKER}\033[0m")
    
    efeito_digitacao(random.choice(FRASES_INSTALACAO), cor="\033[93m", atraso=0.02)
    print("\033[96m" + "="*70 + "\033[0m\n")
    
    resposta = input("\033[95m[?] Do you want to apply the ByDravok theme to your terminal? (y/n): \033[0m").strip().lower()
    if resposta not in ['y', 'yes', 's', 'sim']:
        print("\033[91m[X] Operation aborted. Exiting...\033[0m")
        time.sleep(1)
        sys.exit()

    print("\n\033[96m[!] Initializing kernel handshake...\033[0m")
    time.sleep(0.5)
    
    sys.stdout.write("\033[92m[+] Decrypting core modules: [")
    sys.stdout.flush()
    for _ in range(20):
        time.sleep(0.05)
        sys.stdout.write("█")
        sys.stdout.flush()
    print("] 100%\033[0m\n")
    
    print("\033[92m[✓] Root privileges confirmed.\033[0m")
    efeito_digitacao("Injecting initialization profile into PowerShell...", cor="\033[38;5;208m", atraso=0.02)
    time.sleep(0.5)

    user_home = os.path.expanduser("~")
    destino_script = os.path.join(user_home, ".bydravok_theme.py")

    try:
        profile_path = subprocess.check_output(
            ["powershell", "-Command", "echo $PROFILE"], 
            text=True
        ).strip()
    except:
        profile_path = os.path.join(user_home, "Documents", "PowerShell", "Microsoft.PowerShell_profile.ps1")

    profile_dir = os.path.dirname(profile_path)
    if not os.path.exists(profile_dir):
        os.makedirs(profile_dir, exist_ok=True)

    comando_injetar = f'\n# --- BYDRAVOK THEME START ---\npython "{destino_script}"\n# --- BYDRAVOK THEME END ---\n'

    conteudo_atual = ""
    if os.path.exists(profile_path):
        with open(profile_path, "r", encoding="utf-8", errors="ignore") as f:
            conteudo_atual = f.read()

    if "BYDRAVOK THEME" not in conteudo_atual:
        with open(profile_path, "a", encoding="utf-8") as f:
            f.write(comando_injetar)

    print("\n\033[92m[✓] THEME SUCCESSFULLY DEPLOYED TO SYSTEM MATRIX!\033[0m")
    print("\033[96m[!] Open a new terminal tab to test it.\033[0m\n")
    
    input("\033[93mPress ENTER to close the installer...\033[0m")

if __name__ == "__main__":
    main()