label Classroom:
    scene bg_class
    $ player_location = "Classroom"
    call display_timer
    return

label Residence:
    scene bg_residence 
    $ player_location = "Residence"
    call display_timer
    return

label Park:
    scene bg_park
    $ player_location = "Park"
    call display_timer
    return

label Gym:
    scene bg_gym
    $ player_location = "Gym"
    call display_timer
    return

label Cafeteria:
    scene bg_cafeteria
    $ player_location = "Cafeteria"
    call display_timer
    return