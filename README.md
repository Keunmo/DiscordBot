# Discord Weather Bot
This bot is part of [2020 Jaram Summer Workshop](https://github.com/Jaram2020/Discord-MessageBot).  

# How to use
This description is written for Unix environments. - Mac OS, Ubuntu, Debian, Wsl, etc.  
1. Clone repository. 
```
git clone https://github.com/Keunmo/DiscordBot.git
```
2. move to cloned repository.
```
cd DiscordBot
```
3. set python environments.
```
python -m venv dicoenv
```
4. activate venv.
```
source dicoenv/bin/activate
```
5. install requirements.
```
pip3 install -r requiremments.txt
```
6. get your Discord token and OpenWeatherMap token.  
Discord: https://discord.com/developers/applications/  
OWM: https://home.openweathermap.org/api_keys  

7. make __token.json__ file and write your token in __token.json__ file. 
```
cp token.json.sample token.json
```
8. add your bot to server.  
https://realpython.com/how-to-make-a-discord-bot-python/#adding-a-bot-to-a-guild  
9. run bot. 
```
python3 main.py
```