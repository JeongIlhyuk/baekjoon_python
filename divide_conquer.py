s = int(input())
paper_arr=[list(map(int,input().split())) for _ in range(s)]

w_count = 0
b_count = 0
def divide(arr):
    global w_count, b_count
    l = len(arr)

    first = arr[0][0]
    is_same = True
    for i in range(l):
        for j in range(l):
            if arr[i][j] != first:
                is_same=False
                break
        if not is_same:
            break
    if is_same:
        if arr[0][0] ==0:#하양
            w_count+=1
        else:
            b_count+=1
        return

    half = l//2
    for i in [0,half]:
        for j in [0,half]:
            sub_arr = [row[j:j+half] for row in arr[i:i+half]]
            divide(sub_arr)


divide(paper_arr)
print(w_count)
print(b_count)