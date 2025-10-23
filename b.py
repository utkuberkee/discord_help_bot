import discord
from discord.ext import commands

import os

from model import get_class


IMAGE_DIR   = "image"
os.makedirs(IMAGE_DIR, exist_ok=True)#klasör yoksa klasör yap


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def analiz(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename  #eklerin dosya adını alıyoruz
            file_path = os.path.join(IMAGE_DIR, file_name)
            try:
                await attachment.save(file_path)
                await ctx.send(f"Görsel başarı ile kaldedildi!{file_path}")

                class_name, score = get_class(image_path=file_path)

                await ctx.send(f"Görselinizin sınıfı={class_name}, tahmin scoru={score}")
                if class_name == "ceket":
                    await ctx.send("Ceketi iş görüşmelerine giderken giyebilirsiniz.Onun dışında yanınızda sıcak durmak için taşıyabilirsiniz.")
                elif class_name == "gomlek":
                    await ctx.send("Gömlekleri düğünlerde,iş görüşmelerinde giyebilirsiniz fakat giymeden önce ütü yapmayı unutmayın!")
                elif class_name == "elbise":
                    await ctx.send("Elbiseleri partilerde giyebilirsiniz ama dikkatli bakın hemen yıpranabiliyorlar!")
                elif class_name == "pantolon":
                    await ctx.send("Pantolonu her zaman giyebilirsiniz ama hareket alanınızı kısıtlayabilir.")
            except:
                await ctx.send("Hata çıktı,daha sonra tekrar deneyiniz(Error Code 2)")
    else:
        await ctx.send("Hata çıktı,fotoğraf koyunuz!(Error Code 1)")


bot.run("Tokeb")

