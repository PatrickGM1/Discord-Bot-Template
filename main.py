import discord
from datetime import datetime
from datetime import date
from discord.ext import commands
from discord.ext.commands import CommandNotFound
intents = discord.Intents.all()

client = commands.Bot(command_prefix="+", intents=intents)


@client.event
async def on_member_join(member):
    await member.send(embed=discord.Embed(title="***Welcome***",
                                          description=f"***Info***\n",
                                          color=0xff9f12))


game = discord.Game("Insert bot status")


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
                                                   "2. commands\n"
                                                   "3. clear\n"
                                                   "4. kick\n"
                                                   "5. ban\n"
                                                   "6. unban\n"
                                                   "7. mute\n"
                                                   "8. unmute\n",
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
    f.write("\n"+str(member)+" was muted - "+d1+" "+current_time)
    f.close()


@client.command(aliases=["unmute"])
@commands.has_permissions(kick_members=True)
async def um(ctx, member: discord.Member):
    muted_role = ctx.guild.get_role(818119933509500958)
    await member.remove_roles(muted_role)
    await ctx.send(embed=discord.Embed(title="Mute ",
                                       description="User "+str(member)+" was unmuted!",
                                       color=0xff9f12))
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    f = open("log.txt", "a")
    f.write("\n"+str(member) + " was unmuted - "+d1+" "+current_time)
    f.close()


@client.command(aliases=["clear"])
@commands.has_permissions(manage_messages=True)
async def c(ctx, amount):
    if str(amount) == "all":
        amount = 1000000000
        await ctx.channel.purge(limit=amount+1)
        await ctx.send(embed=discord.Embed(title="Clear ",
                                           description="I cleared all the messages!",
                                           color=0xff9f12))
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        f = open("log.txt", "a")
        f.write("\n"+"I cleared all messages - "+d1+" "+current_time)
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
        f.write("\n"+"Cleared "+str(amount)+" messages - "+d1+" "+current_time)
        f.close()


@client.command(aliases=["kick"])
@commands.has_permissions(kick_members=True)
async def k(ctx, member: discord.Member, *, reason="No specified reason"):
    await ctx.send(embed=discord.Embed(title="kick ",
                                       description="User "+str(member)+" was kicked!",
                                       color=0xff9f12))
    await member.send("You were kicked because: " + reason)
    await member.kick(reason=reason)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    f = open("log.txt", "a")
    f.write("\n"+str(member) + " was kicked - "+d1+" "+current_time)
    f.close()


@client.command(aliases=["ban"])
@commands.has_permissions(ban_members=True)
async def b(ctx, member: discord.Member, *, reason="No specified reason"):
    await member.send("You were banned because: "+reason)
    await member.ban(reason=reason)
    await ctx.send(embed=discord.Embed(title="Ban ",
                                       description="User " + str(member) + " was banned!",
                                       color=0xff9f12))
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    f = open("log.txt", "a")
    f.write("\n"+str(member) + " was banned "+str(reason)+" - " + d1 + " " + current_time)
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
            f.write("\n"+str(member) + " was unbanned - "+d1+" "+current_time)
            f.close()
            return
    await ctx.send(embed=discord.Embed(title="UnBan ",
                                       description="User " + str(member) + " was not found!",
                                       color=0xff9f12))


@client.command(aliases=["social"])
async def sm(ctx):
    await ctx.send(embed=discord.Embed(title="Social media",
                                       description=str("Insert your social media"),
                                       color=0xff9f12))


client.run("")
