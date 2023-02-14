import discord
import os
from discord.ui import Select, View, Button
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(debug_guilds=[guild_id], intents=intents)
