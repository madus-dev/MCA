
def matrix_from_text_string(cript,x,y):
    global cript_mat
    cript_mat = [0] * int(y)
    zero = 0
    mat_zero = 0
    for height in range(0,int(y)):
        vars()["criptl" + str(height)] = [0] * int(x)
        for length in range(0,int(x)):
            vars()["criptl" + str(height)][length] = cript[zero]
            zero += 1
    for val in cript_mat:
        cript_mat[mat_zero] = vars()["criptl" + str(mat_zero)]
        mat_zero += 1
    return (cript_mat)

def array_from_text_string(cript,num):
    array = [0] * int(num)
    for x in range(0,int(num)):
        array[x] = cript[x]

    return(array)
