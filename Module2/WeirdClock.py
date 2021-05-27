hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
newMin = (mins + dura) % 60
newHour = (hour + int((mins+dura)/60)) % 24
print("Ending time: ", newHour, ":", newMin, sep="")
