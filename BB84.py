import random
import numpy as np

n_qubits = 100
eve_is_listening = False

def gate_choice(): 
    list = np.zeros((2, n_qubits))
    for i in range(0, n_qubits):
        basis = random.randint(0,1)
        list[0][i] = 0 if basis == 0 else 1
    return list

def measure(list: np.ndarray): 
    for i in range(0, n_qubits):
        meas = random.randint(0,1)
        list[1][i] = 0 if meas == 0 else 1
    return list

def compare(a_list: np.ndarray, b_list: np.ndarray):
    if len(a_list[0]) != len(b_list[0]):
        print("The lists must have the same length")
        return 0
    for i in range(0, len(a_list[0])):
        if a_list[0][i] == b_list[0][i]:
            b_list[1][i] = a_list[1][i]
        else: #useless
            meas = random.randint(0,1)
            b_list[1][i] = 0 if meas == 0 else 1
    return a_list, b_list

def eavesdrop(a_list: np.ndarray, e_list: np.ndarray):
    if len(a_list[0]) != len(e_list[0]):
        print("The lists must have the same length")
        return 0
    for i in range(0, len(a_list[0])):
        if a_list[0][i] != e_list[0][i]:
            a_list[1][i] = e_list[1][i]
    return a_list

def check(a_list: np.ndarray, b_list: np.ndarray):
    S = [] #codepad
    if len(a_list[0]) != len(b_list[0]):
        print("The lists must have the same length")
        return 0
    for i in range(0, len(a_list[0])):
        if a_list[0][i] == b_list[0][i]:
            if a_list[1][i] == b_list[1][i]:
                S.append(int(b_list[1][i]))
            else:
                print("Be careful! Someone is listening to your conversation.")
                return True
    print("\nThe codepad is: ", S)
    return True

Alice_list = gate_choice()
Bob_list = gate_choice()
Eve_list = gate_choice()

Alice_list = measure(Alice_list)
Alice_list, Bob_list = compare(Alice_list, Bob_list)

Eve_list = measure(Eve_list)

if eve_is_listening:
    Alice:list = eavesdrop(Alice_list, Eve_list)

check(Alice_list, Bob_list)

#print("Alice list is:\n", Alice_list)
#print("\nBob list is:\n", Bob_list)
