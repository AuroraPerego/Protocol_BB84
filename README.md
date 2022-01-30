# Protocol_BB84
Some python scripts to implement the quantum cryptography protocol developed by Bennett and Brassard in 1984.

The goal of the protocol is to send secure information. The sender is Alice, the receiver is Bob and Eve is the eavesdropper.

Both Alice and Bob choose the basis in which perform the measurement between the computational basis (0,1) and the hadamard basis (+,-). 
Alice measures the qubit and sends it to Bob, who in turn measures it.
Then they compare the basis chosen and if they are not the same the result is discharged. If on the other hand the basis are the same, they obtain the same result. This last statement is true unless a third part, Eve in our case, is listening. The only way Eve has to know what Alice is sending is to measure the qubit, but by doing this there is a 25% possibility to alter the qubit state. In the end, when Bob and Alice compare the outcome of the measurement they will obtain different results and will be able to conclude that someone is listening!

In **`BB84.py`** the process is realized classically, considering a probability of 50% for the basis choice and for the measurement outcome.
In **`BB84_quantum.py`** a quantum circuit is used to measure the qubit in the basis chosen. To run this code the *qiskit* library is required.
**`BB84_quantum.ipynb`** is a jupyter notebook file useful to visualize the circuit implemented for the measurements and the results.

It's possible to vary the number of qubit exchanged and to choose whether or not to eavesdrop the conversation.
