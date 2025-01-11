import pygame
from pygame.sprite import Group

import game_functions as gf
from game_stats import GameStats

# from alien import Alien
from settings import Settings
from ship import Ship


def run_game():
    """Initialize the game and create a screen object."""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create a fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)

    # Main loop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

        # Check if the game is over.
        if not stats.game_active:
            pygame.mixer.music.pause()
            pygame.mixer.sound.stop()


run_game()
