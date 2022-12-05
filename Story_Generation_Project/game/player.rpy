label init_player:
    scene bg_Uni
    show eileen happy at right
    menu:
        "Setting":
            jump player_setting
        "Skip Setting":
            call statement_display
            call Set_priority
    return

label player_setting:
    call Set_name
    call Set_priority
    return

label Set_name:
    $ player_name = renpy.input("Your name would be..", default = "Anonymous" )
    e "Good to know you, [player_name]."
    #$ player = renpy.input("Your name would be..", allows = "abcdefg", exclude = "!@#$123456", length = 8)
    return

label Set_priority:
    if player_flag == False:
        e "Would you like to set the priorities of your school life?"
    else:
        e "Would you like to reset the priorities of your school life?"
    menu:
        "Yes":
            if player_flag == True:
                hide screen player_statement_bars
            jump Yes_Priority
        "No":
            #jump No_Settings
            jump No_Priority
    return

label Yes_Priority:
    $ rank = ["highest","second","lowest"]
    $ i = 0

    $ priorities_chosen = [False, False, False];
    while i < len(rank):
        $ Q = "Which one is your " + rank[i] + " priorities? "
        e "[Q]"
        menu:
            "Health" if priorities_chosen[0] == False:
                $ priorities_chosen[0] = True
                $ player_priorities[i] = "Health"
                $ player_health_local -= i*3
            "Study" if priorities_chosen[1] == False:
                $ priorities_chosen[1] = True
                $ player_priorities[i] = "Study"
                $ player_study_local -= i*3
            "Social" if priorities_chosen[2] == False:
                $ priorities_chosen[2] = True
                $ player_priorities[i] = "Social"
                $ player_social_local -= i*3
        $ i += 1

    e "You just set the rank, [player_name]"
    $ A = "Here is your list " + player_priorities[0] + " > " + player_priorities[1]  + " > " + player_priorities[2] + " right?"
    e "[A]"

    jump statement_display

    return

label No_Priority:
    if (player_flag == False):
        e "I told you, if you keep saying NO, we'll just quit the game. I'll ask one more time."
        e "WOULD YOU LIKE TO SET THE PRIORITIES OF YOU SCHOOL LIFE?"
        menu:
            "Yes":
                if player_flag == True:
                    hide screen player_statement_bars
                jump Yes_Priority
            "No":
                jump No_Again_Settings
    else:
        # if flag is false, then settings have already been set, we can continue to the main adventure.
        #jump start
        jump player_begin_game
    return

#label No_Again_Settings:
#    if (player_flag == False):
#        e "If this is what you want, then, bye."
#        $ renpy.quit();
#    else:
#        jump start
#    return

label statement_display:
    scene bg_Uni
    $ player_flag = True

    show eileen happy at left
    e "We would like to output a statement bars for you to check your initial performence."

    show screen player_statement_bars
    e "No worries. It is just a beginning, [player_name].\nJust try not to stay the same."

    jump Set_priority

    return



screen player_statement_bars:
    if player_study_local > 100:
        $ study = 100
    elif player_study_local < 0:
        $ study = 0
    else:
        $ study = player_study_local

    if player_social_local > 100:
        $ social = 100
    elif player_social_local < 0:
        $ social = 0
    else:
        $ social = player_social_local

    if player_health_local > 100:
        $ health = 100
    elif player_health_local < 0:
        $ health = 0
    else:
        $ health = player_health_local

    frame:
        xalign 0.99 ypos 20
        xsize 500
        vbox:
            spacing 5

            bar value ScreenVariableValue("study", 100) style "bar"
            text 'Study: [study]' align(0,50)
            bar value ScreenVariableValue("social", 100) style "bar"
            text 'Social: [social]' align(0,80)
            bar value ScreenVariableValue("health", 100) style "bar"
            text 'Health: [health]' align(0,80)
return
