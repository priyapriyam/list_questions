char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
a_new=[]
n_new=[]
t_new=[]
x_new=[]
u_new=[]
g_new=[]
while i < len(char_list):
    if (char_list[i]) =="a":
        a_new.append(char_list[i])
    elif (char_list[i]) == "n":
        n_new.append(char_list[i])
    elif (char_list[i]) == "t":
        t_new.append(char_list[i])
    elif (char_list[i]) == "x":
        x_new.append(char_list[i])
    elif (char_list[i]) == "u":
        u_new.append(char_list[i])
    else:
        g_new.append(char_list[i])
    i=i+1
print [["a", len(a_new),"n",len(n_new),"t",len(t_new),"x",len(x_new),"u",len(u_new),"g",len(g_new)]]
a=1
while a < len(a_new):
    a=a+1
print "a","-",a,"times"
n=1
while n < len(n_new):
    n=n+1
print "n","-",n,"times"
t=1
while t < len(t_new):
    t=t+1
print "t","-",t,"times"
x=1
while x < len(x_new):
    x=x+1
print "x","-",x,"times"
u=1
while u < len(u_new):
    u=x+1
print "u","-",u,"times"
g=1
while g < len(g_new):
    g=g+1
print "g","-",g,"times"