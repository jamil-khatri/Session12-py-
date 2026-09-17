durations = input("Enter song durations in minutes: ").split(",")
durations = list(map(float, durations))
seconds = list(map(lambda minutes: minutes * 60, durations))

print("Durations in seconds:", seconds)
