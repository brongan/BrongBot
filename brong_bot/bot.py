#!/bin/env python3
import logging

from discord.ext import commands
from brong_bot.secrets_manager import get_discord_api_key
from brong_bot.servers import get_instance, start_server, get_status, stop_server

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)

bot = commands.Bot(command_prefix=">")


@bot.command()
async def start(ctx, arg):
    instance = get_instance(arg)
    if not instance:
        await ctx.send(f"Unknown server: {arg}")
        return
    dns_name = start_server(instance)
    await ctx.send(f"Join at {dns_name}")


@bot.command()
async def status(ctx, arg):
    instance = get_instance(arg)
    if not instance:
        await ctx.send(f"Unknown server: {arg}")
        return
    await ctx.send(f"Server {arg} status: {get_status(instance)}")


@bot.command()
async def stop(ctx, arg):
    instance = get_instance(arg)
    if not instance:
        await ctx.send(f"Unknown server: {arg}")
        return
    stop_server(instance)
    await ctx.send("Server Stopped")


def main():
    api_key = get_discord_api_key()
    bot.run(api_key)


if __name__ == "__main__":
    main()
