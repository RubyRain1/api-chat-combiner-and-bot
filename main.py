from twitchio.ext import commands 
import config
import asyncio
from abcs import Messageable
from typing import Optional, TYPE_CHECKING, Dict

if TYPE_CHECKING:
    from user import User
    from websocket import WSConnection
    
val = input("Enter your channel name: ")
val2 = input("Enter second channel's name: ")


class PartialChatter(Messageable):
    __messageable_channel__ = False

    def __init__(self, websocket, **kwargs):
        self._name = kwargs.get("name")
        self._ws = websocket
        self._channel = kwargs.get("channel", self._name)
        self._message = kwargs.get("message")
        super().__init__(token=config.api_key, prefix='?', initial_channels=[val])

    def __repr__(self):
        return f"<PartialChatter name: {self._name}, channel: {self._channel}>"

    def __eq__(self, other):
        return other.name == self.name and other.channel.name == other.channel.name

    def __hash__(self):
        return hash(self.name + self.channel.name)

    async def user(self) -> "User":
        """|coro|

        Fetches a :class:`twitchio.User` object based off the chatters channel name

        Returns
        --------
            :class:`twitchio.User`
        """
        return (await self._ws._client.fetch_users(names=[self.name]))[0]
        

    @property
    def name(self):
        """The users name"""
        return self._name

    @property
    def channel(self):
        """The channel associated with the user."""
        return self._channel

    def _fetch_channel(self):
        return self  # Abstract method

    def _fetch_websocket(self):
        return self._ws  # Abstract method

    def _fetch_message(self):
        return self._message  # Abstract method

    def _bot_is_mod(self):
        return False
    

class Bot(commands.Bot):
    
    def __init__(self):

        super().__init__(token=config.api_key, prefix='?', initial_channels=[val,val2])
        
   

    async def event_message(self, message):

        if message.echo:
            return
        
        print(f'{message._author}, {message.content}')
       
       
        

        await self.handle_commands(message)

    
    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}')



bot = Bot()
bot.run()


