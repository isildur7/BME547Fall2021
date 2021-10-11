import logging


def fibonacci(input_list):
    next_entry = input_list[-2] + input_list[-1]
    input_list.append(next_entry)
    logging.info("this iteration is: {}".format(input_list))
    if next_entry <= 100:
        fibonacci(input_list)
    else:
        logging.warning("This is the last iteration.")


if __name__ == '__main__':
    logging.basicConfig(filename = "fibonacci.log", filemode ='w',
                        level=logging.INFO)
    start_list = [0,1]
    fibonacci(start_list)
