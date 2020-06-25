from day05_list.class_random import class_random

if __name__ == '__main__':
    names = class_random.Random_name(3)
    print(names.name)
    result = class_random.Random_result(50, 100, 5)
    print(result.one_repetition_result)
    print(result.one_distinc_result)




