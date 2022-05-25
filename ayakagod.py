import googletrans
import lightbulb
import hikari

bot = lightbulb.BotApp(token='OTc4ODMzOTIzODcyMjcyMzg0.GowF-e.xaQLY98OToMZf-lzXVHdOcE0_sH9VVF0HZujO8', 
default_enabled_guilds=(978839879255490664))

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print ('Lets translate')

@bot.command
@lightbulb.command('translate', 'On it!')
@lightbulb.implements(lightbulb.SlashCommand)
async def Translate(ctx):
    await ctx.respond('On it!')

bot.run()