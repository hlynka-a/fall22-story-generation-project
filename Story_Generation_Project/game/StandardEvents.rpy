label classroom:
    scene bg_class
    $ classes = ["Math 1007", "Math 1104","COMP 1805","COMP 2401", "COMP 2402", "COMP 3000"]
    $ randclass = renpy.random.randint(0, 5)
    $ class_schedule = "It is time for class " + classes[randclass]

    e "You chose classroom from MY EXAMPLE."
    $ num_of_people = num_of_people_at(0)
    e "In the classroom, there are currently [num_of_people] here."

    if randclass > 3:
        $ class_schedule += " . You'd better work hard on this one."
    else:
        $ class_schedule += " . Take it easy."
    e "[class_schedule]"

    e "Because of your hard work, today. You just got 3 percent on Study. Good time to take a coffee break."
    $ player_study_local += 3
    $ player_health_local -= 30
    jump imagemap_done

label library:
    scene bg_lib
    show eileen happy

    $ num_of_people = num_of_people_at(1)
    e "In the library, there are currently [num_of_people] here."
    e "What a wonderful experience today. What would you like to do next?"

    show eileen happy at right
    menu:
        "Study by myself.":
            jump self_study
        "Study with my peers.":
            jump study_group
        "Attend the workshop.":
            jump workshop
        "Somewhere else":
            jump imagemap_done
return

label self_study:
    $ randStudy = renpy.random.randint(1,3)
    "Good choice, [player_name]. You just add [randStudy] percent on your study. "
    $ player_study_local += randStudy
    $ player_health_local -= 20
    jump library
    return

label study_group:
    $ randStudy = renpy.random.randint(1,2)
    $ randSocial = renpy.random.randint(1,2)
    "Not bad, [player_name]. You just add [randStudy] percent on you study and [randSocial] percent on social."
    $ player_social_local += randSocial
    $ player_study_local += randStudy
    $ player_health_local -= 25
    jump library
    return

label workshop:
    "The workshop is really helping with the concerns. 5 percent on your study, [player_name]."
    $ player_health_local -= 30
    $ player_study_local += 5
    jump library
    return

label advancetime:
    $ update_time()
    e "The time and day are now [currentDay] and [currentTime]."
    $ player_health_local = 100
    call check_NPC_events()
    jump imagemap_done

label art:
    e "You chose art from MY EXAMPLE."
    e "Really good background art is hard to make, which is why so many games use filtered photographs. Maybe you can change that."
    jump imagemap_done

label home:
    e "You chose to go home from MY EXAMPLE."
    jump imagemap_done

label imagemap_done:
    scene bg_Uni
    show eileen happy
    e "Let's go back to the map."
    jump imagemap_uni

    return
