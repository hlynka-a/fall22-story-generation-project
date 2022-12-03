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

label No_Settings:
    if (player_flag == False):
        e "If this is what you want, then, bye."
        call quit_game
    else:
        hide screen player_statement_bars
        pass
    return

label Quit_game:
    $ renpy.quit();
    return