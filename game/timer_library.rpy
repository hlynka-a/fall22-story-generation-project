# display current time
label background_screen_library:
    $ display_current_time = ""
    $ display_current_time += str(WeekDays[Days]).zfill(2)
    $ display_current_time += "  "
    $ display_current_time += str(Chunks[Parts]).zfill(2)
    $ display_current_time += "  "
    $ display_current_time += str(Hours).zfill(2)
    $ display_current_time += "  "
    $ display_current_time += str(Minutes).zfill(2)

    "[display_current_time]"
return