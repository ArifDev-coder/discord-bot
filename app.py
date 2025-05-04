import random 
import os  # Mengimpor modul os untuk mengakses variabel lingkungan.
from dotenv import load_dotenv  # Mengimpor fungsi load_dotenv untuk memuat variabel dari file .env.
import discord  # Mengimpor pustaka Discord untuk membuat bot.
from discord.ext import commands  # Mengimpor modul commands untuk membuat bot berbasis perintah.
from katakata import pesan_motivasi  # Mengimpor variabel pesan_motivasi dari modul katakata.
from katakata import pesan_tebakan  # Mengimpor variabel pesan_tebakan dari modul katakata.
from katakata import pesan_toxic  # Mengimpor variabel pesan_toxic dari modul katakata.
from katakata import pesan_salam  # Mengimpor variabel pesan_salam dari modul katakata.
from katakata import pesan_jawaban # Mengimpor variable pasan_jawaban dari modul katakata.

load_dotenv()  # Memuat variabel lingkungan dari file .env.
TOKEN = os.getenv("TOKEN_BOT")  # Mengambil token bot dari variabel lingkungan.

intents = discord.Intents.default()  # Membuat objek intents dengan pengaturan default.
intents.message_content = True  # Mengaktifkan intent untuk membaca konten pesan.
bot = commands.Bot(command_prefix="!", intents=intents)  # Membuat instance bot dengan prefix "!" dan intents.

@bot.event
async def on_ready():  # Event handler yang dijalankan saat bot berhasil online.
    print(f"Bot {bot.user} sudah online!")  # Menampilkan pesan di konsol saat bot online.

@bot.event
async def on_message(message):  # Event handler untuk menangani pesan yang diterima bot.
    if message.author == bot.user:  # Mengecek apakah pesan dikirim oleh bot sendiri.
        return  # Jika ya, abaikan pesan tersebut.

    # Proses perintah bot
    await bot.process_commands(message)  # Memproses perintah yang dikirim oleh pengguna.

    # Respon salam
    if any(kata in message.content.lower() for kata in pesan_salam):  # Mengecek apakah pesan mengandung kata salam.
        await message.channel.send(f"{random.choice(pesan_jawaban)}, {message.author.name}!")  # Mengirim balasan salam.

    # Tebak-tebakan
    if "tebakan" in message.content.lower():  # Mengecek apakah pesan mengandung kata "tebakan".
        await message.channel.send(random.choice(pesan_tebakan))  # Mengirim pesan tebak-tebakan.
    if "awk" in message.content.lower():  # Mengecek apakah pesan mengandung kata "awk".
        await message.channel.send(f"Hahaha lucukan {message.author.name}")  # Mengirim balasan lucu.
    if "anjay" in message.content.lower():  # Mengecek apakah pesan mengandung kata "anjay".
        await message.channel.send("Terkesan?")  # Mengirim balasan "Terkesan?".

@bot.command()
async def halo(ctx):  # Command untuk mengirim pesan "Halo dari bot Zarick".
    await ctx.send("Halo dari bot Zarick. Saya adalah Bot yang dikembangkan oleh tim SpaceEnd https://discord.gg/JDzHU32WVr")  # Mengirim pesan ke channel.

@bot.command()
async def tambah(ctx, a: int, b: int):  # Command untuk menjumlahkan dua angka.
    hasil = a + b  # Menjumlahkan angka a dan b.
    await ctx.send(f"Hasil dari {a} + {b} = {hasil}")  # Mengirim hasil penjumlahan.

@bot.command()
async def akardari(ctx, a: int):  # Command untuk menghitung akar dari sebuah angka.
    hasil = a**0.5  # Menghitung akar kuadrat dari angka a.
    await ctx.send(f"Akar dari {a} adalah {hasil}")  # Mengirim hasil perhitungan.

@bot.command()
async def motivasi(ctx):  # Command untuk mengirim pesan motivasi.
    await ctx.send(random.choice(pesan_motivasi))  # Mengirim pesan motivasi yang diambil dari modul katakata.

@bot.command()
async def jawab(ctx):  # Command untuk memeriksa pesan terakhir di channel.
    messages = []  # Membuat list kosong untuk menyimpan pesan.

    async for message in ctx.channel.history(limit=2):  # Mengambil dua pesan terakhir dari channel.
        messages.append(message)  # Menambahkan pesan ke dalam list.

    last_message = messages[1]  # Mengambil pesan terakhir sebelum command.

    # Cek jika isi pesan terakhir adalah "HELLO"
    if last_message.content.upper() == "HELLO":  # Mengecek apakah pesan terakhir adalah "HELLO".
        await ctx.send(f"Jawaban {last_message.content} adalah benar")  # Mengirim balasan benar.
    elif any(word in last_message.content.upper() for word in pesan_toxic):  # Mengecek apakah pesan mengandung kata toxic.
        await ctx.send(f"WADUH GA BOLEH TOXIC BRO 🗿")  # Mengirim peringatan untuk tidak toxic.
    else:  # Jika tidak sesuai dengan kondisi di atas.
        await ctx.send(f"Jawaban {last_message.content} belum benar")  # Mengirim balasan belum benar.

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! Bot sedang online, waktu respon: {round(bot.latency * 1000)}ms")

bot.run(TOKEN)  # Menjalankan bot dengan token yang telah diambil.