define c = Character("firdauskotp")

init python:
    time_left = 10.0

    def start_countdown():
        global time_left
        time_left = 10.0

    def update_countdown():
        global time_left
        time_left -= 0.1
        if time_left <= 0:
            time_left = 0
            renpy.jump("game_over")


screen countdown_hud():
    timer 0.1 repeat True action Function(update_countdown)

    frame:
        xalign 0.98
        yalign 0.02
        padding (12, 8)
        text "Time: [time_left:.1f]s" size 28


screen rick_scene():
    use countdown_hud

    vbox:
        xalign 0.5
        yalign 0.55
        spacing 18

        # add "shocked.png"  # optional if you have a sprite

        hbox:
            xalign 0.5
            spacing 8

            text "Click the " size 44

            textbutton "link":
                text_size 44
                background None
                hover_background None
                action [ OpenURL("https://www.youtube.com/watch?v=dQw4w9WgXcQ"), Jump("win") ]

            text "!" size 44


screen game_over_screen():
    modal True
    add "images/gameover.png"

    vbox:
        xalign 0.5
        yalign 0.8
        spacing 20

        textbutton "Restart" action [ Hide("game_over_screen"), Jump("start") ]
        textbutton "Quit" action Quit(confirm=False)


screen win_screen():
    modal True

    # same background as your game (black). Change if you want an image.
    add Solid("#000")

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20

        text "YOU WIN!" size 60
        textbutton "Restart" action [ Hide("win_screen"), Jump("start") ]
        textbutton "Quit" action Quit(confirm=False)


label start:
    $ start_countdown()
    scene black

    # make sure any overlays are gone
    hide screen game_over_screen
    hide screen win_screen

    show screen rick_scene
    pause


label game_over:
    hide screen rick_scene
    show screen game_over_screen
    pause


label win:
    hide screen rick_scene
    show screen win_screen
    pause
