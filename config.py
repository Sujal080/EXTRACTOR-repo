"""
from os import getenv


API_ID = int(getenv("API_ID", "26330942"))
API_HASH = getenv("API_HASH", "5de9fd033aa828dfd3bf0c28adeee660")
BOT_TOKEN = getenv("BOT_TOKEN", "7363509425:AAF92zS7bv50rpuH6NtlaCN-BOf1GmTaMAM")
OWNER_ID = int(getenv("OWNER_ID", "6883471516"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6883471516").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://biklriplit:efaXfv2Ps9MRfner@cluster0.4hfu8zj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002710444355"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002710444355"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5840594311 7621154046 7793979196 5798579221").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS"))

