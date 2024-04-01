from twitchio.ext import commands 
import config
import random

#twitch username input
val = input("Enter your channel name: ")
val2 = input("Enter second channel's name: ")

class Bot(commands.Bot):
    
    
    
    def __init__(self):

        #chat connection
        super().__init__(token=config.api_key, prefix='?', initial_channels=[val,val2])
        
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
        
    #milk gamble command
    
    @commands.command()
    async def milk(self, ctx: commands.Context):
        milk = round(random.uniform(99,100), 2)
        if (milk >= 99):
           mMilk = "you get the all fated choccy milk"
           await ctx.send(f'{ctx.author.name} {mMilk}')
        else:
            await ctx.send(f'you lose {milk}')
            
    #black jack command?
    
bot = Bot()
bot.run()