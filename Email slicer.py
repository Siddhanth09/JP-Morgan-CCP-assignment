
#Email slicer - Collect an email address from the user and then find out if the user has a custom domain name or a popular domain name. For example:

#Input: mary.jane@gmail.com
#Output: Hey Mary, I see your email is registered with Google. That's cool!.
#Input: peter.pan@myfantasy.com
#Output: Hey Peter, looks like you've got your own custom setup at MyFantasy. Impressive!.


x=str(input("enter your email id \n"))
y='@gmail.com'
if y in x:
 print("Hey %s, I see your email is registered with Google. That's cool!."% x)
else:
    print("Hey %s, looks like you've got your own custom setup at MyFantasy. Impressive!."%x)
    
