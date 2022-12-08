transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

#label display_timer:

#    $ time_to_exit = False
#    $ Minutes = 0
#    $ Hours = 0

#    $ bg_current = "Classroom"
#    $ timer_update_function_name = "check_events"
#    call Refresh_current_background()
#    show screen timer_logic()
#    show screen timer_screen()
#    show screen debug_time_menu_screen()
#    call screen background_screen()

#    return

label display_timer:
    show screen timer_logic()
    show screen timer_screen()
    if player_location == "Classroom":
        show screen NPC_image_v2()
        call screen background_screen_class()
    if player_location == "Residence":
        show screen NPC_image_v2()
        call screen background_screen_residence()
    if player_location == "Library":
        call screen background_screen_library()
    if player_location == "Park":
        show screen NPC_image_v2()
        call screen background_screen_park()
    if player_location == "Gym":
        show screen NPC_image_v2()
        call screen background_screen_gym()
    if player_location == "Cafeteria":
        show screen NPC_image_v2()
        call screen background_screen_cafe()
    return

label overlay_timer:
    show screen timer_logic()
    show screen timer_screen()

label overlay_timer_debug:
    # $ time_to_exit = False
    $ Minutes = 0
    $ Hours = 0
    show screen debug_time_menu_screen()
    #show screen background_screen()


screen timer_logic:
    zorder 100
    #timer .1 repeat True action [Call("update_time")]
    timer .5 repeat True action [Call("update_time")]

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
    hide screen debug_time_menu_screen

    jump start
    return

label check_events_timer:
    # hardcode events here, or iterate through a list of them in a loop
    #if (Hours == 11 and Minutes >= 10 and Minutes <= 20):
    #    $ renpy.notify("Hi!");
    #if (Hours == 13 and Minutes >= 35 and Minutes <= 40):
    #    $ renpy.notify("Hello!");
    #call check_events
    $ renpy.call(timer_update_function_name)
    return

#label update_time:
#    if (time_to_exit == True):
#        return

#    if (real_time == True):
#        $ Minutes = Minutes + 5;
#        call current_time
#    call check_events_timer()
#    call refresh_current_screen()

label update_time:
    if (time_to_exit == True):
        return
    if (real_time == True):
        #$ Minutes = Minutes + 1;
        $ Minutes = Minutes + 5;
        call current_time
    call check_events
    call NPC_schedule_v2_event_update
    #$ renpy.call("NPC_schedule_v2_event_update")
    if Hours == 17:
        call event_recommand_today
    call display_timer

    if Parts == 3:
        call exit_classroom
        call Residence
    return


label refresh_current_screen:
    #scene bg_class
    #scene bg_current
    call Refresh_current_background()
    show screen timer_logic()
    show screen timer_screen()
    show screen debug_time_menu_screen()
    #call screen background_screen()
    #call screen renpy.current_screen().screen_name[0]
    $ renpy.call_screen("%s"%(current_screen_name))

#label pause_real_time:
#    $ real_time = False
#    call refresh_current_screen()

#label resume_real_time:
#    $ real_time = True
#    call refresh_current_screen()

#label increase_time(time_to_add):
#    $ Hours = Hours + time_to_add
#    call current_time()
#    call refresh_current_screen()

label increase_time(time_to_add):
    $ Hours = Hours + time_to_add
    call update_player_statement
    $ update_NPC_statement()
    call current_time()
    call display_timer
    return

#label decrease_time(time_to_remove):
#    #$ Minutes = Minutes - time_to_remove
#    $ Hours = Hours - time_to_remove
#    call current_time()
#    call refresh_current_screen()

#label go_to_different_screen(name_of_new_screen):
#    $ current_screen_name = name_of_new_screen
#    call refresh_current_screen()


#screen background_screen:
screen background_screen:
    textbutton "{size=28}{color=#FFF}Exit Test{/color}{/size}":
        background "#000"
        xpos 1000
        ypos 200
        action [Jump("exit_timer_screen")]

screen debug_time_menu_screen:
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

    textbutton "{size=28}{color=#FFF}Increase Hour by 1{/color}{/size}":
        background "#000"
        xpos 1000
        ypos 350
        action [Call("increase_time", 1)]

    textbutton "{size=28}{color=#FFF}Decrease Hour by 1{/color}{/size}":
        background "#000"
        xpos 1000
        ypos 400
        action [Call("decrease_time", 1)]

label current_time:
    if Minutes > 59:
        $ Minutes = 0
        $ Hours += 1
        call update_player_statement
        $ update_NPC_statement()

    if Hours > 23:
        $ Hours = 0
        $ Days += 1
        $ event_notify = False
    if Days > 6:
        $ Days = 0
    # if Player is increasing / decreasing time, be able to handle it below:
    if Minutes < 0:
        $ Hours -= 1
        $ Minutes = 0
    if Hours < 0:
        $ Hours = 23
        $ Days -= 1
    if Days < 0:
        $ Days = 5
    if Hours >= 5 and Hours < 12:
        $ Parts = 0
    if Hours >= 12 and Hours < 17:
        $ Parts = 1
    if Hours >= 17 and Hours < 21:
        $ Parts = 2
    if Hours < 4 or Hours > 21:
        $ Parts = 3
    return

label check_events:
    call event_notify_today
    $ ee = 0
    while ee < len(Events_library):
        #if Events_library[ee].eventcheck(WeekDays[Days],Hours,Minutes,True):
        if Events_library[ee].eventcheck2(WeekDays[Days],Hours,Minutes,True):
            $ output_event_info = Events_library[ee].event_name
            $ output_event_info += " happens now."
            if player_location == Events_library[ee].event_location:
                $ player_participate = True
            $ renpy.notify(output_event_info)
        #if Events_library[ee].eventinactive(WeekDays[Days],Hours,Minutes,True):
        if Events_library[ee].eventinactive2(WeekDays[Days],Hours,Minutes,True):
            $ output_event_info = Events_library[ee].event_name
            $ output_event_info += " ends now."
            $ player_participate = False
            #"[output_event_info]"
            $ renpy.notify(output_event_info)

        ##############################################################################################

        #    hide screen create_test_NPC_image
        #    if renpy.random.randint(1,6) != 1:
        #        $ test_NPC_lucy.Location = "Cafeteria"
        #    else:
        #        $ test_NPC_lucy.Location = "Park"

        ##############################################################################################

        #if  Events_library[ee].eventhappennow(WeekDays[Days],Hours,Minutes,True):
        #    if player_location == Events_library[ee].event_location:
        #        $ player_participate = True
        #    else:
        #        $ player_participate = False

        ##############################################################################################
        ##############################################################################################
        $ ee += 1
    return

label reset_labels:
    $ event_notify = False
    $ event_recommand = False
    $ player_participate = False
    call reset_irregular_event
    if renpy.random.randint(1,3) == 1:
        $ event_randomize = True
    return

label update_player_statement:

    #############################################################################################
    #if player_location == "Classroom" and player_participate == True:
    #    $ test_NPC_lucy.Location = player_location
    #    call create_test_NPC_image
    #else:
    #    $ test_NPC_lucy.Location == "Park"
    #    hide screen test_NPC_image
    ##############################################################################################

    if player_location == "Classroom":
        call update_player_statement_classroom
    if player_location == "Residence":
        call update_player_statement_residence
    if player_location == "Park":
        call update_player_statement_park
    if player_location == "Gym":
        call update_player_statement_gym
    if player_location == "Cafeteria":
        call update_player_statement_cafe
    return
