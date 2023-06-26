# (©)Codexbotz
# Recife By #Mafia_Tobatz
# Kalo clone Gak usah hapus 
# gue tandain akun tele nya ngentod


import logging
import os
from logging.handlers import RotatingFileHandler

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6112017964:AAEGSO_udXEVLL0aWvZA-5eNAZ2kuFUMGmo")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "16246834"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "29b3ffa9245c07f05375b92f38e8f13d")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001688160207"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1715348447"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "panggil_y")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://rfiftini:JWJYrpa_4Oc6iKL_P4mX7TNYpQlrTrO1@rosie.db.elephantsql.com/rfiftini")

# Username CH & Group
CHANNEL = os.environ.get("CHANNEL", "nakama_asl")
GROUP = os.environ.get("GROUP", " executive02")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001872993011"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001700879807"))

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "-1001527136492"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\nJoin dulu jika mau dapat konten free.\n\nhub @teknisi69_bot jika bot mati. </b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "1715348447 1856497356").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nJoin group and channelnya dulu yah, baru bisa dapat konten free. \n\nhubungi @teknisi69_bot jika bot mati</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True"

ADMINS.append(1715348447)
ADMINS.append(1856497356)
ADMINS.append(0)
ADMINS.append(0)
ADMINS.append(0)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
