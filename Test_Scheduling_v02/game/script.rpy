
screen imagemap_example():
    # Copied from TUTORIAL example.
    # Curious bug: I didn't change the name of the functions (screen, label), and it seemed to be calling the TUTORIAL version instead of mine.
    # But when I modified text displayed inside each function (not the name of the function itself), the correct functions were called.
    imagemap:
        if (currentTime == timeOfDay[0]):
            idle "imagemap ground morning"
        elif (currentTime == timeOfDay[1]):
            idle "imagemap ground afternoon"
        elif (currentTime == timeOfDay[2]):
            idle "imagemap ground evening"
        else:
            idle "imagemap ground"

        idle "imagemap ground morning"
        hover "imagemap hover"

        hotspot (100, 200, 100, 100) action Jump("classroom") alt "Classroom"
        hotspot (300, 200, 100, 100) action Jump("library") alt "Library"
        #hotspot (726, 106, 93, 93) action Jump("art") alt "Art"
        #hotspot (934, 461, 93, 93) action Jump("home") alt "Home"
        hotspot (100, 600, 300, 100) action Jump("advancetime") alt "Advance Time"

label imagemap_example:
    # Call the imagemap_example screen.
    call screen imagemap_example

label classroom:
    e "You chose classroom from MY EXAMPLE."
    $ num_of_people = num_of_people_at(0)
    e "In the classroom, there are currently [num_of_people] here."
    jump imagemap_done

label library:
    e "You chose library from MY EXAMPLE."
    $ num_of_people = num_of_people_at(1)
    e "In the library, there are currently [num_of_people] here."
    jump imagemap_done

label advancetime:
    $ update_time()
    e "The time and day are now [currentDay] and [currentTime]."
    jump imagemap_done

label art:
    e "You chose art from MY EXAMPLE."
    e "Really good background art is hard to make, which is why so many games use filtered photographs. Maybe you can change that."
    jump imagemap_done

label home:
    e "You chose to go home from MY EXAMPLE."
    jump imagemap_done

label imagemap_done:
    e "Anyway..."
    jump continue


# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show eileen happy

    $ my_scheduler_v01();

    # These display lines of dialogue.
    e "You've created a new Ren'Py game."
    e "Once you add a story, pictures, and music, you can release it to the world!"

    jump imagemap_example

    # This ends the game.
    return

label continue:
    scene bg room
    show eileen happy
    e "Let's go back to the map."

    jump imagemap_example
