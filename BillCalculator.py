'''Simple Bill Calculator
Author: Thanh Duy Quach
Description: Calculate total bill with tax, tip, and split option'''

def cal_total(subtotal, final_taxes, final_tips):
    return subtotal + final_tips + final_taxes

def shared_total(total1, people):
    return total1 / people

def head():
    return "*****************\n     BILL\n*****************"

def print_bill(subtotal, taxes, final_taxes, tips, final_tips, total1, people=None, total2=None):
    print(head())
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax({taxes}%): ${final_taxes:.2f}")
    print(f"Tips({tips}%): ${final_tips:.2f}")
    if people is not None and total2 is not None:
        print(f"Number of people: {people}")
        print(f"Total: ${total1:.2f}")
        print(f"Each person pays: ${total2:.2f}")
    else:
        print(f"Total: ${total1:.2f}")
    
def main():
    print("====WELCOME TO BILL CALCULATOR====")
    subtotal = float(input("Please enter subtotal: $"))
    while True:
        taxes = float(input("Please enter tax percentage: "))
        if 0 <= taxes <= 100:
            break
        print("Invalid tax percentage! Please enter again!")
    tips = float(input("Please enter tip percentage: "))
    final_taxes = (taxes / 100) * subtotal
    final_tips = (tips / 100) * subtotal
    total1 = cal_total(subtotal, final_tips, final_taxes)
    
    while True:
        ask = input("Do you want to split bill? (Yes/No): ").lower()
        if ask == "yes" or ask == "no":
            break
        print("Invalid answer! Please enter again!")    
    if ask == "yes":
        while True:
            people = int(input("Please enter the amount of people: "))
            if people > 0:
                break
            print("Invalid number of people! Please enter again!")
        total2 = shared_total(total1, people)
        print_bill(subtotal, taxes, final_taxes, tips, final_tips, total1, people, total2)
        
    elif ask == "no":   
        print_bill(subtotal, taxes, final_taxes, tips, final_tips, total1)
               
    print("Thank you for using our service")
    print("   Have a nice one!")
    

if __name__=="__main__":
    main()
