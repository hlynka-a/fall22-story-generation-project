
# Resource :
#       https://www.renpy.org/wiki/renpy/doc/cookbook/Timed_menus
#       

define e = Character('Eileen', color="#c8ffc8")
define l = Character('Lucy', color = "#8528b4ee")
image bg_lib = im.Scale("bg Library.jpg", 1920, 1080)

default Minutes = 0
default Hours = 0
default Part = 0
default Days = 0
default WeekDays = ["Mon","Tue","Wed","Thu","Fri"]
default Chunks = ["Morning","Afternoon","Evening","Night"]
default dia = 'clock_dialogue'

default no_event = True


transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

init:
    $ timer_range = 0
    $ timer_jump = 0

# time = the time the timer takes to count down to 0.
# timer_range = a number matching time (bar only)
# timer_jump = the label to jump to when time runs out

label start:
    #scene bg_lib

    show screen dialogue_NPC

    call menu1
    call menu2
    return 

screen dialogue_NPC:
    imagebutton:
        xpos 100
        ypos 200
        idle "logo base"
        hover "logo bw"

        action Jump("dialogue_with_logo") 
return
label dialogue_with_logo:
    scene bg_lib
    e "This is where the conversation will take place."
return
label menu1:
    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'menu1_slow'
    show screen countdown
    show eileen happy at right
    menu:
        "The World":
            hide eileen happy
            # hide screen countdown'
            $ no_event = False
            show lucy happy at left
            e "ZA WARUDO"
            e "Time Has Stopped"
            hide screen countdown
            pause 7
            e "7 Seconds have Passed, time resumes"
            $ no_event = True
            show screen countdown
            
            # jump menu1_end
        "Your Future":
            hide screen countdown
            e "King Crimson"
            $ no_event = False
            $ Minutes = Minutes + 10
            e "I skkipped 10 seconds of the past, we are now in the future"
            $ no_event = True
            show screen countdown
            
            # jump menu1_end
    return
   
label menu1_slow:
    e "You didn't choose anything."
    return
    
label menu1_end:
    l "Anyway, let's do something else."
    return

screen countdown:
    #timer 1 repeat True action If(time > 0, true=SetVariable('time', time + 1), false=[Hide('countdown'), Jump(timer_jump)])

    timer 1 repeat no_event action If(Minutes < 59, true = SetVariable('Minutes', Minutes+1), false = SetVariable('Minutes', Minutes-59))
   # timer 1 repeat no_event action If(Minutes%10 == 0, true = Jump(dia))
   # timer 1 repeat no_event action If(WeekDays[Minutes%5] == 0, true = Jump(dia))
   # $ WeekDays
    #timer 1 repeat no_event action If(Minutes == 59 , true = SetVariable('Hours', Hours+1))
    #timer 1 repeat no_event action If(Hours == 23 , true = SetVariable('Hours', Hours - 23))
   # timer 1 repeat no_event action If(Hours == 23, true = SetVariable('Days', Days+1))
   # timer 1 repeat no_event action If(Days == 6 , true = SetVariable('Days', Days - 6))

    
   
    
    #####################################################################################################################
    #####################################################################################################################
    ######################                Less than 2, change the color
    
    #if time <= 2:
    #    text str(time) xpos .1 ypos .1 color "#FF0000" at alpha_dissolve
    #else:
    text str(Days) xpos .1 ypos .1 at alpha_dissolve
    text str(Hours) xpos .2 ypos .1 at alpha_dissolve
    text str(Minutes) xpos .3 ypos .1 at alpha_dissolve
return
##############################         bar statement, might use, unlikely to do so
#screen countdown:
#    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
#    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.
#return 

label time_clock:
    $ Minutes = Minutes + 1
    jump current_time
    pause 1
    jump time_clock
    return




label clock_dialogue:
    e "You just jump to the event that happened every 10 minutes."
    return

label current_time:
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
    return










label menu2:
    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'menu2_v2'
    show screen countdown
    menu:
        "Choice 1 fast":
            hide screen countdown
            e "You chose 'Choice 1' fast"
            jump menu2_end
        "Choice 2 fast":
            hide screen countdown
            e "You chose 'Choice 2' fast"
            jump menu2_end

label menu2_v2:
    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'menu2_slow'
    show screen countdown
    menu:
        "Choice 1 slow":
            hide screen countdown
            e "You chose 'Choice 1', but were slow"
            jump menu2_end
        "Choice 2":
            hide screen countdown
            e "You chose 'Choice 2', but were slow"
            jump menu2_end

label menu2_slow:
    e "You were really slow and didn't choose anything."
    return
    
label menu2_end:
    e "Anyway, let's do something else."
    return 

