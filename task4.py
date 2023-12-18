# def generate_parentheses(n):
#     if n == 0:
#         return [""]

#     stack = [(0, 0, "")]
#     result = []
    

#     while stack:
#         print(stack)
#         opened, closed, current = stack.pop()
#         # print(opened)
#         # print(closed)
#         # print(current)

#         if opened < n:
#             stack.append((opened + 1, closed, current + "("))

#         if closed < opened:
#             stack.append((opened, closed + 1, current + ")"))

#         if opened == n and closed == n:            
#             result.append(current)
#             print("this is a output",result)

#     return result

# n = int(input("Enter the number: "))
# final = generate_parentheses(n)
# # print("this is final output",final)

def func(n):
    if n == 0:
        return [ ""]
    state=[(0,0,"")]
    result=[]
    while state:
        openend,closed,current=state.pop()
        if openend < n:
            state.append((openend+1,closed,current+"{" ))
        if closed < openend:
            state.append((openend,closed+1,current+"}" ))
        if openend==n and closed ==n :
            result.append(current)
    return result
n=int(input("Enter the input :"))
a=func(n)
print(a)