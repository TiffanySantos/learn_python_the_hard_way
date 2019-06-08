print "How old are you?", #comma at the end so print doesn't end the line with a new line character and go to the next line
age = raw_input ()
print "How tall are you?",
height = raw_input ()
print "How much do you weigh?",
weight = raw_input ()

print "So your're %r old, %r tall and %r heavy." % (age, height, weight)