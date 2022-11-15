# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Eileen")
define e = Character('Eileen', color="#c8ffc8")

image bg_Uni = im.Scale("bg CarletonU.jpg", 1920, 1080)
image bg_lib = im.Scale("bg Library.jpg", 1920, 1080)
image bg_clock = im.Scale("bg Clock.jpg", 1920, 1080)
image bg_class = im.Scale("bg Classroom.jpg", 1920, 1080)
image bg_residence = im.Scale("bg Residence.jpg", 1920, 1080)
image cr_idle = im.Scale("classroom idle.jpg", 100, 100)
image cr_hover = im.Scale("classroom hovered.jpg", 100, 100)
image lb_idle = im.Scale("library idle.jpg", 100, 100)
image lb_hover = im.Scale("library hovered.jpg", 100, 100)
image pk_idle = im.Scale("park idle.jpg", 100, 100)
image pk_hover = im.Scale("park hovered.jpg", 100, 100)
image at_idle = im.Scale("advance time idle.jpg", 300, 100)
image at_hover = im.Scale("advance time hovered.jpg", 300, 100)

default player_flag = False
default study_local = 10
default social_local = 10
default health_local = 100


label start:

    # REMOVE this line after debugging is finished
    # jump imagemap_uni
    $ my_scheduler_v01()

    menu:
        "Start with Intro":
            call start_intro()
        "Skip Intro":
            $ player = "Anonymous"
            $ priorities = ["Health","Study","Social"]
            show screen statement_bars
            call imagemap_uni()
        "Andrew's Tests":
            call andrews_tests_menu()


    return

label andrews_tests_menu:
    menu:
        "Dialogue Test":
            call test_dialogue_screen()
        "Back":
            call start()
    return

label start_intro:
    scene bg_clock
    e "Let us do something special here. Count the timechunks."
    call time_flie
    call time_pass

    #e "Again, let us do something special."
    #call button_menu

    scene bg_Uni
    show eileen happy at right
    e "The first day of the semester. Would you like to begin a new way of life in order to gain new experiences?"

    menu:
        "Yes":
            call Settings
        "No":
            jump No_Settings

    #e "Here would be better to add image map. But for verify the project, just move to library."

    call imagemap_uni()
    return

######################################################    Time chunks
label time_flie:
    $ WeekDays = ["Mon","Tue","Wed","Thu","Fri"]
    $ Chunks = ["Morning","Afternoon","Evening","Night"]
    $ Minutes = 0
    $ Hours = 12
    $ Days = 0
    $ Parts = 0
    return
label time_pass:
    $ Gamerunning = True
    $ randint = renpy.random.randint(1,5)
    while Gamerunning and randint !=3:
        $ output = "The time is " + Chunks[Parts] + " of the " + WeekDays[Days] + " " + str(Hours).zfill(2) + " : " + str(Minutes).zfill(2)
        "[output]"
        $ Minutes += 20
        if Minutes > 59:
            $ Minutes = 0
            $ Hours += 1
        if Hours > 23:
            $ Hours = 0
            $ Days += 1
        if Days > 6:
            $ Days = 0
        if Hours >= 5 and Hours < 12:
            $ Parts = 0
        if Hours >= 12 and Hours < 17:
            $ Parts = 1
        if Hours >= 17 and Hours < 21:
            $ Parts = 2
        if Hours < 4 or Hours > 21:
            $ Parts = 3
        $ randint = renpy.random.randint(1,5)

        call SpecialEvents

label SpecialEvents:
    if Days == 0 and Hours == 13:
        "The special Event just happend."
    return

###################################################### Menu Settings

label No_Settings:
    e "If this is what you want, then, bye."
    $ renpy.quit();
    return

label Settings:
    call Set_name
    call Set_priority
    return

label Set_name:
    $ player = renpy.input("Your name would be..", default = "Anonymous" )
    e "Good to know you, [player]."
    #$ player = renpy.input("Your name would be..", allows = "abcdefg", exclude = "!@#$123456", length = 8)
    return

label Set_priority:
    if player_flag == False:
        e "Would you like to set the priorities of your school life?"
    else:
        e "Would you like to reset the priorities of your school life?"
    menu:
        "Yes":
            jump Yes_Priority
        "No":
            jump No_Settings
    return

label Yes_Priority:
    $ priorities = ["","",""]
    $ rank = ["highest","second","lowest"]
    $ i = 0


    while i < len(rank):
        $ Q = "which one is your " + rank[i] + " priorities? "
        e "[Q]"
        menu:
            "Health":
                $ priorities[i] = "Health"
            "Study":
                $ priorities[i] = "Study"
            "Social":
                $ priorities[i] = "Social"
        $ i += 1

    e "You just set the rank, [player]"
    $ A = "Here is your list " + priorities[0] + " > " + priorities[1]  + " > " + priorities[2] + " right?"
    e "[A]"
    call statement_display

    $ player_flag == True
    return

label statement_display:
    show eileen happy at left
    e "We would like to output a statement bars for you to check your initial performence."

    show screen statement_bars
    e "No worries. It is just a beginning.\n Just try not to stay the same."
    return

screen statement_bars:

    $ study = study_local
    $ social = social_local
    $ health = health_local

    frame:
        xalign 0.9 ypos 20
        xsize 500
        vbox:
            spacing 5

            bar value ScreenVariableValue("study", 100) style "bar"
            text 'Study: [study]' align(0,50)
            bar value ScreenVariableValue("social", 100) style "bar"
            text 'Social: [social]' align(0,80)
            bar value ScreenVariableValue("health", 100) style "bar"
            text 'Health: [health]' align(0,80)
return

###################################################### Image maps
label imagemap_uni:
    #call screen imagebuttonoverimagemap_example2
    call screen imagemap_example
    #call screen imagebuttonoverimagemap_example

screen imagemap_example():
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

        #$ num_of_people = num_of_people_at(0)
        #$ notify_message = "In the classroom, there are currently " + str(num_of_people).zfill(2)+" here."

        hotspot (100, 200, 100, 100) action Jump("classroom") alt "Classroom"
        hotspot (300, 200, 100, 100) action Jump("library") alt "Library"
        hotspot (100, 600, 300, 100) action Jump("advancetime") alt "Advance Time"

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

screen imagebuttonoverimagemap_example2():
    zorder 1
    imagebutton:
        xpos 50
        ypos 150
        #idle "cr_idle"
        #hover "cr_hover"

#        with/ [], the message cannot work
        #hovered Notify("notify_message")
        #hovered Notify("[notify_message]")
        #action Jump("classroom")

screen imagebuttonoverimagemap_example():
    zorder 10
    imagebutton:
        xpos 150
        ypos 250
        #idle "cr_idle"
        #hover "cr_hover"

#        with/ [], the message cannot work
        #hovered Notify("notify_message")
        #hovered Notify("[notify_message]")
        #action Jump("classroom")

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
    $ study_local += 3
    $ health_local -= 30
    jump imagemap_done

label library:
    scene bg_lib
    show eileen happy
    e "You chose library from MY EXAMPLE."
    $ num_of_people = num_of_people_at(1)
    e "In the library, there are currently [num_of_people] here."


    e "We are at the Library. What is your plan for today?"
    #jump button_menu
    show eileen happy at right
    menu:
        "Study by myself.":
            call self_study
        "Study with my peers.":
            call study_group
        "Attend the workshop.":
            call workshop
    e "What a wonderful experience today. What would you like to do next?"
    jump imagemap_done

label self_study:
    $ randStudy = renpy.random.randint(1,3)
    "Good choice, [player]. You just add [randStudy] percent on your study. "
    $ study_local += randStudy
    $ health_local -= 20
    return
label study_group:
    $ randStudy = renpy.random.randint(1,2)
    $ randSocial = renpy.random.randint(1,2)
    "Not bad, [player]. You just add [randStudy] percent on you study and [randSocial] percent on social."
    $ social_local += randSocial
    $ study_local += randStudy
    $ health_local -= 25
    return
label workshop:
    "The workshop is really helping with the concerns. 5 percent on your study, [player]."
    $ health_local -= 30
    $ study_local += 5
    return

label advancetime:
    $ update_time()
    e "The time and day are now [currentDay] and [currentTime]."
    $ health_local = 100
    jump imagemap_done

label art:
    e "You chose art from MY EXAMPLE."
    e "Really good background art is hard to make, which is why so many games use filtered photographs. Maybe you can change that."
    jump imagemap_done

label home:
    e "You chose to go home from MY EXAMPLE."
    jump imagemap_done

label imagemap_done:
    jump continue

label continue:
    scene bg_Uni
    show eileen happy
    e "Let's go back to the map."

    jump imagemap_uni
    return

###############################################  Practice of Buttons and Bars
style custom_button:
    idle_background Frame("button glossy idle", 12, 12)
    hover_background Frame("button glossy hover", 12, 12)
    xpadding 20
    ypadding 10
    xmargin 5
    ymargin 5
    size_group "custom_button"

style custom_button_text:
    idle_color "#c0c0c0"
    hover_color "#ffffff"

style custom_bar_style:
    left_bar '#3298cf'
    right_bar '#32cfc7'
    xsize 500
    ysize 30


label button_menu:
    call screen buttons()
    call screen bars()
    hide screen bars
    call screen dif_bars()

    "Time to move to the next one"
    return


screen buttons():
    frame:
        xalign 0.5 ypos 0.5
        has vbox

        textbutton _("Nothing really"):
            style "custom_button"
            hovered Notify("I see you come and check this button")
            action Notify(_("You click the button."))


        textbutton _("Share the concern"):
            style "custom_button"
            action [Notify(_("You clicked the other one.")), Return()]

return

screen bars():
    default n = 66

    frame:
        xalign 0.5 ypos 50
        xsize 500

        vbox:
            spacing 10
            bar value AnimatedValue(n, 100, 0.5) style "bar"
            bar value ScreenVariableValue("n", 100) style "slider"

            button:
                bar value ScreenVariableValue('n', range = 100, style = 'custom_bar_style')
                text '[n]' align(0,80)

return
