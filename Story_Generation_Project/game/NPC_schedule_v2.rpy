label NPC_schedule_v2:
    #scene bg_lib

    #menu:
    #    "Create_NPC":
    #        call create_NPC_v2
    #    "Quit":
    #        jump start

    call initialize_NPC_schedule_v2
    call loop_NPC_schedule_v2

    return

label initialize_NPC_schedule_v2:
    $ bg_current = "Library"
    call Refresh_current_background()
    $ defineRandomNPCs(10)
    $ Location = "Library"
    $ timer_update_function_name = "NPC_schedule_v2_event_update"
    $ time_to_exit = False
    e "(Debug Screen) We're in the Library now. Let's see who appears in this location."

label loop_NPC_schedule_v2:
    # COMMENT: code for 'show' and 'call' screen MUST be in the same function, otherwise the timer loop cycle will escape it (end the first screen before the 2nd screen is called)
    #       Therefore, do not try to organize these calls into their own separate functions.
    call Refresh_current_background()
    show screen timer_logic()
    show screen timer_screen()
    # $ time_to_exit = False
    show screen debug_time_menu_screen()
    $ listOfNPCsAtLocation = []
    show screen NPC_image_v2()
    call screen NPC_background_screen()


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

label create_NPC_image_v2():
    call screen NPC_image_v2()
    return

screen NPC_background_screen:
    #$ renpy.notify("NPC_background_screen screen was called.");
    textbutton "{size=28}{color=#FFF}Exit Test{/color}{/size}":
        background "#000"
        xpos 1000
        ypos 200
        action [Jump("exit_timer_screen")]

screen NPC_image_v2():
    zorder 101
    #textbutton "{size=28}{color=#FFF}Exit Test{/color}{/size}":
    #    background "#000"
    #    xpos 1000
    #    ypos 200
    #    action [Jump("exit_timer_screen")]
    #$ renpy.notify("NPC_image_v2 called");

    if (npcTalkingNow == False):
        $ numOfNPCsAtLocation = len(listOfNPCsAtLocation)

        for i in range(0,numOfNPCsAtLocation):
            imagebutton:
                xpos 0.8 + (0.1*(int(i/4)))
                ypos 0.1 + (0.2*(i%4))
                idle "logo base"
                hover "logo bw"
                hovered [SetVariable("NPCsAtLocationIndex",i),Show("NPC_statements_bars_v2")]
                unhovered Hide("NPC_statements_bars_v2")

                action [Hide("NPC_statements_bars_v2"),Jump("talk_to_NPC_v2")]

screen NPC_statements_bars_v2():

    #$ NPC_study = NPC_study_local
    #$ NPC_social = NPC_social_local
    #$ NPC_health = NPC_health_local
    $ numOfNPCsAtLocation = len(listOfNPCsAtLocation)
    if (numOfNPCsAtLocation <= NPCsAtLocationIndex):
        $ NPCsAtLocationIndex = 0
        $ NPC_study = 0
        $ NPC_social = 0
        $ NPC_health = 0
        $ NPC_name = "null"
    else:
        $ NPC_study = listOfNPCsAtLocation[NPCsAtLocationIndex].npc_study
        $ NPC_social = listOfNPCsAtLocation[NPCsAtLocationIndex].npc_social
        $ NPC_health = listOfNPCsAtLocation[NPCsAtLocationIndex].npc_health
        $ NPC_name = listOfNPCsAtLocation[NPCsAtLocationIndex].npc_firstname + " " + listOfNPCsAtLocation[NPCsAtLocationIndex].npc_lastname

    frame:
        xalign 0.1 ypos 20
        xsize 500
        vbox:
            spacing 5

            text 'Student Name: [NPC_name]'
            bar value ScreenVariableValue("NPC_study", 100) style "bar"
            text 'Study: [NPC_study]' align(0,50)
            bar value ScreenVariableValue("NPC_social", 100) style "bar"
            text 'Social: [NPC_social]' align(0,80)
            bar value ScreenVariableValue("NPC_health", 100) style "bar"
            text 'Health: [NPC_health]' align(0,80)
    #return

label talk_to_NPC_v2:
    # $ renpy.notify("talk to NPC now!")
    # (This was complicated because Timer is constantly refreshing screen, even if dialogue prompt is active.)
    # Timer is still refreshing screen every 0.5 seconds.
    # Actions to pause that refresh and allow speaking MUST be done immediately - DO NOT WAIT for dissolve to occur.
    $ real_time_temp = real_time
    $ real_time = False
    $ time_to_exit = True
    $ npcTalkingNow = True
    hide screen timer_logic
    hide screen timer_screen
    hide screen debug_time_menu_screen

    show logo base with dissolve
    #e "Conversation happens here."
    $ NPC_name = listOfNPCsAtLocation[NPCsAtLocationIndex].npc_firstname + " " + listOfNPCsAtLocation[NPCsAtLocationIndex].npc_lastname
    $ updateDialogueVariables()
    $ temp_this_study = listOfNPCsAtLocation[NPCsAtLocationIndex].npc_study
    $ temp_this_social = listOfNPCsAtLocation[NPCsAtLocationIndex].npc_social
    $ temp_this_health = listOfNPCsAtLocation[NPCsAtLocationIndex].npc_health
    $ sentence = getTraceryDialogue()
    "[NPC_name]: [sentence]"

    $ real_time = real_time_temp
    $ time_to_exit = False
    $ npcTalkingNow = False
    #show screen timer_logic
    #show screen timer_screen
    #show screen debug_time_menu_screen
    #jump loop_NPC_schedule_v2
    hide logo base with dissolve
    jump display_timer

    return

label NPC_schedule_v2_event_update:
    call check_NPC_events()
    #$ listOfNPCsAtLocation = get_NPCs_at_location(Location)
    $ listOfNPCsAtLocation = get_NPCs_at_location(player_location)
    #call create_NPC_image_v2(len(listOfNPCs))
    #call create_NPC_image_v2()
    show screen NPC_image_v2()
    if (listOfNPCsAtLocation != temp_NPCs_at_location):
        hide screen NPC_statements_bars_v2
    $ temp_NPCs_at_location = listOfNPCsAtLocation
    call display_timer
