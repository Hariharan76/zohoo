# def func(word1,word2):
#     dp=[[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
#     # print(dp)
#     for i in range(len(word1)+1):
#         dp[i][0]=i
#     for j in range(len(word2)+1):
#         dp[0][j]=j
#     for i in range(1,len(word1)+1):
#         for j in range(1,len(word2)+1):
#             if word1[i-1] == word2[j-1]:
#                 dp[i][j]=dp[i-1][j-1]
#             else:
#                 dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+1)
#     return dp[len(word1)][len(word2)]

# word1="labrinth"
# word2="brilliant"
# iter=func(word1,word2)
# print("the iteration is :",iter)
a="Hariharan"
b="brilliant"
al=[i for i in a]
bl=[j for j in b]
count=0
for i in al:
    try:
        bl.remove(i)
        count+=1
    except:
        pass
print(bl)
    

