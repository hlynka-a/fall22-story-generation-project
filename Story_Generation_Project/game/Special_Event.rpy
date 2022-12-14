label test_spec_evt :
    e "Special Event Time"

    call screen test_special_event_screen


    jump Old_Debug_features_menu

label update_test_sp_evt_stat():
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
    elif (statType == 8):
        $ Days = Days + statValue;
    call screen test_special_event_screen()


screen test_special_event_screen():
    $ statType = 0
    $ statValue = 0

    textbutton "{size=28}{color=#FFF}Day +{/color}{/size}":
        background "#000"
        xpos 1000
        ypos 150
        action [SetVariable("statType",8),SetVariable("statValue",1), Jump("update_test_sp_evt_stat")]
    textbutton "{size=28}{color=#FFF}Day -{/color}{/size}":
        background "#000"
        xpos 1300
        ypos 150
        action [SetVariable("statType",8),SetVariable("statValue",-1), Jump("update_test_sp_evt_stat")]

    textbutton "{size=28}{color=#FFF}Player Study +{/color}{/size}":
        background "#000"
        xpos 1000
        ypos 200
        action [SetVariable("statType",1),SetVariable("statValue",5), Jump("update_test_sp_evt_stat")]
    textbutton "{size=28}{color=#FFF}Player Study -{/color}{/size}":
        background "#000"
        xpos 1300
        ypos 200
        action [SetVariable("statType",1),SetVariable("statValue",-5), Jump("update_test_sp_evt_stat")]
    textbutton "{size=28}{color=#FFF}Player Social +{/color}{/size}":
        background "#000"
        xpos 1000
        ypos 250
        action [SetVariable("statType",2),SetVariable("statValue",5), Jump("update_test_sp_evt_stat")]
    textbutton "{size=28}{color=#FFF}Player Social -{/color}{/size}":
        background "#000"
        xpos 1300
        ypos 250
        action [SetVariable("statType",2),SetVariable("statValue",-5), Jump("update_test_sp_evt_stat")]
    textbutton "{size=28}{color=#FFF}Player Health +{/color}{/size}":
        background "#000"
        xpos 1000
        ypos 300
        action [SetVariable("statType",3),SetVariable("statValue",5), Jump("update_test_sp_evt_stat")]
    textbutton "{size=28}{color=#FFF}Player Health -{/color}{/size}":
        background "#000"
        xpos 1300
        ypos 300
        action [SetVariable("statType",3),SetVariable("statValue",-5), Jump("update_test_sp_evt_stat")]

    textbutton "{size=28}{color=#FFF}NPC Study +{/color}{/size}":
        background "#000"
        xpos 1000
        ypos 350
        action [SetVariable("statType",4),SetVariable("statValue",5), Jump("update_test_sp_evt_stat")]
    textbutton "{size=28}{color=#FFF}NPC Study -{/color}{/size}":
        background "#000"
        xpos 1300
        ypos 350
        action [SetVariable("statType",4),SetVariable("statValue",-5), Jump("update_test_sp_evt_stat")]
    textbutton "{size=28}{color=#FFF}NPC Social +{/color}{/size}":
        background "#000"
        xpos 1000
        ypos 400
        action [SetVariable("statType",5),SetVariable("statValue",5), Jump("update_test_sp_evt_stat")]
    textbutton "{size=28}{color=#FFF}NPC Social -{/color}{/size}":
        background "#000"
        xpos 1300
        ypos 400
        action [SetVariable("statType",5),SetVariable("statValue",-5), Jump("update_test_sp_evt_stat")]
    textbutton "{size=28}{color=#FFF}NPC Health +{/color}{/size}":
        background "#000"
        xpos 1000
        ypos 450
        action [SetVariable("statType",6),SetVariable("statValue",5), Jump("update_test_sp_evt_stat")]
    textbutton "{size=28}{color=#FFF}NPC Health -{/color}{/size}":
        background "#000"
        xpos 1300
        ypos 450
        action [SetVariable("statType",6),SetVariable("statValue",-5), Jump("update_test_sp_evt_stat")]
    textbutton "{size=28}{color=#FFF}Change Location{/color}{/size}":
        background "#000"
        xpos 1300
        ypos 500
        action [SetVariable("statType",7),SetVariable("statValue",1), Jump("update_test_sp_evt_stat")]


    textbutton "{size=28}{color=#FFF}TRACERY Dialogue{/color}{/size}":
        background "#000"
        xpos 1000
        ypos 600
        action Jump("evt_gens")
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

    $ this_temp_day = Days
    $ this_temp_dayname = WeekDays[Days % 5]
    $ this_temp_player_study = temp_player_study
    $ this_temp_player_social = temp_player_social
    $ this_temp_player_health = temp_player_health
    $ this_temp_this_study = temp_this_study
    $ this_temp_this_social = temp_this_social
    $ this_temp_this_health = temp_this_health
    $ this_temp_current_location = temp_current_location
    textbutton "{size=28}{color=#F00}Day = [this_temp_day]{/color}{/size}":
        background "#000"
        xpos 1600
        ypos 150
    textbutton "{size=28}{color=#F00}[this_temp_dayname]{/color}{/size}":
        background "#000"
        xpos 1750
        ypos 150
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





label evt_gens:
    if (this_temp_day == 30):
        jump final_evalutatiom
    else:
        call screen test_special_event_screen

    if (temp_player_study > temp_this_study):
        jump study_buddy
    else:
        call screen test_special_event_screen



init python:

    special_event_label = ""

    def special_event_can_occur():
        global special_event_label
        if (listOfNPCsAtLocation[NPCsAtLocationIndex].special_event_dictionary["study_buddy"] == False):
            if (listOfNPCsAtLocation[NPCsAtLocationIndex].npc_study < 50 ):
                special_event_label = "study_buddy"
                return True
        # elif : more events can be added here

        return False

    def special_event_possible(tempNPCList, tempIndex):
        if (tempNPCList[tempIndex].special_event_dictionary["study_buddy"] == False):
            if (tempNPCList[tempIndex].npc_study < 50 ):
                return True
        # elif : more events can be added here

        return False




label study_buddy:
    e "I heard you are a studious person"
    e "Are you free right now"
    menu:
        "Yes":
            e "I need help with studies"
           # if (player_location == "Library"):
         #       e "Thank goodness we are in the library"
         #   else:
        #        e "Let's go to the library, I need help"
        ##        call screen background_screen_library()
            $ player_study_local = player_study_local + 10
            e "Thanks for studying"
            $ listOfNPCsAtLocation[NPCsAtLocationIndex].special_event_dictionary["study_buddy"] = True

        "No":
            e "Oh, I hope to meet you on Friday then"
            $ listOfNPCsAtLocation[NPCsAtLocationIndex].special_event_dictionary["study_buddy"] = False

    #call display_timer
    return


label final_evalutatiom:
    if (temp_player_study >= 100 and temp_player_social >= 100 ):
        e "Wow, you're a total ACE"


    call screen test_special_event_screen
