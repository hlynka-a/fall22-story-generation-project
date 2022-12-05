label welcome:
    scene bg_Uni
    show eileen happy at right
    e "The first day of the semester. Would you like to begin a new way of life in order to gain new experiences?"

    menu:
        "Yes":
            pass
        "No":
            jump No_Settings
    return

#label No_Settings:
#    if (player_flag == False):
#        e "If this is what you want, then, bye."
#        call quit_game
#    else:
#        hide screen player_statement_bars
#        pass
#    return
label No_Settings:
    if (player_flag == False):
        e "If you choose NO, then we'll quit the game. Seems like a waste... I'll ask one more time."
        e "WOULD YOU LIKE TO BEGIN A NEW WAY OF LIFE IN ORDER TO GAIN NEW EXPERIENCES?"
        menu:
            "Yes":
                jump player_setting
            "No":
                jump No_Again_Settings
    else:
        jump start
    return

label No_Again_Settings:
    if (player_flag == False):
        e "If this is what you want, then, bye."
        call quit_game
    else:
        jump start
    return


label quit_game:
    #$ renpy.quit();
    $ MainMenu(confirm=False)()
    return
