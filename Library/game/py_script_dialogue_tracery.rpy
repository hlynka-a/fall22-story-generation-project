init python:

    # import renpy_tracery

    def getTraceryDialogue():

        # GIANT limitation of Tracery is the lack of conditional logic.
        rules = {
            'origin': [
                "Oh, #hello#! I didn't know you would also be at the #location#!",
                '#hello.capitalize#. #greeting.capitalize##punctuation#',
                '#<#initSubject#>subjectStory#'
                ],
            'subjectStory':[
                'Let me see your #topic#... your #topic# are #topic_feeling##punctuation#',
                'Your #topic# are #topic_feeling#. You #should# #topic_action#.',
                "For #topic#, you're doing #topic_feeling#. Compared to you... I'm doing #topic_feeling2##punctuation#",
                "My #topic# are #topic_feeling2##punctuation# I #should# #topic_action2#."
                ],
            'punctuation':['.','!','?!','...'],
            'initSubject':[
                "<topic:grades><topic_feeling:#p_study_feeling#><topic_feeling2:#study_feeling#><topic_action:#p_study_actions#><topic_action2:#study_actions#>",
                "<topic:social><topic_feeling:#p_social_feeling#><topic_feeling2:#social_feeling#><topic_action:#p_social_actions#><topic_action2:#social_actions#>",
                "<topic:health><topic_feeling:#p_health_feeling#><topic_feeling2:#health_feeling#><topic_action:#p_health_actions#><topic_action2:#health_actions#>"
                ],
            'should':['should', 'ought to', 'might want to','must','could'],
            'hello': ['hello', 'greetings', 'howdy', 'hey', 'good day', 'hi','yo'],
            'greeting': ['#general_feeling# #small_talk_noun# today', "Today seems like a #general_feeling# day"],
            'location': ['world', 'solar system', 'galaxy', 'universe'],
            'small_talk_noun': ['weather','temperature','food to eat','crowds','stuff to do'],
            'general_feeling':['#great_feeling#','#good_feeling#','#ok_feeling#','#poor_feeling#'],
            'great_feeling':['great','awesome','super','extraordinary','exceptional','first-class'],
            'good_feeling':['good','nice','fine','respectable','decent','solid'],
            'ok_feeling':['acceptable','fair','ok','kinda weak','iffy','passable'],
            'poor_feeling':['poor','...','inferior','deficient','(yikes)','grim', 'kinda bad', 'lousy'],
            'study_actions':['get help','find help','study more','hit the books','do your homework'],
            'p_study_actions':['get help','find help','study more','hit the books','do your homework'],
            'social_actions':["have fun"],
            'p_social_actions':["have fun"],
            'health_actions':["take a break"],
            'p_health_actions':["take a break"],
            'study_feeling':['good'],
            'social_feeling':['good'],
            'health_feeling':['good'],
            'p_study_feeling':['good'],
            'p_social_feeling':['good'],
            'p_health_feeling':['good']
        }

        if (temp_player_study >= 75):
            rules['p_study_feeling'] = rules['great_feeling'];
            rules['p_study_actions'] = ['relax a little','take it easy','keep it up','not get lazy'];
        elif (temp_player_study >= 50 and temp_player_study < 75):
            rules['p_study_feeling'] = rules['good_feeling'];
            rules['p_study_actions'] = ['keep it up','push a little harder','keep up the pace','keep going'];
        elif (temp_player_study >= 25 and temp_player_study < 50):
            rules['p_study_feeling'] = rules['ok_feeling'];
            rules['p_study_actions'] = ['catch up on studying','work a little harder','focus a bit'];
        else:
            rules['p_study_feeling'] = rules['poor_feeling'];
            rules['p_study_actions'] = ['get help','find help','study more','hit the books','do your homework'];
        if (temp_this_study >= 75):
            rules['study_feeling'] = rules['great_feeling'];
            rules['study_actions'] = ['relax a little','take it easy','keep it up','not get lazy'];
        elif (temp_this_study >= 50 and temp_this_study < 75):
            rules['study_feeling'] = rules['good_feeling'];
            rules['study_actions'] = ['keep it up','push a little harder','keep up the pace','keep going'];
        elif (temp_this_study >= 25 and temp_this_study < 50):
            rules['study_feeling'] = rules['ok_feeling'];
            rules['study_actions'] = ['catch up on studying','work a little harder','focus a bit'];
        else:
            rules['study_feeling'] = rules['poor_feeling'];
            rules['study_actions'] = ['get help','find help','study more','hit the books','do your homework'];

        if (temp_player_social >= 75):
            rules['p_social_feeling'] = rules['great_feeling'];
            rules['p_social_actions'] = ['take it easy','stop partying so hard','be the fun person you are','focus on other stuff'];
        elif (temp_player_social >= 50 and temp_player_social < 75):
            rules['p_social_feeling'] = rules['good_feeling'];
            rules['p_social_actions'] = ['keep enjoying yourself','keep it up','stick around','attend the party'];
        elif (temp_player_social >= 25 and temp_player_social < 50):
            rules['p_social_feeling'] = rules['ok_feeling'];
            rules['p_social_actions'] = ['hang out with us more often','stay for a little longer','talk with me for a bit'];
        else:
            rules['p_social_feeling'] = rules['poor_feeling'];
            rules['p_social_actions'] = ['find some friends','go outside more','talk to people','not be such a stick in the mud'];
        if (temp_this_social >= 75):
            rules['social_feeling'] = rules['great_feeling'];
            rules['social_actions'] = ['take it easy','stop partying so hard','be the fun person you are','focus on other stuff'];
        elif (temp_this_social >= 50 and temp_this_social < 75):
            rules['social_feeling'] = rules['good_feeling'];
            rules['social_actions'] = ['keep enjoying yourself','keep it up','stick around','attend the party'];
        elif (temp_this_social >= 25 and temp_this_social < 50):
            rules['social_feeling'] = rules['ok_feeling'];
            rules['social_actions'] = ['hang out with us more often','stay for a little longer','talk with me for a bit'];
        else:
            rules['social_feeling'] = rules['poor_feeling'];
            rules['social_actions'] = ['find some friends','go outside more','talk to people','not be such a stick in the mud'];

        if (temp_player_health >= 75):
            rules['p_health_feeling'] = rules['great_feeling'];
            rules['p_health_actions'] = ['put all that energy to use','go outside and enjoy yourself','study while you can','socialize while you can'];
        elif (temp_player_health >= 50 and temp_player_health < 75):
            rules['p_health_feeling'] = rules['good_feeling'];
            rules['p_health_actions'] = ['put in a bit more studying','stick around and socialize a little more','enjoy yourself'];
        elif (temp_player_health >= 25 and temp_player_health < 50):
            rules['p_health_feeling'] = rules['ok_feeling'];
            rules['p_health_actions'] = ['pace yourself','get some early rest','maybe study just a little more', 'maybe leave early', 'get some coffee'];
        else:
            rules['p_health_feeling'] = rules['poor_feeling'];
            rules['p_health_actions'] = ['get some rest','go to sleep','go home','see a doctor'];
        if (temp_this_health >= 75):
            rules['health_feeling'] = rules['great_feeling'];
            rules['health_actions'] = ['put all that energy to use','go outside and enjoy yourself','study while you can','socialize while you can'];
        elif (temp_this_health >= 50 and temp_this_health < 75):
            rules['health_feeling'] = rules['good_feeling'];
            rules['health_actions'] = ['put in a bit more studying','stick around and socialize a little more','enjoy yourself'];
        elif (temp_this_health >= 25 and temp_this_health < 50):
            rules['health_feeling'] = rules['ok_feeling'];
            rules['health_actions'] = ['pace yourself','get some early rest','maybe study just a little more', 'maybe leave early', 'get some coffee'];
        else:
            rules['health_feeling'] = rules['poor_feeling'];
            rules['health_actions'] = ['get some rest','go to sleep','go home','see a doctor'];

        rules['location']=temp_current_location;

        #grammar = tracery.Grammar(rules);
        grammar = Grammar(rules);
        grammar.add_modifiers(base_english);
        sentence = grammar.flatten("#origin#");
        return sentence;
