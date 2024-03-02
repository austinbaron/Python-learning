value = 2_000
try:
    if value > 1_000:
          
        # raise the ValueError
        raise ValueError("Please add a value lower than 1,000")
    else:
        print("Congratulations! You are the winner!!")
              
# if false then raise the value error
except ValueError as e:
        print("error occured", e)