seats = [34, 108, 145, 150, 211, 309]
n = len(seats)
target = 108

print('===Train Seat Finder===')
print(f"Available Seats: {seats}\nTarget: {target}")
print()

lo = 0
hi = n-1
step = 0
while lo <= hi:
    mid = (lo+hi)//2
    step += 1
    if seats[mid] == target:
        print(f"Binary Search: index = {mid}\nsteps = {step}") 
        break
    elif seats[mid]<target:
        lo = mid+1
    else:
        hi = mid-1
print()

def recur_search(seat, lo, hi, target, call=0):
    call += 1
    if lo < hi:
        return 1,call
    mid = (lo+hi)//2
    if seats[mid]==target:
        return mid,call
    elif seat[mid]<target:
        return recur_search(seat, mid+1, hi, target, call)
    else:
        return recur_search(seat, lo, mid-1, target, call)
    
result,call = recur_search(seats, 0, n-1, target)
print(f"Recursive Binary Search: index = {result}\nsteps = {call}") 
print()