from twitchio.ext import commands 
import config
import asyncio
from abcs import Messageable
from typing import Optional, TYPE_CHECKING, Dict

if TYPE_CHECKING:
    from user import User
    from websocket import WSConnection
    
result = input("Enter your channel name: ")
count = 0
val = result
val4 = ""
val5 = ""
val6= ""
val7 = ""
val8 = ""
val9 = ""
val10 = ""


if result != "" and val != "":
    result = input("enter next channel name: ")
    val2 = result
    if result != "" and val2 != "":
        result = ("enter next channel name: ")
        val3 = result
        if result != "" and val3 != "":
            print("hehe")


class Bot(commands.Bot):
    
    def __init__(self):

        super().__init__(token=config.api_key, prefix='?', initial_channels=[val,val2])
        
   

    async def event_message(self, message):

        if message.echo:
            return
        
        print(f'{message.author.display_name}: {message.content}')
        
       
        

        await self.handle_commands(message)

    
    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}')



bot = Bot()
bot.run()


