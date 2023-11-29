import discord
from discord.ext import commands
import random
import requests
from bs4 import BeautifulSoup
import asyncio

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="!",intents=intents)

TOKEN = open("token.txt","r").read()

#uye giris bildirim
@client.event
async def on_member_join(member):
    channel=discord.utils.get(member.guild.text_channels,name="gelen-giden")
    await channel.send(f"{member.mention} Aramiza Hosşgeldin!")
    print(f"{member} Aramiza Hosşgeldin!")
#uye cikis bildirim
@client.event
async def on_member_remove(member):
    channel=discord.utils.get(member.guild.text_channels,name="gelen-giden")
    await channel.send(f"{member.mention} Aramizdan Ayrildi :(")
    print(f"{member} Aramizdan Ayrildi :(")
#ses kanali giris
@client.command(pass_context=True)
async def join(ctx):
    if(ctx.author.voice):
        channel=ctx.message.author.voice.channel
        await channel.connect()

    else:
        await ctx.send("Herhangi bir ses kanalinda degilsin!")
#ses kanali cikis
@client.command(pass_context=True)
async def leave(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("ses kanalindan ayrildim!")
    else:
        await ctx.send("Herhangi bir ses kanalinda deigilim")
#muho replik
@client.command()
async def muho(ctx):
    await ctx.send("yaktin beni muharrem :d")
#muho emoji
@client.command()
async def muharrem(ctx):
    await ctx.send("muho:https://cdn.discordapp.com/emojis/1073244276886097930.webp?size=96&quality=lossless")
#muho muzik
@client.command()
async def muhomuzik(ctx):
    await ctx.send("https://www.youtube.com/watch?v=zBay15AeVdM")
#mesaj silme
@client.command()
async def clean(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
#oyun
@client.command()
async def oyun(ctx):

    rock = 1
    paper = 2
    scissors = 3
    rounds = 0
    pc = 0
    choice = 0
    x = 0
    y = 0

    await ctx.send("tas=1 , kagit=2 , makas=3\n")

    while x < 3 and y < 3:

        await ctx.send("Seciminizi girin: ")       

        def check(m):
            return m.author == ctx.author and m.content.isdigit()
        
        try:
            choice = int((await client.wait_for("message", check=check, timeout=30.0)).content)
        except asyncio.TimeoutError:
            await ctx.send("30 saniye içinde değer girmediniz.")
            break
            
        print("\n")
        pc = random.randint(1, 3)

        if choice == 1:
            if pc == 3:
                await ctx.send("Girdiginiz deger: tas\n")
                await ctx.send("PC nin girdigi deger: makas\n")
                await ctx.send("Kazandin\n")
                await ctx.send("-----------------------------------------------------------------------\n")
            elif pc == 2:
                await ctx.send("Girdiginiz deger: tas\n")
                await ctx.send("PC nin girdigi deger: kagit\n")
                await ctx.send("Kaybettin\n")
                await ctx.send("-----------------------------------------------------------------------\n")
            elif pc == 1:
                await ctx.send("Girdiginiz deger: tas\n")
                await ctx.send("PC nin girdigi deger: tas\n")
                await ctx.send("Berabere\n")
                await ctx.send("-----------------------------------------------------------------------\n")
        elif choice == 2:
            if pc == 1:
                await ctx.send("Girdiginiz deger: kagit\n")
                await ctx.send("PC nin girdigi deger: tas\n")
                await ctx.send("Kazandin\n")
                await ctx.send("-----------------------------------------------------------------------\n")
            elif pc == 3:
                await ctx.send("Girdiginiz deger: kagit\n")
                await ctx.send("PC nin girdigi deger: makas\n")
                await ctx.send("Kaybettin\n")
                await ctx.send("-----------------------------------------------------------------------\n")
            elif pc == 2:
                await ctx.send("Girdiginiz deger: kagit\n")
                await ctx.send("PC nin girdigi deger: kagit\n")
                await ctx.send("Berabere\n")
                await ctx.send("-----------------------------------------------------------------------\n")
        elif choice == 3:
            if pc == 2:
                await ctx.send("Girdiginiz deger: makas\n")
                await ctx.send("PC nin girdigi deger: kagit\n")
                await ctx.send("Kazandin\n")
                await ctx.send("-----------------------------------------------------------------------\n")
            elif pc == 1:
                await ctx.send("Girdiginiz deger: makas\n")
                await ctx.send("PC nin girdigi deger: tas\n")
                await ctx.send("Kaybettin\n")
                await ctx.send("-----------------------------------------------------------------------\n")
            elif pc == 3:
                await ctx.send("Girdiginiz deger: makas\n")
                await ctx.send("PC nin girdigi deger: makas\n")
                await ctx.send("Berabere\n")
                await ctx.send("-----------------------------------------------------------------------\n")
        else:
            await ctx.send("Yanlis bir deger girdiniz\n")
            await ctx.send("-----------------------------------------------------------------------\n")

        while True:
            if (choice == 1 and pc == 3) or (choice == 2 and pc == 1) or (choice == 3 and pc == 2):
                x += 1
                await ctx.send("skor = {}-{}".format(x, y))
                await ctx.send("-----------------------------------------------------------------------")
                break
            elif (choice == 1 and pc == 2) or (choice == 2 and pc == 3) or (choice == 3 and pc == 1):
                y += 1
                await ctx.send("skor = {}-{}".format(x, y))
                await ctx.send("-----------------------------------------------------------------------")
                break
            else:
                await ctx.send("skor = {}-{}".format(x, y))
                await ctx.send("-----------------------------------------------------------------------")
                break

        if x == 3:
            await ctx.send("TEBRİKLER! KAZANDİN.")
            break
        elif y == 3:
            await ctx.send("OYUNU KAYBETTİN.")
            break
@client.command()
async def hanicikiyodunabi(ctx):
    await ctx.send("SANANE LAN YARRAM!")

@client.command()
async def kur(ctx):
    await ctx.send("Lutfen hangi kura bakmak istiyorsaniz onun birimini girin: ")

    def check(msg):
        return msg.author==ctx.author and msg.channel==ctx.channel
    
    try:
        msg=await client.wait_for("message",check=check,timeout=30)
        stringDegeri=msg.content
        await ctx.send(f"Bakmak istediginiz kur: {stringDegeri}")
    except TimeoutError:
        await ctx.send("Zaman asimina ugradiniz lutfen tekrar deneyin!")

    while True:
        url = f"https://www.google.com/finance/quote/{stringDegeri}-TRY?sa=X&ved=2ahUKEwijjevyzNn_AhWuRPEDHXEGBgoQmY0JegQIBhAc"

        r = requests.get(url)
        soup = BeautifulSoup(r.text,"lxml")

        usd_try = soup.find_all("div", class_ = "YMlKec fxKbKc")
    
        for content in usd_try:
            await ctx.send(f"Anlik 1 {stringDegeri}= {content.text} TRY dir")

        break

@client.command()
async def coin(ctx):
    await ctx.send("Lutfen hangi coine bakmak istiyorsaniz onun birimini girin: ")

    def check(msg):
        return msg.author==ctx.author and msg.channel==ctx.channel
    
    try:
        msg=await client.wait_for("message",check=check,timeout=30)
        stringDegeri=msg.content
        await ctx.send(f"Bakmak istediginiz coin: {stringDegeri}")
    except TimeoutError:
        await ctx.send("Zaman asimina ugradiniz lutfen tekrar deneyin!")

    while True:
        url = f"https://www.google.com/finance/quote/{stringDegeri}-USD?sa=X&ved=2ahUKEwj8yumX3dn_AhVySvEDHbSbB4QQ-fUHegQIChAf"

        r = requests.get(url)
        soup = BeautifulSoup(r.text,"lxml")

        usd_try = soup.find_all("div", class_ = "YMlKec fxKbKc")
    
        for content in usd_try:
            await ctx.send(f"Anlik 1 {stringDegeri}= {content.text} USD dir")

        break

client.run(TOKEN)