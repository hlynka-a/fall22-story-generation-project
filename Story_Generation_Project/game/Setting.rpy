label start_setting:
    scene bg_Uni
    show eileen happy at right
    e "The first day of the semester. Would you like to begin a new way of life in order to gain new experiences?"

    menu:
        "Yes":
            #jump Settings
            jump player_setting
        "No":
            jump No_Settings

    return


#label No_Settings:
#    if (player_flag == False):
#        e "If you choose NO, then we'll quit the game. Seems like a waste... I'll ask one more time."
#        e "WOULD YOU LIKE TO BEGIN A NEW WAY OF LIFE IN ORDER TO GAIN NEW EXPERIENCES?"
#        menu:
#            "Yes":
#                jump Settings
#            "No":
#                jump No_Again_Settings
#    else:
#        jump start
#    return

#label No_Priority:
#    if (player_flag == False):
#        e "I told you, if you keep saying NO, we'll just quit the game. I'll ask one more time."
#        e "WOULD YOU LIKE TO SET THE PRIORITIES OF YOU SCHOOL LIFE?"
#        menu:
#            "Yes":
#                if player_flag == True:
#                    hide screen player_statement_bars
#                jump Yes_Priority
#            "No":
#                jump No_Again_Settings
#    else:
#        # if flag is false, then settings have already been set, we can continue to the main adventure.
#        #jump start
#        jump player_begin_game
#    return

#label No_Again_Settings:
#    if (player_flag == False):
#        e "If this is what you want, then, bye."
#        $ renpy.quit();
#    else:
#        jump start
#    return

#label Settings:
#    call Set_name
#    call Set_priority
#    return

#label Set_name:
#    $ player_name = renpy.input("Your name would be..", default = "Anonymous" )
#    e "Good to know you, [player_name]."
#    #$ player = renpy.input("Your name would be..", allows = "abcdefg", exclude = "!@#$123456", length = 8)
#    return

#label Set_priority:
#    if player_flag == False:
#        e "Would you like to set the priorities of your school life?"
#    else:
#        e "Would you like to reset the priorities of your school life?"
#    menu:
#        "Yes":
#            if player_flag == True:
#                hide screen player_statement_bars
#            jump Yes_Priority
#        "No":
#            jump No_Priority
#    return

#label Yes_Priority:
#    $ rank = ["highest","second","lowest"]
#    $ i = 0
#
#    $ priorities_chosen = [False, False, False];
#    while i < len(rank):
#        $ Q = "Which one is your " + rank[i] + " priorities? "
#        e "[Q]"
#        menu:
#            "Health" if priorities_chosen[0] == False:
#                $ priorities_chosen[0] = True
#                $ player_priorities[i] = "Health"
#                $ player_health_local -= i*3
#            "Study" if priorities_chosen[1] == False:
#                $ priorities_chosen[1] = True
#                $ player_priorities[i] = "Study"
#                $ player_study_local -= i*3
#            "Social" if priorities_chosen[2] == False:
#                $ priorities_chosen[2] = True
#                $ player_priorities[i] = "Social"
#                $ player_social_local -= i*3
#        $ i += 1

#    e "You just set the rank, [player_name]"
#    $ A = "Here is your list " + player_priorities[0] + " > " + player_priorities[1]  + " > " + player_priorities[2] + " right?"
#    e "[A]"

#    jump statement_display

#    return

#label statement_display:
#    scene bg_Uni
#    $ player_flag = True
#
#    show eileen happy at left
#    e "We would like to output a statement bars for you to check your initial performence."
#
#    show screen player_statement_bars
#    e "No worries. It is just a beginning, [player_name].\nJust try not to stay the same."
#    hide screen player_statement_bars
#
#    jump Set_priority
#    return

#screen player_statement_bars:

#    $ study = player_study_local
#    $ social = player_social_local
#    $ health = player_health_local

#    frame:
#        xalign 0.99 ypos 20
#        xsize 500
#        vbox:
#            spacing 5

#            bar value ScreenVariableValue("study", 100) style "bar"
#            text 'Study: [study]' align(0,50)
#            bar value ScreenVariableValue("social", 100) style "bar"
#            text 'Social: [social]' align(0,80)
#            bar value ScreenVariableValue("health", 100) style "bar"
#            text 'Health: [health]' align(0,80)
#return

label player_begin_game:
    e "You have everything you need. Now we can begin."
    e "Remember to track your time wisely, and keep watch on your Study, Social and Health points to ensure you do your best."
    e "Your adventure at school begins now! Good luck!"

    e "Hope you are ready for a new beginning."
    # 10 NPC's chosen instead of smaller number to allow seeing enough variety in a game playthrough.
    $ defineRandomNPCs(10)
    $ Days = 0
    $ Hours = 8
    $ Minutes = 30
    call check_NPC_events()
    #jump imagemap_uni
    jump uni_map

    return
