label imagemap_uni:
    call screen imagemap_university
   

screen imagemap_university():
    # Copied from TUTORIAL example.
    # Curious bug: I didn't change the name of the functions (screen, label), and it seemed to be calling the TUTORIAL version instead of mine.
    # But when I modified text displayed inside each function (not the name of the function itself), the correct functions were called.

    imagemap:
        if (currentTime == timeOfDay[0]):
            idle "imagemap ground morning"
        elif (currentTime == timeOfDay[1]):
            idle "imagemap ground afternoon"
        elif (currentTime == timeOfDay[2]):
            idle "imagemap ground evening"
        else:
            idle "imagemap ground"

        idle "imagemap ground morning"
        hover "imagemap hover"

        hotspot (100, 200, 100, 100) action Jump("classroom") alt "Classroom"
        hotspot (300, 200, 100, 100) action Jump("library") alt "Library"
        hotspot (100, 600, 300, 100) action Jump("advancetime") alt "Advance Time"
        hotspot (0.9,0.6,100,100) action Jump("start") alt "qiut"



    $ num_of_people_classroom = num_of_people_at(0)
    $ notify_message_classroom = "In the classroom, there are currently " + str(num_of_people_classroom).zfill(2)+" here."
    $ num_of_people_library = num_of_people_at(1)
    $ notify_message_library = "In the library, there are currently " + str(num_of_people_library).zfill(2)+" here."
    $ num_of_people_park = num_of_people_at(2)
    $ notify_message_park = "At the park, there are currently " + str(num_of_people_park).zfill(2)+" here."
    $ notify_message_time = "The time and day are now " + str(currentDay) + " and " + str(currentTime) + "."

    imagebutton:
        xpos 100
        ypos 200
        idle "cr_idle"
        hover "cr_hover"

        hovered Notify(notify_message_classroom)
        action Jump("classroom")

    imagebutton:
        xpos 300
        ypos 200
        idle "lb_idle"
        hover "lb_hover"

        hovered Notify(notify_message_library)
        action Jump("library")

    imagebutton:
        xpos 500
        ypos 200
        idle "pk_idle"
        hover "pk_hover"

        hovered Notify(notify_message_park)
        action Jump("library")

    imagebutton:
        xpos 100
        ypos 600
        idle "at_idle"
        hover "at_hover"

        hovered Notify(notify_message_time)
        action Jump("advancetime")
return
