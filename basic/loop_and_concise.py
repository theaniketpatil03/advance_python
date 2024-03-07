
def loop_break_continue():
    for i in range(10):
        i += 1
        print(i)
        if i == 5:
            print('breaking the loop')
            break 
        if i % 2 == 0:
            # print('skipping loop and going forward')
            continue # it will skip the further code and continue to loop

        print('going forward')


def ternary_operator_concise_condition():
    x = 1

    result = 'even' if x % 2 == 0 else 'odd'

    print(result)

if __name__ == "__main__":

    # lloop_break_continue

    ternary_operator_concise_condition()