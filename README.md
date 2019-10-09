# cpsc474-project1
## Lamport's Logical Clocks 
Conceptual Implementation of Lamport's Logical Clocks using string matrices.

Contributors: Stacey Frasier, Nino Vilagi

### Notes for Usage
1. The program asks the user for the following:
   1. The file path of the input file for testing (ex: ./ex1.txt)
   2. Name of the output file the results will be written to (ex: out1.txt) *Note: If the file D.N.E it will create one. If the file exists the output will be appended to the file* 
2. Events within a process should be separated by a _space_. Each process should be separated by an endline (_enter_).
3. To test each algorithm, please use the following lines of code within the current directory of this project:
    --> calculate algorithm:
        ` python3 project1_calculate.py `
    --> verify algorithm
       ` python3 project1_verify.py `
4. If the output is incorrect within the _verify_ algorithm, the result will only display in terminal.
5. We have included one _.txt_ file per example provided in the _Project 1 Outline_