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
        def addEvent(self, event_obj):
            self.Events_library.append(event_obj);
        def defineRandomNPC(self):
            # (don't just get name from male list - need to check if NPC is male or female, and get appropriate name.)
            self.npc_firstname = random.choice(first_name_male_list);
            self.npc_lastname = random.choice(last_name_female_list);
            self.Events_library = defineRandomNPCSchedule();
            return self;
        def defineRandomNPCSchedule():
            randomSchedule = [];
            # use ScheduleGenerator.rpy as example
            # below events should be randomized more - start/end time should be randomized, which location to go to should be randomized.
            # can we direct what locations to go to (example: NPC 'study' stat is low, so they will want to go to the Library today)
            randInt = random.randrange(0,10);
            if (randInt % 3 == 0):
                randomSchedule.append(Event("Library", "Mon", 8, 0, 10, 0, False));
                randomSchedule.append(Event("Classroom","Mon", 10,0,12,0,False));
                randomSchedule.append(Event("Cafe","Mon",12,0,2,0,False));
                randomSchedule.append(Event("Park","Mon",2,0,5,0,False));
            elif (randInt % 3 == 1):
                randomSchedule.append(Event("Library", "Mon", 7, 0, 9, 0, False));
                randomSchedule.append(Event("Classroom","Mon", 10,0,12,0,False));
                randomSchedule.append(Event("Park","Mon",12,0,2,0,False));
                randomSchedule.append(Event("Cafe","Mon",2,0,5,0,False));
            elif (randInt % 3 == 2):
                randomSchedule.append(Event("Cafe", "Mon", 7, 0, 9, 0, False));
                randomSchedule.append(Event("Library","Mon", 9,0,11,0,False));
                randomSchedule.append(Event("Classroom","Mon",11,0,1,0,False));
                randomSchedule.append(Event("Park","Mon",1,0,5,0,False));
            return randomSchedule;
        def updateNPCStat(self, study_add=0, social_add=0, health_add=0):
            self.npc_study = self.npc_study + study_add;
            self.npc_social = self.npc_social + social_add;
            self.npc_health = self.npc_health + health_add;


    NPC_list = [];

    first_name_male_list = ["James","William","Oliver","Henry","Jack","Alex","John","David","Tom"];
    first_name_female_list = ["Olivia","Emma","Sophia","Emily","Mila","Lucy","Alex","Alice","Claire"];
    last_name_list = ["A","B","C","D","E","F","G","H","I","J","K","L",
        "M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
    personality_trait_list = ["Studious","Social","Athletic","Sleepy"]
    # Studious = Library, Classroom
    # Social = Park, Coffee House, Cafeteria, Clubhouse, Pub
    # Athletic = Swimming Pool, Park, Gym, Sports Grounds
    # Sleepy = Residence, Classroom
    # (How do these affect stat values for NPC?
    #   What takes priority - personality or current stat values that need to increase?)



    def defineRandomNPCs(n):
        startTime = time.time();
        i_counter = 0
        while i_counter < n:
            newNPC = NPC()
            newNPC.defineRandomNPC()
            NPC_list.append(newNPC);
            i_counter = i_counter + 1
        endTime = time.time();
        renpy.notify("Time it took to generate " + len(NPC_list) + " NPC's = " + (endTime - startTime) + " seconds.");
