def interface():
    print("Blood Calculator")
    keep_running = True
    while keep_running:
        print("Make a Choice")
        print("1 - HDL Analysis")
        print("2 - LDL Analysis")
        print("9 - Quit")
        choice = int(input("Choose one: "))
        if choice == 9:
            keep_running = False
        elif choice == 1:
            HDL_Driver()
        elif choice == 2:
            LDL_Driver()
            
    print(choice)
    return choice

########## HDL ############
def HDL_Driver():
    HDL_value = hdl_input()
    message = hdl_analysis(HDL_value)
    hdl_output(message, HDL_value)

def hdl_input():
    hdl_value = int(input("Enter HDL Value: "))
    return hdl_value

def hdl_analysis(hdl_value):
    if hdl_value >= 60:
        return "Normal"
    elif 40 <= hdl_value < 60:
        return "Borderline Low"
    else:
        return "Low"
    
def hdl_output(text, value):
    print("Your HDL value is {}. It considered a {} value.".\
          format(value, text))
    return

########## LDL ##############
def LDL_Driver():
    LDL_value = ldl_input()
    message = ldl_analysis(LDL_value)
    ldl_output(message, LDL_value)

def ldl_input():
    ldl_value = int(input("Enter LDL Value: "))
    return ldl_value

def ldl_analysis(ldl_value):
    if ldl_value < 130:
        return "Normal"
    elif 130 <= ldl_value < 160:
        return "Borderline High"
    elif 160 <= ldl_value < 190:
        return "High"
    else:
        return "Very High"
    
def ldl_output(text, value):
    print("Your LDL value is {}. It considered a {} value.".\
          format(value, text))
    return

if __name__ == '__main__':
    interface()
