# Discord bot made for the Fall 2020 SDV Discord event
# Written by aquova, 2020

import discord
import config, db

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as:")
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_raw_reaction_add(payload):
    # If they have reacted to the specified message with the correct emoji, add the role
    if payload.message_id == config.SIGNUP_MES:
        if db.is_on_team(payload.user_id):
            return

        for team in config.TEAMS:
            if team['emoji'] == payload.emoji.name:
                try:
                    server = [x for x in client.guilds if x.id == payload.guild_id][0]
                    team_id = team['id']
                    new_role = discord.utils.get(server.roles, id=team_id)
                    user = discord.utils.get(server.members, id=payload.user_id)
                    db.add_member(payload.user_id, team_id)
                    await user.add_roles(new_role)
                    break
                except Exception as e:
                    print(f"Something has gone wrong with adding team role: {e}")

@client.event
async def on_message(message):
    # Do not react to our own messages
    if message.author.id == client.user.id:
        return

client.run(config.DISCORD_KEY)
