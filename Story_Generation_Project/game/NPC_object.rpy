init python:

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

    NPC_list = [];

    first_name_male_list = ["James","William","Oliver","Henry","Jack","Alex","John","David","Tom"];
    first_name_female_list = ["Olivia","Emma","Sophia","Emily","Mila","Lucy","Alex","Alice","Claire"];
    last_name_list = ["A","B","C","D","E","F","G","H","I","J","K","L",
        "M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
