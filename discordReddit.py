#Author - adsalads

import praw
from discord.ext import commands

#import proper praw API to retrieve reddit information using reddit API id's
#create client for bot, with includes command prefix to intitate any of the commands below
myReddit = praw.Reddit(client_id='', client_secret = '', user_agent = 'me')
client = commands.Bot(command_prefix= '.')

#function to print posts and url of top 6 hottest reddit posts
#function is called in a command event below
def printPosts(desiredsubreddit):
    # create empty dictionary
    result = {}
    # dictionary key = title, value = url
    for item in myReddit.subreddit(desiredsubreddit).hot(limit=6):
            result[item.title] = item.url
    #display dictionary in a cleaner format and return it
    refinedResult = "\n".join("{}: {}".format(k, v) for k, v in result.items())
    return refinedResult

#message printed to terminal to notify is bot is running
@client.event
async def on_ready():
    print("Bot is ready!")

#print instructions on how to use bot for users joining a guild
@client.event
async def on_guild_join(guild):
    await guild.send("Type '.fetch [desired subreddit]' to fetch hottest posts! \n Type '.clear' to clear chat!")

#enter any of the following aliases with the proper commmand prefix ('.')
#any set of characters after the alias will be passed into the function 'printPosts' as a requested subreddit
@client.command(aliases = ["fetchit", "Fetchit", "FETCHIT", "fetch", "Fetch"])
async def fetchPosts(ctx, arg1):
    response = printPosts(arg1)
    await ctx.send(response)

#enter the word "clear" with the proper command prefix to clear last 6 items in the chat
@client.command()
async def clear(ctx, amount = 6):
    await ctx.channel.purge(limit=amount)

#run the bot client with the proper token
client.run('')

