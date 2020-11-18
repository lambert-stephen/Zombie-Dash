import pygame


import pyglet
import os
import sys
import vlc
import time


def callback(self, player):

	print
	# print 'FPS =',  player.get_fps()
	# print 'time =', player.get_time(), '(ms)'
	# print 'FRAME =', .001 * player.get_time() * player.get_fps()

def watchAd(p):
    clock = pygame.time.Clock()

    p.ad = p.ad + 1

    # Create instane of VLC and create reference to movie.
    vlcInstance = vlc.Instance()
    media = vlcInstance.media_new('ads/ad' + str(p.ad) + '.mp4')

    p.ad = p.ad%12

    p.energy_level += 10
    if p.energy_level > 100:
        p.energy_level = 100

    # Create new instance of vlc player
    player = vlcInstance.media_player_new()

    # Pass pygame window id to vlc player, so it can render its contents there.
    win_id = pygame.display.get_wm_info()['window']
    if sys.platform == "linux2":  # for Linux using the X Server
        player.set_xwindow(win_id)
    elif sys.platform == "win32":  # for Windows
        player.set_hwnd(win_id)
    elif sys.platform == "darwin":  # for MacOS
        player.set_agl(win_id)

    # Load movie into vlc player instance
    player.set_media(media)

    # Quit pygame mixer to allow vlc full access to audio device (REINIT AFTER MOVIE PLAYBACK IS FINISHED!)
    pygame.mixer.quit()

    # Start movie playback
    player.play()

    player.video_set_mouse_input(False)
    player.video_set_key_input(False)

    while player.get_state() != vlc.State.Ended:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(2)
            if event.type == pygame.KEYDOWN:
                print
                "OMG keydown!"
            if event.type == pygame.MOUSEBUTTONDOWN:
                print
                "we got a mouse button down!"

    player.stop()

    print('leaving ad func')

    return 'main menu'











    # vidPath = 'longlongman.mp4'
    # window = game_display
    # player = pyglet.media.Player()
    # source = pyglet.media.StreamingSource()
    # MediaLoad = pyglet.media.load(vidPath)
    #
    # player.queue(MediaLoad)
    # player.play()
    #
    # @window.event
    # def on_draw():
    #     if player.source and player.source.video_format:
    #         player.get_texture().blit(50,50)
    #
    # pyglet.app.run()
    #
    # return 'main menu'

    # FPS = 60
    #
    # pygame.init()
    # clock = pygame.time.Clock()
    # movie = pygame.movie.Movie('longlongman.mpg')
    # screen = pygame.display.set_mode(movie.get_size())
    # movie_screen = pygame.Surface(movie.get_size()).convert()
    #
    # movie.set_display(movie_screen)
    # movie.play()
    #
    # playing = True
    # while playing:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             movie.stop()
    #             playing = False
    #
    #     screen.blit(movie_screen, (0, 0))
    #     pygame.display.update()
    #     clock.tick(FPS)
    #
    # pygame.quit()

    # exp = xpy.control.initialize()
    # v = xpy.stimuli.Video("longlongman.mp4")
    # xpy.control.stop_audiosystem()
    # v.preload()
    #
    # v.play()
    # v.present()
    # v.wait_end()
    # v.stop()
    #
    # del v
    #
    # return "main_menu"
