import modules.arraydefiner
import modules.rotation
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
#main state
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

    #data setup state
    while state == 1:
        data = input(str(vars()["newadd" + str(datachose)] + ":"))
        if data == "main":
            state = 0
        if data == "help":
            print("'main' return to main menu")
            print("'matX,Y' to display the string data as a matrix X by Y in size")
            print("'string' display the data in string format")
        if data[0] == "a" and data[1] == "r" and data[2] == "r":
            dataup = data.split('r')
            cript_arr = modules.arraydefiner.array_from_text_string(cripto,dataup[2])
            print(cript_arr)
            state = 4
        if data[0] == 's' and data[1] == 't' and data[2] == 'r' and data[3] == 'i' and data[4] == 'n' and data[5] == 'g':
            print(cripto)
            state = 3
        if data[0] == 'm' and data[1] == 'a' and data[2] == 't':
            foo  = data.split('t')
            baa = foo[1].split(',')
            global cript_mat
            cript_mat = modules.arraydefiner.matrix_from_text_string(cripto,baa[0],baa[1])
            for var in cript_mat:
                print(var)

            #matrix for preservation
            master_mat = cript_mat
            #matrix for editing
            edit_mat = cript_mat
            #matrix for undo
            temp_mat = cript_mat
            state = 2
        
            #matrix editing state
        while state == 2:
            data = input(str(vars()["newadd" + str(datachose)] + "/" + "matrix:"))
            if data == "help":
                print("//'back' to go back")
                print("//'main' to return to main menu")
                print("//'undo' to return to previous matrix state")
                print("//'undoall' to return to initial matrix")
                print("//'rot90' to rotate matrix 90 degrees")
                print("//'rot180' to rotate matrix 180 degrees")
                print("//'rot270' to rotate matrix 270 degrees")
            if data == "back":
                state = 1
            if data == "main":
                state = 0
            if data == "undo":
                edit_mat = temp_mat
                for var in edit_mat:
                    print(var)
            #reset matrix to original state
            if data == "undoall":
                edit_mat = master_mat
                for var in edit_mat:
                    print(var)
            if data[0] == 'g' and data[1] == 'r' and data[2] == 'i' and data[3] == 'd':
                pre_var = data.split('d')
                pos_var = pre_var[1].split(',')
                lengthGrid = int(pos_var[0]) + int(pos_var[2])
                heightGrid = int(pos_var[1]) + int(pos_var[3])
                if len(edit_mat) >= heightGrid and len(edit_mat[0]) >= lengthGrid:
                    temp_mat = edit_mat
                    edit_mat = modules.rotation.matrix_To_Grid(edit_mat,pos_var[0],pos_var[1],pos_var[2],pos_var[3])
                    for x in edit_mat:
                        print(x)
                else:
                    print("grid would be too large")
            
            if data == "rot90":
                temp_mat = edit_mat
                edit_mat = modules.rotation.rot90(edit_mat)
                for x in edit_mat:
                    print(x)
            if data == "rot180":
                temp_mat = edit_mat
                edit_mat = modules.rotation.rot90(edit_mat)
                edit_mat = modules.rotation.rot90(edit_mat)
                for x in edit_mat:
                    print(x)
            if data == "rot270":
                temp_mat = edit_mat
                edit_mat = modules.rotation.rot90(edit_mat)
                edit_mat = modules.rotation.rot90(edit_mat)
                edit_mat = modules.rotation.rot90(edit_mat)
                for x in edit_mat:
                    print(x)
            if data == "fliph":
                temp_mat = edit_mat
                edit_mat = modules.rotation.fliphorizontal(edit_mat)
                for x in edit_mat:
                    print(x)
            if data == "flipv":
                temp_mat = edit_mat
                edit_mat = modules.rotation.flipvertical(edit_mat)
                for x in edit_mat:
                    print(x)
            if data == "test":
                for x in edit_mat:
                    print(x)
            else:
                continue
        #string analysis state
        while state == 3:
            data = input(str(vars()["newadd" + str(datachose)] + "/" + "string:"))
            master_string = cripto
            edit_string = cripto
            temp_string = cripto
            if data == "back":
                state = 1
            if data == "main":
                state = 0
            if data == "undo":
                edit_string = temp_string
                print(master_string)
            if data == "undoall":
                edit_string = master_string
                print(master_string)
            else:
                continue
        while state == 4:
            data = data = input(str(vars()["newadd" + str(datachose)] + "/" + "array:"))
            master_arr = cript_arr
            edit_arr = cript_arr
            temp_arr = cript_arr
            if data == "back":
                state = 1
            if data == "main":
                state = 0
            if data == "undo":
                edit_arr = temp_arr
                print(edit_arr)
            if data == "undoall":
                edit_arr = master_arr
            else:
                continue
    else:
        continue
