import sys
import pygame
from button import Button
from game_stats import GameStats
from settings import settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from scoreboard import Scoreboard



def run_game():
    pygame.init()
    ai = settings()
    screen = pygame.display.set_mode((ai.screen_width, ai.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai, screen)
    play_button = Button(ai, screen, "play")
    stats = GameStats(ai)
    sb = Scoreboard(ai, screen, stats)
    bullets = Group()
    aliens = Group()
    gf.create_Fleet(ai, screen, ship, aliens)

    while True:
        gf.check_events(ai, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai, screen, stats, sb, ship, aliens, bullets)
            print(len(bullets))
            gf.update_aliens(ai,screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
