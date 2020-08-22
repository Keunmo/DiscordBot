import discord, asyncio, json
from weather import Weather

with open('token.json') as token_file:
    token_data = json.load(token_file)
    discord_token = token_data["discord_token"]

token = discord_token
bot = discord.Client()

async def msgEmbed(msg, title, description):
    embed = discord.Embed(title=title, description=description)
    return await msg.channel.send(embed=embed)

@bot.event
async def on_ready():
    print('Logged in as {0} {1}'.format(bot.user.name, bot.user.id))
    print('------')
    game = discord.Game("Simple Bot | 일기예보")
    await bot.change_presence(status=discord.Status.online, activity=game)

    
@bot.event
async def on_message(msg):
    if msg.content == "$help":
        embed = discord.Embed(title=f"Help", description=f'''
            Usage: \n
            $weather 도시명\n
            또는 "도시 날씨" ''')
        await msg.channel.send(embed=embed)
    
    if msg.content.startswith("$weather"):
        message = msg.content.split(" ")
        show = Weather(msg, bot)
        if (len(message) == 1):
            await show.weather()
        else:
            await show.weather(message[1])
    
    if "날씨" in msg.content:
        message = msg.content.split("날씨")
        city = message[0].rstrip()
        city = city.split(' ')[-1]
        # print(city)
        # await msg.channel.send(message)
        show = Weather(msg, bot)
        if city == '':
            await show.weather()
        else:
            await show.weather(city)
        # if (len(message) == 2):
        #     await show.weather(message[0])
        # else:
        #     await show.weather()

bot.run(token)
