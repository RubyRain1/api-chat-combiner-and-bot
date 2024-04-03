from twitchio.ext import commands 
import config
import random

#twitch username input
val = input("Enter your channel name: ")

class Bot(commands.Bot):
    
    
    
    def __init__(self):

        #chat connection
        super().__init__(token=config.api_key, prefix='?', initial_channels=[val])
        
    async def event_message(self, messagae):

        print(f'Logged in as | {self.nick}')
        print(f'user id is | {self.user_id}')

    #chat combiner code
    async def event_message(self, message):

        if message.echo:
            return
        
        rAuthor = message.author.display_name
        rContent = message.content

        print(f'{rAuthor}: {rContent}')

        await self.handle_commands(message)

    # hello command
    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}')

    #cookie command
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
    
bot = Bot()
bot.run()