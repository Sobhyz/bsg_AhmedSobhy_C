import statistics as st
nums=[]
for i in range(3):
    x=eval(input("enter a number: "))
    nums.append(x)
print(f"the sum is {sum(nums)}")
print(f"the avg is {st.mean(nums)}")