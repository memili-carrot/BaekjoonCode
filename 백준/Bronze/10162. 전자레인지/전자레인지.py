seconds = int(input())

button_times = [5 * 60, 60, 10]
button_click_list = [0] * 3

for i, time in enumerate(button_times):
    button_click_list[i] += seconds // time
    seconds %= time
    
if seconds != 0:
    print(-1)
else:
    for click in button_click_list:
        print(click, end=" ")