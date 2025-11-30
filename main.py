Roll = 0

def on_gesture_shake():
    global Roll
    Roll = randint(1, 6)
    music.set_volume(50)
    music.play(music.string_playable("F E A F B G G D ", 120),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_string("I am a dice")
    if Roll == 1:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
        basic.show_icon(IconNames.GHOST)
    elif Roll == 2:
        basic.show_leds("""
            . . . . .
            . # . . .
            . . . . .
            . . . # .
            . . . . .
            """)
    elif Roll == 3:
        basic.show_leds("""
            . . . . .
            . # . . .
            . . # . .
            . . . # .
            . . . . .
            """)
    elif Roll == 4:
        basic.show_leds("""
            . . . . .
            . # . # .
            . . . . .
            . # . # .
            . . . . .
            """)
    elif Roll == 5:
        basic.show_leds("""
            . . . . .
            . # . # .
            . . # . .
            . # . # .
            . . . . .
            """)
    elif Roll == 6:
        basic.show_leds("""
            . # . # .
            . . . . .
            . # . # .
            . . . . .
            . # . # .
            """)
    music.play(music.create_sound_expression(WaveShape.SQUARE,
            1600,
            1,
            255,
            0,
            300,
            SoundExpressionEffect.NONE,
            InterpolationCurve.CURVE),
        music.PlaybackMode.UNTIL_DONE)
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
