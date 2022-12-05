label test_dialogue_tracery_screen:
    scene bg_class

    # $ classes = ["Math 1007", "Math 1104","COMP 1805","COMP 2401", "COMP 2402", "COMP 3000"]
    # $ randclass = renpy.random.randint(0, 5)
    #$ class_schedule = "It is time for class " + classes[randclass]

    # e "You chose classroom from MY EXAMPLE."
    # $ num_of_people = num_of_people_at(0)
    # e "In the classroom, there are currently [num_of_people] here."

    # if randclass > 3:
    #    $ class_schedule += " . You'd better work hard on this one."
    #else:
    #    $ class_schedule += " . Take it easy."
    #e "[class_schedule]"

    $ initializeDialogue()
    #while True:
    #    call screen test_dialogue_screen()
    #    $ sentence = getDialogue()
    #    e "[sentence]"
    call test_dialogue_tracery_screen1()

    #scene black
    #call start()


label test_dialogue_tracery_screen1:
    call screen test_dialogue_tracery_screen()

label test_dialogue_tracery_screen2:
    #$ sentence = getDialogue()
    $ sentence = getTraceryDialogue()
    e "[sentence]"
    call test_dialogue_tracery_screen1()

label exit_dialogue_tracery_screen:
    scene black
    call start()

#default statType = 0
#default statValue = 0

label update_test_tracery_stat():
    if (statType == 1):
        $ temp_player_study = temp_player_study + statValue;
    elif (statType == 2):
        $ temp_player_social = temp_player_social + statValue;
    elif (statType == 3):
        $ temp_player_health = temp_player_health + statValue;
    elif (statType == 4):
        $ temp_this_study = temp_this_study + statValue;
    elif (statType == 5):
        $ temp_this_social = temp_this_social + statValue;
    elif (statType == 6):
        $ temp_this_health = temp_this_health + statValue;
    elif (statType == 7):
        if (temp_current_location == "Library"):
            $ temp_current_location = "Classroom";
        else:
            $ temp_current_location = "Library";
    call test_dialogue_tracery_screen1()

label reset_test_tracery_dialogue():
    $ initializeDialogue()
    call test_dialogue_tracery_screen1()

screen test_dialogue_tracery_screen():
    $ statType = 0
    $ statValue = 0
    textbutton "{size=28}{color=#FFF}Player Study +{/color}{/size}":
        background "#000"
        xpos 1000
        ypos 200
        action [SetVariable("statType",1),SetVariable("statValue",5), Jump("update_test_tracery_stat")]
    textbutton "{size=28}{color=#FFF}Player Study -{/color}{/size}":
        background "#000"
        xpos 1300
        ypos 200
        action [SetVariable("statType",1),SetVariable("statValue",-5), Jump("update_test_tracery_stat")]
    textbutton "{size=28}{color=#FFF}Player Social +{/color}{/size}":
        background "#000"
        xpos 1000
        ypos 250
        action [SetVariable("statType",2),SetVariable("statValue",5), Jump("update_test_tracery_stat")]
    textbutton "{size=28}{color=#FFF}Player Social -{/color}{/size}":
        background "#000"
        xpos 1300
        ypos 250
        action [SetVariable("statType",2),SetVariable("statValue",-5), Jump("update_test_tracery_stat")]
    textbutton "{size=28}{color=#FFF}Player Health +{/color}{/size}":
        background "#000"
        xpos 1000
        ypos 300
        action [SetVariable("statType",3),SetVariable("statValue",5), Jump("update_test_tracery_stat")]
    textbutton "{size=28}{color=#FFF}Player Health -{/color}{/size}":
        background "#000"
        xpos 1300
        ypos 300
        action [SetVariable("statType",3),SetVariable("statValue",-5), Jump("update_test_tracery_stat")]

    textbutton "{size=28}{color=#FFF}NPC Study +{/color}{/size}":
        background "#000"
        xpos 1000
        ypos 350
        action [SetVariable("statType",4),SetVariable("statValue",5), Jump("update_test_tracery_stat")]
    textbutton "{size=28}{color=#FFF}NPC Study -{/color}{/size}":
        background "#000"
        xpos 1300
        ypos 350
        action [SetVariable("statType",4),SetVariable("statValue",-5), Jump("update_test_tracery_stat")]
    textbutton "{size=28}{color=#FFF}NPC Social +{/color}{/size}":
        background "#000"
        xpos 1000
        ypos 400
        action [SetVariable("statType",5),SetVariable("statValue",5), Jump("update_test_tracery_stat")]
    textbutton "{size=28}{color=#FFF}NPC Social -{/color}{/size}":
        background "#000"
        xpos 1300
        ypos 400
        action [SetVariable("statType",5),SetVariable("statValue",-5), Jump("update_test_tracery_stat")]
    textbutton "{size=28}{color=#FFF}NPC Health +{/color}{/size}":
        background "#000"
        xpos 1000
        ypos 450
        action [SetVariable("statType",6),SetVariable("statValue",5), Jump("update_test_tracery_stat")]
    textbutton "{size=28}{color=#FFF}NPC Health -{/color}{/size}":
        background "#000"
        xpos 1300
        ypos 450
        action [SetVariable("statType",6),SetVariable("statValue",-5), Jump("update_test_tracery_stat")]
    textbutton "{size=28}{color=#FFF}Change Location{/color}{/size}":
        background "#000"
        xpos 1300
        ypos 500
        action [SetVariable("statType",7),SetVariable("statValue",1), Jump("update_test_tracery_stat")]


    textbutton "{size=28}{color=#FFF}TRACERY Dialogue{/color}{/size}":
        background "#000"
        xpos 1000
        ypos 600
        action Jump("test_dialogue_tracery_screen2")
    textbutton "{size=28}{color=#FFF}Reset Dialogue{/color}{/size}":
        background "#000"
        xpos 1300
        ypos 600
        action Jump("reset_test_tracery_dialogue")
    textbutton "{size=28}{color=#FFF}Exit Test{/color}{/size}":
        background "#000"
        xpos 1600
        ypos 600
        action Jump("exit_dialogue_tracery_screen")


    $ this_temp_player_study = temp_player_study
    $ this_temp_player_social = temp_player_social
    $ this_temp_player_health = temp_player_health
    $ this_temp_this_study = temp_this_study
    $ this_temp_this_social = temp_this_social
    $ this_temp_this_health = temp_this_health
    $ this_temp_current_location = temp_current_location
    textbutton "{size=28}{color=#F00}Player Study = [this_temp_player_study]{/color}{/size}":
        background "#000"
        xpos 1600
        ypos 200
    textbutton "{size=28}{color=#F00}Player Social = [this_temp_player_social]{/color}{/size}":
        background "#000"
        xpos 1600
        ypos 250
    textbutton "{size=28}{color=#F00}Player Health = [this_temp_player_health]{/color}{/size}":
        background "#000"
        xpos 1600
        ypos 300
    textbutton "{size=28}{color=#F00}NPC Study = [this_temp_this_study]{/color}{/size}":
        background "#000"
        xpos 1600
        ypos 350
    textbutton "{size=28}{color=#F00}NPC Social = [this_temp_this_social]{/color}{/size}":
        background "#000"
        xpos 1600
        ypos 400
    textbutton "{size=28}{color=#F00}NPC Health = [this_temp_this_health]{/color}{/size}":
        background "#000"
        xpos 1600
        ypos 450
    textbutton "{size=28}{color=#F00}Location = [this_temp_current_location]{/color}{/size}":
        background "#000"
        xpos 1600
        ypos 500
