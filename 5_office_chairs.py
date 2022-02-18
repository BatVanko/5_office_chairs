num_of_rooms = int(input())
free_chairs_left = 0
no_need_chairs = True

for i in range (1, num_of_rooms +1):
    free_chairs, visitors = input().split(" ")
    free_chairs = len(free_chairs)
    visitors = int(visitors)
    difference = free_chairs - int(visitors)
    if difference > 0:
        free_chairs_left += difference

    elif difference < 0:
        print(f"{abs(difference)} more chairs needed in room {i}")
        no_need_chairs = False
if no_need_chairs:
    print(f"Game On, {free_chairs_left} free chairs left")



