import discord
from discord.ext import commands
import datetime
from urllib import parse, request
import re
import random
import asyncio
import aiohttp
from discord.utils import get
bot = commands.Bot(command_prefix='>', description="You're Go-to Twitch Channel")
bot.remove_command('help')

# Bot Status --------------------
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Some good content by: NAME", url="http://www.twitch.tv/"))
    print('Ready')

# Bot test ping command
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

# Commands ----------------------
  
# Meme Command (in embed) | Meme retrieved From Reddit
@bot.command(pass_context = True)
async def meme(ctx):
    embed = discord.Embed(title="Rizz Bot | You're best Meme Source.", description=None, color=0xB342FF)
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
        res = await r.json()
        embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
        await ctx.send(embed=embed, content=None)

# Socials Promo (in embed) when using command >socials
@bot.listen('on_message')
async def zsocials(message):
    if message.content.startswith('>socials'):
        embedVar = discord.Embed(title="<:line:811007894953787423> Here's a list of aariztxhir's socials: <:line:811007894953787423>",color=0xB342FF)
        embedVar.add_field(name="Youtube", value="<https://www.youtube.com/channel/UC2PB1vPxDgmVV56FBThGSBA>", inline=False)
        embedVar.add_field(name="Twitch", value="<https://www.twitch.tv/aariztxhir>", inline=False)
        embedVar.add_field(name="Instagram", value="<https://www.instagram.com/aariztxhir/>", inline=False)
        await message.channel.send(embed=embedVar)
        await bot.process_commands(message)

# Lie Test (in embed) command when using >cap
@bot.command()
async def cap(ctx,user:discord.User):
    num1 = 0
    num2 = 100
    try:
        numb = int(num1)
        numb = int(num2)
        value = random.randint(min(num1, num2), max(num1, num2))
        embedVar = discord.Embed(title= "Cap r8 machine",description = f"Hmm :thinking: {user.mention} dk bout that one, it lookin {value}% :billed_cap: to me ", color=0xB342FF)
        await ctx.send(embed=embedVar)
    except:
        await ctx.send(embed=embedVar)

# Peripherals List embed when using command >peripherals
@bot.listen('on_message')
async def zperipherals(message):
    if message.content.startswith('>peripherals'):
        embedVar = discord.Embed(title="<:line:811007894953787423> Here's a list of aariztxhir's peripherals: <:line:811007894953787423>", color=0xB342FF)
        embedVar.add_field(name="Keyboard", value="GK61 \n<https://www.amazon.ca/GK61-Mechanical-Gaming-Keyboard-Programmable/dp/B07PT9NRRY>", inline=False)
        embedVar.add_field(name="Mouse", value="Razer Viper\n <https://www.amazon.ca/Razer-Viper-Ultralight-Ambidextrous-Gaming/dp/B07TT8G59J>", inline=False)
        embedVar.add_field(name="Headset", value="Beexcellent Gaming Headset \n<https://www.amazon.ca/Beexcellent-Headset-Over-Ear-Headphones-Reduction/dp/B0777KYQS7?th=1>", inline=False)
        embedVar.add_field(name="Mouse Pad", value="Luxcom RGB Mousepad \n<https://www.amazon.ca/Oversized-Extended-Mousepad-%EF%BC%8CNon-Slip-Mat%EF%BC%8C31-5X/dp/B07M813YV1>", inline=False)
        await message.channel.send(embed=embedVar)
        await bot.process_commands(message)

# Computer Specs list (in embed) command >specs
@bot.listen('on_message')
async def zspecs(message):
    if message.content.startswith('>specs'):
        embedVar = discord.Embed(title="<:line:811007894953787423> Here's a list of aariztxhir's PC Specs: <:line:811007894953787423>", color=0xB342FF)
        embedVar.add_field(name="CPU", value="Ryzen 5 3600 \n<https://ca.pcpartpicker.com/product/9nm323/amd-ryzen-5-3600-36-thz-6-core-processor-100-100000031box>", inline=False)
        embedVar.add_field(name="GPU", value="GTX 1660ti \n<https://ca.pcpartpicker.com/product/c4F48d/evga-geforce-gtx-1660-ti-6-gb-sc-ultra-gaming-video-card-06g-p4-1667-kr>", inline=False)
        embedVar.add_field(name="RAM", value="16gb 3200mHz \n<https://ca.pcpartpicker.com/product/Cf98TW/gskill-memory-f43200c16d16gvkb>", inline=False)
        embedVar.add_field(name="STORAGE", value="500gb SSD + 1tb HDD \n<https://ca.pcpartpicker.com/product/zFK2FT/western-digital-blue-sn550-500-gb-m2-2280-nvme-solid-state-drive-wds500g2b0c>\n <https://ca.pcpartpicker.com/product/MwW9TW/western-digital-internal-hard-drive-wd10ezex>", inline=False)
        embedVar.add_field(name="CASE", value="DEEPCOOL MATREXX 50 ADD-RGB 4F \n<https://ca.pcpartpicker.com/product/YJfFf7/deepcool-matrexx-50-add-rgb-4f-atx-mid-tower-case-dp-atx-matrexx50-ar-4f-ne>", inline=False)
        await message.channel.send(embed=embedVar)
        await bot.process_commands(message)

# Server Info command (in embed) command >info
@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Server information brought to you by TTV/Rizz Bot", timestamp=datetime.datetime.utcnow(), color=0xB342FF)
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Member Count", value=f"{ctx.guild.member_count}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://i.ibb.co/9wXFKM7/Untitled.png")

    await ctx.send(embed=embed)

# Bot trigger message when mentioning word "streaming" promotes Twitch channel
@bot.listen()
async def on_message(message):
    if "streaming" in message.content.lower():
        await message.channel.send('Your lost udk where ur going if you dont watch https://www.twitch.tv/ on the daily')
        await bot.process_commands(message)

# Bot trigger message when mentioning word "yt" promotes YouTube channel
@bot.listen()
async def on_message(message):
    if message.content.startswith("yt"):
        await message.channel.send("Nah we dont need that we should watch youtube here's a good channel youtube: https://www.youtube.com/channel/")
        await bot.process_commands(message)

# User Info command (in embed) command >whois
@bot.command(aliases=["whois"])
async def userinfo(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)

    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.send(embed=embed)


# Final Help List Command (In Embed)
@bot.group(invoke_without_command=True)
async def help(ctx):
  em = discord.Embed(title ="Command List", color= 0xB342FF)
  em.add_field(name ="Memes", value = ">meme")
  em.add_field(name ="Server Info", value = ">info")
  em.add_field(name ="Cap r8", value = ">cap")
  em.add_field(name ="Peripherals", value = ">peripherals")
  em.add_field(name ="PC Specs", value = ">specs")
  em.add_field(name ="Socials", value = ">socials")
  em.set_thumbnail(url="https://i.ibb.co/Xy7XmvD/gears.png")
  await ctx.send(embed= em)

bot.run("TOKEN")