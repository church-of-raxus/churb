#-------------------------------import----------------------------------#
import discord, asyncio, datetime
#-----------------------------------------------------------------------#


#-------------------------------variables-------------------------------#
client = discord.Client()
TOKEN = 'ODIyMTIwOTMyOTQ0MTE3Nzcw.YFNpyA.WTpHSioOjiAPw8OmKEo_LM2xQFU'
CHAT_ID = 777617289519824949 # Text Channel ID
#-----------------------------------------------------------------------#

#Sends a message to CHAT_ID
async def sendMessage(message):
    await client.get_channel(CHAT_ID).send(message)

#Is called once per asyncio.sleep(seconds)
async def time():
    await client.wait_until_ready()
    while 1:
        await sendMessage("Tell your pals about this place!")
        await asyncio.sleep(300)

#@client.event
#async def on_ready():

# On new message    
@client.event
async def on_message(message):
    
    # To prevent bot from messaging itself
    if message.author == client.user:
        return

    if 'raxus' in message.content.lower():
        await sendMessage("*Church*")

    if message.content.lower() == '!quote':
        await sendMessage("Quote placeholder")

    if 'web' in message.content.lower():
        await sendMessage("https://raxus-church.ml")
    
client.loop.create_task(time()) # Make needed loop
client.run(TOKEN) # Launch bot
