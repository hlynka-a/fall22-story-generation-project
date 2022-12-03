label Library:
    scene bg_lib
    show eileen happy
    $ player_location = "Library"
    e "We currently in the Library now.\nWhat a wonderful experience today. What would you like to do next?"

    show eileen happy at right
    menu:
        "Study by myself.":
            jump self_study
        "Study with my peers.":
            jump study_group
        "Attend the workshop." if WeekDays[Days] != "Fri" and 18 < Hours < 20:
            jump workshop
        "Somewhere else":
            jump imagemap_done 
    return

label self_study:
    $ randStudy = renpy.random.randint(1,3)
    "Good choice, [player_name]. You just add [randStudy] percent on your study. "
    $ player_study_local += randStudy
    $ player_health_local -= 20
    jump Library
    return

# if there are NPCs, then could do the study group
label study_group:
    $ randStudy = renpy.random.randint(1,2)
    $ randSocial = renpy.random.randint(1,2)
    "Not bad, [player_name]. You just add [randStudy] percent on you study and [randSocial] percent on social."
    $ player_social_local += randSocial
    $ player_study_local += randStudy
    $ player_health_local -= 25
    jump Library
    return

# only if the current day has a workshop
label workshop:
    
    "The workshop is really helping with the concerns. 5 percent on your study, [player_name]."
    $ player_health_local -= 30
    $ player_study_local += 5
    jump Library
    return