label exit_park:
    hide screen timer_logic
    hide screen timer_screen
    jump imagemap_done
    return 

label update_player_statement_park:
    if player_participate == True:
        $ player_health_local += renpy.random.randint(20,25)
    else:
        $ player_health_local += renpy.random.randint(3,5)
    return
    
screen background_screen_park:
    textbutton "{size=28}{color=#FFF}Exit Park{/color}{/size}":
        background "#000"
        xpos 0.7
        ypos 0.6
        action [Jump("exit_park")]
    textbutton "{size=28}{color=#FFF}Increase Hour by 1{/color}{/size}":
        background "#000"
        xpos 0.7
        ypos 0.65
        action [Call("increase_time", 1)]