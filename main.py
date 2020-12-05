import os
import discord
from dotenv import load_dotenv
import keep_alive
from textwrap import dedent
from discord.ext import commands, tasks
import schedule
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix="c.", help_command=None)

@bot.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.watching, name="for c.help")

    await bot.change_presence(activity=activity)
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name="help")
async def help(ctx):
    
    """Gives the list of commands"""

    response = dedent("""
    ```
    Current list of commands:
    \thelp:       runs this command
    \tnsfw-off:   toggles nsfw content off
    \tnsfw-on:    toggles nsfw content on
    ```
    """)

    await ctx.send(response)

@bot.command(name="nsfw-off")
async def nsfw_off(ctx):

    """Toggles nsfw content off"""

    message = dedent("```NSFW content is turned off for the whole server.```")

    nsfw = False
    await ctx.send(message)

@bot.command(name="nsfw-on")
async def nsfw_on(ctx):

    """Toggles nsfw content on"""

    message = dedent("```NSFW content is turned on for the whole server.```")

    nsfw = True
    await ctx.send(message)

@tasks.loop(hours=3)
async def remind():

    """Reminds a cursed fact"""

    
    thing1 = "```Reminder:\nA whales' penis is 3m long, and 30cm in diameter.```"
    thing2 = "```Reminder:\nRupunzel, Rupunzel, let down your pubic hair!\nYes I needed to say that. :D```"
    thing3 = "```Reminder:\nYour parents did a special dance in front of god, and god gave them a baby.```"
    thing4 = "```Reminder:\nYou should know how to draw 4D objects!\nHere is the link on how to do it: https://www.youtube.com/watch?v=Q_B5GpsbSQw```"
    thing5 = "```Reminder:\nDon't forget to check out r/guro!\n\n\nDon't visit it if you want to be cursed. You have been warned.```"
    thing6 = "```Reminder:\nCheck out the tricky jar story: https://cursedreminder.herokuapp.com/the_story```"
    thing7 = "```Reminder:\nYou parents did sex while you were alive, if you have younger brothers/sisters.```"

    number = "thing" + str(random.randint(1,7))

    
    response = eval(number)

    text_channel_list = []
    for channel in bot.get_all_channels():
        # print(channel)
        text_channel_list.append(channel)
    
    # print(text_channel_list)

    for channel in text_channel_list:
        channel_name = bot.get_channel(channel.id)
        # print(channel_name)
        try:
            await channel_name.send(response)
        
        except AttributeError:
            continue
    

@remind.before_loop
async def before():
    await bot.wait_until_ready()

remind.start()
keep_alive.keep_alive()

bot.run(TOKEN)