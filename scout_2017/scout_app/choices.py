TEAM_FILTER_CHOICES = (
		(u"perfect climbers", u"perfect climbers"),
		(u"most gears in teleop", u"most gears in teleop"),
		(u"teams ranked by climbs", u"teams ranked by climbs")
		)

ACCURACY_CHOICES = (
		(0, ("unfilled")),
		(1, ("did not attempt")),
		(2, ("poor accuracy")),
		(3, ("A few went in")),
		(4, ("Half went in")),
		(5, ("over half went in")),
		(6, ("100% accuracy")))

SPEED_CHOICES = (
                (u'did not attempt', u"did not attempt"),
                (u"<1 ball/sec", u"<1 ball/sec"),
                (u"1 ball/sec", u"1 ball/sec"),
                (u"3 balls/sec", u"3 balls/sec"),
                (u"5+ balls/sec", u"5+ balls/sec"),
                (u"faster than the speed of light", u"faster than the speed of light"))

HOPPER_EFFICIENCY = (
                (u"did not attempt", u"did not attempt"),
                (u"less than 5 balls caught", u"less than 5 balls caught"),
                (u"almost ten balls caught", u"Almost ten balls caught"),
                (u"over ten balls caught", u"over ten balls caught"),
                (u"only dropped a few", u"only dropped a few"),
                (u"collected every ball", u"collected every single ball"))

GEAR_POSITION = (
		(u"unfilled", u"unfilled"),
		(u"did not attempt", u"did not attempt"),
		(u"left peg", u"left peg"),
		(u"center peg", u"center peg"),
		(u"right peg", u"right peg"))

GEAR_COUNTER = (
	       (0, ("none placed")),
	       (1, ("1")),
	       (2, ("2")),
	       (3, ("3")),
	       (4, ("4")),
	       (5, ("5")),
	       (6, ("6")),
	       (7, ("7")),
	       (8, ("8")),
	       (9, ("9")),
	       (10,("10")),
	       (11,("11")))

ROBOT_SPEED = (
		(u'meh real slow', u'meh real slow'),
		(u'about average', u'about average'),
		(u'BOOLIN', u'BOOLIN'),
	)

PILOT_RATING = (
		(u'not present', u'not present'),
		(u'dropped every gear', u'dropped every gear'),
		(u'dropped 1-2 gears', u'dropped 1-2 gears'),
		(u'no gears dropped', u'no gears dropped')
	)

CLIMBER_SUCCESS = (
		(u'unfilled', u'unfilled'),
		(u'did not attempt', u'did not attempt'),
		(u'did not press button', u'did not press button'),
		(u'fell off rope', u'fell off rope'),
		(u'rope snapped', u'rope snapped'),
		(u'climbed successfully', u'climbed successfully')
	)

ALLIANCE_COLORS = (
		(u'Blue Alliance', u'Blue Alliance'),
		(u'Red Alliance', u'Red Alliance')
	)

WINNING_ALLIANCE = (
                (u'PLEASE SELECT THE WINNER', u'PLEASE SELECT THE WINNER'),
		(u'Blue Alliance', u'Blue Alliance'),
                (u'Red Alliance', u'Red Alliance'),
        )

