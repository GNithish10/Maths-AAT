f1=open("Bubble-Out.txt", "r")
f2=open("Merge-Out.txt", "r")

n1=100
n2=100
sum1=0
sum2=0
square1=0
square2=0

bubble_lines = f1.readlines()
for i in bubble_lines:
    x=float(i)
    sum1+=x
    square1+=x**2

x_1=sum1/(n1-1)

popvar1=(square1/n1) - (sum1/n1)**2

merge_lines = f2.readlines()
for i in merge_lines:
    x=float(i)
    sum2+=x
    square2+=x**2

x_2=sum2/(n2-1)

popvar2=(square2/n2) - (sum2/n2)**2

Z=(x_1-x_2)/(((popvar1/n1)+(popvar2/n2))**0.5)  

print("Z-score:", Z)

Zt5=1.966
Zt1=2.58

if abs(Z) > Zt5:
    print("The difference between the two algorithms is statistically significant at 5% level of significance.\nHence, Null Hypothesis at 5% LOS is Rejected.")
else:
    print("The difference between the two algorithms is not statistically significant at 5% level of significance.\nHence, Null Hypothesis at 5% LOS is Accepted.")
if abs(Z) > Zt1:
    print("The difference between the two algorithms is statistically significant at 1% level of significance.\nHence, Null Hypothesis at 1% LOS is Rejected.")
else:
    print("The difference between the two algorithms is not statistically significant at 1% level of significance.\nHence, Null Hypothesis at 1% LOS is Accepted.")