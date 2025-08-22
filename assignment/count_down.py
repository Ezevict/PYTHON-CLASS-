import time

print("=== COUNTDOWN TIMER ===")
print("Countdown from 10 to 1")

count = 10
while count > 0:
    print(f"{count}")
    time.sleep(1) #Pause the time for 1 seconds
    count -= 1

print("BOOOOMMMM!!!")    