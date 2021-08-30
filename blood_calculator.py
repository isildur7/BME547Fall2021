def interface():
    print("Blood Calculator")
    keep_running = True
    while keep_running:
        print("Make a Choice")
        print("1 - HDL Analysis")
        print("9 - Quit")
        choice = int(input("Choose one: "))
        if choice == 9:
            keep_running = False
        elif choice == 1:
            HDL_Driver()
            
    print(choice)
    return choice

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

interface()
