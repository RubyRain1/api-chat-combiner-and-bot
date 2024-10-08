from twitchio.ext import commands
from twitchio.ext import pubsub
import config
import random
import time
from colorama import init
from colorama import Fore, Back, Style
import sys

#initialize colorama
if sys.platform == "win32":
    init(autoreset=True)
    
# this is the introduction of a terminal based ui incase I cannot implement a working GUI
print('''
 _________      _         _        _____ _           _      _____                _     _                 
 |__   __|     (_) |     | |      / ____| |         | |    / ____|              | |   (_)                
    | |_      ___| |_ ___| |__   | |    | |__   __ _| |_  | |     ___  _ __ ___ | |__  _ _ __   ___ _ __ 
    | \ \ /\ / / | __/ __| '_ \  | |    | '_ \ / _` | __| | |    / _ \| '_ ` _ \| '_ \| | '_ \ / _ \ '__|
    | |\ V  V /| | || (__| | | | | |____| | | | (_| | |_  | |___| (_) | | | | | | |_) | | | | |  __/ |   
    |_| \_/\_/ |_|\__\___|_| |_|  \_____|_| |_|\__,_|\__|  \_____\___/|_| |_| |_|_.__/|_|_| |_|\___|_|   

                                                                                                           
   ''')  

print("this app is used to convert up to 10 chats into one by inputting channel names. This is helpful for any twitch streamer"
" looking to have a cleaner chat experience during collabs! If you would like to give feedback please type 'feedback'"
" during the starting prompt.")
print(" ") #this just adds a space

# this is where some start logic will be.
test = []
start = input("would you like to begin using the program? (Y/N) ").lower()
print(" ")
if start == "feedback":
    print("yippie")
elif start == "n":
    print("thank you for considering the use of my chat combiner! Have a nice day/night!")
elif start == "y":    
    count = 0 #increment up each time in order to trigger different itterations of super.__init__ 

    val = input("Enter your channel name: ") # this is the initial channel value as it is assumed you will always be combining your chat
    test.append(val)
#this will be for terminla color
    colorI1 = int(input("what color would you like it to be? \n (1. green, 2. blue, 3. red): "))
    colorI2 = ""
    colorI3 = ""
    colorI4 = ""
    colorI5 = ""
    colorI6 = ""
    colorI7 = ""
    colorI8 = ""
    colorI9 = ""
    colorI10 = ""


    #these are used to get user input for up to 10 channels.
    userI = input("would you like to add another channel? ").lower()
    userI2 = ""
    userI3 = ""
    userI4 = ""
    userI5 = ""
    userI6 = ""
    userI7 = ""
    userI8 = ""
    userI9 = ""

    #use a loop here
    if userI == "n": 
        print("bot functionality beginning")
        count = 0
    elif userI == "y":
        val2 = input("Enter second channel's name: ")
        test.append(val2)
        count = count + 1
        colorI2 = colorI1
        userI2 = input("would you like to add a third channel? ").lower()
        if userI2 == "n":
            print("combining chats, bot is now in use. Well wishes on your collab :)")
        elif userI2 == "y":
            val3 = input("enter third channel's name: ")
            test.append(val3)
            count = count + 1
            colorI3 = colorI1
            userI3 = input("would you like to add a fourth channel? ").lower()
            if userI3 == "n":
                print("combining chats, bot is now in use. Well wishes on your collab :)")
            elif userI3 == "y":
                val4 = input("enter fourth channel's name: ")
                test.append(val4)
                count = count + 1
                colorI4 = colorI1
                userI4 = input("would you like to add a fifth channel? ").lower()
                if userI4 == "n":
                    print("combining chats, bot is now in use. Well wishes on your collab :)")
                elif userI4 == "y":
                    val5 = input("enter fifth channel's name: ")
                    test.append(val5)
                    count = count + 1
                    colorI5 = colorI1
                    userI5 = input("would you like to add a sixth channel? ").lower()
                    if userI5 == "n":
                        print("combining chats, bot is now in use. Well wishes on your collab :)")
                    elif userI5 == "y":
                            val6 = input("enter sixth channel's name: ")
                            test.append(val6)
                            count = count + 1
                            colorI6 = colorI1
                            userI6 = input("would you like to add a seventh channel? ").lower()
                            if userI6 == "n": 
                                print("combining chats, bot is now in use. Well wishes on your collab :)")
                            elif userI6 == "y":
                                val7 = input("enter seventh channel's name: ")
                                test.append(val7)
                                count = count + 1
                                colorI7 = colorI1
                                userI7 = input("would you like to add a eighth channel? ").lower()
                                if userI7 == "n":
                                    print("combining chats, bot is now in use. Well wishes on your collab :)")
                                elif userI7 == "y":
                                    val8 = input("enter eighth channel's name: ")
                                    test.append(val8)
                                    count = count + 1
                                    colorI8 = colorI1
                                    userI8 = input("would you like to add a ninth channel? ").lower()
                                    if userI8 == "n":
                                        print("combining chats, bot is now in use. Well wishes on your collab :)")
                                    elif userI8 == "y":
                                        val9 = input("enter ninth channel's name: ")
                                        test.append(val9)
                                        count = count + 1
                                        colorI9 = colorI1
                                        userI9 = input("would you like to add a tenth channel? ").lower()
                                        if userI9 == "n":
                                            print("combining chats, bot is now in use. Well wishes on your collab :)")
                                        elif userI9 == "y":
                                            val10 = input("enter tenth channel's name: ")
                                            test.append(val10)
                                            count = count + 1
                                            colorI10 = colorI1

#possibly implement a rating system that will store all ratings in a DB for further improvements.


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
           
            #this if statement catches bot messages and ignores them
            # print(test)
            #this is for the first input color choices will run for all messages other then bots          
            if colorI1 == 1 and message.channel._name == test[0] and message.author._name != "nightbot" and message.author._name != "streamelements":
                print(Fore.GREEN,"-----------------------------------------------------------------")
                print(Fore.MAGENTA, f'{message.channel._name}:')
                print(Fore.GREEN,f'{message.author.display_name}: {message.content}')
                print(Fore.GREEN,"-----------------------------------------------------------------")
                print(" ")
                print(Style.RESET_ALL)
            
            if colorI2 ==  1 and message.channel._name == test[1] and message.author._name.lower() != "nightbot" and message.author._name != "streamelements" :
                print(Fore.GREEN,"-----------------------------------------------------------------")
                print(Fore.YELLOW, f'{message.channel._name}:')
                print(Fore.GREEN,f'{message.author.display_name}: {message.content}')
                print(Fore.GREEN,"-----------------------------------------------------------------")
                print(" ")
                print(Style.RESET_ALL)

            if colorI3==  1 and message.channel._name == test[2] and message.author._name != "nightbot" and message.author._name != "streamelements":
                print(Fore.GREEN,"-----------------------------------------------------------------")
                print(Fore.WHITE, f'{message.channel._name}:')
                print(Fore.GREEN,f'{message.author.display_name}: {message.content}')
                print(Fore.GREEN,"-----------------------------------------------------------------")
                print(" ")
                print(Style.RESET_ALL)
            
            if colorI4 ==  1 and message.channel._name == test[3] and message.author._name != "nightbot" and message.author._name != "streamelements":
                print(Fore.GREEN,"-----------------------------------------------------------------")
                print(Fore.RED, f'{message.channel._name}:')
                print(Fore.GREEN,f'{message.author.display_name}: {message.content}')
                print(Fore.GREEN,"-----------------------------------------------------------------")
                print(" ")
                print(Style.RESET_ALL)

            if colorI5 ==  1 and message.channel._name == test[4] and message.author._name != "nightbot" and message.author._name != "streamelements":
                print(Fore.GREEN,"-----------------------------------------------------------------")
                print(Fore.BLUE, f'{message.channel._name}:')
                print(Fore.GREEN,f'{message.author.display_name}: {message.content}')
                print(Fore.GREEN,"-----------------------------------------------------------------")
                print(" ")
                print(Style.RESET_ALL)
            
            if colorI6 ==  1 and message.channel._name == test[5] and message.author._name != "nightbot" and message.author._name != "streamelements":
                print(Fore.GREEN,"-----------------------------------------------------------------")
                print(Fore.CYAN, f'{message.channel._name}:')
                print(Fore.GREEN,f'{message.author.display_name}: {message.content}')
                print(Fore.GREEN,"-----------------------------------------------------------------")
                print(" ")
                print(Style.RESET_ALL)

            if colorI7 ==  1 and message.channel._name == test[6] and message.author._name != "nightbot" and message.author._name != "streamelements":
                print(Fore.GREEN,"-----------------------------------------------------------------")
                print(Fore.LIGHTBLUE_EX, f'{message.channel._name}:')
                print(Fore.GREEN,f'{message.author.display_name}: {message.content}')
                print(Fore.GREEN,"-----------------------------------------------------------------")
                print(" ")
                print(Style.RESET_ALL)
            
            if colorI8 ==  1 and message.channel._name == test[7] and message.author._name != "nightbot" and message.author._name != "streamelements":
                print(Fore.GREEN,"-----------------------------------------------------------------")
                print(Fore.LIGHTYELLOW_EX, f'{message.channel._name}:')
                print(Fore.GREEN,f'{message.author.display_name}: {message.content}')
                print(Fore.GREEN,"-----------------------------------------------------------------")
                print(" ")
                print(Style.RESET_ALL)
            
            if colorI9 ==  1 and message.channel._name == test[8] and message.author._name != "nightbot" and message.author._name != "streamelements":
                print(Fore.GREEN,"-----------------------------------------------------------------")
                print(Fore.LIGHTGREEN_EX, f'{message.channel._name}:')
                print(Fore.GREEN,f'{message.author.display_name}: {message.content}')
                print(Fore.GREEN,"-----------------------------------------------------------------")
                print(" ")
                print(Style.RESET_ALL)
            
            if colorI10 ==  1 and message.channel._name == test[9] and message.author._name != "nightbot" and message.author._name != "streamelements":
                print(Fore.GREEN,"-----------------------------------------------------------------")
                print(Fore.LIGHTRED_EX, f'{message.channel._name}:')
                print(Fore.GREEN,f'{message.author.display_name}: {message.content}')
                print(Fore.GREEN,"-----------------------------------------------------------------")
                print(" ")
                print(Style.RESET_ALL)

            #this is for the blue chat option
            if colorI1 == 2 and message.channel._name == test[0] and message.author._name != "nightbot" and message.author._name != "streamelements":
                print(Fore.BLUE,"-----------------------------------------------------------------")
                print(Fore.RED, f'{message.channel._name}:')
                print(Fore.BLUE,f'{message.author.display_name}: {message.content}')
                print(Fore.BLUE,"-----------------------------------------------------------------")
                print(" ")
                print(Style.RESET_ALL)
            
            if colorI2 == 2 and message.channel._name == test[1] and message.author._name != "nightbot" and message.author._name != "streamelements":
                print(Fore.BLUE,"-----------------------------------------------------------------")
                print(Fore.GREEN, f'{message.channel._name}:')
                print(Fore.BLUE,f'{message.author.display_name}: {message.content}')
                print(Fore.BLUE,"-----------------------------------------------------------------")
                print(" ")
                print(Style.RESET_ALL)
            
            if colorI3 == 2 and message.channel._name == test[2] and message.author._name != "nightbot" and message.author._name != "streamelements":
                print(Fore.BLUE,"-----------------------------------------------------------------")
                print(Fore.YELLOW, f'{message.channel._name}:')
                print(Fore.BLUE,f'{message.author.display_name}: {message.content}')
                print(Fore.BLUE,"-----------------------------------------------------------------")
                print(" ")
                print(Style.RESET_ALL)

            if colorI4 == 2 and message.channel._name == test[3] and message.author._name != "nightbot" and message.author._name != "streamelements":
                print(Fore.BLUE,"-----------------------------------------------------------------")
                print(Fore.CYAN, f'{message.channel._name}:')
                print(Fore.BLUE,f'{message.author.display_name}: {message.content}')
                print(Fore.BLUE,"-----------------------------------------------------------------")
                print(" ")
                print(Style.RESET_ALL)

            if colorI5 == 2 and message.channel._name == test[4] and message.author._name != "nightbot" and message.author._name != "streamelements":
                print(Fore.BLUE,"-----------------------------------------------------------------")
                print(Fore.MAGENTA, f'{message.channel._name}:')
                print(Fore.BLUE,f'{message.author.display_name}: {message.content}')
                print(Fore.BLUE,"-----------------------------------------------------------------")
                print(" ")
                print(Style.RESET_ALL)
                
            if colorI6 == 2 and message.channel._name == test[5] and message.author._name != "nightbot" and message.author._name != "streamelements":
                print(Fore.BLUE,"-----------------------------------------------------------------")
                print(Fore.WHITE, f'{message.channel._name}:')
                print(Fore.BLUE,f'{message.author.display_name}: {message.content}')
                print(Fore.BLUE,"-----------------------------------------------------------------")
                print(" ")
                print(Style.RESET_ALL)

            if colorI7 == 2 and message.channel._name == test[6] and message.author._name != "nightbot" and message.author._name != "streamelements":
                print(Fore.BLUE,"-----------------------------------------------------------------")
                print(Fore.LIGHTRED_EX, f'{message.channel._name}:')
                print(Fore.BLUE,f'{message.author.display_name}: {message.content}')
                print(Fore.BLUE,"-----------------------------------------------------------------")
                print(" ")
                print(Style.RESET_ALL)

            if colorI8 == 2 and message.channel._name == test[7] and message.author._name != "nightbot" and message.author._name != "streamelements":
                print(Fore.BLUE,"-----------------------------------------------------------------")
                print(Fore.LIGHTCYAN_EX, f'{message.channel._name}:')
                print(Fore.BLUE,f'{message.author.display_name}: {message.content}')
                print(Fore.BLUE,"-----------------------------------------------------------------")
                print(" ")
                print(Style.RESET_ALL)

            if colorI9 == 2 and message.channel._name == test[8] and message.author._name != "nightbot" and message.author._name != "streamelements":
                print(Fore.BLUE,"-----------------------------------------------------------------")
                print(Fore.LIGHTMAGENTA_EX, f'{message.channel._name}:')
                print(Fore.BLUE,f'{message.author.display_name}: {message.content}')
                print(Fore.BLUE,"-----------------------------------------------------------------")
                print(" ")
                print(Style.RESET_ALL)

            if colorI10 == 2 and message.channel._name == test[9] and message.author._name != "nightbot" and message.author._name != "streamelements":
                print(Fore.BLUE,"-----------------------------------------------------------------")
                print(Fore.LIGHTGREEN_EX, f'{message.channel._name}:')
                print(Fore.BLUE,f'{message.author.display_name}: {message.content}')
                print(Fore.BLUE,"-----------------------------------------------------------------")
                print(" ")
                print(Style.RESET_ALL)


            #this is for the red chat option

            if colorI1 == 3 and message.channel._name == test[0] and message.author._name != "nightbot" and message.author._name != "streamelements":
                print(Fore.RED,"-----------------------------------------------------------------")
                print(Fore.BLUE, f'{message.channel._name}:')
                print(Fore.RED,f'{message.author.display_name}: {message.content}')
                print(Fore.RED,"-----------------------------------------------------------------")
                print(" ")
                print(Style.RESET_ALL)
            
            if colorI2 == 3 and message.channel._name == test[1] and message.author._name != "nightbot" and message.author._name != "streamelements":
                print(Fore.RED,"-----------------------------------------------------------------")
                print(Fore.YELLOW, f'{message.channel._name}:')
                print(Fore.RED,f'{message.author.display_name}: {message.content}')
                print(Fore.RED,"-----------------------------------------------------------------")
                print(" ")
                print(Style.RESET_ALL)
            
            if colorI3 == 3 and message.channel._name == test[2] and message.author._name != "nightbot" and message.author._name != "streamelements":
                print(Fore.RED,"-----------------------------------------------------------------")
                print(Fore.GREEN, f'{message.channel._name}:')
                print(Fore.RED,f'{message.author.display_name}: {message.content}')
                print(Fore.RED,"-----------------------------------------------------------------")
                print(" ")
                print(Style.RESET_ALL)
            
            if colorI4 == 3 and message.channel._name == test[3] and message.author._name != "nightbot" and message.author._name != "streamelements":
                print(Fore.RED,"-----------------------------------------------------------------")
                print(Fore.CYAN, f'{message.channel._name}:')
                print(Fore.RED,f'{message.author.display_name}: {message.content}')
                print(Fore.RED,"-----------------------------------------------------------------")
                print(" ")
                print(Style.RESET_ALL)

            if colorI5 == 3 and message.channel._name == test[4] and message.author._name != "nightbot" and message.author._name != "streamelements":
                print(Fore.RED,"-----------------------------------------------------------------")
                print(Fore.MAGENTA, f'{message.channel._name}:')
                print(Fore.RED,f'{message.author.display_name}: {message.content}')
                print(Fore.RED,"-----------------------------------------------------------------")
                print(" ")
                print(Style.RESET_ALL)
            
            if colorI6 == 3 and message.channel._name == test[5] and message.author._name != "nightbot" and message.author._name != "streamelements":
                print(Fore.RED,"-----------------------------------------------------------------")
                print(Fore.WHITE, f'{message.channel._name}:')
                print(Fore.RED,f'{message.author.display_name}: {message.content}')
                print(Fore.RED,"-----------------------------------------------------------------")
                print(" ")
                print(Style.RESET_ALL)

            if colorI7 == 3 and message.channel._name == test[6] and message.author._name != "nightbot" and message.author._name != "streamelements":
                print(Fore.RED,"-----------------------------------------------------------------")
                print(Fore.LIGHTMAGENTA_EX, f'{message.channel._name}:')
                print(Fore.RED,f'{message.author.display_name}: {message.content}')
                print(Fore.RED,"-----------------------------------------------------------------")
                print(" ")
                print(Style.RESET_ALL)
            
            if colorI8 == 3 and message.channel._name == test[7] and message.author._name != "nightbot" and message.author._name != "streamelements":
                print(Fore.RED,"-----------------------------------------------------------------")
                print(Fore.BLUE, f'{message.channel._name}:')
                print(Fore.LIGHTYELLOW_EX,f'{message.author.display_name}: {message.content}')
                print(Fore.RED,"-----------------------------------------------------------------")
                print(" ")
                print(Style.RESET_ALL)
            
            if colorI9 == 3 and message.channel._name == test[8] and message.author._name != "nightbot" and message.author._name != "streamelements":
                print(Fore.RED,"-----------------------------------------------------------------")
                print(Fore.LIGHTBLUE_EX, f'{message.channel._name}:')
                print(Fore.RED,f'{message.author.display_name}: {message.content}')
                print(Fore.RED,"-----------------------------------------------------------------")
                print(" ")
                print(Style.RESET_ALL)

            if colorI10 == 3 and message.channel._name == test[9] and message.author._name != "nightbot" and message.author._name != "streamelements":
                print(Fore.RED,"-----------------------------------------------------------------")
                print(Fore.LIGHTGREEN_EX, f'{message.channel._name}:')
                print(Fore.RED,f'{message.author.display_name}: {message.content}')
                print(Fore.RED,"-----------------------------------------------------------------")
                print(" ")
                print(Style.RESET_ALL)

                
                
                        
                
                

            await self.handle_commands(message)
#here I need to implement a cooldown system.
        #channel points?
       
        

       
          
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
                mMilk = "you get regular milk :3"
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

        @commands.command()
        async def love(self, ctx: commands.Context):
            
            love = random.randint(1,100)
            await ctx.send(f'{ctx.author.name} is {love}% compatable with {val}')
        

        #this command only to be used if the streamer wants to shout out the creator. 
        @commands.command()
        async def support(self, ctx: commands.Context):
            await ctx.send("howdy gang my name is Grave Nelith, I am a small indie vtubing bunny boy! "
                           "I am the creator of this bot, if you would like to support me you can check out"
                           "this project on my kofi! - enter kofi link here -")
    bot = Bot()
    bot.run()
    init()