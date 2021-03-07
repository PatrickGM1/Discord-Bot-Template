import asyncio
import discord
from discord.ext import commands
import time
from random import choice

client = commands.Bot(command_prefix="+")

game = discord.Game("StreamHub Mod 24/7 On. Come join us")
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=game)
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command()
async def hello(ctx):
    await ctx.send("Salutare smechere")


@client.command(aliases=["commenzi"])
async def comenzi(ctx):
    await ctx.send(embed = discord.Embed(title="Comenzi ", description="***Comenzile mele:\n1. hello\n2. comenzi\n3. clear\n4. kick\n5. ban\n6. unban\n7. mute\n8. unmute*** ", color=0xff9f12))


@client.command(aliases=["mute"])
@commands.has_permissions(kick_members = True)
async def m(ctx,member: discord.Member):
    muted_role = ctx.guild.get_role(818119933509500958)
    await member.add_roles(muted_role)
    await ctx.send(embed = discord.Embed(title="Mute ", description="User-ul "+str(member)+" a primit mute!", color=0xff9f12))


@client.command(aliases=["unmute"])
@commands.has_permissions(kick_members = True)
async def um(ctx,member: discord.Member):
    muted_role = ctx.guild.get_role(818119933509500958)
    await member.remove_roles(muted_role)
    await ctx.send(embed = discord.Embed(title="Mute ", description="User-ul "+str(member)+" a primit unmute!", color=0xff9f12))


@client.command(aliases=["clear"])
@commands.has_permissions(manage_messages = True)
async def c(ctx,amount):
    if(str(amount)=="all"):
        amount=1000000000
        await ctx.channel.purge(limit=amount+1)
        await ctx.send(embed = discord.Embed(title="Clear ", description="Am sters toate mesajele!", color=0xff9f12))
    else:
        await ctx.channel.purge(limit=int(amount)+1)
        await ctx.send(embed = discord.Embed(title="Clear ", description="Am sters "+str(amount)+" mesaje!", color=0xff9f12))
    time.sleep(2)
    await ctx.channel.purge(limit=1)


@client.command(aliases=["kick"])
@commands.has_permissions(kick_members = True)
async def k(ctx,member: discord.Member,*,reason="No specified reason"):
    await ctx.send(embed = discord.Embed(title="kick ", description="User-ul "+str(member)+" a primit kick!", color=0xff9f12))
    await member.send("Ai primit kick de pe server deoarece: " + reason)
    await member.kick(reason=reason)


@client.command(aliases=["ban"])
@commands.has_permissions(ban_members = True)
async def b(ctx,member: discord.Member,*,reason="No specified reason"):
    await member.send("Ai primit ban de pe server deoarece: "+reason)
    await member.ban(reason=reason)
    await ctx.send(embed=discord.Embed(title="Ban ", description="User-ul " + str(member) + " a primit ban!", color=0xff9f12))


@client.command(aliases=["unban"])
@commands.has_permissions(ban_members = True)
async def ub(ctx, *,member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc= member.split('#')
    for banned_entry in banned_users:
        user= banned_entry.user

        if(user.name, user.discriminator)==(member_name,member_disc):
            await ctx.guild.unban(user)
            await ctx.send(embed=discord.Embed(title="UnBan ", description="User-ul " + str(member) + " a primit UnBan!", color=0xff9f12))
            return
    await ctx.send(embed=discord.Embed(title="UnBan ", description="User-ul " + str(member) + " nu a fost gasit!", color=0xff9f12))


#music bot


client.run("ODE4MDg0Njg5MTA5NDUwNzgy.YES6vQ.V7jd57b38lDF9FwjvsB7PiZHnPY")