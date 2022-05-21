import os
from discord.ext import commands
from web_server import web_server

my_secret = os.environ['Token']
my_secret_id = os.environ['Author_id']
bot = commands.Bot(command_prefix="-")    


@bot.command()
async def setup(ctx):
  if (ctx.message.author.id != int(my_secret_id)):
    await ctx.message.delete()
    await ctx.channel.send('**You don\'t have permission to use this command.**', delete_after = 2)
    return
  await ctx.message.delete()
  await ctx.channel.send('**The Hall of Fame:**')


@bot.command(name = "id")
async def get_id(ctx, message_id):
  if (ctx.message.author.id != int(my_secret_id)):
    await ctx.channel.send('**You don\'t have permission to use this command.**', delete_after = 2)
    return
  response = 'To add a member, Type: -add ' + message_id + " <video-link> <song-link>"
  await ctx.message.delete()
  await ctx.channel.send(response)
  await ctx.channel.send('-add ' + message_id)


@bot.command()
async def add(ctx, message_id, *args):
  msg = await ctx.channel.fetch_message(message_id)
  await ctx.message.delete()
  response = msg.content + '\n' + 'Next member:' + '\n'
  
  count = 0
  for arg in args:
    if (arg.__contains__('https://www.youtube.com/') 
        or arg.__contains__('https://youtu.be/')):
      count += 1
      response = response + ' | ' + arg
      if count == 2:
        break
    else:
      await ctx.channel.send('**Invalid input, link expected, please try again**', delete_after = 2)
      return

  if (count != 2):
    await ctx.channel.send('**Invalid input, please try again**', delete_after = 2)
    return

  await msg.edit(content=response)


@bot.command()
async def reset(ctx, message_id, arg):
  if (ctx.message.author.id != int(my_secret_id)):
    await ctx.message.delete()
    await ctx.channel.send('**Ask the author to run this command if needed**', delete_after = 2)
    return
  await ctx.message.delete()
  msg = await ctx.channel.fetch_message(message_id)
  
  response = "**The Hall of fame:**\n" + arg
  await msg.edit(content = response)

web_server()
bot.run(my_secret)
  
#channel = ctx.channel
# await ctx.channel.send('To confirm that you want to reset, type \'RESET\'. If this was a mistake, type anything to cancel the command.', delete_after = 2)
  # #await ctx.channel.message.content
  # await bot.wait_for('message', timeout=10.0, check='RESET')
  # await ctx.message.delete()