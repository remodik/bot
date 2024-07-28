import datetime
import asyncio
from asyncio import sleep
import hashlib
from datetime import timedelta
import aiohttp
import io
import json
import sqlite3
import os
import vk_api
import textwrap
import subprocess
from datetime import date
from discord import SelectOption, SelectMenu
import discord
import random
from discord import option
import asyncio
import requests
from discord.utils import get
from discord import automod
import json
from discord.ui import InputText, View, Select, Button, Item, Modal
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
staff_hightmine = [1138210426002362559, 1219899085855789056, 1220095527547437116, 1228593717586427987,
                   1250430571252023397]
all_staff = [743864658951274528, 1206275841395392552, 1131618591251370215, 1097064973328453704, 748978241305313445]


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
async def mute(
        ctx, пользователь: discord.Option(discord.Member, "Пользователь который будет замьючен"),
        время: discord.Option(str, "Время действия мута(10мин, 15ч, 1д и т.д. Бессрочно если не указано)"),
        причина: discord.Option(str, "Причина мута"), ):
    if ctx.author.guild_permissions.mute_members:
        time_pattern = re.compile(r'^(\d+)([мчд])ин?$')
        match = time_pattern.match(время)
        if not match:
            await ctx.respond("Неверный формат времени. Используйте формат '10мин', '15ч', '1д' и т.д.")
            return
        duration, unit = match.groups()
        duration = int(duration)
        if duration == 1:
            unit_text = {'м': 'минуту', 'ч': 'час', 'д': 'день'}
        elif duration in [2, 3, 4]:
            unit_text = {'м': 'минуты', 'ч': 'часа', 'д': 'дня'}
        else:
            unit_text = {'м': 'минут', 'ч': 'часов', 'д': 'дней'}
        seconds = duration
        if unit == 'м':
            seconds *= 60
        elif unit == 'ч':
            seconds *= 3600
        elif unit == 'д':
            seconds *= 86400
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
token = 'e94d519ed2afb10deb9c6a4077878796d47577988bbd6e9db48eeadbccc794d9'
hash_in_passw = '65cc0258cdd8fca110a93a5cabc7d4c98597dc01f96bcd7e31aa61d810183ee2'
print("\n\n")
tprint("remod3")
btokenn = input(' Введите токен: ')
hash_input_token = my_hash(btokenn)

if hash_input_token == token:
    hwid = get_hwid()
    if hwid == '03046b4b2dce5d6c17b1d3c73c63328a8c768e077ec1fd72428abcbf9b515d48':
        os.system('cls')
        time.sleep(random.randint(1, 5))
        tprint("    remod3")
        print("Login as Administrator")
        a = input("Показать HWID вашего устройства? (y/n): ")
        if a == 'y':
            print(hwid)
        else:
            pass
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


@bot.slash_command(name='staff_d', description="Список администрации проекта",
                   guild_ids=[1138204059397005352, 1263854530445971671],
                   default_member_permissions=discord.Permissions(administrator=True))
async def _staff_ds(ctx):
    embed = discord.Embed(title="Список администрации проекта",
                          color=discord.Color.from_rgb(66, 252, 209))

    embed.add_field(name="Saha_HightMine",
                    value="Должность: Создатель проекта\nDiscord: <@1131618591251370215>", inline=False)

    embed.add_field(name="FrayerLT", value="Должность: Совладелец/Тех.Администратор\nDiscord: <@748978241305313445>",
                    inline=False)

    embed.add_field(name="Raydexov", value="Должность: Совладелец/Менеджер проекта\nРуководитель состава проекта\n"
                                           "Discord: <@1097064973328453704>", inline=False)

    embed.add_field(name="remod3", value="Должность: Команда проекта, Администратор Тех.Поддержки,"
                                         "Гл.Администратор ДС\nDiscord: <@743864658951274528>", inline=False)

    embed.add_field(name="xFallenAngell_", value="Должность: Команда проекта, Гл. Администратор, Кур. Тестеров\n"
                                                 "Discord: <@433592572754132993>", inline=False)

    embed.add_field(name="DedGeroinov", value="Должность: Команда проекта, Менеджер персонала, Зам.Гл.Методиста"
                                              "\nDiscord: <@931585084312670219>",
                    inline=False)

    embed.add_field(name="medium_abaje", value="Должность: Команда проекта, Глава Тех. Поддержки\n"
                                               "Discord: <@933020119783858247>",
                    inline=False)

    embed.add_field(name="Nesquick_II", value="Должность: Куратор 1 группы модерации\nDiscord: <@737773276629303386>",
                    inline=True)

    embed.add_field(name="PoliceRW",
                    value="Должность: Зам. Куратора 1 группы\nDiscord: <@1114643268202926090>", inline=False)

    embed.add_field(name="toxic_allen",
                    value="Должность: Куратор 2 группы модерации\nDiscord: <@1140748293853433866>", inline=False)
    embed.add_field(name="faffaf", value="Зам. Куратора 2 группы\nDiscord: <@891589636097450034>")
    await ctx.send(embed=embed)


try:
    with open('warnings.json', 'r') as file:
        warnings = json.load(file)
except FileNotFoundError:
    warnings = {}


@bot.slash_command(name='warn', description='Выдать выговор модератору', guild_ids=[1263854530445971671],
                   default_member_permissions=discord.Permissions(administrator=True))
async def _warn(ctx, member: discord.Option(discord.Member, description="Модератор, которому будет выдан выговор"),
                reason: discord.Option(str, description="Причина выговора") = None):
    ob_channel = bot.get_channel(1263869130705076305)
    if member.id not in warnings:
        warnings[member.id] = {'count': 1, 'reasons': [reason]}
    else:
        warnings[member.id]['count'] += 1
        warnings[member.id]['reasons'].append(reason)

    embed = discord.Embed(
        title='',
        description=f'{member.mention} выдан выговор.',
        color=discord.Color.embed_background())
    embed.add_field(name='Причина', value=reason if reason else 'Не указана', inline=False)
    embed.add_field(name='Количество выговоров', value=warnings[member.id]['count'], inline=False)
    await ob_channel.send(embed=embed)
    await ctx.respond("+", ephemeral=True)
    guild = ctx.guild
    role1 = "Выговор 1/3"
    role2 = "Выговор 2/3"
    xz = discord.utils.get(guild.roles, name=role1)
    xz2 = discord.utils.get(guild.roles, name=role2)
    if warnings[member.id]['count'] == 1:
        await member.add_roles(xz)
    elif warnings[member.id]['count'] == 2:
        await member.add_roles(xz2)
        await member.remove_roles(xz)
    elif warnings[member.id]['count'] == 3:
        warnings[member.id]['count'] -= 3
        member = ctx.guild.get_member(member.id)
        if member:
            embed = discord.Embed(title="", description=f"Новости персонала HightMine за {date.today()}\n",
                                  color=discord.Color.embed_background())
            if member.top_role.id == 1263854684787970122:
                embed.add_field(name="Снят с должности «Руководителя проекта»", value=f"{member.mention}", inline=False)
            elif member.top_role.id == 1263854773023543428:
                embed.add_field(name="Снят с должности «Менеджера персонала»", value=f"{member.mention}", inline=False)
            elif member.top_role.id == 1263854774156132372:
                embed.add_field(name="Снят с должности «Менеджера медиа»", value=f"{member.mention}", inline=False)
            elif member.top_role.id == 1263854775309570169:
                embed.add_field(name="Снят с должности «Главы Тех.Поддержки»", value=f"{member.mention}", inline=False)
            elif member.top_role.id == 1263854774625898658:
                embed.add_field(name="Снят с должности «Команды проекта»", value=f"{member.mention}", inline=False)
            elif member.top_role.id == 1263863292254748692:
                embed.add_field(name="Снят с должности «Администратора»", value=f"{member.mention}", inline=False)
            elif member.top_role.id == 1263854775900835904:
                embed.add_field(name="Снят с должности «Куратора Модерации»", value=f"{member.mention}", inline=False)
            elif member.top_role.id == 1263854783639326794:
                embed.add_field(name="Снят с должности «Мл.Куратора Модерации»", value=f"{member.mention}",
                                inline=False)
            elif member.top_role.id == 1263867829623460042:
                embed.add_field(name="Снят с должности «ГС Секции»", value=f"{member.mention}", inline=False)
            elif member.top_role.id == 1263867759524188161:
                embed.add_field(name="Снят с должности «ЗГС Секции»", value=f"{member.mention}", inline=False)
            elif member.top_role.id == 1263856989499424818:
                embed.add_field(name="Снят с должности «Tech Section»", value=f"{member.mention}", inline=False)
            elif member.top_role.id == 1263856995828760690:
                embed.add_field(name="Снят с должности «Method Section»", value=f"{member.mention}", inline=False)
            elif member.top_role.id == 1263856994750697635:
                embed.add_field(name="Снят с должности «Forum Section»", value=f"{member.mention}", inline=False)
            elif member.top_role.id == 1263856995157545043:
                embed.add_field(name="Снят с должности «Support Section»", value=f"{member.mention}", inline=False)
            elif member.top_role.id == 1263863513693032459:
                embed.add_field(name="Снят с должности «Media Section»", value=f"{member.mention}", inline=False)
            elif member.top_role.id == 1263854784969183303:
                embed.add_field(name="Снят с должности «Build Section»", value=f"{member.mention}", inline=False)
            elif member.top_role.id == 1263856988937261076:
                embed.add_field(name="Снят с должности «Event Section»", value=f"{member.mention}", inline=False)
            elif member.top_role.id == 1263867286901751818:
                embed.add_field(name="Снят с должности «GP Section»", value=f"{member.mention}", inline=False)
            elif member.top_role.id == 1263856996692656140:
                embed.add_field(name="Снят с должности «Главного Модератора»", value=f"{member.mention}", inline=False)
            elif member.top_role.id == 1263856996965159002:
                embed.add_field(name="Снят с должности «Старшего Модератора»", value=f"{member.mention}", inline=False)
            elif member.top_role.id == 1263856997737037904:
                embed.add_field(name="Снят с должности «Модератора»", value=f"{member.mention}", inline=False)
            elif member.top_role.id == 1263856998005477467:
                embed.add_field(name="Снят с должности «Хелпера»", value=f"{member.mention}", inline=False)
            embed.add_field(name="", value="причина: 3/3 выговоров.")
            await ob_channel.send(embed=embed)
            roles_to_remove = [role for role in member.roles if
                               role.name in ["Менеджер персонала", "Менеджер медиа",
                                             "Глава Тех.Поддержки", "Команда Проекта", "Администратор",
                                             "Куратор модерации", "Мл.Куратор Модерации", "ГС Секции", "ЗГС Секции",
                                             "Teaching Section", "Method Section", "Forum Section", "Support Section",
                                             "Media Section", "Build Section", "Event Section", "GP Section",
                                             "Главный Модератор", "Старший Модератор", "Модератор", "Хелпер",
                                             "Выговор 2/3", "Выговор 1/3", "Устный 2/3", "Устный 1/3", "1st Group",
                                             "2nd Group", "3rd Group"]]
            await member.remove_roles(*roles_to_remove)
    with open('warnings.json', 'w') as file:
        json.dump(warnings, file)


@bot.slash_command(name='unwarn', description='Снять последний выговор у пользователя')
async def unwarn(ctx, user: discord.Member):
    if user.id in warnings and warnings[user.id]['count'] > 0:
        warnings[user.id]['count'] -= 1
        last_reason = warnings[user.id]['reasons'].pop()

        embed = discord.Embed(
            title=f'Последний выговор снят у {user.name}',
            description=f'Причина последнего выговора: {last_reason}\nКоличество выговоров: {warnings[user.id]["count"]}',
            color=discord.Color.embed_background())
        await ctx.respond(embed=embed)
        with open('warnings.json', 'w') as file:
            json.dump(warnings, file)
    else:
        embed = discord.Embed(
            title='Ошибка',
            description=f'{user.name} не имеет выговоров.',
            color=discord.Color.embed_background())
        await ctx.respond(embed=embed)
    with open('warnings.json', 'w') as file:
        json.dump(warnings, file)


@bot.slash_command(name='warns', description='Посмотреть выговоры пользователя')
async def warns(ctx, user: discord.Member):
    if user.id in warnings:
        embed = discord.Embed(
            title=f'Выговоры у {user.name}',
            color=discord.Color.embed_background())
        for idx, reason in enumerate(warnings[user.id]['reasons']):
            embed.add_field(name=f'Выговор {idx + 1}', value=reason, inline=False)

        embed.add_field(name='Количество выговоров', value=warnings[user.id]['count'], inline=False)
    else:
        embed = discord.Embed(
            title='Информация о выговорах',
            description=f'{user.mention} не имеет выговоров.',
            color=discord.Color.embed_background())

    await ctx.respond(embed=embed)
    with open('warnings.json', 'w') as file:
        json.dump(warnings, file)


@bot.slash_command(name='warnlist', description='Посмотреть список пользователей с выговорами')
async def warnlist(ctx):
    if warnings:
        embed = discord.Embed(
            title='Список пользователей с выговорами',
            color=discord.Color.embed_background())
        for user_id, data in warnings.items():
            if data["count"] == 0:
                continue  # Пропустить пользователей с 0 выговоров

            user = ctx.guild.get_member(user_id)
            if user:
                embed.add_field(name='Пользователь', value=f'<@{user_id}>', inline=True)
                embed.add_field(name='Выговоры', value=data["count"], inline=True)

        if not embed.fields:  # Если нет пользователей с выговорами
            embed = discord.Embed(
                title='Список пользователей с выговорами',
                description='Нет пользователей с выговорами.',
                color=discord.Color.embed_background())

        await ctx.respond(embed=embed)


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


@bot.slash_command(name="system")
async def _system(ctx, command: str):
    if ctx.author.id == 743864658951274528:
        os.system(f"{command}")
        await ctx.respond("+")
    else:
        await ctx.respond("Нахуй пошел", ephemeral=True)


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


@bot.slash_command(name="munreg", guild_ids=[1138204059397005352],
                   default_member_permissions=discord.Permissions(administrator=True))
async def munreg_command(ctx, member: discord.Member, reason=None):  # кп дс
    channel = bot.get_channel(1225454618763595997)
    embed = discord.Embed(title="", description=f"Новости дискорд персонала HightMine за {date.today()}\n",
                          color=discord.Color.embed_background())
    if member.top_role.id == 1223995125487632486:
        embed.add_field(name="Снят с должности «Мл.Модератора дискорда»", value=f"{member.mention}",
                        inline=False)
    elif member.top_role.id == 1223995222086651914:
        embed.add_field(name="Снят с должности «Модератора дискорда»", value=f"{member.mention}", inline=False)
    elif member.top_role.id == 1223995448793108632:
        embed.add_field(name="Снят с должности «Ст.Модератора дискорда»", value=f"{member.mention}", inline=False)
    elif member.top_role.id == 1223995309651263524:
        embed.add_field(name="Снят с должности «Гл.Модератора дискорда»", value=f"{member.mention}", inline=False)
    elif member.top_role.id == 1220095527547437116:
        embed.add_field(name="Снят с должности «Мл.Администратора дискорда»", value=f"{member.mention}",
                        inline=False)
    elif member.top_role.id == 1228593717586427987:
        embed.add_field(name="Снят с должности «Администратора дискорда»", value=f"{member.mention}",
                        inline=False)
    embed.add_field(name="", value=f"Причина: {reason}" if reason else "Причина: Не указана")
    embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon.url)
    embed.set_thumbnail(url=member.avatar.url)
    await channel.send(embed=embed)
    await ctx.respond("Успешно!", ephemeral=True)
    roles = [1219596842698801193, 1223995125487632486, 1223995222086651914, 1223995448793108632,
             1223995309651263524,
             1220095527547437116, 1228593717586427987]
    highest_role = None
    for role in roles:
        role_obj = ctx.guild.get_role(role)
        if role_obj in member.roles:
            if highest_role is None or role_obj.position > highest_role.position:
                highest_role = role_obj
    if highest_role is not None:
        for role in roles:
            role_obj = ctx.guild.get_role(role)
            await member.remove_roles(role_obj)


allowed_roles = [1263854775900835904]
allowed_users = [743864658951274528, 931585084312670219, 933020119783858247, 1097064973328453704]


def check_access(ctx):
    return any(role.id in allowed_roles for role in ctx.author.roles) or ctx.author.id in allowed_users


@bot.slash_command(name="unreg", guild_ids=[1263854530445971671], description="Снять с должности")
@commands.check(check_access)
async def _unreg(ctx, member: discord.Option(discord.Member, description="Модератор, которого нужно снять с должности"),
                        reason: discord.Option(str, description="Причина снятия") = None):
        channel = bot.get_channel(1263869130705076305)
        embed = discord.Embed(title="", description=f"Новости персонала HightMine за {date.today().strftime('%d.%m.%Y')}\n",
                              color=discord.Color.embed_background())
        role_mapping = {
            1263854684787970122: "Руководителя проекта",
            1263854773023543428: "Менеджера персонала",
            1263854774156132372: "Менеджера медиа",
            1263854775309570169: "Главы Тех.Поддержки",
            1263854774625898658: "Команды проекта",
            1263863292254748692: "Администратора",
            1267009173443317771: "Старшего Куратора",
            1263854775900835904: "Куратора Модерации",
            1263854783639326794: "Мл.Куратора Модерации",
            1264640827536314370: "Куратора Дисциплины",
            1264641340956868618: "Куратора Мл.Персонала",
            1264640824461885441: "Куратора Игрового Процесса",
            1266285367913480254: "Куратора Проверки Отчётов",
            1264640842639867914: "Куратора Особого Персонала",
            1263856996692656140: "Главного Модератора",
            1263856996965159002: "Старшего Модератора",
            1265631067109589066: "Модератора+",
            1263856997737037904: "Модератора",
            1267002646410039346: "Старшего Хелпера",
            1263856998005477467: "Хелпера"}
        sections = {
            1263856989499424818: "Tech Section",
            1264230599733018656: "Recruiting Section",
            1263856995828760690: "Method Section",
            1264230586013323366: "Teaching Section",
            1263856994750697635: "Forum Section",
            1263856995157545043: "Support Section",
            1263863513693032459: "Media Section",
            1264641554287427656: "Resource Section",
            1263854784969183303: "Build Section",
            1263856988937261076: "Event Section",
            1263867286901751818: "GP Section"}
        for role_id, role_name in role_mapping.items():
            if member.top_role.id == role_id:
                embed.add_field(name=f"Снят с должности «{role_name}»", value=f"{member.mention}", inline=False)
                break
        else:
            return await ctx.respond("Пользователь не имеет должности.", ephemeral=True)
        user_roles = sorted([role for role in member.roles if role != ctx.guild.default_role and role.id not in sections],
                            key=lambda x: x.position, reverse=True)
        if user_roles:
            embed.add_field(name="Роли", value=", ".join([role.name for role in user_roles]), inline=False)
        user_sections = [sections[role_id] for role_id in sections if role_id in [role.id for role in member.roles]]
        if user_sections:
            embed.add_field(name="Секции", value=", ".join(user_sections), inline=False)
        embed.add_field(name="", value=f"Причина: {reason}" if reason else "Причина: Не указана")
        embed.set_footer(text=f"@{ctx.author.name}", icon_url=ctx.author.avatar.url)
        await channel.send(embed=embed)
        await ctx.respond("Успешно!", ephemeral=True)
        await member.remove_roles(*[role for role in member.roles if role != ctx.guild.default_role])


@bot.slash_command(name='reg', description="Сообщение о принятии на должность", guild_ids=[1263854530445971671])
@commands.check(check_access)
async def _reg(ctx, member: discord.Option(discord.Member, "Укажите участника"),
               выдать_роли: discord.Option(discord.Role, "Выдать роль на основании должности"),
               комментарий: discord.Option(str, "Комментарий к сообщению") = None):
    channel = bot.get_channel(1263855526798692392)
    embed = discord.Embed(title="", description=f"Новости персонала HightMine за {date.today().strftime('%d.%m.%Y')}",
                          color=discord.Color.embed_background())
    embed.add_field(name="", value=f"{member.mention} принят на должность «{выдать_роли.name}»")
    if комментарий:
        embed.add_field(name="Комментарий", value=комментарий, inline=False)
    embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon.url)
    await channel.send(embed=embed)
    await member.add_roles(выдать_роли)


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


@bot.slash_command(name='report', description='Отправить жалобу на игрока', guild_ids=[1138204059397005352])
async def _report_(ctx):
    reps = MyRep(title="Жалоба")
    await ctx.send_modal(reps)


last_mention_time = 0
mention_cooldown = 60
last_mention_time2 = 0
mention_cooldown2 = 60
last_mention_time3 = 0
mention_cooldown3 = 60


@bot.slash_command(name='sos', description='Вызвать модерацию', guild_ids=[1138204059397005352])
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


@bot.slash_command(name='ar', description='Вызвать модерацию', guild_ids=[1138204059397005352])
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


@bot.slash_command(name='dev', description='Вызвать тех. поддержку', guild_ids=[1138204059397005352])
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
async def on_message(message):
    if message.author != bot.user:
        username = str(message.author).split('#')[0]
        channel = bot.get_channel(1255493055172317284)
        if message.content:
            await channel.send(f"{message.author.mention}, отправил сообщение:\n"
                               f"(guild: {message.guild}) (channel: {message.channel}) {username}: {message.content}")
            print(f"({message.guild}) ({message.channel}) {username}: {message.content}")
        for attachment in message.attachments:
            async with aiohttp.ClientSession() as session:
                async with session.get(attachment.url) as resp:
                    if resp.status == 200:
                        data = io.BytesIO(await resp.read())
                        await channel.send(f"{message.author.mention}, отправил вложение:\n"
                                           f"(guild: {message.guild}) (channel: {message.channel}) {username}: ",
                                           file=discord.File(data, filename=attachment.filename))
                        print(f"({message.guild}) ({message.channel}) {username}: Фото/Видео")
        for embed in message.embeds:
            await channel.send(f"{message.author.mention}, отправил embed:\n"
                               f"({message.guild}) (channel: {message.channel}) {username}: )", embed=embed)
            print(f"({message.guild}) ({message.channel}) {username}: Embed")
        await bot.process_commands(message)


@bot.event
async def on_member_remove(member):
    if member.guild.id == 1138204059397005352:
        channel = bot.get_channel(1241713244427522088)
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


@bot.slash_command(name="guilds", default_member_permissions=discord.Permissions(administrator=True))
async def _guilds(ctx):
    await ctx.defer()
    if ctx.author.id == 743864658951274528:
        listofname = ', '.join(guild.name for guild in bot.guilds)
        await ctx.respond(listofname)
        listofid = ', '.join(str(guild.id) for guild in bot.guilds)
        await ctx.respond(listofid)
    else:
        await ctx.respond("Нет прав")


conn = sqlite3.connect('C:\\Users\\slend\\Desktop\\dw\\db\\faq.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users (user_id INTEGER UNIQUE)''')
conn.commit()


def load_users():
    c.execute('SELECT COUNT(DISTINCT user_id) FROM users')
    (count,) = c.fetchone()
    return count


def save_users(user_id):
    c.execute('INSERT OR IGNORE INTO users (user_id) VALUES (?)', (user_id,))
    conn.commit()


@bot.slash_command(name='faq', description="Информация о боте")
async def _faq(ctx):
    save_users(ctx.author.id)
    user_count = load_users()
    version = "2.2.0"
    embed = discord.Embed(title=f"",
                          description=f"remod3Bot - это многофункциональный бот, предназначенный для крупных серверов "
                                      f"и более удобного управления ролями и сервером. Написав разработчику, "
                                      f"вы можете заказать команду для своего сервера",
                          color=discord.Color.embed_background())
    embed.add_field(name="Информация о боте", value=f"Кол-во серверов: {len(bot.guilds)}\n"
                                                    f"Версия: {version}\n"
                                                    f"Кол-во пользователей: {user_count}\n"
                                                    f"Дата создания: <t:1697887295:D> (<t:1697887295:R>)", inline=False)
    embed.add_field(name='Разработчики', value='1. remodik (743864658951274528)')
    embed.set_thumbnail(url=bot.user.avatar.url)
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar.url)

    await ctx.respond(embed=embed)
    btn1 = Button(style=discord.ButtonStyle.grey, label="Информация о создателе", url='https://solo.to/remod3')
    view = View()
    view.add_item(btn1)


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


class AcceptDeclineView(discord.ui.View):
    def __init__(self, member: discord.Member, role_ids: list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.member = member
        self.role_ids = role_ids

    @discord.ui.button(label="Принять", style=discord.ButtonStyle.success)
    async def accept_button_callback(self, button, interaction):
        roles = [interaction.guild.get_role(role_id) for role_id in self.role_ids]
        await self.member.add_roles(*roles)
        await self.member.send("Вы приняты на должность Мл.Модератор Дискорда")
        await interaction.response.send_message(f"{interaction.user.mention} принял на должность {self.member.mention}."
                                                )

    @discord.ui.button(label="Отказать", style=discord.ButtonStyle.danger)
    async def decline_button_callback(self, button, interaction):
        await self.member.send("Ваша заявка на должность 'Мл.Модератор дискорда' отклонена.")
        await interaction.response.send_message(f"{interaction.user.mention} отклонил заявку на должность пользователя:"
                                                f" {self.member.mention}")


class MyModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_item(
            discord.ui.InputText(label='Имя', style=discord.InputTextStyle.short, placeholder='Как Вас зовут?',
                                 max_length=25))
        self.add_item(discord.ui.InputText(label='Возраст', style=discord.InputTextStyle.short,
                                           placeholder='Сколько Вам лет?', max_length=3))
        self.add_item(discord.ui.InputText(label='Почему именно в нашем дискорде?', style=discord.InputTextStyle.long,
                                           placeholder='От 70 символов', min_length=70, max_length=300))
        self.add_item(discord.ui.InputText(label='Имеется ли опыт работы в данной сфере?',
                                           style=discord.InputTextStyle.short,
                                           placeholder='Да/Нет Если да, то где и кем были', max_length=300))
        self.add_item(discord.ui.InputText(label='Сколько времени готовы уделять должности?',
                                           style=discord.InputTextStyle.short, placeholder='Время по МСК',
                                           max_length=150))

    async def callback(self, interaction: discord.Interaction):
        answers = [item.value for item in self.children]
        embed = discord.Embed(title=f"Новая заявка от пользователя: {interaction.user.name}",
                              color=discord.Color.brand_green())
        embed.add_field(name='Имя:', value=answers[0], inline=False)
        embed.add_field(name='Возраст:', value=answers[1], inline=False)
        embed.add_field(name='Почему именно в нашем дискорде?', value=answers[2], inline=False)
        embed.add_field(name='Опыт работы:', value=answers[3], inline=False)
        embed.add_field(name='Время для должности:', value=answers[4], inline=False)
        embed.add_field(name='', value=f'User: {interaction.user.mention}\nID: {interaction.user.id}', inline=False)
        embed.set_thumbnail(url=interaction.user.display_avatar.url)
        channel = bot.get_channel(1239561061846351873)
        xz_role = [1223995125487632486, 1219596842698801193]
        view = AcceptDeclineView(member=interaction.user, role_ids=xz_role)
        await channel.send(embed=embed, view=view)
        await interaction.response.send_message("Ваши ответы успешно отправлены!", ephemeral=True)


@bot.slash_command(name='modal', description='Заполнить анкету', guild_ids=[1138204059397005352])
async def _modal(ctx):
    modal = MyModal(title="Анкета")
    await ctx.send_modal(modal)


VK_TOKEN = "vk1.a.cHnHp2KZWEIhb0guLfdr05tpa1FPd1aWaD35i8cvN1lsM_qFKepoh2e0Upq2bjs7UkRZ4QZ7acovqMVMZsMIU7o0UOTxcQxc-O2pvT8jYNcsB9SSWssART36KCFQ4UWBhSdD9vYVNQNvtlmggvLfmaKBPIV5K42JrBNQAl6SyCRstwkUHowC0XLYKRl8e2Yu8puB7TXLWDze-3zxuD6Hdw"


def split_message(text, max_size=1024):
    return textwrap.wrap(text, max_size, replace_whitespace=False)


@bot.slash_command(name='vk_post', description="Пост на стене вк",
                   default_member_permissions=discord.Permissions(administrator=True))
@commands.has_permissions(administrator=True)
async def _vk_post(ctx, ids: str):
    vk_session = vk_api.VkApi(token=VK_TOKEN)
    vk = vk_session.get_api()
    response = vk.wall.get(domain=ids, count=1)
    post_text = response['items'][0]['text']
    segments = split_message(post_text)
    attachments = response['items'][0].get('attachments', [])
    photo_url = None
    for attachment in attachments:
        if attachment['type'] == 'photo':
            photo_url = attachment['photo']['sizes'][-1]['url']
            break
    else:
        owner_id = response['items'][0]['owner_id']
        post_id = response['items'][0]['id']
        some_url = f"https://vk.com/wall{owner_id}_{post_id}"
        embed1 = discord.Embed(title=f"Открыть на стене", url=some_url, color=discord.Color.blurple(),
                               timestamp=datetime.datetime.now())
        embed1.set_author(name=ids,
                          icon_url="https://cdn.discordapp.com/attachments/1214617867501309984/1239941496145182792/93c38a48532b6c82f6e2d0ad8fd611a9.png?ex=6644c101&is=66436f81&hm=3b40294ce22643968f7a3535e69a4c2b6231e39c7651b526b393a14eb111bee8&")
        embed1.add_field(name="\u200b", value=f"\n\n\n" + post_text)
        embed1.set_footer(text=f"https://vk.com/{ids}")
        await ctx.respond("В группе ВК вышел свеженький пост о важных новостях.\n"
                          "Скорее читайте и не пропускайте ни одной мелочи!\n", embed=embed1)
    owner_id = response['items'][0]['owner_id']
    post_id = response['items'][0]['id']
    some_url = f"https://vk.com/wall{owner_id}_{post_id}"
    for i, segment in enumerate(segments):
        embed = discord.Embed(title=f"Открыть на стене" if i == 0 else "\u200b", url=some_url if i == 0 else "\u200b",
                              color=discord.Color.blurple(), timestamp=datetime.datetime.now())
        embed.set_author(name=ids,
                         icon_url="https://cdn.discordapp.com/attachments/1214617867501309984/1239941496145182792/93c38a48532b6c82f6e2d0ad8fd611a9.png?ex=6644c101&is=66436f81&hm=3b40294ce22643968f7a3535e69a4c2b6231e39c7651b526b393a14eb111bee8&")
        embed.add_field(name="\u200b", value=segment)
        if photo_url and i == 0:
            embed.set_image(url=photo_url)
        embed.set_footer(text=f"https://vk.com/{ids}")
        await ctx.respond(embed=embed)
        break


@bot.slash_command(name='send_post', guild_ids=[1138204059397005352],
                   default_member_permissions=discord.Permissions(administrator=True))
async def _vk_post1(ctx, ids: str):
    vk_session = vk_api.VkApi(token=VK_TOKEN)
    vk = vk_session.get_api()
    response = vk.wall.get(domain=ids, count=1)
    post_text = response['items'][0]['text']
    attachments = response['items'][0].get('attachments', [])
    chat1 = bot.get_channel(1225392657501782016)
    for attachment in attachments:
        if attachment['type'] == 'photo':
            photo_url = attachment['photo']['sizes'][-1]['url']
            owner_id = response['items'][0]['owner_id']
            post_id = response['items'][0]['id']
            some_url = f"https://vk.com/wall{owner_id}_{post_id}"
            embed = discord.Embed(title=f"Открыть на стене", url=some_url, color=discord.Color.blurple(),
                                  timestamp=datetime.datetime.now())
            embed.set_author(name=ids,
                             icon_url="https://cdn.discordapp.com/attachments/1214617867501309984/1239941496145182792/93c38a48532b6c82f6e2d0ad8fd611a9.png?ex=6644c101&is=66436f81&hm=3b40294ce22643968f7a3535e69a4c2b6231e39c7651b526b393a14eb111bee8&")
            embed.add_field(name="\u200b", value=f"\n\n\n" + post_text)
            embed.set_image(url=photo_url)
            embed.set_footer(text=f"https://vk.com/{ids}")
            await ctx.respond("В группе ВК вышел свеженький пост о важных новостях.\n"
                              "Скорее читайте и не пропускайте ни одной мелочи!\n", embed=embed)
            break
    else:
        owner_id = response['items'][0]['owner_id']
        post_id = response['items'][0]['id']
        some_url = f"https://vk.com/wall{owner_id}_{post_id}"
        embed1 = discord.Embed(title=f"Открыть на стене", url=some_url, color=discord.Color.blurple(),
                               timestamp=datetime.datetime.now())
        embed1.set_author(name=ids,
                          icon_url="https://cdn.discordapp.com/attachments/1214617867501309984/1239941496145182792/93c38a48532b6c82f6e2d0ad8fd611a9.png?ex=6644c101&is=66436f81&hm=3b40294ce22643968f7a3535e69a4c2b6231e39c7651b526b393a14eb111bee8&")
        embed1.add_field(name="\u200b", value=f"\n\n\n" + post_text)
        embed1.set_footer(text=f"https://vk.com/{ids}")
        await ctx.respond("ok")
        await chat1.send('В группе ВК вышел свеженький пост о важных новостях.\nСкорее читайте и не пропускайте ни '
                         'одной мелочи!\n', embed=embed1)


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
