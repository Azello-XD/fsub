import os


class Config:
    API_ID = int(os.environ.get("API_ID", 26859834)) #GANTI "1234" DENGAN API_ID
    API_HASH: str = os.environ.get("API_HASH", "c66a6ff86f1680a1f0c18a1dfc38c764") #GANTI "b184" DENGAN API_HASH , JANGAN HAPUS TANDA (" ") NYA !!!
    BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "7749393831:AAE_3aM2X2R7KqVZRUW6iPdYEwCE4DFOtYc") #GANTI "7u9jl" DENGAN TOKEN BOT , JANGAN HAPUS TANDA (" ") NYA !!!
    OWNER_ID = int(os.environ.get("OWNER_ID", 1927018403)) #GANTI "1234" DENGAN ID PEMILIK BOT
    MONGODB_URI: str = os.environ.get("MONGODB_URI", "mongodb+srv://iyaaaaaa:anjingggg@iyaaanjing.uzkxmrz.mongodb.net/?retryWrites=true&w=majority&appName=iyaaanjing") #GANTI "mongodb://root:passwd@mongo" DENGAN URI MONGO , JANGAN HAPUS TANDA (" ") NYA !!!
    DATABASE_CHAT_ID = int(os.environ.get("DATABASE_CHAT_ID", -1002517617021)) #GANTI DENGAN DATABASE CHANNEL


config: "Config" = Config()
BOT_ID = config.BOT_TOKEN.split(":", 1)[0]
