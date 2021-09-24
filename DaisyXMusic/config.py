# DAISYXMUSIC- Telegram bot project
# Copyright (C) 2021  Roj Serbest
# Copyright (C) 2021  Inuka Asith
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Modified by Inukaasith

import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "AQCsuAnE3LGTKF-wulM7CuX72nhibhPXrysW6cGeZUTZ0wVG2e-SNk-DHDj6dYqIlKfR7x6XgWtDmjWl81_kH5Pi8f95vRl_J344bdYebM6X2OIZj-zMpulfUVqECx7lWONu2KDWuBykpVDUiHVm6Ug2MqXMEmMdQAZ832sDzGVP0M9NIRblytLdW914CwCPGUQuEnPLjimPh1Z7CazFu-RJEr9-cRIIAF0TvIm81CcT2bUMevDV9Asvhv2eHzlyznq0vaxhmgMTnPubkEoUyKcv8eIjDxgb9HI6HspDsu3T76ybFnxDq4lDGl5zxR9qv7xVA_fqn7c77ZivKa4fNPPxcYBvogA")
BOT_TOKEN = getenv("BOT_TOKEN", "1903350099:AAEN0UWc83XdvdiJuypUX4yTUS8_QNX65Pc")
BOT_NAME = getenv("BOT_NAME", "Mikey")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "DaisyXupdates")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/d198f5cded6b1390ba801.jpg")
admins = {}
API_ID = int(getenv("API_ID", "1995654"))
API_HASH = getenv("API_HASH", "91aa713a74d1bccb50cd1c03758316bf")
BOT_USERNAME = getenv("SanoManjiro_Robot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "MikeyVCBot")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Mikey_Support")
PROJECT_NAME = getenv("PROJECT_NAME", "Mikey VC v1")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/teamdaisyx/daisyxmusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
ARQ_API_KEY = getenv("ARQ_API_KEY", 'LRLZAM-NLHKDS-TDLCLI-ZHFIMB-ARQ')
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "860540443").split()))
