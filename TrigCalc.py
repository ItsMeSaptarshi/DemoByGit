import math

def trig_values(degrees):
    radians = math.radians(degrees)
    sine = math.sin(radians)
    cosine = math.cos(radians)
    tangent = math.tan(radians)
    return sine, cosine, tangent

angle_degrees = float(input("Enter angle in degrees: "))

sine, cosine, tangent = trig_values(angle_degrees)

print("Sine:", sine)
print("Cosine:", cosine)
print("Tangent:", tangent)
print("bye!:)I'll cya tmrw!!:P")
