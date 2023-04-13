import socket

print("""         ##############################
         ##WHAT WOULD YOU LIKE TO DO?##
         ##############################""")
print("""
1. scan for ip with hostname-
2. scan for hostname with ip- 
""")

print("select the number")
action = input("\n>")
if action == "1" or 1:
    hostname = input("enter the hostname/website you want to scan for ip-\n>")
    ans = socket.gethostbyname(hostname)
    print(ans)