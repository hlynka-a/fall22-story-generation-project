init python:

    hello_world_dialogue = "hello world!";

    class DialogueOptionClass:
        player_study_range = [0,100];
        player_social_range = [0,100];
        player_health_range = [0,100];

        this_study_range = [0,100];
        this_social_range = [0,100];
        this_health_range = [0,100];

        # what is the format for days?
        required_day_range = [0,100];

        # if location = empty, then dialogue can occur anywhere
        required_location = [];

        # add extra check based on NPC interests

        # add extra check based on special events (by ID number per event?)

        # add extra check for what dialogue was already said by this character
        # if past_dialogue = empty, then no other dialogue had to be said first.
        required_past_dialogue = [];

        dialogue_id = "someid_123";
        output_string = "This is example text that is written like dialogue.";

        def __init__(self, *, dialogue_id="someid_123",
            player_study_range=[0,100], player_social_range=[0,100], player_health_range=[0,100],
            this_study_range=[0,100], this_social_range=[0,100], this_health_range=[0,100],
            required_day_range=[0,100], required_location=[], required_past_dialogue=[],
            output_string="This is example text that is written like dialogue."):

            self.player_study_range = player_study_range;
            self.player_social_range = player_social_range;
            self.player_health_range = player_health_range;
            self.this_study_range = this_study_range;
            self.this_social_range = this_social_range;
            self.this_health_range = this_health_range;

            self.required_day_range = required_day_range;
            self.required_location = required_location;
            self.required_past_dialogue = required_past_dialogue;

            self.dialogue_id = dialogue_id;
            self.output_string = output_string;

        def isDialogueValid(self,*,dialogue_history=[],
            player_study=-1, player_social=-1, player_health=-1,
            this_study=-1, this_social=-1, this_health=-1,
            current_day=-1, current_location=""):
            #renpy.notify("return False?");
            if (player_study != -1):
                if (player_study < self.player_study_range[0] or player_study > self.player_study_range[1]):
                    return False;
            if (player_social != -1):
                if (player_social < self.player_social_range[0] or player_social > self.player_social_range[1]):
                    return False;
            if (player_health != -1):
                if (player_health < self.player_health_range[0] or player_health > self.player_health_range[1]):
                    return False;
            if (this_study != -1):
                if (this_study < self.this_study_range[0] or this_study > self.this_study_range[1]):
                    return False;
            if (this_social != -1):
                if (this_social < self.this_social_range[0] or this_social > self.this_social_range[1]):
                    return False;
            if (this_health != -1):
                if (this_health < self.this_health_range[0] or this_health > self.this_health_range[1]):
                    return False;
            if (current_day != -1):
                if (current_day < self.required_day_range[0] or current_day > self.required_day_range[1]):
                    return False;
            if (current_location != ""):
                if (len(self.required_location) != 0):
                    if ((current_location in self.required_location)==False):
                        return False;
            if (dialogue_history[self.dialogue_id] == True):
                return False;
            if (len(self.required_past_dialogue) != 0):
                for id in self.required_past_dialogue:
                    if (dialogue_history[id] == False):
                        return False;

            #renpy.notify("return True");
            return True;

    dialogue_choices = [];
    spoken_dialogue = [];

    temp_player_study=50;
    temp_player_social=50;
    temp_player_health=50;
    temp_this_study=50;
    temp_this_social=50;
    temp_this_health=50;
    temp_current_day=0;
    temp_current_hour=0;
    temp_current_minute=0;
    temp_current_location="Library";

    def updateDialogueVariables():
        global temp_player_study;
        global temp_player_social;
        global temp_player_health;

        global temp_current_day;
        global temp_current_hour;
        global temp_current_minute;
        global temp_current_location;

        temp_player_study = Player_study;
        temp_player_social = Player_social;
        temp_player_health = Player_health;

        temp_current_day = Days;
        temp_current_hour = Hours;
        temp_current_minute = Minutes;
        temp_current_location = Location;
        #renpy.notify("updateDialogueVariables() called. Location = "+ temp_current_location);

    def initializeDialogue():
        global dialogue_choices;
        global spoken_dialogue;

        dialogue_choices = [];
        spoken_dialogue = {};

        # Can we replace the hard-written lines of dialogue with 'Tracery' dialogue?
        dialogue_choices.append(DialogueOptionClass(dialogue_id="id_100",
            player_study_range=[70,100],
            output_string="Wow, you've been studying a lot!"));
        dialogue_choices.append(DialogueOptionClass(dialogue_id="id_101",
            player_study_range=[70,100],required_location=["Library"],
            output_string="Still studying at the Library? You're a hard worker!"));
        dialogue_choices.append(DialogueOptionClass(dialogue_id="id_102",
            this_study_range=[70,100],required_location=["Library"],
            output_string="I love studying at the Library! It's a great place to focus."));
        dialogue_choices.append(DialogueOptionClass(dialogue_id="id_103",
            this_study_range=[30,100],this_social_range=[60,100],required_location=["Library"],
            output_string="I like reading. Don't you?"));
        dialogue_choices.append(DialogueOptionClass(dialogue_id="id_104",
            this_study_range=[30,100],required_location=["Library"],required_past_dialogue=["id_105"],
            output_string="You found the book! Thank you!"));
        dialogue_choices.append(DialogueOptionClass(dialogue_id="id_105",
            this_study_range=[30,100],required_location=["Library"],
            output_string="I can't find this book... please let me know if you find it."));
        dialogue_choices.append(DialogueOptionClass(dialogue_id="id_106",
            player_study_range=[20,40],required_location=["Library"],
            output_string="I'm surprised to see you at the Library, you don't seem to study often."));
        dialogue_choices.append(DialogueOptionClass(dialogue_id="id_107",
            player_study_range=[0,20],this_study_range=[60,100],
            output_string="Hit the books! You have a lot to catch up on!"));
        dialogue_choices.append(DialogueOptionClass(dialogue_id="id_108",
            player_study_range=[0,20],this_study_range=[60,100],this_social_range=[60,100],required_location=["Library"],
            output_string="I know you don't come to the Library often... if you get lost or need help, let me know."));
        dialogue_choices.append(DialogueOptionClass(dialogue_id="id_109",
            player_study_range=[0,30],this_study_range=[0,30],required_location=["Library"],
            output_string="It looks like both of us need to study a lot more. I guess it's good we're both at the Library."));
        dialogue_choices.append(DialogueOptionClass(dialogue_id="id_110",
            this_study_range=[0,30],required_location=["Library"],
            output_string="I'm falling behind a little in classes. I need to focus here at the Library."));
        dialogue_choices.append(DialogueOptionClass(dialogue_id="id_111",
            this_study_range=[0,30],this_health_range=[0,30],required_location=["Library"],
            output_string="I need to keep studying... but I'm SO tired..."));
        dialogue_choices.append(DialogueOptionClass(dialogue_id="id_112",
            player_health_range=[0,25],required_location=["Library"],
            output_string="Why are you at the Library? You look exhausted! Go back to Residence to rest."));
        dialogue_choices.append(DialogueOptionClass(dialogue_id="id_113",
            player_health_range=[0,25],required_location=["Classroom"],
            output_string="It's important to be in class, but you also need to rest too. Go back to Residence to sleep."));
        dialogue_choices.append(DialogueOptionClass(dialogue_id="id_114",
            player_study_range=[0,40],player_social_range=[0,40],required_location=["Classroom"],
            output_string="Why are you distracting me in class? Pay attention! Your grades are already bad enough."));
        dialogue_choices.append(DialogueOptionClass(dialogue_id="id_115",
            player_study_range=[0,40],player_social_range=[60,100],required_location=["Classroom"],
            output_string="I know we should be paying attention in class, but your jokes are too funny!"));
        dialogue_choices.append(DialogueOptionClass(dialogue_id="id_116",
            this_study_range=[0,40],required_location=["Classroom"],
            output_string="This class is SO HARD! I have no idea what I'm doing..."));
        dialogue_choices.append(DialogueOptionClass(dialogue_id="id_117",
            this_study_range=[60,85],required_location=["Classroom"],
            output_string="I think I understand this class. I wonder if I can get an A- on my next test..."));
        dialogue_choices.append(DialogueOptionClass(dialogue_id="id_118",
            this_study_range=[85,100],required_location=["Classroom"],
            output_string="I hope I get at least an A+ in this class. I don't want to bring down my average."));
        dialogue_choices.append(DialogueOptionClass(dialogue_id="id_119",
            this_study_range=[70,100],this_social_range=[0,40],required_location=["Classroom"],
            output_string="People say I'm not social enough, but my grades are more important than having fun."));
        dialogue_choices.append(DialogueOptionClass(dialogue_id="id_119",
            this_study_range=[70,100],this_health_range=[0,30],required_location=["Classroom"],
            output_string="I've been up all night studying for today's class. I'm exhausted, but I think it was worth it."));
        dialogue_choices.append(DialogueOptionClass(dialogue_id="id_000",
            output_string="This is an initialized dialogue line."));
        dialogue_choices.append(DialogueOptionClass(dialogue_id="id_001",
            output_string="This is an yet another initialized dialogue line."));

        for dialogue in dialogue_choices:
            spoken_dialogue.update({dialogue.dialogue_id: False});

        renpy.notify("dialogue initialized.");

    def getDialogue():
        global spoken_dialogue;
        valid_dialogue = [];
        #renpy.notify("len of dialogue is = " + str(len(dialogue_choices)));
        somestring = "";
        for dialogue in dialogue_choices:
            if (dialogue.isDialogueValid(current_day = 1, dialogue_history=spoken_dialogue,
                player_study=temp_player_study, player_social=temp_player_social, player_health=temp_player_health,
                this_study=temp_this_study, this_social=temp_this_social, this_health=temp_this_health,
                current_location=temp_current_location) == True):
                valid_dialogue.append(dialogue);
        # renpy.notify("len of valid_dialogue is = " + str(len(valid_dialogue)) + " " + somestring);
        renpy.notify("list of possible valid_dialogue = " + str(len(valid_dialogue)));
        if (len(valid_dialogue) == 0):
            return_dialogue = "(no valid dialogue left)";
        else:
            return_dialogue = valid_dialogue[0].output_string;
            spoken_dialogue[valid_dialogue[0].dialogue_id] = True;
        return return_dialogue;
