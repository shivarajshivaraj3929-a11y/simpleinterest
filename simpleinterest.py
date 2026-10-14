def simple_interest(principal,interest,time)
    return(principal*interest*time)/100

if __name__ == "__main__":
    p=int(input("Enter principal amt"))
    i=float(input("Enter interest"))
    t=int(input("Enter time in months"))

    print("simple interest is:",simple_interest(p,i,t))