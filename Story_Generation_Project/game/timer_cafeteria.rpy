label exit_cafe:
    hide screen timer_logic
    hide screen timer_screen
    jump imagemap_done
    return 

label update_player_statement_cafe:
    if player_participate == True:
        $ player_health_local += renpy.random.randint(8,10)
        $ player_social_local += renpy.random.randint(5,8)
    else:
        $ player_health_local += renpy.random.randint(1,5)
    return
    
screen background_screen_cafe:
    textbutton "{size=28}{color=#FFF}Exit Cafeteria{/color}{/size}":
        background "#000"
        xpos 0.7
        ypos 0.6
        action [Jump("exit_cafe")]
    textbutton "{size=28}{color=#FFF}Increase Hour by 1{/color}{/size}":
        background "#000"
        xpos 0.7
        ypos 0.65
        action [Call("increase_time", 1)]