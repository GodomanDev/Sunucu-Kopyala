import os
import discord
import asyncio
from colorama import Fore, Style, init
from serverclone import Clone

mytitle = "GODOMAN Cloner"
os.system("title " + mytitle)

init(autoreset=True)

client = discord.Client()
os_name = os.name
if os_name == "nt":
    os.system("cls")
else:
    os.system("clear")
    print(chr(27) + "[2J")

print(f"""{Fore.YELLOW}
⡏⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿
⣿⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⣿
⣿⣧⡀⠀⠀⠀⠀⠙⠿⠿⠿⠻⠿⠿⠟⠿⠛⠉⠀⠀⠀⠀⠀⣸⣿
⣿⣿⣷⣄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿
⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣴⣿⣿⣿⣿
⣿⣿⣿⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⣷⠀⠀⠀⠸⣿⣿⣿⣿
⣿⣿⣿⠃⠀⠀⠈⠉⠀⠀⠤⠄⠀⠀⠀⠉⠁⠀⠀⠀⠀⢿⣿⣿⣿
⣿⣿⣿⢾⣿⣷⠀⠀⠀⠀⡠⠤⢄⠀⠀⠀⠠⣿⣿⣷⠀⢸⣿⣿⣿
⣿⣿⣿⡀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣿⣿⣿
⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿
⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿
{Style.RESET_ALL}""")

token = input(f'{Fore.CYAN}Token girin:{Style.RESET_ALL}')
guild_s = input(f'{Fore.CYAN}Kopyalamak istediğiniz sunucu kimliğini girin:{Style.RESET_ALL}')
guild = input(f'{Fore.CYAN}Kopyalanacak olan sunucunun kimliğini girin:{Style.RESET_ALL}')

@client.event
async def on_ready():
    print(f"{Fore.GREEN}Logged In as: {client.user}{Style.RESET_ALL}")
    print("Cloning Server...")
    guild_from = client.get_guild(int(guild_s))
    guild_to = client.get_guild(int(guild))
    
    if guild_from and guild_to:
        await Clone.guild_edit(guild_to, guild_from)
        await Clone.roles_delete(guild_to)
        await Clone.channels_delete(guild_to)
        await Clone.roles_create(guild_to, guild_from)
        await Clone.categories_create(guild_to, guild_from)
        await Clone.channels_create(guild_to, guild_from)
        print(f"""{Fore.GREEN}
░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██║░░██║
██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██║░░██║
╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██████╔╝
░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═════╝░
{Style.RESET_ALL}""")
    else:
        print(f"{Fore.RED}[ERROR] Invalid guild IDs provided.{Style.RESET_ALL}")
    
    await asyncio.sleep(5)
    await client.close()

client.run(token, bot=False)