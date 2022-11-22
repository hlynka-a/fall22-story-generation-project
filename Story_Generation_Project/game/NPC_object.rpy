init python:

    import time;

    class NPC(object):
        def __init__(self, npc_firstname = "AnnoymousNPC", npc_lastname = "A",
            npc_study = 50, npc_social = 50, npc_health = 50,
            Location = "Residence", Events_library = []):
            self.npc_firstname = npc_firstname;
            self.npc_lastname = npc_lastname;
            self.npc_study = npc_study;
            self.npc_social = npc_social;
            self.npc_health = npc_health;
            self.Location = Location;
            self.Events_library = Events_library;
        def addEvent(self, event_obj):
            self.Events_library.append(event_obj);
        def defineRandomNPC(self):
            self.Events_library = defineRandomNPCSchedule();
            return;
        def defineRandomNPCSchedule():
            randomSchedule = [];
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

    def defineRandomNPCs(n):
        startTime = time.time();
        i_counter = 0
        while i_counter < n:
            NPC_list.append(0);
            i_counter = i_counter + 1
        endTime = time.time();
        renpy.notify("Time it took to generate " + len(NPC_list) + " NPC's = " + (endTime - startTime) + " seconds.");
