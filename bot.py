import datetime
import asyncio
from asyncio import sleep
import hashlib
from datetime import timedelta
import io
import json
import sqlite3
import os
import textwrap
import subprocess
from datetime import date
from discord import SelectOption, SelectMenu
import discord
import random
import asyncio
import requests
from discord.utils import get
from discord import automod
import json
from discord.ui import TextInput, View, Select, Button, Item, Modal
from progress import bar as pb
import time
from art import tprint
from discord.ext import commands
from vk_api.utils import get_random_id
from discord import slash_command
import re
intents = discord.Intents.default()
intents.voice_states = True
intents.typing = True
bot = commands.Bot(command_prefix='r!', intents=discord.Intents.all())
bot.remove_command("help")
staff_hightmine = [ROLE_IDS]
all_staff = [MEMBER_IDS]


def get_time_string(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    time_parts = []
    if days > 0:
        time_parts.append(f"{days} {'день' if days == 1 else 'дня' if 2 <= days <= 4 else 'дней'}")
    if hours > 0:
        time_parts.append(f"{hours} {'час' if hours == 1 else 'часа' if 2 <= hours <= 4 else 'часов'}")
    if minutes > 0:
        time_parts.append(f"{minutes} {'минута' if minutes == 1 else 'минуты' if 2 <= minutes <= 4 else 'минут'}")
    if seconds > 0:
        time_parts.append(f"{seconds} {'секунда' if seconds == 1 else 'секунды' if 2 <= seconds <= 4 else 'секунд'}")

    return ", ".join(time_parts)


@bot.slash_command(name="mute", description="Отправить пользователя в тайм-аут",
                   default_member_permissions=discord.Permissions(mute_members=True))
async def mute(ctx, пользователь: discord.Option(discord.Member, "Пользователь который будет замьючен"),
               время: discord.Option(str, "Время действия мута(10мин, 15ч, 1д, 2ч15мин и т.д. Бессрочно если не указано)"),
               причина: discord.Option(str, "Причина мута"), ):
    if ctx.author.guild_permissions.mute_members:
        time_pattern = re.compile(r'^(\d+)([мчд])(ин)?$|(\d+)([чмд])(\d+)([мчд])(ин)?$')
        match = time_pattern.match(время)
        if not match:
            await ctx.respond("Неверный формат времени. Используйте формат '10мин', '15ч', '1д', '2ч15мин' и т.д.\n")
            return
        if match.group(1) and match.group(2):
            duration, unit = int(match.group(1)), match.group(2)
            seconds = duration
            if unit == 'м':
                seconds *= 60
            elif unit == 'ч':
                seconds *= 3600
            elif unit == 'д':
                seconds *= 86400
        elif match.group(3) and match.group(4) and match.group(5) and match.group(6):
            hours, _, minutes, _ = int(match.group(3)), match.group(4), int(match.group(5)), match.group(6)
            seconds = hours * 3600 + minutes * 60
        await пользователь.timeout(until=datetime.datetime.utcnow() + timedelta(seconds=seconds))

        time_string = get_time_string(seconds)
        embed = discord.Embed(title="",
                              description=f":white_check_mark: Участник {пользователь.name} замьючен! :speak_no_evil:",
                              color=0x2ECC71)
        embed.add_field(name="Модератор", value=ctx.author.mention, inline=True)
        embed.add_field(name="Время мута", value=time_string, inline=True)
        embed.add_field(name="Причина", value=причина, inline=False)
        await ctx.respond(embed=embed)
    else:
        await ctx.send('У вас нет прав на использование этой команды!')


@bot.slash_command(name="unmute", description="Размутить пользователя",
                   default_member_permissions=discord.Permissions(mute_members=True))
async def _unmute(ctx, пользователь: discord.Option(discord.Member, "Пользователь, который будет размьючен")):
    try:
        if ctx.author.guild_permissions.mute_members:
            await пользователь.timeout(until=None)
            embed = discord.Embed(title="",
                                  description=f":white_check_mark: Участник {пользователь.name} размьючен!:speaker:",
                                  color=0x2ECC71)
            embed.add_field(name="Модератор", value=ctx.author.mention, inline=True)
            await ctx.respond(embed=embed)
        else:
            print("")
    except discord.Forbidden:
        await ctx.respond("У меня нет прав чтобы замутить этого пользователя!")


def get_hwid():
    cpu_info = subprocess.check_output("wmic cpu get processorid", shell=True).decode().strip().split("\n")[1]
    hdd_info = (subprocess.check_output("wmic diskdrive get serialnumber", shell=True).decode().strip().split("\n")[1])
    hwide = cpu_info + hdd_info
    hwide = hwide.encode()
    hwide = hashlib.sha256(hwide).hexdigest()
    return hwide


os.system('color a')
os.system('cls')
os.system('title Discord Bot')
token = 'HASH_TOKEN'
hash_in_passw = 'HASH_PASSWORD'
print("\n\n")
tprint("remod3")
btokenn = input(' Введите токен: ')
hash_input_token = my_hash(btokenn)

if hash_input_token == token:
    hwid = get_hwid()
    if hwid == 'HWID':
        os.system('cls')
        time.sleep(random.randint(1, 5))
        print("Login as Administrator")
    else:
        passw = input(" Введите пароль: ")
        hash_password = my_hash(passw)
        if hash_password == hash_in_passw:
            os.system('cls')
            t = random.randint(1, 5)
            time.sleep(t)
            tprint("\n    remod3\n\n")
            bar = pb.IncrementalBar("Loading...  |  ", max=100)
            for i in range(100):
                bar.next()
                time.sleep(random.uniform(0.1, 0.5))
            bar.finish()
            tprint("    Complete!\n\n\n")
            print("    |--------------------------------|")
            print("    |Вход в систему выполнен успешно!|")
            print("    |--------------------------------|\n\n")
        else:
            print("Неверный пароль.")
            exit()
else:
    print("Неверный токен.")
    exit()


@bot.event
async def on_ready():
    print(f"Бот {bot.user} подключен к Discord!")
    await bot.change_presence(activity=discord.Game(name="osu!"))


@bot.slash_command(name='clear', description="Удалить сообщения",
                   default_member_permissions=discord.Permissions(manage_messages=True))
async def _clear(ctx,
                 число: discord.Option(int, description="Сколько нужно удалить сообщений (Макс 100)", min_value=1,
                                       max_value=100),
                 пользователь: discord.Option(discord.User,
                                              description="Удалить сообщения от этого пользователя") = None, ):
    if пользователь is None:
        await ctx.channel.purge(limit=число)
    else:
        messages = []
        async for message in ctx.channel.history(limit=число):
            if message.author == пользователь:
                messages.append(message)
        await ctx.channel.delete_messages(messages)


@bot.slash_command(name="kick", description="Кикнуть пользователя",
                   default_member_permissions=discord.Permissions(kick_members=True))
async def _kick(ctx,
                пользователь: discord.Option(discord.Member, description="Участник сервера, которого нужно кикнуть"),
                причина: discord.Option(str, description="Причина кика") = None):
    if ctx.author.top_role > пользователь.top_role:
        try:
            await пользователь.kick(reason=причина)
            embed = discord.Embed(title="", description=f"Пользователь {пользователь.mention} был кикнут с сервера.",
                                  color=discord.Color.embed_background())
            embed.add_field(name="Модератор", value=ctx.author.mention, inline=True)
            embed.add_field(name="Причина", value=причина)
            await ctx.respond(embed=embed)
        except discord.Forbidden:
            await ctx.respond("У меня нет прав на кикнуть этого пользователя", ephemeral=True)
    else:
        await ctx.respond(f"{ctx.author.mention}, Вы не можете кикнуть пользователя, который выше вас по рангу.",
                          ephemeral=True)


@bot.slash_command(name='rcolor', description="Изменить цвет роли",
                   default_member_permissions=discord.Permissions(manage_roles=True))
async def _change_role_color(ctx, цвет: discord.Option(discord.Color, description="Цветовой код в формате HEX"),
                             *, роль: discord.Option(discord.Role, description="Роль, которой нужно изменить цвет")):
    if роль:
        if ctx.author.top_role >= роль:
            try:
                await роль.edit(color=цвет)
                guild = ctx.guild
                await guild.system_channel.send(
                    f"Цвет роли «{роль.name}» изменен на «{цвет}», автор: {ctx.author.mention}")
            except discord.Forbidden:
                await ctx.respond("У меня нет прав на изменение цвета этой роли", ephemeral=True)
        else:
            await ctx.respond(
                f"{ctx.author.mention}, Вы не можете изменить цвет роли, которая выше Вашей самой высокой роли.",
                ephemeral=True)
    else:
        await ctx.respond(f"Роль с именем «{роль.name}» не найдена", ephemeral=True)


@bot.slash_command(name='pre', description='Изменить приоритет роли',
                   default_member_permissions=discord.Permissions(manage_roles=True))
async def _pre(ctx, позиция: discord.Option(int, description="Позиция, на которую нужно переместить роль"), *,
               роль: discord.Option(discord.Role, description="Роль, которую нужно переместить")):
    if ctx.author.top_role >= роль:
        if not роль:
            await ctx.respond('Роль не найдена', ephemeral=True)
            return
        try:
            await роль.edit(position=позиция)
            await ctx.respond(f'«{роль.name}» перемещана на позицию {позиция}.')
        except discord.Forbidden:
            await ctx.respond('У меня нет прав для изменения приоритета для этой роли', ephemeral=True)
    else:
        await ctx.respond(f"{ctx.author.mention}, Вы не можете переместить роль, которая выше Вашей роли.",
                          ephemeral=True)


@bot.slash_command(name='addrole', description='Выдать роль пользователю',
                   default_member_permissions=discord.Permissions(manage_roles=True))
async def _give_role(ctx,
                     пользователь: discord.Option(discord.Member,
                                                  description="Пользователь, которому нужно выдать роль"),
                     роль: discord.Option(discord.Role, description="Роль, которую нужно выдать")):
    if ctx.author.guild_permissions.manage_roles:
        if ctx.author.top_role >= роль:
            if роль:
                await пользователь.add_roles(роль)
                await ctx.respond(f'Роль «{роль.name}» выдана пользователю: {пользователь.mention}', ephemeral=True)
            else:
                await ctx.respond(f'Роль с именем «{роль.name}» не найдена.', ephemeral=True)
        await ctx.respond(f'{ctx.author.mention}, Вы не можете выдать роль, которая выше вашей роли.', ephemeral=True)


@bot.slash_command(name='removerole', description='Удалить роль у пользователя',
                   default_member_permissions=discord.Permissions(manage_roles=True))
async def _remove_role(ctx,
                       пользователь: discord.Option(discord.Member,
                                                    description="Пользователь, у которого нужно забрать роль"),
                       *, роль: discord.Option(discord.Role, description="Роль, которую нужно забрать")):
    if ctx.author.top_role > роль:
        if пользователь and роль:
            if роль:
                await пользователь.remove_roles(роль)
                await ctx.respond(f'Роль «{роль.name}» удалена для пользователя {пользователь.mention}', ephemeral=True)
            else:
                await ctx.respond("Роль не найдена", ephemeral=True)
        else:
            await ctx.respond("Роль или пользователь не найдены", ephemeral=True)
    else:
        await ctx.respond(f"{ctx.author.mention}, Вы не можете забрать роль, которая выше вашей роли.", ephemeral=True)


@bot.slash_command(name="nick", default_member_permissions=discord.Permissions(manage_nicknames=True))
async def _nick(ctx,
                пользователь: discord.Option(discord.Member, description="Пользователь, которому нужно изменить ник"),
                ник: discord.Option(str, description="Новый ник пользователя")):
    try:
        await пользователь.edit(nick=ник)
        await ctx.respond(f"Пользователю {пользователь.name} изменён ник на: {ник}", ephemeral=True)
    except discord.Forbidden:
        await ctx.respond("У меня нет прав на изменение ника этого пользователя", ephemeral=True)


@bot.slash_command(name='send', description='Отправить сообщение в канал',
                   default_member_permissions=discord.Permissions(administrator=True))
async def _send(ctx, чат_айди: discord.Option(str, description="Айди чата, в которй нужно отправить сообщение"),
                *, сообщение: discord.Option(str, description="Сообщение для отправки")):
    try:
        channel = await bot.fetch_channel(чат_айди)
    except discord.HTTPException:
        await ctx.respond('Неверный ID канала', ephemeral=True)
        return
    try:
        await channel.send(сообщение)
        await ctx.respond("Сообщение отправлено", ephemeral=True)
    except discord.HTTPException as e:
        await ctx.respond(f'Ошибка отправки сообщения: {e}', ephemeral=True)


@bot.slash_command(name='nbot', description='Изменить ник бота',
                   default_member_permissions=discord.Permissions(administrator=True))
async def _nbot(ctx, *, имя: discord.Option(str, description="Новое имя бота")):
    try:
        member = ctx.guild.get_member(bot.user.id)
        await member.edit(nick=имя)
    except discord.Forbidden:
        await ctx.respond("У меня нет прав на изменение ника этого бота", ephemeral=True)


@bot.slash_command(name='uprole', description='Повысить роль пользователя на 1 уровень',
                   default_member_permissions=discord.Permissions(manage_roles=True))
async def _uprole(ctx, пользователь: discord.Option(discord.Member,
                                                    description="Пользователь, которому нужно повысить роль")):
    try:
        if ctx.author.top_role > пользователь.top_role:
            guild = ctx.guild
            roles = [role for role in member.roles if role != guild.default_role]
            highest_role = max(roles, key=lambda x: x.position)
            new_role = discord.utils.get(guild.roles, position=highest_role.position + 1)
            await пользователь.add_roles(new_role)
            await пользователь.remove_roles(highest_role)
            await ctx.respond(
                f'Пользователю {пользователь.mention} ({пользователь.id}) повышен ранг до: {new_role.name} ({new_role.id})')
        else:
            await ctx.respond(f"{ctx.author.mention}, Вы не можете повысить роль которая вышей вашей роли.",
                              ephemeral=True)
    except PermissionError:
        await ctx.respond("У бота недостаточно прав", ephemeral=True)


@bot.slash_command(name='do', description='Понизить роль пользователя на 1 уровень',
                   default_member_permissions=discord.Permissions(manage_roles=True))
async def _do(ctx,
              пользователь: discord.Option(discord.Member, description="Пользователь, которому нужно понизить роль")):
    try:
        if ctx.author.top_role > пользователь.top_role:
            highest_role = member.top_role
            await пользователь.remove_roles(highest_role)
            roles = ctx.guild.roles
            new_role_position = highest_role.position - 1
            new_role = discord.utils.get(roles, position=new_role_position)
            await пользователь.add_roles(new_role)
            await пользователь.remove_roles(highest_role)
            await ctx.respond(
                f'Пользователю {пользователь.mention} ({пользователь.id}) понижен ранг до: {new_role.name} '
                f'({new_role.id})')
        else:
            await ctx.respond(f"{ctx.author.mention}, Вы не можете понизить роль которая выше вашей роли.",
                              ephemeral=True)
    except PermissionError:
        await ctx.respond("Недостаточно прав.", ephemeral=True)


@bot.slash_command(name='rclear', description='Удалить все роли пользователя',
                   default_member_permissions=discord.Permissions(administrator=True))
async def _rclear(ctx, пользователь: discord.Option(discord.Member,
                                                    description="Пользователь, роли которого нужно очистить")):
    if ctx.author.top_role > пользователь.top_role:
        roles = member.roles
        roles.reverse()
        for role in roles:
            if role != ctx.guild.default_role:
                await member.remove_roles(role)
        await ctx.respond(f"Все роли пользователя {member.display_name} удалены")
    else:
        await ctx.respond(f"{ctx.author.mention}, Вы не можете очистить роли этого пользователя.", ephemeral=True)


@bot.slash_command(name='mserver', description='Получить информацию о сервере')
async def _mserver(ctx, ip_address: discord.Option(str, description="IP адрес сервера")):
    url = f"https://api.mcsrvstat.us/2/{ip_address}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    if data.get('online'):
        players_online = data.get('players', {}).get('online', 'Хз')
        server_name = data.get("hostname", "Хз")
        server_version = data.get('version', "Хз")
        software_n = data.get('software', "Хз")
        info_n = ' '.join(data.get('motd', {}).get('clean', ["Хз"]))

        embed = discord.Embed(title=f"Информация о сервере {ip_address}", color=ctx.author.color)
        embed.add_field(name="Игроков онлайн", value=f"{players_online} онлайн", inline=True)
        embed.add_field(name="Имя хоста", value=server_name, inline=True)
        embed.add_field(name="Версия сервера", value=server_version, inline=True)
        embed.add_field(name="ПО сервера", value=software_n, inline=True)
        embed.add_field(name="Описание", value=info_n, inline=True)
        await ctx.respond(embed=embed)

    else:
        await ctx.respond(f"Сервер {ip_address} не отвечает или не найден.")


@bot.slash_command(name="jn", default_member_permissions=discord.Permissions(administrator=True))
async def _jn(ctx):
    author_voice_state = ctx.author.voice
    if author_voice_state:
        voice_channel = author_voice_state.channel
        await voice_channel.connect()
        await ctx.respond(f'Joined voice channel: {voice_channel}', ephemeral=True)
    else:
        await ctx.respond('You are not connected to a voice channel.', ephemeral=True)


@bot.slash_command(name='ping')
async def ping(ctx):
    ping = bot.latency
    await ctx.respond(f"The bot ping is: {round(ping * 1000)}ms!")


@bot.slash_command(name="avatar", description="В аргументе 'сервер' пишите g")
async def _avatar(ctx,
                  пользователь: discord.Option(discord.Member,
                                               description="Пользователь, аватар которого вы хотите получить") = None,
                  guild: discord.Option(str, description="", ) = None):
    if пользователь:
        avatar_url = пользователь.avatar.url
    elif guild == 'g':
        avatar_url = ctx.guild.icon.url
    else:
        avatar_url = 'Аватар не найден.'
    await ctx.respond(avatar_url)


last_used = {}


@bot.slash_command(name='8ball', description="Сыграть в игру на кик с сервера")
async def eight_ball(ctx):
    user_id = ctx.author.id
    current_time = time.time()
    one_day = 86400
    if user_id in last_used and current_time - last_used[user_id] < one_day:
        next_use_time = last_used[user_id] + one_day
        await ctx.respond(f"До следующего использования команды осталось: <t:{int(next_use_time)}:R>")
        return
    last_used[user_id] = current_time
    if not ctx.guild.me.guild_permissions.kick_members:
        await ctx.respond(f"У меня нет прав чтобы кикнуть проигравшего пользователя в 8ball! ({ctx.author.mention})")
        return
    if random.randint(1, 10) == 1:
        try:
            await ctx.author.kick(reason="Проиграл в 8ball")
            await ctx.respond(f"{ctx.author.mention}, Не повезло и он кикнут с сервера!")
        except discord.Forbidden:
            await ctx.respond(
                f"У меня нет прав чтобы кикнуть проигравшего пользователя в 8ball! ({ctx.author.mention})")
    else:
        await ctx.send("Вам повезло!")


class MyRep(discord.ui.Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(label='Ник', style=discord.InputTextStyle.short,
                                           placeholder='Ваш ник на сервере', max_length=40))
        self.add_item(discord.ui.InputText(label='Ник нарушителя', style=discord.InputTextStyle.short, max_length=40))
        self.add_item(discord.ui.InputText(label='Правило', style=discord.InputTextStyle.short,
                                           placeholder="Пункт правил который нарушил игрок", max_length=300))
        self.add_item(discord.ui.InputText(label='Описание нарушения', style=discord.InputTextStyle.long, min_length=5,
                                           max_length=300))
        self.add_item(discord.ui.InputText(label='Ссылка на доказательство', style=discord.InputTextStyle.short,
                                           max_length=300))

    async def callback(self, interaction: discord.Interaction):
        answers = [item.value for item in self.children]
        embed = discord.Embed(title=f"Новая жалоба от пользователя: {interaction.user.nick}",
                              color=discord.Color.brand_green())
        embed.add_field(name='Его ник:', value=answers[0], inline=False)
        embed.add_field(name='Ник нарушителя:', value=answers[1], inline=False)
        embed.add_field(name='Нарушенный Пункт правил', value=answers[2], inline=False)
        embed.add_field(name='Описание нарушения:', value=answers[3], inline=False)
        embed.add_field(name='Ссылка на доказательство:', value=answers[4], inline=False)
        embed.add_field(name='', value=f'User: {interaction.user.mention}\nID: {interaction.user.id}', inline=False)
        embed.set_thumbnail(url=interaction.user.display_avatar.url)
        channel = bot.get_channel(1236274747910783057)
        await channel.send(embed=embed)
        await interaction.response.send_message("Ваша жалоба успешно отправлена!", ephemeral=True)


@bot.slash_command(name='report', description='Отправить жалобу на игрока', guild_ids=[GUILD_ID])
async def _report_(ctx):
    reps = MyRep(title="Жалоба")
    await ctx.send_modal(reps)


last_mention_time = 0
mention_cooldown = 60
last_mention_time2 = 0
mention_cooldown2 = 60
last_mention_time3 = 0
mention_cooldown3 = 60


@bot.slash_command(name='sos', description='Вызвать модерацию', guild_ids=[GUILD_ID])
async def _sos(ctx, trigger=None):
    global last_mention_time2
    cur_time = time.time()
    time_since_last_mention = cur_time - last_mention_time2
    if trigger is None:
        if time_since_last_mention >= mention_cooldown:
            await ctx.respond(f"{ctx.author.mention}, Вы вызвали модерацию дискорда, скоро Вам помогут!\n\n"
                              f"<@&1219596842698801193>")
            last_mention_time2 = cur_time
        else:
            time_remaining = mention_cooldown - time_since_last_mention
            unix_time = int(cur_time + time_remaining)
            await ctx.respond(f"{ctx.author.mention}, Вы сможете вызвать модерацию через <t:{unix_time}:R>.")
    elif trigger == '-s':
        if time_since_last_mention >= mention_cooldown:
            await ctx.respond(f"{ctx.author.mention}, Вы вызвали модерацию, скоро Вам помогут!\n\n"
                              f"<@&1220822024545505280> <@&1221721452299157515>", ephemeral=True)
            last_mention_time2 = cur_time
        else:
            time_remaining = mention_cooldown - time_since_last_mention
            unix_time = int(cur_time + time_remaining)
            await ctx.respond(f"{ctx.author.mention}, Вы сможете вызвать модерацию через <t:{unix_time}:R>.",
                              ephemeral=True)


@bot.slash_command(name='ar', description='Вызвать модерацию', guild_ids=[GUILD_ID])
async def _ar(ctx, trigger=None):
    global last_mention_time2
    cur_time = time.time()
    time_since_last_mention = cur_time - last_mention_time2
    if trigger is None:
        if time_since_last_mention >= mention_cooldown:
            await ctx.respond(f"{ctx.author.mention}, Вы вызвали модерацию, скоро Вам помогут!\n\n"
                              f"<@&1220822024545505280> <@&1221721452299157515>")
            last_mention_time2 = cur_time
        else:
            time_remaining = mention_cooldown - time_since_last_mention
            unix_time = int(cur_time + time_remaining)
            await ctx.respond(f"{ctx.author.mention}, Вы сможете вызвать модерацию через <t:{unix_time}:R>.")
    elif trigger == '-s':
        if time_since_last_mention >= mention_cooldown:
            await ctx.respond(f"{ctx.author.mention}, Вы вызвали модерацию, скоро Вам помогут!\n\n"
                              f"<@&1220822024545505280> <@&1221721452299157515>", ephemeral=True)
            last_mention_time2 = cur_time
        else:
            time_remaining = mention_cooldown - time_since_last_mention
            unix_time = int(cur_time + time_remaining)
            await ctx.respond(f"{ctx.author.mention}, Вы сможете вызвать модерацию через <t:{unix_time}:R>.",
                              ephemeral=True)


@bot.slash_command(name='dev', description='Вызвать тех. поддержку', guild_ids=[GUILD_ID])
async def _dev(ctx, trigger=None):
    global last_mention_time3
    cur_time = time.time()
    time_since_last_mention = cur_time - last_mention_time3
    if trigger is None:
        if time_since_last_mention >= mention_cooldown:
            await ctx.respond(f"{ctx.author.mention}, Вы вызвали тех. поддержку, скоро Вам помогут!\n\n"
                              f"<@&1213107239364337706> <@&1222968194965307583>")
            last_mention_time3 = cur_time
        else:
            time_remaining = mention_cooldown - time_since_last_mention
            unix_time = int(cur_time + time_remaining)
            await ctx.respond(f"{ctx.author.mention}, Вы сможете вызвать модерацию через <t:{unix_time}:R>.")
    elif trigger == '-s':
        if time_since_last_mention >= mention_cooldown:
            await ctx.respond(f"{ctx.author.mention}, Вы вызвали тех. поддержку, скоро Вам помогут!\n\n"
                              f"<@&1213107239364337706> <@&1222968194965307583>", ephemeral=True)
            last_mention_time3 = cur_time
        else:
            time_remaining = mention_cooldown - time_since_last_mention
            unix_time = int(cur_time + time_remaining)
            await ctx.respond(f"{ctx.author.mention}, Вы сможете вызвать модерацию через <t:{unix_time}:R>.",
                              ephemeral=True)


@bot.slash_command(name='createrole', description='Создать роль',
                   default_member_permissions=discord.Permissions(manage_roles=True), )
async def _createrole(ctx, *, роль: discord.Option(str, description="Название роли")):
    if ctx.author.guild_permissions.manage_roles:
        guild = ctx.guild
        await guild.create_role(name=роль)
        await ctx.respond(f'Роль «{роль}» создана.')
    else:
        await ctx.respond(f"{ctx.author.mention}, У вас нет прав на использование команды 'createrole'", ephemeral=True)


@bot.slash_command(name='setperm', description='Установить право для роли',
                   default_member_permissions=discord.Permissions(administrator=True))
async def _setperm(ctx, роль: discord.Option(discord.Role, description="Роль, которой нужно установить права"),
                   разрешение: discord.Option(str, description="Разрешение для установки",
                                              choices=["view_channels", "manage_channels", "manage_roles",
                                                       "manage_guild", "view_audit_log", "manage_server",
                                                       "change_nickname", "manage_nicknames", "kick_members",
                                                       "ban_members", "administrator", "send_messages", "embed_links",
                                                       "attach_files", "manage_messages", "read_message_history",
                                                       "use_application_commands", "connect", "speak", "video",
                                                       "priority_speaker", "mute_members", "deafen_members",
                                                       "move_members", "request_to_speak"])):
    if ctx.author.guild_permissions.administrator:
        permissions = роль.permissions
        permissions.update(**{разрешение: True})
        await роль.edit(permissions=permissions)
        await ctx.respond(f"Разрешение {разрешение} установлено для роли {роль.name}")
    else:
        await ctx.respond(f"{ctx.author.mention}, У Вас нет прав на использование команды 'setperm'", ephemeral=True)


@bot.event
async def on_member_join(member):
    if member.guild:
        channel = member.guild.system_channel
        if channel and channel == member.guild.system_channel:
            embed = discord.Embed(title="Пользователь присоединился к серверу", color=discord.Color.green())
            embed.add_field(name="Тег", value=member.mention, inline=False)
            embed.add_field(name="Имя пользователя", value=member.name, inline=False)
            embed.add_field(name="ID", value=member.id, inline=False)
            await channel.send(f"{member.mention}, Добро пожаловать!", embed=embed)


@commands.has_permissions(manage_guild=True)
@bot.slash_command(guild_ids=[1138204059397005352], name='setwelcome',
                   description="Устанавливает приветственное сообщение для новых пользователей",
                   default_member_permissions=discord.Permissions(manage_guild=True))
async def set_welcome(ctx, *, message: str):
    message = message.replace('!n', '\n')
    settings = load_settings()
    settings['welcome_message'] = message
    save_settings(settings)
    await ctx.respond(f"Приветственное сообщение установлено: \n{message}")


@set_welcome.error
async def set_welcome_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.respond("У вас нет прав для использования этой команды.", ephemeral=True)
    else:
        await ctx.respond("Произошла ошибка при выполнении команды.", ephemeral=True)


@bot.event
async def on_member_remove(member):
    if member.guild:
      channel = member.guild.system_channel
      if channel and channel == member.guild.system_channel:
        embed = discord.Embed(title=f"Пользователь покинул сервер", color=discord.Color.red())
        embed.add_field(name="Тег", value=f"{member.mention}", inline=False)
        embed.add_field(name="Имя пользователя", value=member.name, inline=False)
        embed.add_field(name="ID", value=member.id, inline=False)
        await channel.send(embed=embed)


@bot.slash_command(name='delperm', description='Удалить право у роли',
                   default_member_permissions=discord.Permissions(administrator=True))
async def _delperm(ctx, *, role: discord.Role):
    if ctx.author.guild_permissions.administrator:
        await ctx.respond(f"Введите название разрешения для роли")
        try:
            permission = await bot.wait_for('message', timeout=30,
                                            check=lambda message: message.author == ctx.author)
            await role.edit(permissions=discord.Permissions(**{permission.content: False}))
            await ctx.respond(f"Разрешение {permission.content} удалено у роли {role.name}")
        except TimeoutError:
            await ctx.respond("Время истекло")
    else:
        await ctx.respond(f"{ctx.author.mention}, У вас нет прав на использование команды 'setperm'", ephemeral=True)


@bot.slash_command(name='roles', description='Список ролей сервера',
                   default_member_permissions=discord.Permissions(manage_roles=True))
async def _roles(interaction: discord.Interaction):
    if interaction.user.guild_permissions.manage_roles:
        roles = interaction.guild.roles
        role_list = discord.Embed(title="Список ролей сервера", color=discord.Color.blue())
        MAX_ROLES_PER_PAGE = 15
        start_index = 0
        end_index = min(start_index + MAX_ROLES_PER_PAGE, len(roles))
        for role in roles[start_index:end_index]:
            if role.name != "@everyone":
                role_list.add_field(name="", value=f"{role.name}\n", inline=False)
        view = RoleView(interaction, roles, start_index, end_index, len(roles), MAX_ROLES_PER_PAGE)
        await interaction.response.send_message(embed=role_list, view=view)
    else:
        await interaction.response.send_message(f"{interaction.author.mention}, У вас нет прав на использование команды"
                                                f"' roles'", ephemeral=True)


class RoleView(discord.ui.View):
    def __init__(self, interaction, roles, start_index, end_index, total_roles, max_roles_per_page):
        super().__init__(timeout=None)
        self.interaction = interaction
        self.roles = roles
        self.start_index = start_index
        self.end_index = end_index
        self.total_roles = total_roles
        self.max_roles_per_page = max_roles_per_page

    @discord.ui.button(label='Предыдущие', style=discord.ButtonStyle.red)
    async def previous_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.start_index > 0:
            self.start_index -= self.max_roles_per_page
            self.end_index = min(self.start_index + self.max_roles_per_page, self.total_roles)
            role_list = discord.Embed(title="Список ролей сервера", color=discord.Color.blue())
            for role in reversed(self.roles[self.start_index:self.end_index]):
                if role.name != "@everyone":
                    role_list.add_field(name="", value=f"{role.name}\n", inline=False)
            await interaction.response.edit_message(embed=role_list, view=self)

    @discord.ui.button(label='Следующие', style=discord.ButtonStyle.green)
    async def next_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.end_index < self.total_roles:
            self.start_index += self.max_roles_per_page
            self.end_index = min(self.start_index + self.max_roles_per_page, self.total_roles)
            role_list = discord.Embed(title="Список ролей сервера", color=discord.Color.blue())
            for role in reversed(self.roles[self.start_index:self.end_index]):
                if role.name != "@everyone":
                    role_list.add_field(name="", value=f"{role.name}\n", inline=False)
            await interaction.response.edit_message(embed=role_list, view=self)


@bot.slash_command(name='replace', description='Заменить роль у пользователя',
                   default_member_permissions=discord.Permissions(manage_roles=True))
async def _replace(ctx, member: discord.Member, prev_role: discord.Role, new_role: discord.Role):
    if ctx.author.guild_permissions.manage_roles:
        if prev_role not in member.roles:
            await ctx.respond(f'{member.mention} не имеет роли {prev_role.name}')
            return
        await member.remove_roles(prev_role)
        await member.add_roles(new_role)
        await ctx.respond(f'{member.mention}, Ваша роль «{prev_role.name}» заменена на роль «{new_role.name}»')
    else:
        await ctx.respond(f"{ctx.author.mention}, У вас нет прав на использование команды 'replace'", ephemeral=True)


@bot.slash_command(name='delrole', description='Удалить роль',
                   default_member_permissions=discord.Permissions(manage_roles=True))
async def _delrole(ctx, *, роль: discord.Option(discord.Role, description="Роль, которую нужно удалить")):
    if ctx.author.guild_permissions.manage_roles:
        if роль:
            await роль.delete()
            await ctx.respond(f'Роль «{роль.name}» удалена')
        else:
            await ctx.respond(f'Роль «{роль.name}» не найдена')
    else:
        await ctx.respond(f"{ctx.author.mention}, У вас нет прав на использование команды 'delrole'", ephemeral=True)


@bot.slash_command(name='delchat', description='Удалить текстовый канал',
                   default_member_permissions=discord.Permissions(manage_channels=True))
async def _delchat(ctx, *,
                   name: discord.Option(discord.TextChannel, description="Текстовый канал, который нужно удалить")):
    if ctx.author.guild_permissions.manage_channels:
        try:
            await name.delete()
            await ctx.respond(f'Текстовый канал «{name.name}» был удален.')
        except discord.Forbidden:
            await ctx.respond(f"{ctx.author.mention}, У Вас недостаточно прав для удаления канала «{name.name}».",
                              ephemeral=True)
        except discord.NotFound:
            await ctx.respond(f"Чат с именем«{name.name}» не найден.", ephemeral=True)
    else:
        await ctx.respond(f"{ctx.author.mention}, У Вас нет прав на использование команды 'delchat'.", ephemeral=True)


@bot.slash_command(name='delvoice', description='Удалить голосовой канал',
                   default_member_permissions=discord.Permissions(manage_channels=True))
async def _delvoice(ctx, *,
                    name: discord.Option(discord.VoiceChannel, description="Голосовой канал, который нужно удалить")):
    if ctx.author.guild_permissions.manage_channels:
        try:
            await name.delete()
            await ctx.respond(f'Текстовый канал «{name.name}» был удален.')
        except discord.Forbidden:
            await ctx.respond(f"{ctx.author.mention}, У Вас недостаточно прав для удаления канала «{name.name}».",
                              ephemeral=True)
        except discord.NotFound:
            await ctx.respond(f"{ctx.author.mention}, Канал «{name.name}» не найден.", ephemeral=True)
    else:
        await ctx.respond(f"{ctx.author.mention}, У Вас нет прав на использование команды 'delchat'.", ephemeral=True)


@bot.slash_command(name="rname", description="Изменить имя роли",
                   default_member_permissions=discord.Permissions(manage_roles=True))
async def _rname(ctx, роль: discord.Option(discord.Role, description="Роль, имя которой нужно изменить"),
                 new_name: discord.Option(str, description="Новое имя роли")):
    if ctx.author.guild_permissions.manage_roles:
        try:
            await роль.edit(name=new_name)
            await ctx.respond(f'Роль {роль.name} переименована в {new_name}')
        except discord.Forbidden:
            await ctx.respond('У меня нет прав для изменения роли.')
        except discord.HTTPException:
            await ctx.respond('Произошла ошибка при попытке изменить имя роли.')
    else:
        await ctx.respond(f"{ctx.author.mention}, У вас нет прав на использование команды 'rname'", ephemeral=True)


@bot.slash_command(name='server')
async def _embed(ctx):
    embed = discord.Embed(title=f'{ctx.guild.name}', description='Информация о сервере', color=discord.Color.blue())
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar.url)
    embed.set_thumbnail(url=ctx.guild.icon.url)
    embed.add_field(name='Кол-во участников:', value=f'{ctx.guild.member_count}', inline=True)
    text1 = len(ctx.guild.text_channels)
    text2 = len(ctx.guild.voice_channels)
    roles = len(ctx.guild.roles)
    channels = text1 + text2
    embed.add_field(name='Всего каналов:', value=f'{channels}', inline=True)
    embed.add_field(name='Кол-во ролей:', value=f'{roles}', inline=True)
    embed.set_image(
        url='https://sun9-78.userapi.com/impf/gMIhKf4uPQHEDtCrB4Ek4OJFrKodmk7yn-Z4LQ/5dGftKsMKZ8.jpg?size=1590x'
            '530&quality=95&crop=262,0,1200,400&sign=07f3df3002e602c971c6ae8d6c90826a&type=cover_group')
    embed.set_footer(text=f'Запрос от {ctx.author}', icon_url=ctx.author.display_avatar.url)
    await ctx.respond(embed=embed)


class GiveawayView(discord.ui.View):
    def __init__(self, seconds, prize, description, winners_count, participants_limit):
        super().__init__(timeout=seconds)
        self.prize = prize
        self.description = description
        self.winners_count = int(winners_count)
        self.participants_limit = int(participants_limit)
        self.participants = []

    @discord.ui.button(label="Участвовать в розыгрыше", style=discord.ButtonStyle.green)
    async def join_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        if len(self.participants) < self.participants_limit:
            if interaction.user not in self.participants:
                self.participants.append(interaction.user)
                await interaction.response.send_message(f"{interaction.user.mention} теперь участвует в розыгрыше!",
                                                        ephemeral=True)
            else:
                await interaction.response.send_message("Вы уже участвуете в этом розыгрыше.", ephemeral=True)
        else:
            await interaction.response.send_message("Лимит участников уже достигнут.", ephemeral=True)

    async def on_timeout(self):
        embed = discord.Embed(title="🎉 Розыгрыш завершен! 🎉", description="Время вышло, вот и результаты!",
                              color=0x42f57b)
        if len(self.participants) >= self.winners_count:
            winners = random.sample(self.participants, self.winners_count)
            winners_mentions = ', '.join([winner.mention for winner in winners])
            embed.add_field(name="🏆 Победители", value=winners_mentions, inline=False)
            embed.add_field(name="🎁 Приз", value=self.prize, inline=False)
            embed.add_field(name="📜 Описание", value=self.description or "Описание отсутствует", inline=False)
            embed.add_field(name="👥 Участники",
                            value=", ".join([participant.mention for participant in self.participants]
                                            ), inline=False)
            embed.set_footer(text="Спасибо всем за участие!")
            await self.message.channel.send(embed=embed)
        else:
            embed.description += "\nК сожалению, в розыгрыше не было достаточно участников."
            await self.message.channel.send(embed=embed)


@bot.slash_command(name="giveaway", description="Создать розыгрыш")
async def giveaway(ctx, seconds: discord.Option(int, description="Время в секундах"),
                   приз: discord.Option(str, description="Приз который получит победитель"),
                   число_победителей: discord.Option(int, description="Сколько человек смогут выиграть в розыгрыше"),
                   лимит_участников: discord.Option(int, description="Сколько человек сможет участвовать в розыгрыше"),
                   description: discord.Option(str, description="Описание розыгрыша") = None):
    if description is None:
        embed = discord.Embed(title="🎉 Розыгрыш!", description="Описание отсутствует", color=0x42f57b)
        embed.add_field(name="Приз", value=приз)
        embed.add_field(name="Продолжительность", value=f"{seconds} секунд")
        embed.add_field(name="Кол-во победителей", value=str(число_победителей))
        embed.add_field(name="Максимальное кол-во участников", value=str(лимит_участников))
        view = GiveawayView(seconds, приз, description, число_победителей, лимит_участников)
        giveaway_message = await ctx.respond(embed=embed, view=view)
        view.message = giveaway_message
    else:
        embed = discord.Embed(title="🎉 Розыгрыш!", description=f"{description}", color=0x42f57b)
        embed.add_field(name="Приз", value=приз)
        embed.add_field(name="Продолжительность", value=f"{seconds} секунд")
        embed.add_field(name="Кол-во победителей", value=str(число_победителей))
        embed.add_field(name="Максимальное кол-во участников", value=str(лимит_участников))
        view = GiveawayView(seconds, приз, description, число_победителей, лимит_участников)
        giveaway_message = await ctx.respond(embed=embed, view=view)
        view.message = giveaway_message


bot.run(btokenn)
