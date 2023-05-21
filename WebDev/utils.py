def common_function():
    # Your common function logic here
    return "Common Function Result"


def checkUser(request, Username, PassCode)
    item ={
        "username" : "admin",
        "password" : "admin123"
    }
    if Username == item.username:
        if PassCode == item.password:
            permissionForLogin = True
        else:
            permissionForLogin = False;
    else:
        permissionForLogin=False;
    return permissionForLogin