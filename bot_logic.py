import random


def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password


def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)


def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "ОРЕЛ"
    else:
        return "РЕШКА"

import discord 
import random 

client = discord.Client() 

@client.event 
async def on_ready(): 
  print(f'We have logged in as {client.user}') 

@client.event 
async def on_message(message): 
  if message.author   == client.user: 
    return 

  if message.content.startswith('!подбрось'): 
    result = random.choices(["Вариант 1", "Вариант 2"], weights=[0.5, 0.5])[0]  # 50/50 шанс для каждого варианта 
    await message.channel.send(f'Результат: {result}') 
 
