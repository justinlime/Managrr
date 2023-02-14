from dotenv import load_dotenv
from discord import Colour
from discord.embeds import Embed as DiscordEmbed

load_dotenv()

class Config:
    token = os.getenv("DISCORD_TOKEN")

    radarr_api = os.getenv("RADARR_API_KEY")
    radarr_address = os.getenv("RADARR_ADDRESS")
    
    sonarr_api = os.getenv("SONARR_API_KEY")
    sonarr_address = os.getenv("SONARR_ADDRESS")

    radarr_roles = [int(x) for x in os.getenv("RADARR_ALLOWED_ROLES").split(",")]
    sonarr_roles = [int(x) for x in os.getenv("SONARR_ALLOWED_ROLES").split(",")]

    allowed_channels = [int(x) for x in os.getenv("ALLOWED_CHANNELS").split(",")]
    
    
