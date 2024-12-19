def convert_cel_to_far(celsius):
    return celsius *9/5 + 32
def convert_far_to_cel(far):
    return (far - 32) * 5/9

a = float(input("Enter a temperature in degrees F: "))
b = round((convert_far_to_cel(a)), 2)
print(f"{a} degrees F = {b} degrees C")
c = float(input("Enter a temperature in degrees C: "))
d = round((convert_cel_to_far(c)), 2)
print(f"{c} degrees C = {d} degrees F")