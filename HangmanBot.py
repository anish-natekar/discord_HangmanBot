import discord
from discord.ext import commands
import random
client = commands.Bot(command_prefix = ".")
@client.event
async def on_ready():
    print("Bot is Online")
# global variables
datafiles = ["Triple_A_bollywoodtext.txt","Triple_A_IMDBtext.txt","Triple_A_MALtext.txt"]
cat = 1
word = str
blank_word = str
guessed = False
letters_guessed = []
chances = 6
hint_ctr = 0
game = False
def get_word(datalist):
    data=datafileread(datalist)
    word = random.choice(data)
    word[0] = word[0].upper()
    return word
def get_blank_word(word):
    hints = len(word) // 8 + 1
    global letters_guessed
    letters_guessed = []
    while (hints):
        rnd = random.choice(word)
        letters_guessed.append(rnd)
        hints -= 1
    blank_word = ""
    for i in word:
        if (i in letters_guessed):
            blank_word += i
        elif (i.isalpha()):
            blank_word += "?"
        elif (i not in letters_guessed):
            blank_word += i
            letters_guessed.append(i)
        else:
            blank_word += i
    return blank_word
def datafileread(datafilename):
    file=open(datafilename, mode='r')
    List=file.readlines()
    file.close()
    temp=[]
    data=[]
    s=""
    for i in List:
        for j in i:
            if(j=='#'):
                temp.append(s)
                s=""
            else:
                s+=j
        temp.append(s[:-1])
        s=""
        data.append(temp)
        temp=[]
    return data
def display_hangman(tries):
    stages = [  """
    --------
    |      |
    |     O
    |   \ | /
    |      |
    |    / \ 
    =====
    """,
    """
    --------
    |      |
    |     O
    |   \ | /
    |      |
    |    /
    =====
    """,
    """
    --------
    |      |
    |     O
    |   \ | /
    |      |
    |
    =====
    """,
    """
    --------
    |      |
    |     O
    |   \ |
    |      |
    |
    =====
    """,
    """
    --------
    |      |
    |     O
    |      |
    |      |
    |
    =====
    """,
    """
    --------
    |      |
    |     O
    |
    |
    |
    =====
    """,
    """
    --------
    |      |
    |      
    |
    |
    |
    =====
    """
    ]
    return stages[tries]
def hints(hint_list,i,cat):
    if cat ==1:
        L = [0,1,3,2]
    elif cat ==2:
        L=[0,1]
    else:
        L=[1,0]
    if i>=len(L):
        return hint_list[L[-1]]
    else:
        return hint_list[L[i]]  
@client.command(aliases=['category1', 'category2', 'category3'])
async def categories(ctx):
    if(game == False):
        await ctx.send(f"You chose {ctx.message.content[1:]}")
        global cat
        cat = int(ctx.message.content[-1])-1
@client.command()
async def hangman(ctx):
    await ctx.send("""Welcome, I am HangmanBot made by Anish Natekar
    Make sure to select your category
    we currently have 3 options
    '.category1' - Bollywood
    '.category2' - IMDB
    '.category3' - Anime
    '.start' will start the game
    to guess alphabets in game put it after '.' eg to guess 'a' i will type '.a'
    if you get stuck somewhere midgame then use '.hint' to get some clues""")
# https://discord.com/api/oauth2/authorize?client_id=878562781866127393&permissions=0&scope=bot
@client.command()
async def start(ctx):
    global word
    global game
    global blank_word
    global chances
    global guessed
    global hint_ctr
    hint_ctr = 0
    guessed = False
    chances = 6
    word = get_word(datafiles[cat])
    game = True
    blank_word = get_blank_word(word[0])
    await ctx.send("Let's play hangman")
    await ctx.send(display_hangman(chances))
    await ctx.send(blank_word)
@client.command(aliases=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
async def hint(ctx):
    global game
    guess = ctx.message.content[1:].upper()
    await ctx.send(f"alpphabet selected was {guess}, game status {game}.") 
    if(game):
        global hint_ctr
        global guessed
        global blank_word
        global chances
        global letters_guessed
        global word
        if(not guessed and chances > 0):
            if len(guess) == 1:
                if guess in letters_guessed:
                    await ctx.send(f"You already tried {guess} !!")
                elif guess not in word[0]:
                    await ctx.send(f"Oops, {guess} isn't the word")
                    chances -= 1
                    await ctx.send(f"{display_hangman(chances)}")
                else:
                    letters_guessed.append(guess)
                    await ctx.send(f"Well done !!, {guess} is in the word")
                    await ctx.send(f"{display_hangman(chances)}")
                    present_word = ""
                    for i in range(len(word[0])):
                        if guess == str(word[0][i]):
                            present_word += guess
                        else:
                            present_word += blank_word[i]
                    blank_word = present_word  
                    if "?" not in blank_word:
                        guessed = True
            elif guess == 'HINT':
                await ctx.send(hints(word[1:], hint_ctr, cat))
                hint_ctr += 1
            await ctx.send(blank_word)
        if guessed:
            await ctx.send(f"Yay!, you guessed it correct, the word is {word[0]}")
            game = False
        elif chances == 0:
            await ctx.send(f"Sorry, 0 attempts left, the word was {word[0]}, better luck next time.")
            game = False
client.run("ODc4NTYyNzgxODY2MTI3Mzkz.YSC_Wg.9hZP_EvI4jb-hWzQ8BUDJGHvrJ0")

