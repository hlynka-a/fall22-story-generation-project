# Minutes = 0 Hours = 8 Parts = 0 Days = 0 WeekDays = ["Mon","Tue","Wed","Thu","Fri"] Chunks = ["Morning","Afternoon","Evening","Night"]
# $ WeekDays = ["Mon","Tue","Wed","Thu","Fri"]
init python:
    class Event(object):
        def __init__(self, event_name = "",event_day = 0,event_hstarts = 1,event_mstatrs = 0, event_hends = 1, event_mends = 0,event_active = False,event_focus = "Course", event_location = "Classroom", event_regular = True):
            self.event_name = event_name;
            self.event_day = event_day;
            self.event_hstarts = event_hstarts;
            self.event_mstatrs = event_mstatrs;
            self.event_hends = event_hends;
            self.event_mends = event_mends;
            self.event_active = event_active;
            self.event_location = event_location;
            self.event_focus = event_focus;
            self.event_regular = event_regular;

        def eventcheck(self, e_d, e_hs, e_ms, e_re):
            if self.event_day == e_d and self.event_hstarts == e_hs and self.event_mstatrs == e_ms and self.event_regular == e_re:
                self.event_active = True;
                return True
            else:
                return False

        def eventcheck2(self,e_d,e_hs,e_ms, e_re):
            temp_tstart = (self.event_hstarts * 100) + self.event_mstatrs;
            temp_tend = (self.event_hends * 100) + self.event_mends;
            temp_currenttime = (e_hs * 100) + e_ms;
            if self.event_day == e_d and temp_tstart <= temp_currenttime and temp_tend > temp_currenttime and self.event_active == False and self.event_regular == e_re:
                self.event_active = True;
                return True
            else:
                return False

        def eventinactive(self, e_d, e_he, e_me, e_re):
            if self.event_day == e_d and self.event_hends == e_he and self.event_mends == e_me and self.event_regular == e_re:
                self.event_active = False;
                return True
            else:
                return False

        def eventinactive2(self,e_d,e_hs,e_ms, e_re):
            temp_tstart = (self.event_hstarts * 100) + self.event_mstatrs;
            temp_tend = (self.event_hends * 100) + self.event_mends;
            temp_currenttime = (e_hs * 100) + e_ms;
            if self.event_day == e_d and temp_tend <= temp_currenttime and self.event_active == True and self.event_regular == e_re:
                self.event_active = False;
                return True
            else:
                return False

        def npceventcheck(self,e_d,e_hs,e_ms):
            temp_tstart = (self.event_hstarts * 100) + self.event_mstatrs;
            temp_tend = (self.event_hends * 100) + self.event_mends;
            temp_currenttime = (e_hs * 100) + e_ms;
            if self.event_day == e_d and temp_tstart <= temp_currenttime and temp_tend >= temp_currenttime and self.event_active == False:
                self.event_active = True;
                return True
            else:
                return False

        def npceventinactive(self, e_d, e_he, e_me):
            temp_tstart = (self.event_hstarts * 100) + self.event_mstatrs;
            temp_tend = (self.event_hends * 100) + self.event_mends;
            temp_currenttime = (e_he * 100) + e_me;

            if (self.event_day != e_d or (temp_tstart > temp_currenttime or temp_tend < temp_currenttime)) and self.event_active == True:
                self.event_active = False;
                return True
            else:
                return False

        #def eventhappennow(self, c_d, c_h, c_m, e_re):
        #    if self.event_day == c_d and (self.event_hstarts == c_h and self.event_mstatrs <= c_m ) or (self.event_hends == c_h and self.event_mends >= c_m )and self.event_regular == e_re:
        #        return True
        #    else:
        #        return False

        def eventhappenDay(self, e_d):
            if self.event_day == e_d:
                return True
            else:
                return False
        def eventrecommand(self, focus, e_d, e_re):
            if self.event_focus == focus and self.event_day == e_d and self.event_regular == e_re:
                return True
            else:
                return False

    Events_library = []

# Course 9:00 - 16:00
    Events_library.append(Event("COMP1805", "Mon", 9, 00, 10, 00, False));
    Events_library.append(Event("COMP3000", "Mon", 12, 0, 13, 0, False));
    Events_library.append(Event("COMP2401", "Tue", 10, 0, 11, 0, False));
    Events_library.append(Event("COMP1405", "Wed", 14, 0, 16, 0, False));
    Events_library.append(Event("COMP2401", "Thu", 10, 0, 11, 0, False));
    Events_library.append(Event("COMP1405", "Fri", 14, 0, 16, 0, False));

# Workshop 18:00 - 20:00

    Events_library.append(Event("Workshop", "Mon", 18, 0, 20, 0, False,"Study","Library", False));
    Events_library.append(Event("Workshop", "Tue", 18, 0, 20, 0, False,"Study","Library", False));
    Events_library.append(Event("Workshop", "Wed", 18, 0, 20, 0, False,"Study","Library", False));
    Events_library.append(Event("Workshop", "Thu", 18, 0, 20, 0, False,"Study","Library", False));

# Party 18:00 - 20: 00
    Events_library.append(Event("Party", "Mon", 18, 0, 20, 0, False,"Social","Cafeteria",False));
    Events_library.append(Event("Party", "Fri", 18, 0, 20, 0, False,"Social","Cafeteria", False));

# Run 18:00 - 20:00
    Events_library.append(Event("Corlor Run", "Tue", 18, 0, 20, 0, False,"Health","Park",False));
    Events_library.append(Event("Bubble Run", "Wed", 18, 0, 20, 0, False,"Health","Park",False));
    Events_library.append(Event("Cross Country Run", "Thu", 18, 0, 20, 0, False,"Health","Park",False));
    Events_library.append(Event("The Light Run", "Fri", 18, 0, 20, 0, False,"Health","Park",False));

# Exams
#    Events_library.append(Event("COMP2401 Exam", "Tue", 9, 0, 10, 0, False, "Exam",False));
#    Events_library.append(Event("COMP1405 Exam", "Wed", 13, 0, 15, 0, False, "Exam",False));

####
#### The end of the python code
####

# Create random events
label irregular_event:
    $ ee = 0
    while ee < len(Events_library):
        if WeekDays[Days] == Events_library[ee].event_day and Events_library[ee].event_regular == False:
            if renpy.random.randint(1,3) == 1:
                $ Events_library[ee].event_regular = True
        $ ee += 1
    return

label reset_irregular_event:
    $ ee = 0
    while ee < len(Events_library):
        if Events_library[ee].event_focus == "Course":
            $ Events_library[ee].event_regular = True
        else:
            if WeekDays[Days] == Events_library[ee].event_day and Events_library[ee].event_regular == True:
                $ Events_library[ee].event_regular = False
        $ ee +=1
    return


# Create a list of events that occurred on the current day.
label generate_event_notify:
    $ ee = 0
    $ Events_today = ""
    while ee < len(Events_library):
        if WeekDays[Days] == Events_library[ee].event_day and Events_library[ee].event_regular == True:
            $ Events_today += Events_library[ee].event_name
            $ Events_today += " "
            $ Events_today += "{:02d}".format(Events_library[ee].event_hstarts) #str(Events_library[ee].event_hstarts)
            $ Events_today += ":"
            $ Events_today += "{:02d}".format(Events_library[ee].event_mstatrs) #str(Events_library[ee].event_mstatrs)
            $ Events_today += " "
        $ ee += 1
    $ Events_today += " will happen today."
    return

# Call the events list and display the message
label event_notify_today:
    if event_randomize == True:
        call irregular_event
        $ event_randomize = False
    call generate_event_notify
    if event_notify == False:
            $ output_event_info = Events_today
            "[output_event_info]"
            $ event_notify = True
            $ defineNextNPCSchedule()
    return


# Check the events that related to player's focus
label check_events_recommand:
    $ ee = 0
    while ee < len(Events_library):
        if Events_library[ee].eventrecommand(player_focus, WeekDays[Days], True):
            $ output_event_info = Events_library[ee].event_name
            $ output_event_info += " will help you with your "
            $ output_event_info += player_focus
            #$ renpy.notify(output_event_info)
            "[output_event_info]"
        $ ee += 1
    return

label event_recommand_today:
    if event_recommand == False:
        call events_recommand
        $  event_recommand = True
    return

label events_recommand:
    $ player_focus = player_priorities[0]
    call check_events_recommand
    #
    # 1/5 will recommand second priorities; 1/10 third
    #if renpy.random.randint(1,5) == 1:
    #    $ player_focus = player_priorities[1]
    #    call check_events_recommand
    #if renpy.random.randint(1,10) == 1:
    #    $ player_focus = player_priorities[2]
    #    call check_events_recommand
    return



#
# label schedule_generator:
#   $ time_to_exit = False
#    $ Minutes = 0

#    scene bg_class
#    show screen timer_logic()
#    show screen timer_screen()
#    show screen debug_time_menu_screen()
#    call screen background_screen()
#    return
