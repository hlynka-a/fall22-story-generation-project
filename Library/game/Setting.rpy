label start_setting:
    scene bg_Uni
    show eileen happy at right
    e "The first day of the semester. Would you like to begin a new way of life in order to gain new experiences?"

    menu:
        "Yes":
            jump Settings
        "No":
            jump No_Settings
 
    return


label No_Settings:
    if (player_flag == False):
        e "If this is what you want, then, bye."
        $ renpy.quit();
    else:
        jump start
    return

label Settings:
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

    jump Set_priority
    return

screen player_statement_bars:

    $ study = player_study_local
    $ social = player_social_local
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

