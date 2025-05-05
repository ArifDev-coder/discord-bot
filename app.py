from discord import Intents
from discord.ext import commands
from discord import Bot
import random
import os
from dotenv import load_dotenv
from katakata import pesan_motivasi, pesan_tebakan, pesan_toxic, pesan_salam, pesan_jawaban

load_dotenv()
TOKEN = os.getenv("TOKEN_BOT")

intents = Intents.default()
intents.message_content = True

bot = Bot(intents=intents)  # <-- Gunakan discord.Bot untuk slash commands

# ? Bot Event
@bot.event
async def on_ready():
    print(f"Bot {bot.user} sudah online!")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    content = message.content.lower()

    if any(word in content for word in pesan_salam):
        await message.channel.send(f"{random.choice(pesan_jawaban)}, {message.author.name}")

    if any(word in content for word in pesan_toxic):
        await message.channel.send(f"Waduh, Jangan toxic ya {message.author.name}")

    if "tebakan" in content:
        await message.channel.send(random.choice(pesan_tebakan))

    if "awk" in content:
        await message.channel.send(f"Hahaa lucu ya, {message.author.name}")

    if "anjay" in content:
        await message.channel.send(f"Kamu terkesan {message.author.name}")

    await bot.process_application_commands(message)


# ? Bot Command
@bot.slash_command(name="halo", description="Memberi salam dari bot Zarick")
async def halo(ctx):
    await ctx.respond("Halo dari bot Zarick. Saya adalah Bot yang dikembangkan oleh tim SpaceEnd https://discord.gg/JDzHU32WVr")

@bot.slash_command(name="tambah", description="Menambahkan dua angka")
async def tambah(ctx, a: int, b: int):
    hasil = a + b
    await ctx.respond(f"Hasil dari {a} + {b} = {hasil}")

@bot.slash_command(name="motivasi", description="Mengirimkan pesan motivasi")
async def motivasi(ctx):
    await ctx.respond(random.choice(pesan_motivasi))

@bot.slash_command(name="ping", description="Cek status bot")
async def ping(ctx):
    await ctx.respond(f"Pong! Bot sedang online, waktu respon: {round(bot.latency * 1000)}ms")

bot.run(TOKEN)