# import frontend.gui as gui
import backend.controller as ctl

def do_tests():
    print()
    print(60 * '=')
    print('|', end='')
    print("-- TEST 1 --".center(58), end='|\n')
    print('|', end='')
    print("- Simple communication -".center(58), end='|\n')
    print(60 * '=')
    
    t1 = ctl.Controller.test_simple_1()
    
    ctl.Controller.clear()
    
    print()
    print(60 * '=')
    print('|', end='')
    print("-- TEST 2 --".center(58), end='|\n')
    print('|', end='')
    print("- Broadcast packet -".center(58), end='|\n')
    print(60 * '=')
    
    t2 = ctl.Controller.test_broadcast()

    ctl.Controller.clear()

    print()
    print(60 * '=')
    print('|', end='')
    print("-- TEST 3 --".center(58), end='|\n')
    print('|', end='')
    print("- RIP Protocol -".center(58), end='|\n')
    print(60 * '=')
    
    t3 = ctl.Controller.test_rip()
    
    # ------------------------------------------------
    
    print('\n' + 40 * '*')
    print('RESULTS:')
    print('--------')
    
    T = [t1, t2, t3]
    for i, t in enumerate(T):
        if t:
            print(f'Test[{i+1}] : Passed!')
        else:
            print(f'Test[{i+1}] : Not Passed!')

def main():
    # app = gui.GUI()
    # app.run()
    do_tests()

if __name__ == '__main__':
    main()
