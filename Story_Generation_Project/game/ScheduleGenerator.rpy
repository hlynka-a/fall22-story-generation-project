# Minutes = 0 Hours = 8 Parts = 0 Days = 0 WeekDays = ["Mon","Tue","Wed","Thu","Fri"] Chunks = ["Morning","Afternoon","Evening","Night"]
# $ WeekDays = ["Mon","Tue","Wed","Thu","Fri"]
#init python:
#    class Event(object):
#        def __init__(self, event_name = "",event_day = 0,event_hstarts = 1,event_mstatrs = 0, event_hends = 1, event_mends = 0,event_active = False):
#            self.event_name = event_name;
#            self.event_day = event_day;
#            self.event_hstarts = event_hstarts;
#            self.event_mstatrs = event_mstatrs;
#            self.event_hends = event_hends;
#            self.event_mends = event_mends;
#            self.event_active = event_active;

#        def eventcheck(self, e_d, e_hs, e_ms):
#            temp_tstart = (self.event_hstarts * 100) + self.event_mstatrs;
#            temp_tend = (self.event_hends * 100) + self.event_mends;
#            temp_currenttime = (e_hs * 100) + e_ms;
#            if self.event_day == e_d and temp_tstart <= temp_currenttime and temp_tend >= temp_currenttime and self.event_active == False:
#                self.event_active = True;
#                return True
#            else:
#                return False
#
#        def eventinactive(self, e_d, e_he, e_me):
#            temp_tstart = (self.event_hstarts * 100) + self.event_mstatrs;
#            temp_tend = (self.event_hends * 100) + self.event_mends;
#            temp_currenttime = (e_he * 100) + e_me;
#
#            if (self.event_day != e_d or (temp_tstart > temp_currenttime or temp_tend < temp_currenttime)) and self.event_active == True:
#                self.event_active = False;
#                return True
#            else:
#                return False
#        def eventhappenDay(self, e_d):
#            if self.event_day == e_d:
#                return True
#            else:
#                return False


#    Events_library = []
#    Events_today = []
#    WeekDays = ["Mon","Tue","Wed","Thu","Fri"]

#    Events_library.append(Event("COMP1405", "Wed", 14, 0, 16, 0, False));
#    Events_library.append(Event("COMP1805", "Mon", 9, 10, 10, 0, False));
#    Events_library.append(Event("COMP2401", "Tue", 10, 0, 11, 0, False));
#    Events_library.append(Event("COMP2401", "Thu", 10, 0, 11, 0, False));
#    Events_library.append(Event("COMP3000", "Mon", 12, 0, 13, 0, False));

#    i = 0
#    e = 0
#    while i < len(WeekDays):
#        Events_today.append("");
#        while e < len(Events_library):
#            if WeekDays[i] == Events_library[e].event_day:
#                Events_today[i] += Events_library[e].event_name
#                Events_today[i] += " "
#            e += 1
#        Events_today[i] += " will happen today."
#        i += 1




label schedule_generator:
    $ time_to_exit = False
    $ Minutes = 0

    scene bg_class
    show screen timer_logic()
    show screen timer_screen()
    show screen debug_time_menu_screen()
    call screen background_screen()

    return

define event_notify = False

#label check_events:
#    call event_notify_today
#    $ ee = 0
#    while ee < len(Events_library):
#        if Events_library[ee].eventcheck(WeekDays[Days],Hours,Minutes,True):
#            $ output_event_info = Events_library[ee].event_name
#            $ output_event_info += " happens now."
#            $ renpy.notify(output_event_info)
#        if Events_library[ee].eventinactive(WeekDays[Days],Hours,Minutes,True):
#            $ output_event_info = Events_library[ee].event_name
#            $ output_event_info += " ends now."
#            #"[output_event_info]"
#            $ renpy.notify(output_event_info)
#        $ ee += 1
#    return

#label event_notify_today:
#    if event_notify == False:
#            $ output_event_info = Events_today[Days]
#            "[output_event_info]"
#            $ event_notify = True
#    return
