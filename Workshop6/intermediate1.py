color = {"Aliceblue" : "#f0f8ff", "Antiquewhite" : "#faebd7", "Antiquewhite1" : "#ffefdb", "Antiquewhite2" : "#eedfcc", "Antiquewhite3" : "#cdc0b0", "Antiquewhite4" : "#8b8378", "Aquamarine1" : "#7fffd4","Aquamarine2": "#76eec6", "Aquamarine4" : "#458b74", "Azure1" : "#f0ffff"}
color_name = input("Enter the color name : ").capitalize()

for key, value in color.items():
    if color_name == key:
        print(value)
if color_name not in color:
        print("No hexadecimal color code detected.")