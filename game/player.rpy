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
            jump No_Settings
    return

label Yes_Priority:
    $ rank = ["highest","second","lowest"]
    $ i = 0

    while i < len(rank):
        $ Q = "which one is your " + rank[i] + " priorities? "
        e "[Q]"
        menu:
            "Health":
                $ player_priorities[i] = "Health"
                $ player_health_local -= i*3
            "Study":
                $ player_priorities[i] = "Study"
                $ player_study_local -= i*3
            "Social":
                $ player_priorities[i] = "Social"
                $ player_social_local -= i*3
        $ i += 1

    e "You just set the rank, [player_name]"
    $ A = "Here is your list " + player_priorities[0] + " > " + player_priorities[1]  + " > " + player_priorities[2] + " right?"
    e "[A]"

    jump statement_display

    return

label statement_display:
    scene bg_Uni
    $ player_flag = True

    show eileen happy at left
    e "We would like to output a statement bars for you to check your initial performence."

    show screen player_statement_bars
    e "No worries. It is just a beginning, [player_name].\nJust try not to stay the same."

    return

screen player_statement_bars:

    if player_study_local > 100:
        $ player_study_local = 100
    if player_study_local < 0:
        $ player_study_local = 0 
    $ study = player_study_local

    if player_social_local > 100 :
        $ player_social_local = 100
    if player_social_local < 0:
        $ player_social_local = 100
    $ social = player_social_local 

    if player_health_local > 100:
        $ player_health_local = 100
    if player_health_local < 0:
        $ player_health_local = 0
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


