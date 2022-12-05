label imagemap_uni:
    #$ hover_location_title = "(hover for location)"
    show screen timer_screen
    call screen imagemap_university


#$ hover_location_title = "(some location)"

screen location_population_display():
    #$renpy.notify("[hover_location_title]")
    $ listOfNPCsAtLocation = get_NPCs_at_location(hover_location_title)
    frame:
        xalign 1.0 ypos 25
        vpgrid:
            cols 1
            xalign 1.0 ypos 0 xysize (400, 600)
            child_size (400, 100)
            scrollbars "vertical"
            side_spacing 5
            mousewheel True
            arrowkeys True
            #add text "Library"
            #add text "There are 0 people here"
            text "                          "
            text "[hover_location_title]"
            text "------"
            for i in range(0, len(listOfNPCsAtLocation)):
                $ NPC_name = listOfNPCsAtLocation[i].npc_firstname + " " + listOfNPCsAtLocation[i].npc_lastname
                text "[NPC_name]"
            text ""

#screen imagemap_university():
#    # Copied from TUTORIAL example.
#    # Curious bug: I didn't change the name of the functions (screen, label), and it seemed to be calling the TUTORIAL version instead of mine.
#    # But when I modified text displayed inside each function (not the name of the function itself), the correct functions were called.

#    imagemap:
#        if (currentTime == Chunks[0]):
#            idle "imagemap ground morning"
#        elif (currentTime == Chunks[1]):
#            idle "imagemap ground afternoon"
#        elif (currentTime == Chunks[2]):
#            idle "imagemap ground evening"
#        else:
#            idle "imagemap ground morning"

#        idle "imagemap ground morning"
#        hover "imagemap hover"

#        #hotspot (100, 200, 100, 100) action Jump("classroom") alt "Classroom"
#        #hotspot (300, 200, 100, 100) action Jump("library") alt "Library"
#        #hotspot (100, 600, 300, 100) action Jump("advancetime") alt "Advance Time"
#        hotspot (0.9,0.6,100,100) action [Hide("location_population_display"),Jump("start")] alt "qiut"



#    #$ num_of_people_classroom = num_of_people_at(0)
#    $ num_of_people_classroom = len(get_NPCs_at_location("Classroom"))
#    $ notify_message_classroom = "In the classroom, there are currently " + str(num_of_people_classroom).zfill(2)+" here."
#    #$ num_of_people_library = num_of_people_at(1)
#    $ num_of_people_library = len(get_NPCs_at_location("Library"))
#    $ notify_message_library = "In the library, there are currently " + str(num_of_people_library).zfill(2)+" here."
#    #$ num_of_people_park = num_of_people_at(2)
#    $ num_of_people_park = len(get_NPCs_at_location("Park"))
#    $ notify_message_park = "At the park, there are currently " + str(num_of_people_park).zfill(2)+" here."
#    $ notify_message_time = "The time and day are now " + str(currentDay) + " and " + str(currentTime) + "."




#    #if hover_location_title == "Classroom":
#        #$ renpy.notify("Classroom was hovered.")
#        #show screen location_population_display

#    imagebutton:
#        # classroom
#        xpos 100
#        ypos 200
#        idle "cr_idle"
#        hover "cr_hover"
#
#        #hovered Notify(notify_message_classroom)
#        hovered [
#            SetVariable("hover_location_title", "Classroom"),
#            Show("location_population_display")
#        ]
#        #unhovered[
#            #Hide("location_population_display")
#        #]
#        action [Hide("location_population_display"),Jump("classroom")]
#
#    imagebutton:
#        # library
#        xpos 300
#        ypos 200
#        idle "lb_idle"
#        hover "lb_hover"

#        #hovered Notify(notify_message_library)
#        hovered [
#            SetVariable("hover_location_title", "Library"),
#            Show("location_population_display")
#        ]
#        action [Hide("location_population_display"),Jump("library")]

#    imagebutton:
#        # park
#        xpos 500
#        ypos 200
#        idle "pk_idle"
#        hover "pk_hover"

#        #hovered Notify(notify_message_park)
#        hovered [
#            SetVariable("hover_location_title", "Park"),
#            Show("location_population_display")
#        ]
#        action [Hide("location_population_display"),Jump("library")]

#    imagebutton:
#        xpos 100
#        ypos 600
#        idle "at_idle"
#        hover "at_hover"

#        hovered Notify(notify_message_time)
#        action [Hide("location_population_display"),Jump("advancetime")]





#return
