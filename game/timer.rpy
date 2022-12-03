# display style
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

# display functions
label display_timer:
    show screen timer_logic()
    show screen timer_screen()
    if player_location == "Classroom":
        call screen background_screen_class()
    if player_location == "Residence":
        call screen background_screen_residence()
    if player_location == "Library":
        call screen background_screen_library()
    if player_location == "Park":
        call screen background_screen_park()
    if player_location == "Gym":
        call screen background_screen_gym()
    if player_location == "Cafeteria":
        call screen background_screen_cafe()
    return

screen timer_logic:
    zorder 100
    timer 0.5 repeat True action [Call("update_time")]
return

screen timer_screen:
    zorder 100
    text str(WeekDays[Days]) xpos .1 ypos .1 color '#FF0000' at alpha_dissolve
    text str(Chunks[Parts]) xpos .2 ypos .1 color '#FF0000'at alpha_dissolve
    text str(Hours) xpos .3 ypos .1 color '#FF0000'at alpha_dissolve
    text str(Minutes) xpos .4 ypos .1 color '#FF0000'at alpha_dissolve
return

label increase_time(time_to_add):
    $ Hours = Hours + time_to_add
    call update_player_statement
    call current_time()
    call display_timer
    return

label update_time:
    if (time_to_exit == True):
        return
    if (real_time == True):
        #$ Minutes = Minutes + 1;
        $ Minutes = Minutes + 5;
        call current_time
    call check_events
    if Hours == 13:
        call event_recommand_today
    call display_timer

    if Parts == 3:
        call exit_classroom
        call Residence
    return

label current_time:
    if Minutes > 59:
        $ Minutes = 0
        $ Hours += 1
        call update_player_statement

    if Hours > 23:
        $ Hours = 0
        $ Days += 1
        call reset_labels
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
        if Events_library[ee].eventcheck(WeekDays[Days],Hours,Minutes,True):
            $ output_event_info = Events_library[ee].event_name
            $ output_event_info += " happens now."
            $ renpy.notify(output_event_info)
        if Events_library[ee].eventinactive(WeekDays[Days],Hours,Minutes,True):
            $ output_event_info = Events_library[ee].event_name
            $ output_event_info += " ends now."
            #"[output_event_info]"
            $ renpy.notify(output_event_info)
        $ ee += 1
    return

label reset_labels:
    $ event_notify = False
    $ event_recommand = False
    call reset_irregular_event
    if renpy.random.randint(1,3) == 1:
        $ event_randomize = True
    return 

label update_player_statement:
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

