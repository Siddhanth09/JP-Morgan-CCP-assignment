#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

#Input Format
#The first line contains . The second line contains an array A[] of n integers each separated by a space.

#Constraints
#2 <= n <= 10
#-100 <= A[i] <= 100

#Output Format:
#Print the runner-up score

#Sample input:
#5
#2 3 6 6 5

#Output:
#5

#Explanation:
#Given list is [2,3,6,6,5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.

n = int(input())
ar = map(int, input().split())
ar=sorted(ar,reverse=True)
for i in range(len(ar)):
    if ar[i]==ar[0]:
            continue
    else:
            print(ar[i])  
            break
                    
