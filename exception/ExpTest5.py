def validate(username):
    if(len(username)<6):
        raise RuntimeError("Invalid length")
    else:
        print("Valid username")
    print("Complete...")
    return

try:
    validate(input("username required: "))
    print("Thankyou...")
except RuntimeError as e :
    print("validation failure", e)

