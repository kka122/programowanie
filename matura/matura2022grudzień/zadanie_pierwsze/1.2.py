with open("mecz_przyklad.txt", "r")as f:
    wszystko=f.read()
count_a=0
count_b=0
for i in wszystko:
    if i =="A":
        count_a+=1
    elif i =="B":
        count_b+=1
    if (count_b >= 1000 or count_a >=1000) and abs(count_a-count_b)>=3 :
        print(count_a,count_b)
        break