import datetime
from asyncio import sleep
from datetime import timedelta
from datetime import date
import discord
import random
import requests
from discord.utils import get
from discord.ui import InputText, View, Select, Button, Item, Modal
import time
from art import tprint
from discord.ext import commands
from discord import slash_command
intents = discord.Intents.default()
intents.voice_states = True
intents.typing = True
bot = commands.Bot(command_prefix='r!', intents=discord.Intents.all())
bot.remove_command("help")


@bot.slash_command(name="timeo", description="Отправить пользователя в тайм-аут")
async def timeo(ctx, member: discord.Member, times: int, unit: str):
    if times > 27 and unit == "d":
        await ctx.respond("Максимальные срок для мута 27 дней", ephemeral=True)
    else:
        pass
    if ctx.author.id == 743864658951274528:
        if unit == 's':
            timeout_du = times
        elif unit == 'm':
            timeout_du = times * 60
        elif unit == 'h':
            timeout_du = times * 3600
        elif unit == 'd':
            timeout_du = times * 86400
        else:
            return await ctx.respond("Неверная единица времени.", ephemeral=True)
        try:
            await member.timeout(until=datetime.datetime.utcnow() + timedelta(seconds=timeout_du))
            await ctx.respond(f"{member.mention} в муте", ephemeral=True)
        except discord.Forbidden:
            await ctx.respond("Net prav", ephemeral=True)
    else:
        await ctx.respond(f"{ctx.author.mention} Net prav", ephemeral=True)
        print(f"{ctx.guild.name} -> {ctx.author.name} Net prav")


@bot.event
async def on_ready():
    print(f"Бот {bot.user} подключен к Discord!")
    await bot.change_presence(activity=discord.Game(name="osu!"))


@bot.slash_command(name='clear', description="Удалить сообщения")
async def _clear(ctx, amount=100, user: discord.User = None):
    if ctx.author.guild_permissions.manage_messages:
        if user is None:
            await ctx.channel.purge(limit=amount)
        else:
            messages = []
            async for message in ctx.channel.history(limit=amount):
                if message.author == user:
                    messages.append(message)
            await ctx.channel.delete_messages(messages)
    else:
        await ctx.respond(f"{ctx.author.mention}, У вас нет прав на использование команды 'clear'", ephemeral=True)


@bot.slash_command(name='rcolor', description="Изменить цвет роли")
async def _change_role_color(ctx, color: discord.Color, *, role: discord.Role):
    if ctx.author.guild_permissions.manage_roles:
        if role:
            try:
                await role.edit(color=color)
                await ctx.respond(f"Цвет роли «{role.name}» изменен на «{color}")
            except discord.Forbidden:
                await ctx.respond("У меня нет прав на изменение цвета этой роли", ephemeral=True)
        else:
            await ctx.respond(f"Роль с именем «{role.name}» не найдена", ephemeral=True)
    else:
        await ctx.respond(f"{ctx.author.mention}, У вас нет прав на использование команды 'rcolor'", ephemeral=True)


@bot.slash_command(name='pre', description='Изменить приоритет роли')
async def _pre(ctx, position: int, *, role: discord.Role):
    if ctx.author.guild_permissions.manage_roles:
        if not role:
            await ctx.respond('Роль не найдена', ephemeral=True)
            return
        try:
            await role.edit(position=position)
            await ctx.respond(f'«{role.name}» перемещана на позицию {position}.')
        except discord.Forbidden:
            await ctx.respond('У меня нет прав для изменения приоритета для этой роли', ephemeral=True)
    else:
        await ctx.respond(f"{ctx.author.mention}, У вас нет прав на использование команды 'pre'", ephemeral=True)


@bot.slash_command(name='addrole', description='Выдать роль пользователю')
async def _give_role(ctx, user: discord.Member, role: discord.Role):
    if ctx.author.guild_permissions.manage_roles:
        if role:
            await user.add_roles(role)
            await ctx.respond(f'Роль «{role.name}» выдана пользователю: {user.mention}', ephemeral=True)
        else:
            await ctx.respond(f'Роль с именем «{role.name}» не найдена.', ephemeral=True)
    else:
        await ctx.respond(f"{ctx.author.mention}, У вас нет прав на использование команды 'addrole'", ephemeral=True)


@bot.slash_command(name='removerole', description='Удалить роль у пользователя')
async def _remove_role(ctx, member: discord.Member, *, role: discord.Role):
    if ctx.author.guild_permissions.manage_roles:
        if member and role:
            if role:
                await member.remove_roles(role)
                await ctx.respond(f'Роль «{role.name}» удалена для пользователя {member.mention}', ephemeral=True)
            else:
                await ctx.respond("Роль не найдена", ephemeral=True)
        else:
            await ctx.respond("Роль или пользователь не найдены", ephemeral=True)
    else:
        await ctx.respond(f"{ctx.author.mention}, У вас нет прав на использование команды 'removerole'", ephemeral=True)


@bot.slash_command(name="nick")
async def _nick(ctx, user: discord.Member, nick):
    if ctx.author.guild_permissions.manage_nicknames:
        await user.edit(nick=nick)
        await ctx.respond(f"Пользователю {user} изменён ник на: {nick}", ephemeral=True)
    else:
        await ctx.respond(f"{ctx.author.mention}, У вас нет прав на использование команды 'nick'", ephemeral=True)


@bot.slash_command(name='send', description='Отправить сообщение в канал')
async def _send(ctx, channel_id, *, message):
    if ctx.author.guild_permissions.administrator:
        try:
            channel = await bot.fetch_channel(channel_id)
        except discord.HTTPException:
            await ctx.respond('Неверный ID канала', ephemeral=True)
            return
        try:
            await channel.send(message)
            await ctx.respond("+", ephemeral=True)
        except discord.HTTPException as e:
            await ctx.respond(f'Ошибка отправки сообщения: {e}', ephemeral=True)
    else:
        await ctx.respond(f"{ctx.author.mention}, У вас нет прав на использование команды 'send'", ephemeral=True)


@bot.slash_command(name='nbot', description='Изменить ник бота')
async def _nbot(ctx, *, new_name):
    if ctx.author.guild_permissions.manage_nicknames:
        member = ctx.guild.get_member(bot.user.id)
        await member.edit(nick=new_name)
    else:
        await ctx.respond(f"{ctx.author.mention}, У вас нет прав на использование команды 'nbot'", ephemeral=True)


@bot.slash_command(name='uprole', description='Повысить роль пользователя на 1 уровень')
async def _uprole(ctx, member: discord.Member):
    try:
        if ctx.author.guild_permissions.manage_roles:
            guild = ctx.guild
            roles = [role for role in member.roles if role != guild.default_role]
            highest_role = max(roles, key=lambda x: x.position)
            new_role = discord.utils.get(guild.roles, position=highest_role.position + 1)
            await member.add_roles(new_role)
            await member.remove_roles(highest_role)
            await ctx.respond(
                f'Пользователю {member.mention} ({member.id}) повышен ранг до: {new_role.name} ({new_role.id})')
        else:
            await ctx.respond(f"{ctx.author.mention}, У вас нет прав на использование команды 'uprole'", ephemeral=True)
    except PermissionError:
        await ctx.respond("У бота недостаточно прав", ephemeral=True)


@bot.slash_command(name='do', description='Понизить роль пользователя на 1 уровень')
async def _do(ctx, member: discord.Member):
    try:
        if ctx.author.guild_permissions.manage_roles:
            highest_role = member.top_role
            await member.remove_roles(highest_role)
            roles = ctx.guild.roles
            new_role_position = highest_role.position - 1
            new_role = discord.utils.get(roles, position=new_role_position)
            await member.add_roles(new_role)
            await member.remove_roles(highest_role)
            await ctx.respond(f'Пользователю {member.mention} ({member.id}) понижен ранг до: {new_role.name} '
                              f'({new_role.id})')
        else:
            await ctx.respond(f"{ctx.author.mention}, У вас нет прав на использование команды 'do'", ephemeral=True)
    except PermissionError:
        await ctx.respond("Недостаточно прав.", ephemeral=True)


@bot.slash_command(name='rclear', description='Удалить все роли пользователя')
async def _rclear(ctx, member: discord.Member):
    if ctx.author.guild_permissions.manage_roles:
        roles = member.roles
        roles.reverse()
        for role in roles:
            if role != ctx.guild.default_role:
                await member.remove_roles(role)
        await ctx.respond(f"Все роли пользователя {member.display_name} удалены")
    else:
        await ctx.respond(f"{ctx.author.mention}, У вас нет прав на использование команды 'rclear'", ephemeral=True)


@bot.slash_command(name='mserver', description='Получить информацию о сервере Minecraft')
async def _mserver(ctx, server_address):
    url = f"https://api.mcsrvstat.us/2/{server_address}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    if data.get('online'):
        players_online = data.get('players', {}).get('online', 'Хз')
        server_name = data.get("hostname", "Хз")
        server_version = data.get('version', "Хз")
        software_n = data.get('software', "Хз")
        info_n = ' '.join(data.get('motd', {}).get('clean', ["Хз"]))

        embed = discord.Embed(title=f"Информация о сервере {server_address}", color=ctx.author.color)
        embed.add_field(name="Игроков онлайн", value=f"{players_online} онлайн", inline=True)
        embed.add_field(name="Имя хоста", value=server_name, inline=True)
        embed.add_field(name="Версия сервера", value=server_version, inline=True)
        embed.add_field(name="ПО сервера", value=software_n, inline=True)
        embed.add_field(name="Описание", value=info_n, inline=True)
        await ctx.respond(embed=embed)

    else:
        await ctx.respond(f"Сервер {server_address} не отвечает или не найден.")


@bot.slash_command(name='kick', description='Кикнуть пользователя с сервера')
async def _kick(ctx, member: discord.Member, reason: str = None):
    if ctx.author.guild_permissions.kick_members:
        await member.kick(reason=reason)
        await ctx.respond(f"{member.mention} был кикнут из сервера за причину: {reason or 'Не указано'}")
    else:
        await ctx.respond(f"{ctx.author.mention}, У вас нет прав на использование команды 'kick'", ephemeral=True)


@bot.slash_command(name="avatar", description="В аргументе 'сервер' пишите g")
async def _avatar(ctx, member: discord.Member = None, guild: str = None):
    if member:
        avatar_url = member.avatar.url
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
        await ctx.send(f"До следующего использования команды осталось: <t:{int(next_use_time)}:R>")
        return
    last_used[user_id] = current_time
    if not ctx.guild.me.guild_permissions.kick_members:
        await ctx.send(f"У меня нет прав чтобы кикнуть проигравшего пользователя в 8ball! ({ctx.author.mention})")
        return
    if random.randint(1, 10) == 1:
        try:
            await ctx.author.kick(reason="Проиграл в 8ball")
            await ctx.send(f"{ctx.author.mention}, Не повезло и он кикнут с сервера!")
        except discord.Forbidden:
            await ctx.send(f"У меня нет прав чтобы кикнуть проигравшего пользователя в 8ball! ({ctx.author.mention})")
    else:
        await ctx.send("Вам повезло!")


@bot.slash_command(name='createrole', description='Создать роль')
async def _createrole(ctx, *, role_name):
    if ctx.author.guild_permissions.manage_roles:
        guild = ctx.guild
        await guild.create_role(name=role_name)
        await ctx.respond(f'Роль «{role_name}» создана.')
    else:
        await ctx.respond(f"{ctx.author.mention}, У вас нет прав на использование команды 'createrole'", ephemeral=True)


@bot.slash_command(name='setperm', description='Установить право для роли')
async def _setperm(ctx, *, role: discord.Role):
    if ctx.author.guild_permissions.administrator:
        await ctx.respond(f"Введите название разрешения для роли")
        try:
            permission = await bot.wait_for('message', timeout=30,
                                            check=lambda message: message.author == ctx.author)
            await role.edit(permissions=discord.Permissions(**{permission.content: True}))
            await ctx.respond(f"Разрешение {permission.content} установлено для роли {role.name}")
        except TimeoutError:
            await ctx.respond("Время истекло")
    else:
        await ctx.respond(f"{ctx.author.mention}, У вас нет прав на использование команды 'setperm'", ephemeral=True)


@bot.slash_command(name='delperm', description='Удалить право у роли')
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


@bot.slash_command(name='roles', description='Список ролей сервера')
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


@bot.slash_command(name='replace', description='Заменить роль у пользователя')
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


@bot.slash_command(name='delrole', description='Удалить роль')
async def _delrole(ctx, *, role: discord.Role):
    if ctx.author.guild_permissions.manage_roles:
        if role:
            await role.delete()
            await ctx.respond(f'Роль «{role.name}» удалена')
        else:
            await ctx.respond(f'Роль «{role.name}» не найдена')
    else:
        await ctx.respond(f"{ctx.author.mention}, У вас нет прав на использование команды 'delrole'", ephemeral=True)


@bot.slash_command(name='delchat', description='Удалить текстовый канал')
async def _delchat(ctx, *, text_chat: discord.TextChannel):
    if ctx.author.guild_permissions.manage_channels:
        try:
            await text_chat.delete()
            await ctx.respond(f'Текстовый канал «{text_chat.name}» был удален.')
        except discord.Forbidden:
            await ctx.respond(f"{ctx.author.mention}, У Вас недостаточно прав для удаления канала «{text_chat.name}».",

                              ephemeral=True)
        except discord.NotFound:
            await ctx.respond(f"{ctx.author.mention}, Канал «{text_chat.name}» не найден.", ephemeral=True)
    else:
        await ctx.respond(f"{ctx.author.mention}, У Вас нет прав на использование команды 'delchat'.", ephemeral=True)


@bot.slash_command(name='delvoice', description='Удалить голосовой канал')
async def _delvoice(ctx, *, voice_chat: discord.VoiceChannel):
    if ctx.author.guild_permissions.manage_channels:
        try:
            await voice_chat.delete()
            await ctx.respond(f'Текстовый канал «{voice_chat.name}» был удален.')
        except discord.Forbidden:
            await ctx.respond(f"{ctx.author.mention}, У Вас недостаточно прав для удаления канала «{voice_chat.name}».",
                              ephemeral=True)
        except discord.NotFound:
            await ctx.respond(f"{ctx.author.mention}, Канал «{voice_chat.name}» не найден.", ephemeral=True)
    else:
        await ctx.respond(f"{ctx.author.mention}, У Вас нет прав на использование команды 'delchat'.", ephemeral=True)


@bot.slash_command(name="rname", description="Изменить имя роли")
async def _rname(ctx, role: discord.Role, new_role_name: str):
    if ctx.author.guild_permissions.manage_roles:
        try:
            await role.edit(name=new_role_name)
            await ctx.respond(f'Роль {role.name} переименована в {new_role_name}')
        except discord.Forbidden:
            await ctx.respond('У меня нет прав для изменения роли.')
        except discord.HTTPException:
            await ctx.respond('Произошла ошибка при попытке изменить имя роли.')
    else:
        await ctx.respond(f"{ctx.author.mention}, У вас нет прав на использование команды 'rname'", ephemeral=True)


@bot.slash_command(name='server', description='Информация о сервере')
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
            embed.add_field(name="👥 Участники", value=", ".join([participant.mention for participant in self.participants]
                                                                ), inline=False)
            embed.set_footer(text="Спасибо всем за участие!")
            await self.message.channel.send(embed=embed)
        else:
            embed.description += "\nК сожалению, в розыгрыше не было достаточно участников."
            await self.message.channel.send(embed=embed)


@bot.slash_command(name="giveaway", description="Создать розыгрыш")
async def giveaway(ctx, seconds: int, prize: str, winners_count, participants_limit: int, description=None):
    if description is None:
        embed = discord.Embed(title="🎉 Розыгрыш!", description="Описание отсутствует", color=0x42f57b)
        embed.add_field(name="Приз", value=prize)
        embed.add_field(name="Продолжительность", value=f"{seconds} секунд")
        embed.add_field(name="Кол-во победителей", value=str(winners_count))
        embed.add_field(name="Максимальное кол-во участников", value=str(participants_limit))
        view = GiveawayView(seconds, prize, description, winners_count, participants_limit)
        giveaway_message = await ctx.respond(embed=embed, view=view)
        view.message = giveaway_message
    else:
        embed = discord.Embed(title="🎉 Розыгрыш!", description=f"{description}", color=0x42f57b)
        embed.add_field(name="Приз", value=prize)
        embed.add_field(name="Продолжительность", value=f"{seconds} секунд")
        embed.add_field(name="Кол-во победителей", value=str(winners_count))
        embed.add_field(name="Максимальное кол-во участников", value=str(participants_limit))
        view = GiveawayView(seconds, prize, description, winners_count, participants_limit)
        giveaway_message = await ctx.respond(embed=embed, view=view)
        view.message = giveaway_message


bot.run("<YOUR BOT TOKEN>")
