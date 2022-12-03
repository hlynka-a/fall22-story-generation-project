label uni_map:
    scene bg_Uni
    call screen imagemap_university
    return

screen imagemap_university():
    # Modified from RenPy TUTORIAL example.
    imagemap:
        #if (currentTime == timeOfDay[0]):
        #    idle "imagemap ground morning"
        #elif (currentTime == timeOfDay[1]):
        #    idle "imagemap ground afternoon"
        #elif (currentTime == timeOfDay[2]):
        #    idle "imagemap ground evening"
        #else:
        #    idle "imagemap ground"

        idle "imagemap ground afternoon"
        hover "imagemap hover"

   
    #    hotspot (100, 600, 300, 100) action Jump("advancetime") alt "Advance Time"
        hotspot (100, 200, 100, 100)  alt "Classroom"
        hotspot (300, 200, 100, 100) alt "Library"
        hotspot (500, 200, 100, 100) alt "Park"
        hotspot (100, 300, 100, 100) alt "Cafeteria"
        hotspot (300, 300, 100, 100) alt "Gym"
        hotspot (500, 300, 100, 100) alt "Residence"
        hotspot (0.9,0.6,100,100) alt "Quit"
        



    #$ num_of_people_classroom = num_of_people_at(0)
    #$ notify_message_classroom = "In the classroom, there are currently " + str(num_of_people_classroom).zfill(2)+" here."
    #$ num_of_people_library = num_of_people_at(1)
    #$ notify_message_library = "In the library, there are currently " + str(num_of_people_library).zfill(2)+" here."
    #$ num_of_people_park = num_of_people_at(2)
    #$ notify_message_park = "At the park, there are currently " + str(num_of_people_park).zfill(2)+" here."
    #$ notify_message_time = "The time and day are now " + str(currentDay) + " and " + str(currentTime) + "."

    imagebutton:
        xpos 100
        ypos 200
        idle "cr_idle"
        hover "cr_hover"
        #hovered Notify(notify_message_classroom)
        action Jump("Classroom")

    imagebutton:
        xpos 300
        ypos 200
        idle "lb_idle"
        hover "lb_hover"
        #hovered Notify(notify_message_library)
        action Jump("Library")

    imagebutton:
        xpos 500
        ypos 200
        idle "pk_idle"
        hover "pk_hover"
        #hovered Notify(notify_message_park)
        action Jump("Park")
    
    imagebutton:
        xpos 0.9
        ypos 0.6
        idle "ex_idle"
        hover "ex_hover"
        #hovered Notify(notify_message_park)
        action Jump("Quit_game")
    
    imagebutton:
        xpos 100
        ypos 300
        idle "cf_idle"
        hover "cf_hover"
        #hovered Notify(notify_message_park)
        action Jump("Cafeteria")
    
    imagebutton:
        xpos 300
        ypos 300
        idle "gy_idle"
        hover "gy_hover"
        #hovered Notify(notify_message_park)
        action Jump("Gym")

    imagebutton:
        xpos 500
        ypos 300
        idle "re_idle"
        hover "re_hover"
        #hovered Notify(notify_message_park)
        action Jump("Residence")

    #imagebutton:
    #    xpos 100
    #    ypos 600
    #    idle "at_idle"
    #    hover "at_hover"

    #    hovered Notify(notify_message_time)
    #    action Jump("Advancetime")
return

label imagemap_done:
    scene bg_Uni
    if Parts == 3:
        "It is time to sleep."
        jump Residence
    else:
        "Let's go back to the map."
        jump uni_map

    return