import webbrowser
import time

total_breaks = 3
break_count  = 0

print(f"This program started at {time.ctime()}")
while break_count<total_breaks:
    time.sleep(.5*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=xLFqFP4ZdJE")
    print(f"Video played at {time.ctime()}")
    break_count+=1
