from itertools import count

import disnake
from disnake.ext import commands

import Qin2007s_list_of_swear_words as qlosw

intents = disnake.Intents(guilds=True, emojis_and_stickers=True)
ibot = commands.InteractionBot(intents=intents)
credit = '''this bot is made for @! Trevor#3022 by <@894198592670158898>
this was a custom bot made for a user
to have your own join https://discord.gg/SRjFkx66VZ and dm <@894198592670158898>
bot support season 2 additions
i want to have a friend
'''


@ibot.slash_command(name='credits', description='who mde this bot')
async def credits_slash(inter):
    await inter.send(credit)


# class MYModal(disnake.ui.Modal):
#
#     def __init__(self, title, customid, comps, call_back: callable,defer=False):
#         # The details of the modal, and its components
#         self.defer = defer
#         components = comps
#         super().__init__(
#             title=title,
#             custom_id=customid,
#             components=components,
#         )
#         self.call_back = call_back
#
#     async def callback(self, inter: disnake.ModalInteraction):
#         if self.defer:
#             await inter.response.defer()
#         await self.call_back(inter)
async def check_message(content, isbot):
    # print('new')
    fap = await qlosw.filterstringasync(content)
    return fap and not isbot


@ibot.slash_command(description='the reason shows to the user')
async def warn(inter, user: disnake.Member, reason: str):
    if user == ibot.user:
        await inter.send('I refuse to punish myself.')
        return
    if isinstance(inter.author, disnake.Member) and disnake.utils.find(lambda m: m.id == 937432085256359967 or
                                                                                 m.id == 937432086351065108,
                                                                       inter.author.roles):
        if await check_message(reason, inter.author.bot) or not reason.startswith('same'):
            try:
                await user.send('you\'ve been waned for ' + f'{reason}')
            except disnake.Forbidden:
                await inter.send('cant dm', ephemeral=True)
            else:
                await inter.send(f'{user.mention} has been waned for ' + f'{reason}', ephemeral=True)
        else:
            await inter.send('reason invalid', ephemeral=True)
    else:
        await inter.send('you\'re not 1 of them', ephemeral=True)


@ibot.event
async def on_button_click(inter_mess):
    customid: str = inter_mess.component.custom_id
    split: list[str] = customid.split('.')
    print(customid, split[2])
    if customid.startswith('@role'):
        if split[1] == 'give':
            role = disnake.utils.find(lambda m: str(m.id) == split[2], inter_mess.guild.roles)
            if role:
                await inter_mess.author.add_roles(role)
                await inter_mess.send('success')
            else:
                await inter_mess.send('role not found 404')
        else:
            await inter_mess.send('only can give role')
    else:
        await inter_mess.send('invalid button')


counter = count()


@ibot.slash_command(description='verify prompt')
async def verprompt(inter, button_lable: str, rolegivven: disnake.Role):
    if await check_message(button_lable, False):
        b = disnake.ui.Button(
            style=disnake.ButtonStyle.green, label=button_lable,
            custom_id=f'@role.give.{rolegivven.id}.{next(counter)}'
        )
        mm = disnake.ui.Button(
            style=disnake.ButtonStyle.grey, label='help',
            custom_id=f'@mail.mods.{next(counter)}', disabled=True
        )
        await inter.send(
            components=[b, mm],
            embed=disnake.Embed(
                description=f'on click {rolegivven.mention} wil be given'
            )
        )
    else:
        await inter.send('label invalid')


@ibot.user_command()
async def ban(inter, user: disnake.Member):
    if user == ibot.user:
        await inter.send('I refuse to punish myself.')
        return
    if isinstance(inter.author, disnake.Member) and disnake.utils.find(lambda m: m.id == 937432085256359967 or
                                                                                 m.id == 937432086351065108,
                                                                       inter.author.roles):
        try:
            await inter.guild.ban(user, reason='banhammer')
        except disnake.Forbidden:
            await inter.send('u sure u gave perms?', ephemeral=True)
        else:
            await inter.send('Done')
    else:
        await inter.send('the ban hammer must be in his case', ephemeral=True)


@ibot.slash_command()
async def leave(inter):
    await inter.send('bye')


@ibot.user_command()
async def kick(inter, user: disnake.Member):
    if user == ibot.user:
        await inter.send('I refuse to punish myself.')
        return
    if isinstance(inter.author, disnake.Member) and disnake.utils.find(lambda m: m.id == 937432085256359967 or
                                                                                 m.id == 937432086351065108,
                                                                       inter.author.roles):

        try:
            await inter.guild.kick(user, reason='banhammer')
        except disnake.Forbidden:
            await inter.send('u sure u gave perms?', ephemeral=True)
        else:
            await inter.send('Done')
    else:
        await inter.send('your shoes arent strong enough', ephemeral=True)


@ibot.slash_command(
    description='change the status (only for 2 people)',
    options=[
        disnake.Option(
            name='activity_type', description='playing,watching,listening,streaming,custom',
            type=disnake.OptionType.string,
            required=True,
            choices=[
                disnake.OptionChoice(
                    name='streaming', value='stream'
                ),
                # disnake.OptionChoice(
                #     name='watching', value='wathing'
                # ),

                disnake.OptionChoice(
                    name='custom', value='custom'
                ),
                disnake.OptionChoice(
                    name='playing', value='game'
                ),
                disnake.OptionChoice(
                    name='none', value='None'
                ),
            ]
        ),
        disnake.Option(
            name='activtext', description='for custom only',
            type=disnake.OptionType.string,
            required=True,
        ),
        disnake.Option(
            name='name', description='the name',
            type=disnake.OptionType.string,
            required=True,
        ),
    ]
)
async def change_presence(inter, activtext='im better than you', activity_type='none', name=''):
    activ = None
    if activity_type == 'stream':
        activ = disnake.Streaming(
            platform='leveling ant stream',
            name=name,
            url='https://discord.com/developers/docs/topics/permissions#permissions-bitwise-permission-flags'
        )
    elif activity_type == 'game':
        activ = disnake.Game(
            name=name,
        )
    elif activity_type == 'custom':
        activ = disnake.CustomActivity(
            name=activtext,
        )
    elif activity_type == 'None':
        activ = None
    if activ:
        await ibot.change_presence(activity=activ)
    await inter.send('if it doesnt change, you might have the wrong combination\n this might be broken')


ibot.run('MTAxNDgzMzkwMzk3MTg2MDUxMA.GaPM5X.rCAPk3HqqhHfR9x5AXZOzx5IOIOOzV8uJRH8z0')
