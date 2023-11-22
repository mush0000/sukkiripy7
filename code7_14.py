#7-4
#(1)
# print("数値を比較します")
# num1 = int(input("1番目の数値を比較します>>"))
# num2 = int(input("2番目の数値を比較します>>"))
# num3 = int(input("3番目の数値を比較します>>"))
# print("入力された数値の中で一番大きいのは" + max(num1,num2,num3) +"です")
nums = list()
for n in range(3):
    data = int(input("{}個目の整数を入力してください>>".format(n +1)))
    nums.append(data)
print(max(nums))


#(2)
from math import*
# print(pi)
# print((ceil(pi)))
pi = 3.141519
print(round(pi))
for n in range(4):
    print(round(pi,n+1))
