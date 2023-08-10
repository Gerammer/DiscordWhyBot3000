import discord
import requests
import json

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'
    .format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello.')
    
    prompt = 'why'  # Your bot's prompt
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + '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'}
    data = {'context': prompt, 'max_tokens': 100}  #The max size of the question
    response = requests.post('https://api.aigpt2.com', headers=headers, data=json.dumps(data))
    res_data = response.json()
    bot_message = res_data['choices'][0]['text']
    if bot_message.startswith('why'):
        await message.channel.send(bot_message)
       

client.run('MTEzOTI1NjkzOTg2MDIwNTYzOA.GjTDfI.g-yaNhPeiu6FV3YO2Lbb_y4pqQuqKNMzRJbSe0')
