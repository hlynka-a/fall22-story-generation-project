label NPC_schedule_v2:
    scene bg_lib
    e "(Debug Screen) We're in the Library now. Let's see who appears in this location."
    #menu:
    #    "Create_NPC":
    #        call create_NPC_v2
    #    "Quit":
    #        jump start
    return

label create_NPC_v2:
    scene bg_lib
    call init_NPC_statements_v2

    # Check if the NPC will be in the library.
    #if(daily_locations[0] == 1):
    #    e "The NPC will show up here. Create NPC image button. The image button will represents the NPC. By click the image button, a conversation will happened."
    #       call create_NPC_image
    #else:
    #    e "It seems like the NPC will not be here. Try another time to meet him/her."
    return

label create_NPC_image_v2:
    call screen NPC_image_v2
    return

screen NPC_image_v2:
    imagebutton:
        xpos 0.8
        ypos 0.5
        idle "logo base"
        hover "logo bw"
        hovered Show("NPC_statements_bars_v2")
        unhovered Hide("NPC_statements_bars_v2")

        action [Hide("NPC_statements_bars_v2"),Jump("talk_to_NPC_v2")]
return

label init_NPC_statements_v2:

    #define NPC_study_local = renpy.random.randint(1,10)
    #define NPC_social_local = renpy.random.randint(1,10)
    #define NPC_health_local = 100

    #define loc_lib = renpy.random.randint(0,1)
    #define loc_classrm = renpy.random.randint(0,1)

    # The schedule here is still incomplete; I will create one based on the time chunks.
    #define daily_locations = [1,loc_classrm]
    return

screen NPC_statements_bars_v2():

    $ NPC_study = NPC_study_local
    $ NPC_social = NPC_social_local
    $ NPC_health = NPC_health_local

    frame:
        xalign 0.1 ypos 20
        xsize 500
        vbox:
            spacing 5

            bar value ScreenVariableValue("NPC_study", 100) style "bar"
            text 'Study: [NPC_study]' align(0,50)
            bar value ScreenVariableValue("NPC_social", 100) style "bar"
            text 'Social: [NPC_social]' align(0,80)
            bar value ScreenVariableValue("NPC_health", 100) style "bar"
            text 'Health: [NPC_health]' align(0,80)
return

label talk_to_NPC_v2:
    show logo base with dissolve
    e "Conversation happens here."
    jump NPC_schedule
    return
