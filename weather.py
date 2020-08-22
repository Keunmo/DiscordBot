# import discord, asyncio
from googletrans import Translator
import requests, discord, json

with open('token.json') as token_file:
    token_data = json.load(token_file)
    weather_token = token_data["weather_token"]

class Weather:
    def __init__(self, msg, bot):
        self.msg = msg
        self.bot = bot
        self.weather_key = weather_token
    
    async def weather(self, args='서울'):   # 도시명을 입력하지 않았을 경우, 서울이 기본값으로 표시됩니다
        ''' Show weather condition. Usage : $weather <city name>. 도시명은 영문으로 입력해야 합니다. 한국 일부 도시들에 한해 한글입력을 지원합니다. '''
            
        translator = Translator()
        trans = translator.translate(args, dest='en')
        if trans.src == 'ko':
            args = trans.text
        if ' ' in args:
            args = args.replace(' ', '')
        if '-' in args:
            args = args.replace('-', '')
        # print('city input trans:',args)
            
        url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': args, 'appid': self.weather_key, 'units': 'metric', 'lang': 'kr'}
        response = requests.get(url, params = params).json()
        if ('message' in response.keys()):
            embed = discord.Embed(title=f"Error!", description=f'''
            존재하지 않는 도시입니다. 다시 시도해 주세요.\n
            Usage: \n
            $weather 도시명\n
            또는 "도시 날씨" ''')
            return await self.msg.channel.send(embed=embed)
        
        city_name = response["name"]
        # print('city output:   ',city_name)
        tran_res = translator.translate(city_name, src='en', dest='ko')
        # print('city output trans:',tran_res.text)
        weather_main = response["weather"][0]["description"]
        temp = response["main"]["temp"]
        feels_like = response["main"]["feels_like"]
        temp_min = response["main"]["temp_min"]
        temp_max = response["main"]["temp_max"]
        humidity = response["main"]["humidity"]
        if(200 <= response["weather"][0]["id"] <= 299):
            emoji = '⚡️'
        elif(300 <= response["weather"][0]["id"] <= 499):
            emoji = '🌧'
        elif(500 <= response["weather"][0]["id"] <= 599):
            emoji = '☔'
        elif (600 <= response["weather"][0]["id"] <= 699):
            emoji = '☃️'
        elif (700 <= response["weather"][0]["id"] <= 799):
            emoji = '🌫'
        elif (response["weather"][0]["id"] == 800):
            emoji = '☀️'
        elif (801 <= response["weather"][0]["id"] <= 804):
            emoji = '☁️'
        if emoji =='⚡️' or emoji =='🌧' or emoji =='☔' or emoji =='☃️':
            embed = discord.Embed(title=f"현재 %s의 날씨는 %s입니다. %s" %(tran_res.text, weather_main, emoji), description=f"우산을 챙기세요.")
        else:
            embed = discord.Embed(title=f"현재 %s의 날씨는 %s입니다. %s" %(tran_res.text, weather_main, emoji))
        embed.add_field(name=f"온도", value=f"현재온도 : %d℃\n체감온도 : %d℃\n최고온도 : %d℃\n최저온도 : %d℃\n" %(temp, feels_like, temp_max, temp_min))
        embed.add_field(name=f"습도", value=f"현재습도 : %d%%" %(humidity))
        await self.msg.channel.send(embed=embed)

# bot = commands.Bot(command_prefix="$", activity=discord.Activity(name="Weather Bot | $help", type=1), description='Weather Bot')

# @bot.event
# async def on_ready():
#     print('Logged in as {0} ({0.id})'.format(bot.user))
#     print('------')

# bot.add_cog(Weather(bot))

# bot.run(token)
