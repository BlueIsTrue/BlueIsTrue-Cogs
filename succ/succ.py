import discord
from discord.ext import commands
from random import choice as rndchoice
from .utils.dataIO import fileIO
from .utils import checks
import os


class Succ:
    """Succ command."""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True, invoke_without_command=True)
    async def givemethesucc(self, ctx, *, user: discord.Member=None):
        """Gives you succ"""
        botid = self.bot.user.id
            user = ctx.message.author
            await self.bot.say("**Slurp Slurp**")

def setup(bot):
    n = Succ(bot)
    bot.add_cog(n)
