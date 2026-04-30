giaTriTruoc = 0
thoaManYeuCau = True

while True:
    x = int(input())
    if x == 0:
        break
    
    if x < giaTriTruoc:
        thoaManYeuCau = False
    
    giaTriTruoc = x

if thoaManYeuCau:
    print("YES")
else:
    print("NO")