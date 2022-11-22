
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

default Location = "Classroom"
