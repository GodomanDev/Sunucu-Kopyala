import discord
from colorama import Fore, Style, init

init(autoreset=True)

def print_add(message):
    print(f'{Fore.GREEN}[+]{Style.RESET_ALL} {message}')

def print_delete(message):
    print(f'{Fore.RED}[-]{Style.RESET_ALL} {message}')

def print_warning(message):
    print(f'{Fore.YELLOW}[Uyarı]{Style.RESET_ALL} {message}')

def print_error(message):
    print(f'{Fore.RED}[HATA]{Style.RESET_ALL} {message}')

class Clone:
    @staticmethod
    async def roles_delete(guild_to: discord.Guild):
        for role in guild_to.roles:
            if role.name != "@everyone":
                try:
                    await role.delete()
                    print_delete(f"Rol Silindi: {role.name}")
                except discord.Forbidden:
                    print_error(f"Rol Silinemedi: {role.name}")
                except discord.HTTPException:
                    print_error(f"Rol silinemiyor: {role.name}")

    @staticmethod
    async def roles_create(guild_to: discord.Guild, guild_from: discord.Guild):
        roles = [role for role in guild_from.roles if role.name != "@everyone"]
        for role in reversed(roles):
            try:
                await guild_to.create_role(
                    name=role.name,
                    permissions=role.permissions,
                    colour=role.colour,
                    hoist=role.hoist,
                    mentionable=role.mentionable
                )
                print_add(f"Rol Oluşturuldu {role.name}")
            except discord.Forbidden:
                print_error(f"Rol Oluşturulurken Hata Oluştu: {role.name}")
            except discord.HTTPException:
                print_error(f"Rol Oluşturulamadı: {role.name}")

    @staticmethod
    async def channels_delete(guild_to: discord.Guild):
        for channel in guild_to.channels:
            try:
                await channel.delete()
                print_delete(f"Silinen Kanal: {channel.name}")
            except discord.Forbidden:
                print_error(f"Kanal Silinirken Hata: {channel.name}")
            except discord.HTTPException:
                print_error(f"Kanal Silinemiyor: {channel.name}")

    @staticmethod
    async def categories_create(guild_to: discord.Guild, guild_from: discord.Guild):
        for category in guild_from.categories:
            try:
                overwrites_to = {discord.utils.get(guild_to.roles, name=key.name): value for key, value in category.overwrites.items()}
                new_category = await guild_to.create_category(name=category.name, overwrites=overwrites_to)
                await new_category.edit(position=category.position)
                print_add(f"Oluşturulan Kategori: {category.name}")
            except discord.Forbidden:
                print_error(f"Kategori Oluşturulurken Hata: {category.name}")
            except discord.HTTPException:
                print_error(f"Kategori Oluşturulamadı: {category.name}")

    @staticmethod
    async def channels_create(guild_to: discord.Guild, guild_from: discord.Guild):
        text_channels = sorted(guild_from.text_channels, key=lambda x: x.position)
        voice_channels = sorted(guild_from.voice_channels, key=lambda x: x.position)

        for channel in text_channels + voice_channels:
            try:
                overwrites_to = {discord.utils.get(guild_to.roles, name=key.name): value for key, value in channel.overwrites.items()}
                
                if isinstance(channel, discord.TextChannel):
                    new_channel = await guild_to.create_text_channel(
                        name=channel.name,
                        overwrites=overwrites_to,
                        position=channel.position,
                        topic=channel.topic,
                        slowmode_delay=channel.slowmode_delay,
                        nsfw=channel.nsfw
                    )
                else:
                    new_channel = await guild_to.create_voice_channel(
                        name=channel.name,
                        overwrites=overwrites_to,
                        position=channel.position,
                        bitrate=channel.bitrate,
                        user_limit=channel.user_limit
                    )
                
                category = discord.utils.get(guild_to.categories, name=channel.category.name) if channel.category else None
                if category:
                    await new_channel.edit(category=category)
                
                print_add(f"Oluşturulan Kanal: {channel.name}")
            except discord.Forbidden:
                print_error(f"Kanal Oluşturulurken Hata: {channel.name}")
            except discord.HTTPException:
                print_error(f"Kanal Oluşturulamadı: {channel.name}")

    @staticmethod
    async def guild_edit(guild_to: discord.Guild, guild_from: discord.Guild):
        try:
            icon_image = await guild_from.icon_url.read() if guild_from.icon else None
            await guild_to.edit(name=guild_from.name, icon=icon_image)
            print_add(f"Sunucu Logosunu Değişti: {guild_to.name}")
        except discord.Forbidden:
            print_error(f"Sunucu Logosunu Değiştirilirken Hata: {guild_to.name}")
        except discord.HTTPException:
            print_error(f"Sunucu Logosunu Değiştirilemiyor: {guild_to.name}")
        except AttributeError:
            print_warning(f"Sunucu {guild_from.name} Logosunu yok.")