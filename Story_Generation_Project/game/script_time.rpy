

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

#default Minutes = 0
default Minutes = 0
default real_time = True
default time_to_exit = False
default current_screen_name = "background_screen"

label exit_timer_screen:
    $ stopTime()
    $ time_to_exit = True
    hide screen timer_logic
    hide screen timer_screen
    scene black
    call start()
    return

label test_timer_screen:

    ### PROBLEM WITH TIMER: it must be inside a "screen", cannot be inside a "label"
    #timer 1 repeat True action Show('timer_screen')
    #timer 1 repeat True action [Minutes = Minutes + 1]

    ### PROBLEM WITH PYTHON THREADS: if any thread is still active, the game cannot exit.
    ### therefore, be VERY careful with threads!

    ### PROBLEM WITH PYTHON: you cannot seem to call-back to Ren'Py functions very easily
    ### (example, if you are in the middle of a Python function that calls a Ren'Py script function, it will not return back to the Python code)
    ### This is intended behavior by the Ren'Py developers.
    ### Therefore, Python should only really be used for data structures and complex checking / returning of data structures.
    #$ startTime();

    ### PROBLEM WITH REN'PY: 'pause 1' seems to force a pause until user clicks, not what I expect. No good for real-time.

    ### PROBLEM WITH REN'PY: code patterns seems to require that EVERY 'label' ends with calling a screen.
    ### If a label does not activate a new screen, the game automatically ends (goes back to start menu).
    ### Therefore, REN'PY is really built purely for click-based games, not meant for anything else.

    $ time_to_exit = False
    $ Minutes = 0

    scene bg_class
    show screen timer_logic()
    show screen timer_screen()
    call screen background_screen()
    $ current_screen_name = "background_screen"

    #call exit_timer_screen()
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

screen timer_logic:
    zorder 100
    timer 1 repeat True action [Call("update_time")]

screen timer_screen:
    zorder 100
    text str(Minutes) xpos .3 ypos .1 at alpha_dissolve

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

    textbutton "{size=28}{color=#FFF}Go To Different Screen{/color}{/size}":
        background "#000"
        xpos 1000
        ypos 450
        action [Call("go_to_different_screen", "background_screen_02")]

screen background_screen_02:
    textbutton "{size=28}{color=#FFF}Previous Screen{/color}{/size}":
        background "#000"
        xpos 1200
        ypos 200
        action [Call("go_to_different_screen", "background_screen")]
