import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print(f'Бот {bot.user.name} готов к работе.')

@bot.command()
async def calc(ctx, *, expression):
    try:
        result = eval(expression)
        await ctx.send(f'Результат: {result}')
    except Exception as e:
        await ctx.send(f'Произошла ошибка: {e}')

# Токен вашего бота
bot_token = 'YOUR_BOT_TOKEN'
bot.run(bot_token)
