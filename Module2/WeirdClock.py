import math
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
added_time = mins + dura
end_time = added_time % 60
hour_count = math.ceil((dura / 60) % 60)
if added_time > 60:
    hour += hour_count

print((hour % 24), ":", end_time)
