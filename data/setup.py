"""
This module initializes the display and creates dictionaries of resources.
"""

import os
import pygame as pg
from . import tools
from .import constants as c

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RESOURCE_DIR = BASE_DIR / "resources"


ORIGINAL_CAPTION = c.ORIGINAL_CAPTION


os.environ['SDL_VIDEO_CENTERED'] = '1'
pg.init()
pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])
pg.display.set_caption(c.ORIGINAL_CAPTION)
SCREEN = pg.display.set_mode(c.SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()


FONTS = tools.load_all_fonts(str(RESOURCE_DIR / "fonts"))
MUSIC = tools.load_all_music(str(RESOURCE_DIR / "music"))
GFX = tools.load_all_gfx(str(RESOURCE_DIR / "graphics"))
SFX = tools.load_all_sfx(str(RESOURCE_DIR / "sound"))
