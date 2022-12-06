init python:

    import time;
    import random;

    class NPC(object):
        def __init__(self, npc_firstname = "AnnoymousNPC", npc_lastname = "A",
            npc_study = 50, npc_social = 50, npc_health = 50,
            Location = "Residence", Events_library = [],
            Personality = []):
            self.npc_firstname = npc_firstname;
            self.npc_lastname = npc_lastname;
            self.npc_study = npc_study;
            self.npc_social = npc_social;
            self.npc_health = npc_health;
            self.Location = Location;
            self.Events_library = Events_library;
            self.Personality = Personality;
            self.special_event_dictionary = {
                    "study_buddy":False
                };
        def addEvent(self, event_obj):
            self.Events_library.append(event_obj);
        def defineRandomNPC(self):
            # (don't just get name from male list - need to check if NPC is male or female, and get appropriate name.)
            self.npc_firstname = random.choice(first_name_male_list);
            self.npc_lastname = random.choice(last_name_list);
            self.Events_library = self.defineRandomNPCSchedule();
            randInt = random.randrange(1,10);
            self.npc_study = randInt * 10;
            randInt = random.randrange(1,10);
            self.npc_social = randInt * 10;
            randInt = random.randrange(1,10);
            self.npc_health = randInt * 10;
            return self;
        def defineRandomNPCSchedule(self):
            randomSchedule = [];
            # use ScheduleGenerator.rpy as example
            # below events should be randomized more - start/end time should be randomized, which location to go to should be randomized.
            # can we direct what locations to go to (example: NPC 'study' stat is low, so they will want to go to the Library today)
            randInt = random.randrange(0,10);
            if (randInt % 3 == 0):
                randomSchedule.append(Event("Park", "Mon", 8, 0, 10, 0, False));
                randomSchedule.append(Event("Classroom","Mon", 10,0,12,0,False));
                randomSchedule.append(Event("Cafeteria","Mon",12,0,14,0,False));
                randomSchedule.append(Event("Park","Mon",14,0,17,0,False));
            elif (randInt % 3 == 1):
                randomSchedule.append(Event("Cafeteria", "Mon", 7, 0, 9, 0, False));
                randomSchedule.append(Event("Classroom","Mon", 10,0,12,0,False));
                randomSchedule.append(Event("Park","Mon",12,0,14,0,False));
                randomSchedule.append(Event("Cafeteria","Mon",14,0,17,0,False));
            elif (randInt % 3 == 2):
                randomSchedule.append(Event("Park", "Mon", 7, 0, 9, 0, False));
                randomSchedule.append(Event("Library","Mon", 9,0,11,0,False));
                randomSchedule.append(Event("Classroom","Mon",11,0,13,0,False));
                randomSchedule.append(Event("Park","Mon",13,0,17,0,False));

            # assume we want to reset special events options every time schedule is made

            return randomSchedule;
        def updateNPCStat(self, study_add=0, social_add=0, health_add=0):
            self.npc_study = self.npc_study + study_add;
            self.npc_social = self.npc_social + social_add;
            self.npc_health = self.npc_health + health_add;


    NPC_list = [];

    # (names taken from top 100 baby names in USA - please add more interesting names to these lists.)
    first_name_male_list = ["James","William","Oliver","Henry","Jack","Alex","John","David","Tom"];
    first_name_female_list = ["Olivia","Emma","Sophia","Emily","Mila","Lucy","Alex","Alice","Claire"];
    last_name_list = ["A","B","C","D","E","F","G","H","I","J","K","L",
        "M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
    personality_trait_list = ["Studious","Social","Athletic","Sleepy"]
    # Studious = Library, Classroom
    # Social = Park, Coffee House, Cafeteria, Clubhouse, Pub
    # Athletic = Swimming Pool, Park, Gym, Sports Grounds
    # Sleepy = Residence, Classroom
    #       (How do these affect stat values for NPC?
    #           What takes priority - personality or current stat values that need to increase?)
    #           Should "mood" also be a variable?
    #           Does mood change based on whether they go to places they like that day, or how the Player talks to them?



    npcTalkingNow = False;

    def defineRandomNPCs(n):
        startTime = time.time();
        i_counter = 0
        while i_counter < n:
            newNPC = NPC()
            newNPC.defineRandomNPC()
            NPC_list.append(newNPC);
            i_counter = i_counter + 1
        endTime = time.time();
        renpy.notify("Time it took to generate " + str(len(NPC_list)) + " NPC's = " + str(endTime - startTime) + " seconds.");

    def get_NPCs_at_location(someLocation):
        list_of_NPCs_at_location = []
        npc_index = 0
        while (npc_index < len(NPC_list)):
            if (NPC_list[npc_index].Location == someLocation):
                list_of_NPCs_at_location.append(NPC_list[npc_index])
            npc_index = npc_index + 1
        return list_of_NPCs_at_location

label check_NPC_events():
    $ npc_index = 0
    while (npc_index < len(NPC_list)):
        $ event_index = 0
        $ location_was_set = False
        while event_index < len(NPC_list[npc_index].Events_library):
            if NPC_list[npc_index].Events_library[event_index].npceventcheck(WeekDays[Days],Hours,Minutes):
                $ output_event_info = NPC_list[npc_index].Events_library[event_index].event_name
                #$ output_event_info += " - NPC (" + NPC_list[npc_index].npc_firstname + " " + NPC_list[npc_index].npc_lastname + ") happens now."
                #$ renpy.notify(output_event_info)
            if NPC_list[npc_index].Events_library[event_index].npceventinactive(WeekDays[Days],Hours,Minutes):
                $ output_event_info = NPC_list[npc_index].Events_library[event_index].event_name
                #$ output_event_info += " - NPC (" + NPC_list[npc_index].npc_firstname + " " + NPC_list[npc_index].npc_lastname + ") ends now."
                #"[output_event_info]"
                #$ renpy.notify(output_event_info)
            if NPC_list[npc_index].Events_library[event_index].event_active == True:
                $ NPC_list[npc_index].Location = NPC_list[npc_index].Events_library[event_index].event_name
                $ location_was_set = True
            $ event_index += 1
        # If no scheduled-location for NPC, make them go to Residence by default
        if (location_was_set == False):
            $ NPC_list[npc_index].Location = "Residence"
        $ npc_index = npc_index + 1
    return

label display_NPC_list_summary():
    e "Let's see how all the students are doing!"
    call screen screen_NPC_list_summary
    return

screen screen_NPC_list_summary():

    $ listOfNPC = NPC_list
    frame:
        xalign 0.5 ypos 300
        vpgrid:
            cols 1
            xalign 1.0 ypos 0 xysize (800, 600)
            child_size (800, 100)
            scrollbars "vertical"
            side_spacing 5
            mousewheel True
            arrowkeys True
            #add text "Library"
            #add text "There are 0 people here"
            text "---------------------------------------------------------------"
            text "Name:_Study:_Social:_Health:_"
            for i in range(0, len(listOfNPC)):
                $ NPC_name = listOfNPC[i].npc_firstname + " " + listOfNPC[i].npc_lastname + " " + str(listOfNPC[i].npc_study) + " " + str(listOfNPC[i].npc_social) + " " + str(listOfNPC[i].npc_health)
                text "[NPC_name]"
            text ""
    imagebutton:
        # Residence
        xpos 1600
        ypos 300
        idle "re_idle"
        hover "re_hover"
        #hovered Notify(notify_message_park)
        #action Jump("Residence")
        action [Jump("uni_map")]
