const fetch = require('node-fetch');
const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
  console.log(`Bot is ready as: ${client.user.tag}`);
});

client.on('message', msg => {
  if (msg.author.bot) return; // Ignore bots
  
  const prompt = 'why'; // Your bot's prompt
  fetch('https://api.aigpt2.com', {
    method: 'post',
    body: JSON.stringify({
      'context': prompt,
      'max_tokens': 100  // the max size of the question
    }),
    headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + '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' + '527d62d12175703ca72e4e54842b65374d64a95288e400e9968e8243bc556beb'}
  })
    .then(response => response.json())
    .then(data => {
      const message = data['choices'][0]['text']
      if (message.startsWith('why')) {
        msg.channel.send(message);
      } 
    });
});

client.login('Your Discord Bot Token');