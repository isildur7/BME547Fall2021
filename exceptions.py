def generates_error():
    try:
        b = "adgh" + 5
    except TypeError:
        b = "adgh" + str(5)
        
    return b

def main():
    a = generates_error()
    print(a)

if __name__ == "__main__":
    main()
