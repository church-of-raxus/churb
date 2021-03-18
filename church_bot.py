#-------------------------------import----------------------------------#
import discord, asyncio, datetime, random
#-----------------------------------------------------------------------#


#-------------------------------variables-------------------------------#
client = discord.Client()
TOKEN = 'ODIyMTIwOTMyOTQ0MTE3Nzcw.YFNpyA.ZpBl82cyxEUpRBFPTfQ5UV6swFA'
CHAT_ID = 777617289519824949 # Text Channel ID
quotes = ["I'd never name a baby 'mommy milkers'", "People don’t think it be like it is, but it do.", "You’ll always be my little pogchamp", "Everyone asks if they’re my little pogchamp, but no one ever asks how their server dad is doing", "You're walking in the Caledon Fairgrounds\nThere's no one around and your phone is dead\nOut of the corner of your eye you spot him:\nKan Gao.\nHe's following you, about 30 mooses back.\nHe gets down on all fours and starts shouting probably copyrighted attack warcries\nHe's galloping at you.\nKan Gao.\nYou're looking for the World’s Smallest Ferris Wheel but you're all turned around\nHe's almost upon you now\nAnd you can see there's blood on his face\nMy God, there's tentacles too!\nRunning for your life (from Kan Gao)\nHe's brandishing long cat (holding a knife)\nCthulhu tentacles spreading out (from Kan Gao)\nIndie Game developer Kan Gao", "In 2003, I was camping in the Chilean mountains. After an Ayahuasan ceremony, a Canadian group camped near by. A man, who I had never met before, snuck into my tent mid-trip and made me write out my hallucinations on alpaca wool, using macaroni, Capri-Suns, and raccoon feces. His name was Kan Gao and my name is Quincy.", "Breasts are temporary. Rome is forever.", "Nothing wrong with me loving Moony's mommy milkers", "Pure-chan...\nNyaaa", "I want Pure to take a picture of my crotch.", "Mommy milkers", "*lights a cigarette*", "I’ll show you true pain.", "If humans are innately good, why aren’t all shopping carts returned?", "The worst part of growing up is when no one gets excited if you poop in the toilet."]
#-----------------------------------------------------------------------#

#Sends a message to CHAT_ID
async def sendMessage(message):
    await client.get_channel(CHAT_ID).send(message)

#Is called once per asyncio.sleep(seconds)
#async def time():
#    await client.wait_until_ready()
#    while 1:
#        await sendMessage("Tell your pals about this place!")
#        await asyncio.sleep(300)

#@client.event
#async def on_ready():

# On new message    
@client.event
async def on_message(message):
    
    if get(message.author.roles, name="Father Raxus"):
        await sendMessage("Yes, m'lord :pray:")
    
    # To prevent bot from messaging itself
    elif message.author == client.user:
        pass

    elif 'raxus' in message.content.lower():
        await sendMessage("Our Lord :pray:")

    elif message.content.lower() == '!quote':
        #generate random quote
        await sendMessage(random.choice(quotes))

    elif 'web' in message.content.lower():
        await sendMessage("https://raxus-church.ml")
    
    
#client.loop.create_task(time()) # Make needed loop
client.run(TOKEN) # Launch bot
