print("----------------------")
qty=int(input("enter the qty="))
rate=int(input("enter the rate="))
total=qty*rate
print("total",total)
dis=int(input("enter the dis="))
dis_value=(dis*total)/rate
print("dis_val",dis_value)
basic_total=total-dis_value
print("basic_total",basic_total)
gst=int(input("enter the gst"))
g=gst/100*1000
net_total=basic_total+g
print("net_total=",net_total)





