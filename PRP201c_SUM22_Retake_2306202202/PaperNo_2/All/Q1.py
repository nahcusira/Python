try:
    num = input("Enter a number: ")
    if int(num) <= 0:
        print("The number must be a positive.")
    else:
        print("Maximum is: "+ str(max(num)))
        print("Minimum is: " + str(min(num)))
except:
    print("The number must be a positive.")
