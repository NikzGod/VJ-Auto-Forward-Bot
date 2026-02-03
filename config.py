from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "aa677b47c070611cab663cf8018b114c")
      API_ID = int(getenv("API_ID", "22333911"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "8298957650:AAFbvbDeTqq5WgwoGhG9och0UbhBGIOyFRA")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1003542269000:-1003405114992").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
