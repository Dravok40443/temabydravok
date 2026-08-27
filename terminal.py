import os
import time
import sys
import random
import platform
import socket
import subprocess

# Previne que o script rode mais de uma vez na mesma sessão do terminal
if os.environ.get("TEMABYDRAVOK_LOADED") == "1":
    sys.exit(0)
os.environ["TEMABYDRAVOK_LOADED"] = "1"

# ==========================================
# 🎨 ÁREA DE PERSONALIZAÇÃO (SUAS ARTES E FRASES)
# ==========================================

ASCII_SIDE_ART = [
    r"""⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄ ⣀⣠⣤⣴⡶⠶⠾⠿⠛⠛⠛⠛⠿⠿⠶⢶⣦⣤⣄⣀
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⣤⡶⠟⠛⠉⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠉⠛⠻⢶⣤⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⣴⠾⠋⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠙⠷⣦⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⠋⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠙⢷⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⣠⡾⠋⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢷⣄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⣀⡾⠏⠄⠄⠄⠄⢀⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⡀⠄⠄⠄⠄⠹⢷⣀⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⢀⣼⠏⠄⠄⠄⡀⣰⣾⡟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠻⣷⣦⢀⠄⠄⠄⠹⣷⡀⠄⠄⠄⠄
⠄⠄⠄⠄⡾⠃⠄⢀⣴⠋⣴⣿⢋⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡙⣿⣦⠙⣦⡀⠄⠘⢷⡄⠄⠄⠄
⠄⠄⠄⣼⠁⠄⢀⣿⡏⢰⠟⢡⡎⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⡠⣤⣀⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢱⣌⠻⡇⢹⣿⡀⠄⠈⢧⠄⠄⠄
⠄⠄⣼⠏⣠⡎⢸⣿⢣⣥⡾⠏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠐⠿⠄⠈⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢷⣬⣜⣿⡇⢱⣄⠸⣧⠄⠄
⠄⣸⡟⠄⣿⡇⢸⣷⡿⢋⡔⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡼⠛⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢢⡙⢿⣾⡇⢸⣿⡀⢻⣇⠄
⢀⣿⠁⠄⣿⣧⠸⢋⣴⡿⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢿⣦⡙⠇⣸⣿⡇⠈⣿⡀
⢸⡏⠄⡄⣿⡿⣰⣿⡿⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢿⡿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢿⣿⣆⢻⣿⢣⠄⢹⡇
⣾⡇⢠⣧⠹⣧⡿⠋⣰⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⠄⠠⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣦⠙⢿⣼⠏⢸⡄⢸⣿
⣿⠄⠘⣿⡀⢻⢁⣼⡟⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣴⠄⠛⢿⡿⠛⠄⣲⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⣧⡈⡿⢀⣾⠃⠄⣿
⣿⠄⠄⢿⣷⠄⣾⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⣀⣤⣤⣴⣶⣿⡏⠄⠠⢻⡟⠄⠄⢹⣿⣶⣦⣤⣤⣀⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⣿⣷⠄⣾⡿⠄⠄⣿
⢿⡇⢰⠘⣿⡇⣿⡏⢸⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⣼⣧⠄⠄⢈⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⢀⡇⢹⣿⢸⣿⠇⡆⢸⡿
⢸⣇⠈⣷⠈⢻⣿⠄⣼⣇⠄⠄⠄⠄⠄⠄⠄⠄⢀⣿⣿⣿⣿⣿⣿⣿⣧⠄⠄⣿⣿⠄⠄⣼⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⣸⣧⠄⣿⡟⠁⣼⠁⣸⡇
⠈⣿⡀⠹⣷⣄⠙⠄⣿⣿⢀⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣆⠄⣿⣿⠄⣰⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⡀⣿⣿⠄⠋⣠⣾⡏⢀⣿⠁
⠄⢹⣧⠄⠻⣿⣷⡄⣿⣿⠄⣇⠄⠄⠄⠄⠄⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠄⠄⠄⠄⠄⠄⣠⠄⣿⣿⢠⣾⣿⠟⠄⣼⡏⠄
⠄⠄⢻⣆⠡⣈⠻⠿⣞⣿⡄⢸⣆⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⣰⣿⢠⣿⣳⠿⠟⣁⠌⢰⡿⠄⠄
⠄⠄⠄⢻⡀⠹⣷⣦⣀⠙⠳⣸⣿⣇⢀⡀⠄⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⢀⡀⣸⣿⡏⠞⠋⣀⣴⣾⠏⢀⡞⠄⠄⠄
⠄⠄⠄⠄⢷⡄⠈⠻⢿⣿⣷⣆⡻⣿⡄⢻⣦⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣴⡟⢠⣿⢟⣠⣾⣿⡿⠟⠁⢠⡾⠃⠄⠄⠄
⠄⠄⠄⠄⠈⢿⣆⠄⠄⣉⠛⠿⢿⣮⣿⣄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣠⣿⣵⡿⠿⠛⣉⠄⠄⣰⡿⠁⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠙⢷⣄⠈⠓⢦⣤⣤⣤⣭⣥⣭⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣭⣤⣭⣤⣤⣤⡴⠚⠁⣠⡾⠋⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠙⢷⣄⡀⠈⢉⠛⠛⠛⠛⠛⠉⣁⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣈⠉⠙⠛⠛⠛⠛⡉⠁⠄⣠⡾⠋⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢳⣄⡀⠙⠳⢶⣶⣾⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣷⣶⡶⠞⠋⢀⣠⡾⠋⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⠻⢶⣄⡀⠄⠄⠄⠄⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⢀⣠⣶⠟⠋⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠉⠓⠶⣦⣤⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣤⣴⡶⠚⠉⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠙⠛⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠟⠛⠋⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
    """,
    r"""
    [ByDravok / ANONYMOUS40443]
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢻⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⠀⠙⠻⣿⣿⣿⣿⣿⡃⠀⠀⢀⣴⣶⣿⣷⡦⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣷⣦⣤⣾⣿⣿⣿⡿⠃⣠⣴⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠈⠉⠻⣿⣿⣿⣿⣇⣼⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣄⣀⠀⠀⠀⣀⣠⣴⣶⡄⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⣾⣿⣿⣷⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠘⠻⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⡛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢶⣾⣿⣿⣏⠛⠿⣿⣿⡿⠋⢉⣿⣿⣿⣿⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠘⣆⠀⠈⠛⠿⠿⠿⠃⠀⠀⠀⠀⠀⠙⠿⠛⠛⠁⠀⢠⡿⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠘⣧⠀⢀⣀⣀⣀⠀⠀⠸⠿⠆⠀⣀⣀⣠⣤⠀⢠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠈⢧⡀⢉⡛⠿⠿⠿⠶⠶⠾⠿⠿⠟⠋⠁⢠⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⣾⣿⣿⣷⣄⠀⠀⠀⢠⣤⣶⡆⣠⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⠿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠹⣿⣿⣿⣿⠀⠀⠀⢸⣿⣿⣷⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛
⡿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠈⢿⣿⣿⡄⠀⠀⢸⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀       ⠙⠻⠇⠀⠀⠘⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
]

FRASES = [
    "“YOU ARE 1 OR 0?”",
    "“Nao esquece da vpn kkkkkk se nao os pulisa te pega ”",
    "“Control is ilusion Just a Tech. ”",
    "“Um exército dá tiros para a guerra começar; um hacker aperta enter.”",
    "“Anonymous40443 & ByDravok: Elite protocols engaged.”"
]

CORES = {
    "1": "\033[91m",  # Red
    "2": "\033[92m",  # Green
    "3": "\033[93m",  # Yellow
    "4": "\033[95m",  # Purple
    "5": "\033[38;5;208m", # Orange
    "6": "\033[96m",  # Blue
    "7": "\033[97m"   # White
}
RESET = "\033[0m"
AZUL_TEXTO = "\033[96m"

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def efeito_digitacao(texto, cor=RESET, atraso=0.02):
    for char in texto:
        sys.stdout.write(cor + char + RESET)
        sys.stdout.flush()
        time.sleep(atraso)
    print()

def autenticacao_inicial():
    limpar_tela()
    print("\033[96m" + "="*50 + "\033[0m")
    efeito_digitacao("YOU ARE 1 OR 0?", cor="\033[91m", atraso=0.04)
    print("\033[96m" + "="*50 + "\033[0m")
    
    while True:
        sys.stdout.write("\033[93m[>] Enter value (1 or 0): \033[0m")
        sys.stdout.flush()
        resposta = sys.stdin.readline().strip()
        if resposta in ["1", "0"]:
            efeito_digitacao("\n[✓] Access Granted. Decrypting environment...", cor="\033[92m", atraso=0.02)
            time.sleep(0.8)
            break
        else:
            print("\033[91m[X] Invalid choice. You must be 1 or 0.\033[0m")

def tela_glitch_loading(cor_escolhida):
    limpar_tela()
    passos = [
        "[!] Initializing Fsociety Core...",
        "[!] Aligning system layout matrix...",
        "[✓] SYSTEM MATRIX LOADED SUCCESSFULLY."
    ]
    glitch_chars = "!@#$%^&*()_+-=[]{}|;:,.<>/?\\~`01"
    
    for passo in passos:
        for _ in range(2):
            falsidade = "".join(random.choice(glitch_chars) for _ in range(len(passo)))
            sys.stdout.write(f"\r{cor_escolhida}{falsidade}{RESET}")
            sys.stdout.flush()
            time.sleep(0.02)
        sys.stdout.write(f"\r{cor_escolhida}{passo}{RESET}\n")
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(0.3)

def menu_cores(cor_digitacao):
    limpar_tela()
    efeito_digitacao("====================================================", cor=cor_digitacao, atraso=0.005)
    efeito_digitacao("        SELECT YOUR TERMINAL COLOR THEME        ", cor="\033[93m", atraso=0.005)
    efeito_digitacao("====================================================", cor=cor_digitacao, atraso=0.005)
    
    opcoes = [
        " [1] Red",
        " [2] Green",
        " [3] Yellow",
        " [4] Purple",
        " [5] Orange",
        " [6] Blue",
        " [7] White"
    ]
    for opt in opcoes:
        efeito_digitacao(opt, cor=cor_digitacao, atraso=0.005)
        
    efeito_digitacao("====================================================", cor=cor_digitacao, atraso=0.005)
    
    sys.stdout.write(cor_digitacao + "Select option (1-7): " + RESET)
    sys.stdout.flush()
    escolha = sys.stdin.readline().strip()
    return CORES.get(escolha, "\033[92m")

def obter_infos_reais():
    try:
        usuario = os.getlogin()
    except:
        usuario = "User"
        
    hostname = socket.gethostname()
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_local = s.getsockname()[0] + "/24"
        s.close()
    except:
        ip_local = "192.168.0.4/24"

    os_versao = f"Windows 11 Pro {platform.release()} x86_64"
    kernel = f"WIN32_NT {platform.version()}"
    
    try:
        mem_info = subprocess.check_output("powershell -Command \"Get-CimInstance Win32_OperatingSystem | Select-Object FreePhysicalMemory,TotalVisibleMemorySize\"", shell=True).decode()
        linhas_mem = [l.strip() for l in mem_info.split('\n') if l.strip() and not l.startswith('-') and not l.startswith('Free')]
        if linhas_mem:
            partes = linhas_mem[0].split()
            livre_kb = int(partes[0])
            total_kb = int(partes[1])
            total_gb = total_kb / (1024 * 1024)
            livre_gb = livre_kb / (1024 * 1024)
            uso_gb = total_gb - livre_gb
            porcentagem = int((uso_gb / total_gb) * 100)
            memoria_str = f"Memory: {uso_gb:.2f} GiB / {total_gb:.2f} GiB ({porcentagem}%)"
        else:
            memoria_str = "Memory: 7.52 GiB / 15.15 GiB (50%)"
    except:
        memoria_str = "Memory: 7.52 GiB / 15.15 GiB (50%)"

    discos_str = []
    try:
        import shutil
        for letra in ['C', 'D', 'E', 'F']:
            caminho = f"{letra}:\\"
            if os.path.exists(caminho):
                uso = shutil.disk_usage(caminho)
                total_g = uso.total / (1024**3)
                livre_g = uso.free / (1024**3)
                usado_g = total_g - livre_g
                perc_d = int((usado_g / total_g) * 100)
                discos_str.append(f"Disk ({letra}:\\): {usado_g:.2f} GiB / {total_g:.2f} GiB ({perc_d}%) - NTFS")
    except:
        discos_str = ["Disk (C:\\): 381.13 GiB / 475.89 GiB (80%) - NTFS"]

    if not discos_str:
        discos_str = ["Disk (C:\\): 381.13 GiB / 475.89 GiB (80%) - NTFS"]

    linhas_dados = [
        f"{usuario}@{hostname}",
        f"--------------------",
        f"OS: {os_versao}",
        f"Host: Custom Rig",
        f"Kernel: {kernel}",
        f"Uptime: Active",
        f"Packages: 17 (choco)",
        f"Shell: Windows PowerShell {platform.python_version()}",
        f"Display: Primary Display",
        f"WM: Desktop Window Manager",
        f"WM Theme: Custom Dark",
        f"Theme: ByDravok x anonymous40443",
        f"Icons: Recycle Bin",
        f"Font: Segoe UI (12pt)",
        f"Cursor: Windows Default",
        f"Terminal: Windows Terminal",
        f"Terminal Font: Cascadia Mono (12pt)",
        f"CPU: {platform.processor() or 'AMD Ryzen / Intel Core'}",
        f"GPU: Integrated Graphics",
        memoria_str,
    ]
    
    for d in discos_str:
        linhas_dados.append(d)
        
    linhas_dados.append(f"Local IP (Ethernet): {ip_local}")
    linhas_dados.append(f"Locale: pt-BR")

    return linhas_dados

def exibir_fastfetch_gigante(cor_escolhida):
    limpar_tela()
    linhas_dados = obter_infos_reais()
    
    arte = random.choice(ASCII_SIDE_ART).strip("\n").split("\n")
    
    max_linhas = max(len(arte), len(linhas_dados))
    for i in range(max_linhas):
        parte_arte = arte[i] if i < len(arte) else ""
        parte_dado = linhas_dados[i] if i < len(linhas_dados) else ""
        print(f"{cor_escolhida}{parte_arte:<38}{RESET}    {AZUL_TEXTO}{parte_dado}{RESET}")
    
    print("\n" + cor_escolhida + "="*75 + RESET)

def main():
    try:
        autenticacao_inicial()
        
        cor_menu_inicial = "\033[92m" 
        cor_atual = menu_cores(cor_menu_inicial)
        
        tela_glitch_loading(cor_atual)
        exibir_fastfetch_gigante(cor_atual)
        
        frase_escolhida = random.choice(FRASES)
        print(cor_atual + "[Thought of the Day]:" + RESET)
        efeito_digitacao(frase_escolhida, cor=cor_atual, atraso=0.02)
        print("\n" + cor_atual + "="*75 + RESET + "\n")
    except KeyboardInterrupt:
        print("\n\n\033[91m[!] Execution aborted by user.\033[0m")
        sys.exit(0)

if __name__ == "__main__":
    main()