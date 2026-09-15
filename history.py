history = []

history.append("Google")
history.append("Youtube")
history.append("Instagram")

print("current history:", history)

if len(history) >1:
    history.pop()
    print("Went back to:", history[-1])
else:
    print("No previous page")

print("History:", history)        