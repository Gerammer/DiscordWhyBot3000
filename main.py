import discord
import requests
import json

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    prompt = 'why'  # Your bot's prompt
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + 'API_KEY'}
    data = {'context': prompt, 'max_tokens': 100}  #The max size of the question
    response = requests.post('https://api.aigpt2.com', headers=headers, data=json.dumps(data))
    res_data = response.json()
    bot_message = res_data['choices'][0]['text']
    if bot_message.startswith('why'):
        await message.channel.send(bot_message)
       

client.run('YOUR_DISCORD_TOKEN')
