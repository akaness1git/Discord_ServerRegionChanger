import discord

client = discord.Client()

region_london = 'ロンドン'
region_japan = '日本'
region_hongkong = '香港'

change_bef = 'に変更します。'
change_aft = 'に変更しました。'
    
@client.event
async def on_ready():
    print('Botを起動しました。')

@client.event
async def on_message(message):
    if message.content.startswith('!region london'):
        await client.send_message(message.channel, region_london + change_bef)
        await client.edit_server(message.server,region='london')
        await client.send_message(message.channel, region_london + change_aft)
    elif message.content.startswith('!region japan'):
        await client.send_message(message.channel, region_japan + change_bef)
        await client.edit_server(message.server,region='japan')
        await client.send_message(message.channel, region_japan + change_aft)
    elif message.content.startswith('!region hongkong'):
        await client.send_message(message.channel, region_hongkong + change_bef)
        await client.edit_server(message.server,region='hongkong')
        await client.send_message(message.channel, region_hongkong + change_aft)
    elif message.content.startswith('!ikiteru'):
        reply = '生きてます'
        await client.send_message(message.channel, reply)

#ここにbotのアクセストークンを入力
client.run('***')