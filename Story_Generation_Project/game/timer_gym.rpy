label exit_gym:
    hide screen timer_logic
    hide screen timer_screen
    jump imagemap_done
    return 

label update_player_statement_gym:
    $ player_study_local -= 4
    $ player_health_local += 10
    return
    
screen background_screen_gym:
    textbutton "{size=28}{color=#FFF}Exit Gym{/color}{/size}":
        background "#000"
        xpos 0.7
        ypos 0.6
        action [Jump("exit_gym")]
    textbutton "{size=28}{color=#FFF}Increase Hour by 1{/color}{/size}":
        background "#000"
        xpos 0.7
        ypos 0.65
        action [Call("increase_time", 1)]