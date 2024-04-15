print("10 Subject Marks")
m1=56
m2=39
m3=56
m4=34
m5=87
# Create a list of marks
marks = [m1, m2, m3, m4, m5]

# Sort the marks in descending order
marks.sort(reverse=True)

# Take the best three marks
best_three_marks = marks[:3]
print("10 Standard Marksheet")
print("1.Tamil   : ", m1, " | pass" if m1>=40 else " | Fail")
print("2.English : ", m2, " | pass" if m2>=40 else " | Fail")
print("3.Maths   : ", m3, " | pass" if m3>=40 else " | Fail")
print("4.Science : ", m4, " | pass" if m4>=40 else " | Fail")
print("5.Soc_Sci : ", m5, " | pass" if m5>=40 else " | Fail")

Total = sum(best_three_marks)
Avg10 = Total / 3  # Calculate the average of the best three marks
ori_avg=Avg10/2

print("Total of best three marks:", Total, "/300")
print("Average of best three marks:", Avg10)
print("Original Average:",ori_avg)

print("----------------------------------------------")

print("11 Standard Marks")
m11=56
m22=34
m33=87
m44=98
m55=38
m66=87
print("1.Tamil     : ", m11, " | pass" if m11>=40 else " | Fail")
print("2.English   : ", m22, " | pass" if m22>=40 else " | Fail")
print("3.Maths     : ", m33, " | pass" if m33>=40 else " | Fail")
print("4.Biology   : ", m44, " | pass" if m44>=40 else " | Fail")
print("5.Physics   : ", m55, " | pass" if m55>=40 else " | Fail")
print("5.Chemistry : ", m66, " | pass" if m66>=40 else " | Fail")
total=m11+m22+m33+m44+m55+m66
avg12=total/6
print("Total:",total,"/600")
print("Avg:{:.2f}".format(avg12))

print("-------------------------------------------------")
print("12 Standard Marks")

grees_mark=30
k1 = m11/100 * 20
k2 = m22/100 * 20
k3 = m33/100 * 20
k4 = m44/100 * 20
k5 = m55/100 * 20
k6 = m66/100 * 20
print("1.Tamil     : {:.2f}".format(ori_avg+k1+grees_mark), " | pass" if ori_avg+k1+grees_mark>=40 else " | Fail")
print("2.English   : {:.2f}".format(ori_avg+k2+grees_mark), " | pass" if ori_avg+k2+grees_mark>=40 else " | Fail")
print("3.Maths     : {:.2f}".format(ori_avg+k3+grees_mark), " | pass" if ori_avg+k3+grees_mark>=40 else " | Fail")
print("4.Biology   : {:.2f}".format(ori_avg+k4+grees_mark), " | pass" if ori_avg+k4+grees_mark>=40 else " | Fail")
print("5.Physics   : {:.2f}".format(ori_avg+k5+grees_mark), " | pass" if ori_avg+k5+grees_mark>=40 else " | Fail")
print("5.Chemistry : {:.2f}".format(ori_avg+k6+grees_mark), " | pass" if ori_avg+k6+grees_mark>=40 else " | Fail")
total= (ori_avg+k1+grees_mark)+( ori_avg+k2+grees_mark)+( ori_avg+k3+grees_mark)+( ori_avg+k4+grees_mark)+( ori_avg+k5+grees_mark)+( ori_avg+k6+grees_mark)
Avg=total/6
print("Total:{:.2f}".format(total),"/600")
print("Average:",Avg)