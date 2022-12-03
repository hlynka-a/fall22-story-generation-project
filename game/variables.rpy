
# Welcome
define e = Character("Eileen")

image bg_Uni = im.Scale("bg CarletonU.jpg", 1920, 1080)
image bg_lib = im.Scale("bg Library.jpg", 1920, 1080)
image bg_class = im.Scale("bg Classroom.jpg", 1920, 1080)
image bg_residence = im.Scale("bg Residence.jpg", 1920, 1080)
image bg_park = im.Scale("bg Park.jpg",1920,1080)
image bg_cafeteria = im.Scale("bg lounge.jpg",1920,1080)
image bg_gym = im.Scale("bg Gym.jpg",1920,1080)

# Player
default player_flag = False
default player_name = "Anonymous"
default player_priorities = ["Study","Health","Social"]

default player_study_local = 10
default player_social_local = 10
default player_health_local = 100

#default LocationList = ["Classroom","Library","Park","Coffee Shop","Cafeteria","Shop","Lounge","Residence"]
default player_location = "Residence"
default player_focus = "Study"


# Timer
default Minutes = 0
default Hours = 8
default Parts = 0
default Days = 0
default Chunks = ["Morning","Afternoon","Evening","Night"]
default WeekDays = ["Mon","Tue","Wed","Thu","Fri"]
default Calender = 0

default time_to_exit = False
default no_event = True
default real_time = True

default current_screen_name = "background_screen"

# Uni_map
image cr_idle = im.Scale("classroom idle.jpg", 100, 100)
image cr_hover = im.Scale("classroom hovered.jpg", 100, 100)
image lb_idle = im.Scale("library idle.jpg", 100, 100)
image lb_hover = im.Scale("library hovered.jpg", 100, 100)
image pk_idle = im.Scale("park idle.jpg", 100, 100)
image pk_hover = im.Scale("park hovered.jpg", 100, 100)
image cf_idle = im.Scale("cafeteria idle.jpg", 100, 100)
image cf_hover = im.Scale("cafeteria hovered.jpg", 100, 100)
image gy_idle = im.Scale("gym idle.jpg", 100, 100)
image gy_hover = im.Scale("gym hovered.jpg", 100, 100)
image re_idle = im.Scale("residence idle.jpg", 100, 100)
image re_hover = im.Scale("residence hovered.jpg", 100, 100)
image ex_idle = im.Scale("exit idle.jpg", 100, 100)
image ex_hover = im.Scale("exit hovered.jpg", 100, 100)

# EventsGenerator 
default event_notify = False
default event_recommand = False
default event_randomize = False
default Events_today = ["","","","",""]

