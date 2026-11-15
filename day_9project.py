print("Welcome to the secret auction program")
bidders={}
name=input("What is your name?: \n")
amount=int(input("What is your bid?: \n"))
netx_person=input("Are there any other bidders: Type 'yes'or 'no'")
bidders[name]=amount
print(bidders)
if netx_person=="yes":
    maximum_value=0
    clear()
    name=input("What is your name?: \n")
    amount=int(input("What is your bid?: \n"))
    bidders[name]=amount
    netx_person=input("Are there any other bidders: Type 'yes'or 'no'")
    for names in bidders:
        int_amount=bidders[name]
        if int_amount>maximum_value:
            maximum_value=int_amount
    print(f"The winner is {name} with a bid of{maximum_value}")
        