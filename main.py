import discord
from datetime import datetime
from datetime import date
from discord.ext import commands
import time
import webbrowser
from discord.ext.commands import CommandNotFound
intents = discord.Intents.all()

client = commands.Bot(command_prefix="+", intents=intents)


@client.event
async def on_member_join(member):
    await member.send(embed=discord.Embed(title="***Welcome***",
                                          description=f"***Info***\n"
                                                      f"The server's idea is to be the center for a community "
                                                      f" of streamers that started from the bottom and"
                                                      f" want to climb as high as possible\n"
                                                      f"We want to bring quality entertainment "
                                                      f"to the world, funny moments and once in a while good advice\n"
                                                      f"Feel free to ask our moderators anything"
                                                      f" on the support room. They will try to "
                                                      f"answer you as soon as possible\n",
                                          color=0xff9f12))


game = discord.Game("StreamHub Mod 24/7 On. Come join us: https://discord.gg/AwxmTaek8h")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(embed=discord.Embed(description="***COMMAND NOT FOUND***", color=0xff9f12))
        return
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=discord.Embed(description="***MISSING ARGUMENT***", color=0xff9f12))
        return
    raise error


@client.event
async def on_ready():

    webbrowser.open("https://glitch.com/edit/#!/workable-serious-brisket?path=.env%3A1%3A0")
    await client.change_presence(status=discord.Status.online, activity=game)
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)   
    print('------')


@client.command()
async def hello(ctx):
    await ctx.send("Hi")


@client.command(aliases=["commands"])
async def comenzi(ctx):
    await ctx.send(embed=discord.Embed(title="***Commands***",
                                       description="1. hello\n"
                                                   "2. comands\n"
                                                   "3. clear\n"
                                                   "4. kick\n"
                                                   "5. ban\n"
                                                   "6. unban\n"
                                                   "7. mute\n"
                                                   "8. unmute\n"
                                                   "9. Summonmusicbot\n",
                                       color=0xff9f12))


@client.command(aliases=["mute"])
@commands.has_permissions(kick_members=True)
async def m(ctx, member: discord.Member):
    muted_role = ctx.guild.get_role(818119933509500958)
    await member.add_roles(muted_role)
    await ctx.send(embed=discord.Embed(title="Mute ",
                                       description="User-ul "+str(member)+" was muted!",
                                       color=0xff9f12))
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    f = open("log.txt", "a")
    f.write("\n"+str(member)+" a primit mute - "+d1+" "+current_time)
    f.close()


@client.command(aliases=["unmute"])
@commands.has_permissions(kick_members=True)
async def um(ctx, member: discord.Member):
    muted_role = ctx.guild.get_role(818119933509500958)
    await member.remove_roles(muted_role)
    await ctx.send(embed=discord.Embed(title="Mute ",
                                       description="User-ul "+str(member)+" was unmuted!",
                                       color=0xff9f12))
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    f = open("log.txt", "a")
    f.write("\n"+str(member) + " a primit unmute - "+d1+" "+current_time)
    f.close()


@client.command(aliases=["clear"])
@commands.has_permissions(manage_messages=True)
async def c(ctx, amount):
    if str(amount) == "all":
        amount = 1000000000
        await ctx.channel.purge(limit=amount+1)
        await ctx.send(embed=discord.Embed(title="Clear ",
                                           description="I cleared all the mesages!",
                                           color=0xff9f12))
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        f = open("log.txt", "a")
        f.write("\n"+"Am sters toate mesajele - "+d1+" "+current_time)
        f.close()
    else:
        await ctx.channel.purge(limit=int(amount)+1)
        await ctx.send(embed=discord.Embed(title="Clear ",
                                           description="I cleared "+str(amount)+" messages!",
                                           color=0xff9f12))
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        f = open("log.txt", "a")
        f.write("\n"+"Am sters "+str(amount)+" mesaje - "+d1+" "+current_time)
        f.close()


@client.command(aliases=["kick"])
@commands.has_permissions(kick_members=True)
async def k(ctx, member: discord.Member, *, reason="No specified reason"):
    await ctx.send(embed=discord.Embed(title="kick ",
                                       description="User-ul "+str(member)+" was kicked!",
                                       color=0xff9f12))
    await member.send("You were kicked because: " + reason)
    await member.kick(reason=reason)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    f = open("log.txt", "a")
    f.write("\n"+str(member) + " a primit kick - "+d1+" "+current_time)
    f.close()


@client.command(aliases=["spam"])
@commands.has_permissions(administrator=True)
async def msg(ctx, member: discord.Member, *, msg1):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    f = open("log.txt", "a")
    f.write("\nMi-am batut joc de: " + str(member) + " - " + d1 + " " + current_time)
    f.close()
    i = 0
    await member.send(""+str(msg1))


@client.command(aliases=["ban"])
@commands.has_permissions(ban_members=True)
async def b(ctx, member: discord.Member, *, reason="No specified reason"):
    await member.send("Ai primit ban de pe server deoarece: "+reason)
    await member.ban(reason=reason)
    await ctx.send(embed=discord.Embed(title="Ban ",
                                       description="User " + str(member) + " was banned!",
                                       color=0xff9f12))
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    f = open("log.txt", "a")
    f.write("\n"+str(member) + " a primit ban "+str(reason)+" - " + d1 + " " + current_time)
    f.close()


@client.command(aliases=["unban"])
@commands.has_permissions(ban_members=True)
async def ub(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')
    for banned_entry in banned_users:
        user = banned_entry.user

        if(user.name, user.discriminator) == (member_name, member_disc):
            await ctx.guild.unban(user)
            await ctx.send(embed=discord.Embed(title="UnBan ",
                                               description="User " + str(member) + " was UnBanned!",
                                               color=0xff9f12))
            today = date.today()
            d1 = today.strftime("%d/%m/%Y")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            f = open("log.txt", "a")
            f.write("\n"+str(member) + " a primit unban - "+d1+" "+current_time)
            f.close()
            return
    await ctx.send(embed=discord.Embed(title="UnBan ",
                                       description="User " + str(member) + " was not found!",
                                       color=0xff9f12))


@client.command(aliases=["social"])
async def sm(ctx):
    await ctx.send(embed=discord.Embed(title="Instagram",
                                       description=str("***Stream House team***\n"
                                                       "PatrickGM - Patrickgheba\n "
                                                       "C3rberuS -  _davidgrs\n"
                                                       "Livius91 - livius.91\n"
                                                       "hola bb - 67jouvert\n"
                                                       "Starigo - cornel_andrei76\n "
                                                       "Hermano. - david_geamanu\n"
                                                       "***Stream Squad***\n"
                                                       "Vladut - vladut_marian10"),
                                       color=0xff9f12))


@client.command(aliases=["summonmusicbot"])
async def smb(ctx):
    webbrowser.open("https://glitch.com/edit/#!/workable-serious-brisket?path=.env%3A1%3A0")
    await ctx.send(embed=discord.Embed(description="Done",
                                       color=0xff9f12))


@client.command(aliases=["opengubabrowser"])
async def ogb(ctx, site):
    if str(site) == "pornhub.com" or str(site) == "redtube.com" or str(site) == "youporn.com" or\
            str(site) == "www.brazzers.com" or str(site) == "www.xvideos.com" or str(site) == "www.xnxx.com":
        await ctx.send(embed=discord.Embed(description="Nu coaie pls",
                                           color=0xff9f12))
    else:
        # webbrowser.open(site)
        await ctx.send(embed=discord.Embed(description="De unde stii comanda asta?",
                                           color=0xff9f12))


client.run("ODE4MDg0Njg5MTA5NDUwNzgy.YES6vQ.V7jd57b38lDF9FwjvsB7PiZHnPY")
