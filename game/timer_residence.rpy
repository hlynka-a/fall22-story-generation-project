label exit_residence:
    hide screen timer_logic
    hide screen timer_screen
    
    $ player_study_local -= 2

    jump imagemap_done
    return 

label update_player_statement_residence:
    $ player_health_local += 10
    return
    
screen background_screen_residence:
    textbutton "{size=28}{color=#FFF}Exit Residence{/color}{/size}":
        background "#000"
        xpos 0.7
        ypos 0.6
        action [Jump("exit_residence")]
    textbutton "{size=28}{color=#FFF}Increase Hour by 1{/color}{/size}":
        background "#000"
        xpos 0.7
        ypos 0.65
        action [Call("increase_time", 1)]