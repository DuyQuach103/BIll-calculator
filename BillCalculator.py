import stdio 

def cal_total(subtotal, final_taxes, final_tips):
    return subtotal + final_tips + final_taxes

def shared_total(total1, people):
    return total1 / people

def head():
    return "*****************\n     BILL\n*****************"

def print_bill(subtotal, taxes, final_taxes, tips, final_tips, total1, people=None, total2=None):
    stdio.writeln(head())
    stdio.writef("Subtotal: $%.2f\n", subtotal)
    stdio.writef("Tax(%.1f%%): $%.2f\n", taxes, final_taxes)
    stdio.writef("Tips(%.1f%%): $%.2f\n", tips, final_tips)
    if people is not None and total2 is not None:
        stdio.writeln("Number of people: " + str(people))
        stdio.writef("Total: $%.2f\n", total1)
        stdio.writef("Each person pays: $%.2f\n", total2)
    else:
        stdio.writef("Total: $%.2f\n", total1)
    
def main():
    stdio.writeln("====WELCOME TO BILL CALCULATOR====")
    subtotal = float(input("Please enter subtotal: $"))
    while True:
        taxes = float(input("Please enter tax percentage: "))
        if 0 <= taxes <= 100:
            break
        stdio.writeln("Invalid tax percentage! Please enter again!")
    tips = float(input("Please enter tip percentage: "))
    final_taxes = (taxes / 100) * subtotal
    final_tips = (tips / 100) * subtotal
    total1 = cal_total(subtotal, final_tips, final_taxes)
    
    while True:
        ask = input("Do you want to split bill? (Yes/No): ").lower()
        if ask == "yes" or ask == "no":
            break
        stdio.writeln("Invalid answer! Please enter again!")    
    if ask == "yes":
        while True:
            people = int(input("Please enter the amount of people: "))
            if people > 0:
                break
            stdio.writeln("Invalid number of people! Please enter again")
        total2 = shared_total(total1, people)
        print_bill(subtotal, taxes, final_taxes, tips, final_tips, total1, people, total2)
        
    elif ask == "no":   
        print_bill(subtotal, taxes, final_taxes, tips, final_tips, total1)
               
    stdio.writeln("Thank you for using our service")
    stdio.writeln("   Have a nice one!")
    

if __name__=="__main__":
    main()
