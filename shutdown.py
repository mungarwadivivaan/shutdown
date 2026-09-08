n=input("enter yes or no if you want to shutdown the sytem")
def shutdown(n):
    if n=="yes":
        msg="shutting down"
        return msg
    else:
        if n=="no":
            msg="abord shuting down"
            return msg
        else:
            print("sorry")
print(shutdown(n))