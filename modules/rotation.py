def rot90(matrixinput):
    lines = len(matrixinput[0])

    #create the matrix lines variables
    for x in range(0,lines):
        vars()["line" + str(x)] = ["0"] * len(matrixinput)
    start = 0
    collumn = int(len(matrixinput)) - 1
    for lin in range(0,lines):
        for y in range(0,len(matrixinput)):
            vars()["line" + str(lin)][y] = matrixinput[collumn][start]
            collumn -= 1
        start += 1
        collumn = int(len(matrixinput)) - 1

    global matrixoutput
    matrixoutput = ["0"] * lines
    for z in range(0,lines):
        matrixoutput[z] = vars()["line" + str(z)]

    return(matrixoutput)

def fliphorizontal(matrixinput):
    length = len(matrixinput[0])
    height = len(matrixinput)
    mat_arr_pos = len(matrixinput[0]) - 1

    for x in range(0,height):
        vars()["linef" + str(x)] = ["0"] * length

    for i in range(0,height):
        for x in range(0,length):
            vars()["linef" + str(i)][x] = matrixinput[i][mat_arr_pos]
            mat_arr_pos -= 1
        mat_arr_pos = len(matrixinput[0]) - 1


    global flip_mat_output
    flip_mat_output = ['0'] * height

    for var in range(0,height):
        flip_mat_output[var] = vars()["linef" + str(var)] 

    return(flip_mat_output)

def flipvertical(matrixinput):
    length = len(matrixinput[0])
    height = len(matrixinput)
    mat_arr_pos = len(matrixinput[0]) -1
    mat_arr_posS = len(matrixinput) - 1
    
    for x in range(0,height):
        vars()["linef" + str(x)] = ["0"] * length

    for i in range(0,height):
        for x in range(0,length):
           vars()["linef" + str(i)][x] =  matrixinput[mat_arr_posS][x]
        mat_arr_posS -= 1
 

    global vflip_mat_output
    vflip_mat_output = ['0'] * height

    for z in range(0,height):
        vflip_mat_output[z] = vars()["linef" + str(z)] 

    return(vflip_mat_output)
