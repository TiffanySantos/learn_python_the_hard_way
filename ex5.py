name = 'Zed A. Shaw'
age = 35 # not a lie
height_inch = 74 # inches
height_cm = height_inch * round(2.45)
weight_lbs = 180 # lbs
weight_kg = weight_lbs * float(0.45)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall, or rather %d centimetres in total." % (height_inch, height_cm)
print "He's %d pounds heavy." % weight_lbs
print "Actually that's not too heavy. That's only %d kilograms" % weight_kg
print "He's got %s eyes and %s hair." % (eyes, hair)
print "This teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height_inch, weight_lbs, age + height_inch + weight_lbs)
