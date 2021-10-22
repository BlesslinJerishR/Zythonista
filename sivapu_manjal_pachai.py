secs = 60 * 60 + 1
green = list(blink for blink in range(30,secs,30))
red   = list(blink for blink in range(40,secs,40))

# print(green)
# print(red)

# Driver for Blinking Together
blinks = green + red
# print(blinks)
# Both blinks @ 120s - 1x in 2M
coincide_g = list(blink for blink in green[::3])
coincide_r = list(blink for blink in red[::2])

# Removing 0th Index
coincide_g.pop(0)
coincide_r.pop(0)

# Coincide Points
# print(coincide_g)
# print(coincide_r)

# Coincides @
coincide = int(60 / 2)
print("Both the lights coincide for ", coincide, " times in 1 Hour.")
# or
# coincide_alpha = 3600 / 120

