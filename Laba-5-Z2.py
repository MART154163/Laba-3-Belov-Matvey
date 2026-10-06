N = int (input('введение кол числ N:'))
ng = []
pos = []
print(f"введите {N}")
for i in range(N):
    num = int(input(f"числ{i + 1}:"))
    if num < 0:
        ng.append(num)
    elif num >0:
        pos.append(num)
max_abs_ng = max(ng,key=abs)
min_abs_pos = min (pos)
diff = max=abs_neg - min_abs_pos
print(f'{ng}')
print(f'{pos}')
print(f'{max_abs_ng}: {abs(max_abs_ng)}')
print(f'{max_abs_ng} - {min_abs_pos} = {diff}') 

