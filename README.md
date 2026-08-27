<img width="2594" height="1093" alt="Captura de tela 2026-08-27 185003" src="https://github.com/user-attachments/assets/c32b005d-6edd-4b40-b6c6-90cad4936921" />
# THEME BY DRAVOK ANONYMOUS40443

## TemaByDravok

Custom hacker-style Python terminal tool inspired by Mr. Robot & Fsociety. Features live fastfetch system specs, ASCII art, dynamic color themes, and interactive prompts. Control is an illusion. Are you 1 or 0? 🚀💻

---

## Overview

TemaByDravok é um tema de terminal interativo personalizado e ferramenta de resumo de sistema projetada para o Windows PowerShell. Ele exibe métricas de computador em tempo real (OS, CPU, memória, discos, IP) dentro de uma interface estilizada com tema hacker, cores ANSI personalizáveis, matrizes de arte ASCII e frases cinematográficas aleatórias.

---

## Files in this Repository

* **`terminal.py`**: O script principal do motor que lida com a análise do sistema (estilo fastfetch), temas de cores interativos, telas de carregamento com efeito glitch e prompts de autenticação de segurança.
* **`installer.py`**: Um script de instalação automatizado com um assistente CLI interativo que copia o tema para o diretório local do usuário e o vincula diretamente ao seu perfil do PowerShell (`$PROFILE`) para rodar toda vez que você abrir uma nova aba.
* **`installer.spec`**: Arquivo de configuração usado para compilar os scripts Python em binários autônomos via PyInstaller.

---

## How to Use

### Prerequisites

* Windows 11 / Windows 10
* Python 3.x instalado e adicionado ao PATH do sistema.

### Installation Steps

1. Clone ou baixe este repositório para sua máquina local:
   ```powershell
   git clone https://github.com/Dravok40443/temabydravok.git
   cd temabydravok

   Execute o script de instalação automatizado:
    PowerShell

    python installer.py

    Siga os prompts na tela (y/n) para aplicar o tema ao seu ambiente do PowerShell.

    Abra uma nova aba do PowerShell ou Windows Terminal para ver o tema em ação.

### Como vincular ao sistema manualmente (Auto-Start)

Se você preferir configurar manualmente para iniciar toda vez que abrir o terminal usando o seu caminho exato:

##    Abra o seu Perfil do PowerShell
    Execute o seguinte comando no terminal para abrir o arquivo de perfil no Bloco de Notas:
    PowerShell

  #  notepad $PROFILE

    (Se o Bloco de Notas perguntar se deseja criar um novo arquivo porque ele não existe, clique em Sim).

 ##   Adicione o Comando de Execução
    Cole exatamente este bloco de código no final do arquivo:
    PowerShell

  #  # --- BYDRAVOK THEME START ---
    python "C:\Users\User\temabydravok\terminal.py"
 #   # --- BYDRAVOK THEME END ---

    Salve e Feche

        Salve o arquivo no Bloco de Notas (Ctrl + S) e feche-o.

        Abra uma nova aba do terminal e o tema vai iniciar sozinho!
