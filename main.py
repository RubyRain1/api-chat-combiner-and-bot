from twitchio.ext import commands 
import config
import random


# this is the introduction of a terminal based ui incase I cannot implement a working GUI
print(((((""""
  _______       _ _       _            _           _                                   _            
 |__   __|     (_) |     | |          | |         | |                                 | |           
    | |_      ___| |_ ___| |__     ___| |__   __ _| |_    ___ ___  _ ____   _____ _ __| |_ ___ _ __ 
    | \ \ /\ / / | __/ __| '_ \   / __| '_ \ / _` | __|  / __/ _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
    | |\ V  V /| | || (__| | | | | (__| | | | (_| | |_  | (_| (_) | | | \ V /  __/ |  | ||  __/ |   
    |_| \_/\_/ |_|\__\___|_| |_|  \___|_| |_|\__,_|\__|  \___\___/|_| |_|\_/ \___|_|   \__\___|_|   


   """"")))))  

print("this app is used to convert up to 10 chats into one by inputting channel names. This is helpful for any twitch streamer"
"looking to have a cleaner chat experience during collabs! MUST HAVE COLLAB STREAMS OPEN " 
"(support your fellow streamers even in a collab).")
print(" ") #this just adds a space
start = input("would you like to begin using the program? (Y/N) ")
print(" ")

val = input("Enter your channel name: ")
val2 = input("Enter second channel's name: ")

class Bot(commands.Bot):
    
    
    
    def __init__(self):
        #try if statement here 
        super().__init__(token=config.api_key, prefix='?', initial_channels=[val,val2])
        
    async def event_message(self, messagae):

        print(f'Logged in as | {self.nick}')
        print(f'user id is | {self.user_id}')

    async def event_message(self, message):

        if message.echo:
            return
        
        print(f'{message.author.display_name}: {message.content}')

        await self.handle_commands(message)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}')

    @commands.command()
    async def cookie(self, ctx: commands.Context):
        await ctx.send(f'{ctx.author.name} gets a cookie!!!')

    #8ball command
    @commands.command()
    async def fortune(self, ctx: commands.Context):
        fortune = random.randint(1,100) #this gets a random number 1-100 in order for logic to run.
        if fortune <= 25:
            await ctx.send(f'{ctx.author.name} yes I assume so.')
        elif fortune <= 50:
            await ctx.send(f'{ctx.author.name} no this is unlikely.')
        elif fortune <= 75: 
            await ctx.send(f'{ctx.author.name} there is but a chance.')
        elif fortune <= 100: 
            await ctx.send(f'{ctx.author.name} perchance :skull:')
        
    #milk gamble command
    @commands.command()
    async def milk(self, ctx: commands.Context):
            #this is going to be the random logic for the command.
        milk = round(random.uniform(1,100), 2) #this gets a random float number from 1-100 and stops it at 2 dec points.
        if milk <= 33.33:
            mMilk = "you regular milk :3"
            await ctx.send(f'{ctx.author.name} {mMilk}')
        elif milk <= 66.66:
            mMilk = "you get the kinda mid strawberry milk if we are really being honest here."
            await ctx.send(f'{ctx.author.name} {mMilk}')
        elif milk <= 99.99:
            mMilk = "you get the all fated choccy milk."
            await ctx.send(f'{ctx.author.name} {mMilk}')
        elif milk <= 100:
            mMilk = "you get the rare banana milk"
            await ctx.send(f'{ctx.author.name} {mMilk}')
                 
    
            
    #black jack command?
    @commands.command()
    async def BJ(self, ctx: commands.Context):
        dCard = random.randint(17,21)
        pCard1 = random.randint(1,11)
        pCard2 = random.randint(1,11)
        pTotal = pCard1 + pCard2
        
        if pTotal > 21:
            await ctx.send(f'the dealer drew {dCard}, {ctx.author.name} pulled {pTotal} YOU WINNNNN')
        elif dCard < pTotal:
            await ctx.send(f'the dealer drew {dCard}, {ctx.author.name} pulled {pTotal} YOU WINNNNN')
        else:
            await ctx.send(f'the dealer drew {dCard}, {ctx.author.name} pulled {pTotal} YOU LOSE WOMP WOMP')

            
bot = Bot()
bot.run()