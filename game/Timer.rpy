transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

label dispaly_timer:

    $ time_to_exit = False
    $ Minutes = 0

    scene bg_class
    show screen timer_logic()
    show screen timer_screen()
    call screen background_screen()

    return

screen timer_logic:
    zorder 100
    timer .1 repeat True action [Call("update_time")]

screen timer_screen:
    zorder 100
    text str(WeekDays[Days]) xpos .1 ypos .1 color '#FF0000' at alpha_dissolve 
    text str(Chunks[Parts]) xpos .2 ypos .1 color '#FF0000'at alpha_dissolve
    text str(Hours) xpos .3 ypos .1 color '#FF0000'at alpha_dissolve
    text str(Minutes) xpos .4 ypos .1 color '#FF0000'at alpha_dissolve

label exit_timer_screen:

    $ time_to_exit = True
    hide screen timer_logic
    hide screen timer_screen

    jump start
    return

label check_events_timer:
    # hardcode events here, or iterate through a list of them in a loop
    if (Minutes >= 10 and Minutes <= 20):
        $ renpy.notify("Hi!");
    if (Minutes >= 35 and Minutes <= 40):
        $ renpy.notify("Hello!");
    return

label update_time:
    if (time_to_exit == True):
        return

    if (real_time == True):
        $ Minutes = Minutes + 1;
        call current_time
    call check_events_timer()
    call refresh_current_screen()


label refresh_current_screen:
    scene bg_class
    show screen timer_logic()
    show screen timer_screen()
    #call screen background_screen()
    #call screen renpy.current_screen().screen_name[0]
    $ renpy.call_screen("%s"%(current_screen_name))

label pause_real_time:
    $ real_time = False
    call refresh_current_screen()

label resume_real_time:
    $ real_time = True
    call refresh_current_screen()

label increase_time(time_to_add):
    $ Minutes = Minutes + time_to_add
    call refresh_current_screen()

label decrease_time(time_to_remove):
    $ Minutes = Minutes - time_to_remove
    call refresh_current_screen()

label go_to_different_screen(name_of_new_screen):
    $ current_screen_name = name_of_new_screen
    call refresh_current_screen()


screen background_screen:

    textbutton "{size=28}{color=#FFF}Exit Test{/color}{/size}":
        background "#000"
        xpos 1000
        ypos 200
        action [Jump("exit_timer_screen")]

    textbutton "{size=28}{color=#FFF}Pause Real Time{/color}{/size}":
        background "#000"
        xpos 1000
        ypos 250
        action [Jump("pause_real_time")]

    textbutton "{size=28}{color=#FFF}Resume Real Time{/color}{/size}":
        background "#000"
        xpos 1000
        ypos 300
        action [Jump("resume_real_time")]

    textbutton "{size=28}{color=#FFF}Increase Time by 10{/color}{/size}":
        background "#000"
        xpos 1000
        ypos 350
        action [Call("increase_time", 10)]

    textbutton "{size=28}{color=#FFF}Decrease Time by 10{/color}{/size}":
        background "#000"
        xpos 1000
        ypos 400
        action [Call("decrease_time", 10)]

label current_time:
    if Minutes > 59:
        $ Minutes = 0
        $ Hours += 1
    if Hours > 23:
        $ Hours = 0
        $ Days += 1
    if Days > 6:
        $ Days = 0
    if Hours >= 5 and Hours < 12:
        $ Parts = 0
    if Hours >= 12 and Hours < 17:
        $ Parts = 1
    if Hours >= 17 and Hours < 21:
        $ Parts = 2
    if Hours < 4 or Hours > 21:
        $ Parts = 3
    return    