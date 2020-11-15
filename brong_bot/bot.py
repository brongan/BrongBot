#!/bin/env python3
import logging

from discord.ext import commands
from brong_bot.secrets_manager import get_discord_api_key
from brong_bot.servers import EC2_Instances, startServer, stopServer

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)

bot = commands.Bot(command_prefix=">")


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.command()
async def start_factorio(ctx):
    await ctx.send("Starting Factorio Server")
    dns_name = startServer(EC2_Instances.Factorio)
    await ctx.send(f"Join at:  {dns_name}:34197")


@bot.command()
async def stop_factorio(ctx):
    await ctx.send("Stopping Factorio Server")
    stopServer(EC2_Instances.Factorio)
    await ctx.send("Server Stopped")


@bot.command()
async def start_minecraft(ctx):
    await ctx.send("Starting Minecraft Server")
    dns_name = startServer(EC2_Instances.Minecraft)
    await ctx.send(f"Please wait a few minutes and join at {dns_name}:25565")


@bot.command()
async def stop_minecraft(ctx):
    await ctx.send("Stopping Minecraft Server")
    stopServer(EC2_Instances.Minecraft)
    await ctx.send("Server Stopped")


def main():
    api_key = get_discord_api_key()
    bot.run(api_key)


if __name__ == "__main__":
    main()
