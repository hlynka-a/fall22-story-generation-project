
### Time:
###     Days = [0 - 5]
###     Hours = [0 - 23]
###     Minutes = [0 - 59]
###     WeekDays = ["Mon" - "Fri"]      # list of possible week days
###     Chunks = ["Morning" - "Night"]  # discrete periods of the day, calculated based on current Hours and Minutes
default Days = 0
default Hours = 0
default Minutes = 0
default WeekDays = ["Mon","Tue","Wed","Thu","Fri"]
default Chunks = ["Morning","Afternoon","Evening","Night"]

### Normal Events:
###     Access schedule of Player events from:
###         Events_library = []                 # a Python data object with sub-objects (listed below)
###             Events_library[0].event_name = "somestring"
###             Events_library[0].event_day = [0 - 5]
###             Events_library[0].event_hstarts = [0 - 23]
###             Events_library[0].event_mstarts = [0 - 59]
###             Events_library[0].event_hends = [0 - 23]
###             Events_library[0].event_mends = [0 - 59]
###             Events_library[0].event_active = [True or False]


### Normal Dialogue with NPC:
###     Call '$ initializeDialogue()' once at beginning of the game (for non-Tracery dialogue).
###     BEFORE calling to get a line of dialogue, first update the following variables:
###             temp_player_study=50;
###             temp_player_social=50;
###             temp_player_health=50;
###             temp_this_study=50;
###             temp_this_social=50;
###             temp_this_health=50;
###             temp_current_day=0;
###             temp_current_hour=0;
###             temp_current_minute=0;
###             temp_current_location="Library";
###         OR do this automatically by calling '$ updateDialogueVariables()'
###     Call '$ dialogue = getDialogue()' to get 1 line of (non-Tracery) dialogue.
###     Call '$ dialogue = getTraceryDialogue()' to get 1 line of (Tracery) dialogue.

### Location:
###     Location = "Classroom"      (a string, can be ["Classroom", "Library", "Park", "Coffee Shop", "Cafeteria", "Shop", "Lounge", "Residence"], more can be added.)
default Location = "Classroom"
default LocationList = ["Classroom","Library","Park","Coffee Shop","Cafeteria","Shop","Lounge","Residence"]

### Player Stats:
###     Player_study = [0 - 100]
###     Player_social = [0 - 100]
###     Player_health = [0 - 100]
default Player_study = 50
default Player_social = 50
default Player_health = 50

### NPC Stats:
###     Access NPC elements from:
###         NPC_list = []                               # a Python data object with sub-objects (listed below)
###             NPC_list[0].npc_firstname = "somestring"
###             NPC_list[0].npc_lastname = "somestring"
###             NPC_list[0].npc_study = [0 - 100]
###             NPC_list[0].npc_social = [0 - 100]
###             NPC_list[0].npc_health = [0 - 100]
###             NPC_list[0].Location = "Classroom"      # some location from LocationList
###             NPC_list[0].Events_library = []         # similar to Player's Events_library, but does not notify screen when change occurs, and changes location attribute of NPC
