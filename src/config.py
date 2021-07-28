import discord, json

PTS_PER_AWARD = 1

DATABASE_PATH = "/private/summer.db"
_config_path = "/private/config.json"
with open(_config_path) as config_file:
    cfg = json.load(config_file)

DISCORD_KEY = cfg['discord']
CMD_PREFIX = cfg['command_prefix']
TEAMS = cfg['teams']
JUNIMO_ROLE = cfg['roles']['junimo']
ROLE_ANNUAL = cfg['roles']['annual']
ROLE_CURRENT = cfg['roles']['current']
SIGNUP_MES = cfg['messages']['signup']

VOTING_CHANNELS = cfg['channels']['vote']
HIDDEN_EVENTS = cfg['channels']['hidden']
VERIFY_EVENT = cfg['channels']['verify']
VERIFY_EMOJI = cfg['emoji']['verify']

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
