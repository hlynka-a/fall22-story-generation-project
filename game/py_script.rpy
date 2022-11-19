init python:
    def my_func_v01():
        print("This is a function called 'my_funcv01()'")
        #show eileen happy
        renpy.notify("my_funcv01() was called.");
        print("end of 'my_funcv01()'")

    my_schedule = "hello world";
    character_schedules = [];
    #locations = ["class", "residence", "library", "park", "cafe"];
    locations = ["classroom", "library", "park"];
    timeOfDay = ["morning", "afternoon", "evening"];
    day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];
    currentDay = day[0];
    currentTime = timeOfDay[0];
    currentTimeIndex = 0;
    currentDayIndex = 0;
    hello_world = "hello world!";


    def my_scheduler_v01():
        print("This is a function called 'my_scheduler_v01()'")
        renpy.notify("my_scheduler_v01() was called.");

        global my_schedule;
        global character_schedules;
        character_schedules = [];

        my_schedule = [];
        my_schedule.append([timeOfDay[0], locations[1]]);
        my_schedule.append([timeOfDay[1], locations[0]]);
        my_schedule.append([timeOfDay[2], locations[2]]);
        character_schedules.append(my_schedule);

        my_schedule = [];
        my_schedule.append([timeOfDay[0], locations[2]]);
        my_schedule.append([timeOfDay[1], locations[0]]);
        my_schedule.append([timeOfDay[2], locations[1]]);
        character_schedules.append(my_schedule);

        my_schedule = [];
        my_schedule.append([timeOfDay[0], locations[2]]);
        my_schedule.append([timeOfDay[1], locations[0]]);
        my_schedule.append([timeOfDay[2], locations[2]]);
        character_schedules.append(my_schedule);
        #my_schedule.append([day[0],timeOfDay[0], locations[1]]);
        #my_schedule.append([day[0],timeOfDay[1], locations[0]]);
        #my_schedule.append([day[0],timeOfDay[2], locations[2]]);
        #my_schedule.append([day[0],timeOfDay[0], locations[1]]);
        #my_schedule.append([day[0],timeOfDay[1], locations[0]]);
        #my_schedule.append([day[0],timeOfDay[2], locations[2]]);

        print("end of 'my_scheduler_v01()'")

    def update_time():
        renpy.notify("update_time() was called.");

        global currentTime;
        global currentTimeIndex;
        global currentDayIndex;
        global currentDay;
        currentTimeIndex = currentTimeIndex + 1;
        if (currentTimeIndex >= 3):
            currentTimeIndex = 0;
            currentDayIndex = currentDayIndex + 1;
            if (currentDayIndex >= 5):
                currentDayIndex = 0;
        currentTime = timeOfDay[currentTimeIndex];
        currentDay = day[currentDayIndex];

    def num_of_people_at(locationIndex):
        totalPeople = 0;
        place = locations[locationIndex];
        global character_schedules;
        for schedule in character_schedules:
            if (schedule[currentTimeIndex][1] == place):
                totalPeople = totalPeople + 1;
        #renpy.notify(character_schedules[0][0][1]);
        return totalPeople;
