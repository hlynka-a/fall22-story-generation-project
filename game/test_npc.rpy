init python: 
    class test_NPC_Lucy(object):
        def __init__(self, npc_firstname = "Lucy", npc_lastname = "A",
            npc_study = 10, npc_social = 10, npc_health = 10,
            Location = "Residence", Personality = "Study"):
            self.npc_firstname = npc_firstname;
            self.npc_lastname = npc_lastname;
            self.npc_study = npc_study;
            self.npc_social = npc_social;
            self.npc_health = npc_health;
            self.Location = Location;
            self.Personality = Personality;

    test_NPC_lucy = test_NPC_Lucy()


label create_test_NPC_image:
    call screen test_NPC_image
    return

screen test_NPC_image:
    imagebutton:
        xpos 0.3
        ypos 0.3
        idle "logo base"
        hover "logo idle"
        #hovered Show("test_NPC_statements_bars")
        #unhovered Hide("test_NPC_statements_bars")

        #action [Hide("test_NPC_statements_bars")]
return


screen test_NPC_statements_bars():

    $ NPC_study = test_NPC_lucy.npc_study
    $ NPC_social = test_NPC_lucy.npc_social
    $ NPC_health = test_NPC_lucy.npc_health

    frame:
        xalign 0.1 ypos 20
        xsize 500
        vbox:
            spacing 5

            bar value ScreenVariableValue("NPC_study", 100) style "bar"
            text 'Study: [NPC_study]' align(0,50)
            bar value ScreenVariableValue("NPC_social", 100) style "bar"
            text 'Social: [NPC_social]' align(0,80)
            bar value ScreenVariableValue("NPC_health", 100) style "bar"
            text 'Health: [NPC_health]' align(0,80)
return