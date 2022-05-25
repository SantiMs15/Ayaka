import googletrans
import lightbulb
import hikari

bot = lightbulb.BotApp(token= 'OTc4ODMzOTIzODcyMjcyMzg0.GpnhW4.UAifPG6NuEYViOFXyY_HP_yEllnnUdCaF020Zk',                                                                                                                                                              
 default_enabled_guilds=(978839879255490664))

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print ('Lets translate')

@bot.command
@lightbulb.command('translate', 'This will translate a short sentence said by a member of the voice chat!')
@lightbulb.implements(lightbulb.SlashCommand)
async def Translate(ctx):   
    await ctx.respond('I can hear you now!')

bot.run()
