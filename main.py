from twitchio.ext import commands 
import config
import random


# this is the introduction of a terminal based ui incase I cannot implement a working GUI
print(((((""""
 _________      _         _        _____ _           _      _____                _     _                 
 |__   __|     (_) |     | |      / ____| |         | |    / ____|              | |   (_)                
    | |_      ___| |_ ___| |__   | |    | |__   __ _| |_  | |     ___  _ __ ___ | |__  _ _ __   ___ _ __ 
    | \ \ /\ / / | __/ __| '_ \  | |    | '_ \ / _` | __| | |    / _ \| '_ ` _ \| '_ \| | '_ \ / _ \ '__|
    | |\ V  V /| | || (__| | | | | |____| | | | (_| | |_  | |___| (_) | | | | | | |_) | | | | |  __/ |   
    |_| \_/\_/ |_|\__\___|_| |_|  \_____|_| |_|\__,_|\__|  \_____\___/|_| |_| |_|_.__/|_|_| |_|\___|_|   

                                                                                                           
   """"")))))  

print("this app is used to convert up to 10 chats into one by inputting channel names. This is helpful for any twitch streamer"
" looking to have a cleaner chat experience during collabs!")
print(" ") #this just adds a space
start = input("would you like to begin using the program? (Y/N) ")
print(" ")

count = 0 #increment up each time in order to trigger different itterations of super.__init__ 

val = input("Enter your channel name: ") # this is the initial channel value as it is assumed you will always be combining your chat

#these are used to get user input for up to 10 channels.
userI = input("would you like to add another channel? ")
userI2 = ""
userI3 = ""
userI4 = ""
userI5 = ""
userI6 = ""
userI7 = ""
userI8 = ""
userI9 = ""


if userI == "n": 
    print("bot functionality beginning")
    count = 0
elif userI == "y":
    val2 = input("Enter second channel's name: ")
    count = count + 1
    userI2 = input("would you like to add a third channel? ")
    if userI2 == "n":
        print("combining chats, bot is now in use. Well wishes on your collab :)")
    elif userI2 == "y":
        val3 = input("enter third channel's name: ")
        count = count + 1
        userI3 = input("would you like to add a fourth channel? ")
        if userI3 == "n":
            print("combining chats, bot is now in use. Well wishes on your collab :)")
        elif userI3 == "y":
            val4 = input("enter fourth channel's name: ")
            count = count + 1
            userI4 = input("would you like to add a fifth channel? ")
            if userI4 == "n":
                print("combining chats, bot is now in use. Well wishes on your collab :)")
            elif userI4 == "y":
                val5 = input("enter fifth channel's name: ")
                count = count + 1
                userI5 = input("would you like to add a sixth channel? ")
                if userI5 == "n":
                    print("combining chats, bot is now in use. Well wishes on your collab :)")
                elif userI5 == "y":
                        val6 = input("enter sixth channel's name: ")
                        count = count + 1
                        userI6 = input("would you like to add a seventh channel? ")
                        if userI6 == "n": 
                            print("combining chats, bot is now in use. Well wishes on your collab :)")
                        elif userI6 == "y":
                            val7 = input("enter seventh channel's name: ")
                            count = count + 1
                            userI7 = input("would you like to add a eighth channel? ")
                            if userI7 == "n":
                                print("combining chats, bot is now in use. Well wishes on your collab :)")
                            elif userI7 == "y":
                                val8 = input("enter eighth channel's name: ")
                                count = count + 1
                                userI8 = input("would you like to add a ninth channel? ")
                                if userI8 == "n":
                                    print("combining chats, bot is now in use. Well wishes on your collab :)")
                                elif userI8 == "y":
                                    val9 = input("enter ninth channel's name: ")
                                    count = count + 1
                                    userI9 = input("would you like to add a tenth channel? ")
                                    if userI9 == "n":
                                        print("combining chats, bot is now in use. Well wishes on your collab :)")
                                    elif userI9 == "y":
                                        val10 = input("enter tenth channel's name: ")
                                        count = count + 1



class Bot(commands.Bot):
    
    def __init__(self):
        #try if statement here 

        if count == 0:
            super().__init__(token=config.api_key, prefix='?', initial_channels=[val])
        elif count == 1:
            super().__init__(token=config.api_key, prefix='?', initial_channels=[val,val2])
        elif count == 2:
            super().__init__(token=config.api_key, prefix='?', initial_channels=[val,val2, val3])
        elif count == 3:
            super().__init__(token=config.api_key, prefix='?', initial_channels=[val,val2, val3, val4])
        elif count == 4:
            super().__init__(token=config.api_key, prefix='?', initial_channels=[val,val2, val3, val4, val5])
        elif count == 5:
            super().__init__(token=config.api_key, prefix='?', initial_channels=[val,val2, val3, val4, val5, val6])
        elif count == 6:
            super().__init__(token=config.api_key, prefix='?', initial_channels=[val,val2, val3, val4, val5, val6, val7])
        elif count == 7: 
            super().__init__(token=config.api_key, prefix='?', initial_channels=[val,val2, val3, val4, val5, val6, val7, val8])
        elif count == 8:
            super().__init__(token=config.api_key, prefix='?', initial_channels=[val,val2, val3, val4, val5, val6, val7, val8, val9])
        elif count == 9:
            super().__init__(token=config.api_key, prefix='?', initial_channels=[val,val2, val3, val4, val5, val6, val7, val8, val9, val10])
        
    async def event_message(self, messagae):

        print(f'Logged in as | {self.nick}')
        print(f'user id is | {self.user_id}')

    async def event_message(self, message):

        if message.echo:
            return
        print(("              Messages begin below                  "
              "----------------------------------------------------"))
        print(f'{message.author.display_name}: {message.content}')
        print(" ")

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
        if milk <= 55:
            mMilk = "you regular milk :3"
            await ctx.send(f'{ctx.author.name} {mMilk}')
        elif milk <= 85:
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
    async def bj(self, ctx: commands.Context):
        dCard = random.randint(1,11)
        dCard2 = random.randint(1,11)
        pCard1 = random.randint(1,11)
        pCard2 = random.randint(1,11)
        pTotal = pCard1 + pCard2
        dTotal = dCard + dCard2
        
        # if pTotal > 21:
        #     await ctx.send(f'the dealer drew {dTotal}, {ctx.author.name} pulled {pTotal} YOU WINNNNN')
        if dTotal < pTotal:
            await ctx.send(f'the dealer drew {dTotal}, {ctx.author.name} pulled {pTotal} YOU WINNNNN')
        else:
            await ctx.send(f'the dealer drew {dTotal}, {ctx.author.name} pulled {pTotal} YOU LOSE WOMP WOMP')

    

bot = Bot()
bot.run()
