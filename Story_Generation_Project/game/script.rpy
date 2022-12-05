# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

image bg_Uni = im.Scale("bg CarletonU.jpg", 1920, 1080)
image bg_lib = im.Scale("bg Library.jpg", 1920, 1080)
image bg_clock = im.Scale("bg Clock.jpg", 1920, 1080)
image bg_class = im.Scale("bg Classroom.jpg", 1920, 1080)
image bg_residence = im.Scale("bg Residence.jpg", 1920, 1080)
default bg_current = "Classroom"
image cr_idle = im.Scale("classroom idle.jpg", 100, 100)
image cr_hover = im.Scale("classroom hovered.jpg", 100, 100)
image lb_idle = im.Scale("library idle.jpg", 100, 100)
image lb_hover = im.Scale("library hovered.jpg", 100, 100)
image pk_idle = im.Scale("park idle.jpg", 100, 100)
image pk_hover = im.Scale("park hovered.jpg", 100, 100)
image at_idle = im.Scale("advance time idle.jpg", 300, 100)
image at_hover = im.Scale("advance time hovered.jpg", 300, 100)

#default player_study_local = 10
#default player_social_local = 10
#default player_health_local = 100
#default player_name = "Anonymous"
#default player_priorities = ["Study","Health","Social"]
#default player_flag = False

default NPC_study_local = 10
default NPC_social_local = 10
default NPC_health_local = 100

#default Minutes = 0
#default Hours = 8
#default Parts = 0
#default Days = 0
#default WeekDays = ["Mon","Tue","Wed","Thu","Fri"]
#default Chunks = ["Morning","Afternoon","Evening","Night"]


#default no_event = True
#default real_time = True
#default time_to_exit = False
#default current_screen_name = "background_screen"

label start:
    scene bg_Uni
    menu:
        "Start Game":
            #$ renpy.notify("(Start Game not complete yet, just go to 'Player_settings')")
            jump Player_settings
        # add option here to "Start Game" in middle of the story, to be able to skip intro and early parts of the game
        "Debug Features Menu":
            jump Debug_features_menu
        "Quit":
            #$ renpy.quit();
            $ MainMenu(confirm=False)()


    return

label Debug_features_menu:
    scene bg_Uni
    menu:
        "(Legacy debug features)":
            jump Old_Debug_features_menu
        "Back":
            jump start
    return

label Old_Debug_features_menu:
    scene bg_Uni
    menu:
        "Player Setting":
            jump Player_settings
        "School Life":
            e "Hope you are ready for a new beginning."
            jump imagemap_uni
        "Generate NPC":
            jump NPC_schedule
        "Generate NPC v2 (schedule)":
            jump NPC_schedule_v2
        "Timer Test":
            jump display_timer
        "Generate Schedule":
            jump schedule_generator
        "Dialogue Test":
            jump test_dialogue_screen
        "TRACERY Dialogue Test":
            jump test_dialogue_tracery_screen
        "Back":
            jump Debug_features_menu
    return

label Player_settings:
    menu:
        "With Player Introduction":
            jump start_setting
        "Skip Player Introduction":
            jump statement_display
        "Back":
            jump start
    return

label Refresh_current_background():
    if (bg_current == "Classroom"):
        scene bg_class
    elif (bg_current == "Library"):
        scene bg_lib
    elif (bg_current == "Uni"):
        scene bg_Uni
    elif (bg_current == "Residence"):
        scene bg_residence
