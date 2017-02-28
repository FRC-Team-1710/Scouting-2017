ACCURACY_CHOICES = (
		(0, ("did not attempt")),
		(1, ("poor accuracy")),
		(2, ("A few went in")),
		(3, ("Half went in")),
		(4, ("over half went in")),
		(5, ("100% accuracy")))

SPEED_CHOICES = (
                (0, ("did not attempt")),
                (1, ("<1 ball/sec")),
                (2, ("1 ball/sec")),
                (3, ("3 balls/sec")),
                (4, ("5+ balls/sec")),
                (5, ("faster than the speed of light")))

HOPPER_EFFICIENCY = (
                (0, ("did not attempt")),
                (1, ("less than 5 balls caught")),
                (2, ("Almost ten balls caught")),
                (3, ("over ten balls caught")),
                (4, ("only dropped a few")),
                (5, ("collected every single ball")))

GEAR_COUNTER = (
	       (0, ("none placed")),
	       (1, ("1")),
	       (2, ("2")),
	       (3, ("3")),
	       (4, ("4")),
	       (5, ("5")),
	       (6, ("6")),
	       (7, ("7")))

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
		(u'did not attempt', u'did not attempt'),
		(u'did not press button', u'did not press button'),
		(u'fell off rope', u'fell off rope'),
		(u'rope snapped', u'rope snapped'),
		(u'climbed successfully', u'climbed successfully')
	)
