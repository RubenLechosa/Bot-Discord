from discord.ext import commands, tasks
import discord
import asyncio
import os

########################################################################################################################
# Paste your token and a custom prefix right here:
dc_token = "OTA1MTkyODk4MjI2NjgzOTM0.YYGglA.dv-qTzfBFikZgld7hf2dtAyC9S0"  # DISCORD-TOKEN
dc_prefix = "!!"  # BOT-PREFIX

########################################################################################################################

greencolors = [0x4cd137, 0x44bd32, 0xA3CB38]
redcolors = [0xeb4d4b, 0xff7979, 0xee5253]
bluecolors = [0x74b9ff, 0x487eb0, 0x686de0]

timeout = 35
waitmsg = "⏳ | Buscando los mejores memes para ti..."
donemsg = "✅ | **Tengo algo muy bueno**"
no_msg = "❎ | **Okay.**"
timeout_msg = "☕ | **Un momento porfa, algo va mal**"
