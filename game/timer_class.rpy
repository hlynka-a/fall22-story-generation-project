label exit_classroom:
    hide screen timer_logic
    hide screen timer_screen
    jump imagemap_done
    return

label update_player_statement_classroom:
    $ player_study_local += renpy.random.randint(3,5)
    $ player_health_local -= renpy.random.randint(15,20)
    return

label pause_real_time:
    $ real_time = False
    call display_timer
    return

label resume_real_time:
    $ real_time = True
    call display_timer
    return

label decrease_time(time_to_remove):
    $ Hours = Hours - time_to_remove
    call current_time()
    call display_timer
    return

label go_to_different_screen(name_of_new_screen):
    $ current_screen_name = name_of_new_screen
    call display_timer
    return

screen background_screen_class:
    textbutton "{size=28}{color=#FFF}Exit Classroom{/color}{/size}":
        background "#000"
        xpos 0.7
        ypos 0.5
        action [Jump("exit_classroom")]

    textbutton "{size=28}{color=#FFF}Pause Real Time{/color}{/size}":
        background "#000"
        xpos 0.7
        ypos 0.55
        action [Jump("pause_real_time")]

    textbutton "{size=28}{color=#FFF}Resume Real Time{/color}{/size}":
        background "#000"
        xpos 0.7
        ypos 0.6
        action [Jump("resume_real_time")]

    textbutton "{size=28}{color=#FFF}Increase Hour by 1{/color}{/size}":
        background "#000"
        xpos 0.7
        ypos 0.65
        action [Call("increase_time", 1)]

    textbutton "{size=28}{color=#FFF}Decrease Hour by 1{/color}{/size}":
        background "#000"
        xpos 0.7
        ypos 0.7
        action [Call("decrease_time", 1)]