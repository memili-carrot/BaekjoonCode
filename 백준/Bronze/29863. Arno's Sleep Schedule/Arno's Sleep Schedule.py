sleep_time = int(input())
wake_time = int(input())
if wake_time >= sleep_time:
    sleep_duration = wake_time - sleep_time
else:
    sleep_duration = (24 - sleep_time) + wake_time
print(sleep_duration)