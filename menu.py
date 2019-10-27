import modules.arraydefiner
import glob

path = 'c:\\projects\\MCA\\pylib\\'

files = [f for f in glob.glob(path + "**/*.txt", recursive=True)]
        
increment = 0
for f in files:
    vars()["address" + str(increment)] = f
    vars()["newadd" + str(increment)] = vars()["address" + str(increment)].split('\\')
    vars()["newadd" + str(increment)] = vars()["newadd" + str(increment)][4].split('.')
    vars()["newadd" + str(increment)] = vars()["newadd" + str(increment)][0]
    increment += 1
print("Madus' Cryptographic Analyzer V0.01")
state = 0

while state == 0:
    data = input('')
    
    if (len(data) == 1 or len(data) == 2) and (0 <= int(data) <= 100):
        state = 1
        datachose = data
        with open(vars()["address" + str(data)],'r') as file:
            cripto = file.read()
            print("'help' to view commands")
    if data == "libs":
        newinc = 0
        for f in files:
            print('[' + str(newinc) + '] ' + vars()["newadd" + str(newinc)])


    while state == 1:
        data = input(str(vars()["newadd" + str(datachose)] + ":"))
        if data == "main":
            state = 0
        if data == "help":
            print("'main' return to main menu")
            print("'matX,Y' to display the string data as a matrix X by Y in size")    

        if data[0] == 'm' and data[1] == 'a' and data[2] == 't':
            foo  = data.split('t')
            baa = foo[1].split(',')
            cript_mat = modules.arraydefiner.matrix_from_text_string(cripto,baa[0],baa[1])
            for var in cript_mat:
                print(var)
            
