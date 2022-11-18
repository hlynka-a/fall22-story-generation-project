init python:

    import time;
    import threading;

    Minutes = 0;

    real_time_on = False;
    time_thread = 0;

    def startTime():
        renpy.notify("startTime() called");
        if (real_time_on == True):
            startTimeReal();

    def stopTime():
        if (real_time_on == True):
            stopTimeReal();

    def startTimeReal():
        renpy.notify("startTimeReal() called");
        global time_thread;
        global real_time_on;
        time_thread = threading.Thread(target=realTimeThread);
        real_time_on = True;
        time_thread.start();

    def stopTimeReal():
        global time_thread;
        global real_time_on;
        if (real_time_on == True):
            real_time_on = False;
            time_thread.join();

    def increaseTime(timeToAdd):
        global Minutes;
        Minutes = Minutes + timeToAdd;

    def decraeseTime(timeToTake):
        global Minutes;
        Minutes = Minutes - timeToTake;

    # WARNING - If thread is still running in background, game cannot close! BE VERY CAREFUL!
    def realTimeThread():
        renpy.notify("realTimeThread() called");
        global real_time_on;
        global Minutes;
        while (real_time_on):
            time.sleep(1)
            Minutes = Minutes + 1;
            renpy.notify("minutes updated in thread, now = " + str(Minutes));
            renpy.call("check_events_timer");
