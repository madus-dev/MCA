
string340 = "HER>pl^VPk|1LTG2dNp+B(#O%DWY.<*Kf)By:cM+UZGW()L#zHJSpp7^l8*V3pO++RK2_9M+ztjd|5FP+&4k/p8R^FlO-*dCkF>2D(#5+Kq%;2UcXGV.zL|(G2Jfj#O+_NYz+@L9d<M+b+ZR2FBcyA64K-zlUV+^J+Op7<FBy-U+R/5tE|DYBpbTMKO2<clRJ|*5T4M.+&BFz69Sy#+N|5FBc(;8RlGFN^f524b.cV4t++yBX1*:49CE>VUZ5-+|c.3zBK(Op^.fMqG2RcT+L16C<+FlWB|)L++)WCzWcPOSHT/()p|FkdW<7tB_YOB*-Cc>MDHNpkSzZO8A|K;+"
arr340 = [0] * 340
arr340l1 = [0] * 17
arr340l2 = [0] * 17
arr340l3 = [0] * 17
arr340l4 = [0] * 17
arr340l5 = [0] * 17
arr340l6 = [0] * 17
arr340l7 = [0] * 17
arr340l8 = [0] * 17
arr340l9 = [0] * 17
arr340l10 = [0] * 17
arr340l11 = [0] * 17
arr340l12 = [0] * 17
arr340l13 = [0] * 17
arr340l14 = [0] * 17
arr340l15 = [0] * 17
arr340l16 = [0] * 17
arr340l17 = [0] * 17
arr340l18 = [0] * 17
arr340l19 = [0] * 17
arr340l20 = [0] * 17
arr340c1 = [0] * 20
arr340c2 = [0] * 20
arr340c3 = [0] * 20
arr340c4 = [0] * 20
arr340c5 = [0] * 20
arr340c6 = [0] * 20
arr340c7 = [0] * 20
arr340c8 = [0] * 20
arr340c9 = [0] * 20
arr340c10 = [0] * 20
arr340c11 = [0] * 20
arr340c12 = [0] * 20
arr340c13 = [0] * 20
arr340c14 = [0] * 20
arr340c15 = [0] * 20
arr340c16 = [0] * 20
arr340c17 = [0] * 20
arr340c18 = [0] * 20
arr340c19 = [0] * 20
arr340c20 = [0] * 20
num = 0
#assign the ascii string to ann array
for i in range(0,340):
    arr340[i] = string340[i]

#when arr340l + num is called display the corresponging line
for foo in range(0,340):
    if foo <= 16:
        arr340l1[num] = arr340[foo]
        num += 1
    if foo >= 17 and foo <= 33:
        if num > 16:
            num = 0
        arr340l2[num] = arr340[foo]
        num += 1
    if foo >= 34 and foo <= 50:
        if num > 16:
            num = 0
        arr340l3[num] = arr340[foo]
        num += 1
    if foo >= 51 and foo <= 67:
        if num > 16:
            num = 0
        arr340l4[num] = arr340[foo]
        num += 1
    if foo >= 68 and foo <= 84:
        if num > 16:
            num = 0
        arr340l5[num] = arr340[foo]
        num += 1
    if foo >= 85 and foo <=101:
        if num > 16:
            num = 0
        arr340l6[num] = arr340[foo]
        num += 1
    if foo >= 102 and foo <= 118:
        if num > 16:
            num = 0
        arr340l7[num] = arr340[foo]
        num += 1
    if foo >= 119 and foo <= 135:
        if num > 16:
            num = 0
        arr340l8[num] = arr340[foo]
        num += 1
    if foo >= 136 and foo <= 152:
        if num > 16:
            num = 0
        arr340l9[num] = arr340[foo]
        num += 1
    if foo >= 153 and foo <= 169:
        if num > 16:
            num = 0
        arr340l10[num] = arr340[foo]
        num += 1
    if foo >= 170 and foo <= 186:
        if num > 16:
            num = 0
        arr340l11[num] = arr340[foo]
        num += 1
    if foo >= 187 and foo <= 203:
        if num > 16:
            num = 0
        arr340l12[num] = arr340[foo]
        num += 1
    if foo >= 204 and foo <= 220:
        if num > 16:
            num = 0
        arr340l13[num] = arr340[foo]
        num += 1
    if foo >= 221 and foo <= 237:
        if num > 16:
            num = 0
        arr340l14[num] = arr340[foo]
        num += 1
    if foo >= 238 and foo <= 254:
        if num > 16:
            num = 0
        arr340l15[num] = arr340[foo]
        num += 1
    if foo >= 255 and foo <= 271:
        if num > 16:
            num = 0
        arr340l16[num] = arr340[foo]
        num += 1
    if foo >= 272 and foo <= 288:
        if num > 16:
            num = 0
        arr340l17[num] = arr340[foo]
        num += 1
    if foo >= 289 and foo <= 305:
        if num > 16:
            num = 0
        arr340l18[num] = arr340[foo]
        num += 1
    if foo >= 306 and foo <= 322:
        if num > 16:
            num = 0
        arr340l19[num] = arr340[foo]
        num += 1
    if foo >= 323 and foo <= 339:
        if num > 16:
            num = 0
        arr340l20[num] = arr340[foo]
        num += 1
#when arr340c + number 1-20 is called display the collumn which attributes to that collumn
num = 0
numss = 0
for z in range(0,17):
    for y in range(0,20):
        vars()["arr340c" + str(numss + 1)][y] = vars()["arr340l" + str(y + 1)][numss]
    numss += 1
    
#Display the whole 340 cipher as ascii
nums = 1
print("0    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17")
for n in range(0,20):
    if nums <= 9:
        print(nums,'',vars()["arr340l" + str(nums)])
        nums += 1
    else:
        print(nums,vars()["arr340l" + str(nums)])
        nums += 1        

#arr340 as a matrix
arr340m = [[arr340l1],
           [arr340l2],
           [arr340l3],
           [arr340l4],
           [arr340l5],
           [arr340l6],
           [arr340l7],
           [arr340l8],
           [arr340l9],
           [arr340l10],
           [arr340l11],
           [arr340l12],
           [arr340l13],
           [arr340l14],
           [arr340l15],
           [arr340l16],
           [arr340l17],
           [arr340l18],
           [arr340l19],
           [arr340l20]]
           
while True:
    data = input("z340:")
    if data == "help":
        print("//'rowY' to display individual rows")
        print("//'colX' to display individual collumns")
        print("//'mat' display matrix data")
        print("//'grid(X,Y,gridX,gridY)' plots defined grid size via gridX,gridY at coordinates x,y of data")
        print("//'rotD' where D =90,180 or 270 to rotate the data by D degrees")

    #get row data
    if data[0] == "r" and data[1] == "o" and data[2] == "w":
        if len(data) == 4:
            print(vars()["arr340l" + data[3]])
        if len(data) == 5:
            if int(data[3] + data[4]) > 20:
                print("please Select a number between 1-20")
            else:
                print(vars()["arr340l" + data[3] + data[4]])
            if len(data) > 5:
                print("please Select a number between 1-20")
            

    #get column data
    if data[0] == "c" and data[1] == "o" and data[2] == "l":
        if len(data) == 4:
            print(vars()["arr340c" + data[3]])
        if len(data) == 5:
            if int(data[3] + data[4]) > 17:
                print("please Select a number between 1-17")
            else:
                print(vars()["arr340c" + data[3] + data[4]])
        if len(data) > 5:
            print("please Select a number between 1-17")

    #get matrix data
    if data[0] == "m" and data[1] == "a" and data[2] == "t":
        for array in arr340m:
            print(array)

    #rotate data 180 degrees
    if data[0] == "r" and data[1] == "o" and data[2] == "t" and data[3] == "1" and data[4] == "8" and data[5] == "0":
        rotl1 = [0] * 17
        rotl2 = [0] * 17
        rotl3 = [0] * 17
        rotl4 = [0] * 17
        rotl5 = [0] * 17
        rotl6 = [0] * 17
        rotl7 = [0] * 17
        rotl8 = [0] * 17
        rotl9 = [0] * 17
        rotl10 = [0] * 17
        rotl11 = [0] * 17
        rotl12 = [0] * 17
        rotl13 = [0] * 17
        rotl14 = [0] * 17
        rotl15 = [0] * 17
        rotl16 = [0] * 17
        rotl17 = [0] * 17
        rotl18 = [0] * 17
        rotl19 = [0] * 17
        rotl20 = [0] * 17
        length = 16
        height = 20
        heightl = 1
        for i in range(0,20):
            for i in range(0,17):
                vars()["rotl" + str(heightl)][i] = vars()["arr340l" + str(height)][length]
                length -= 1
            height -= 1
            length = 16
            heightl += 1

        rotm180 = [[rotl1],
                  [rotl2],
                  [rotl3],
                  [rotl4],
                  [rotl5],
                  [rotl6],
                  [rotl7],
                  [rotl8],
                  [rotl9],
                  [rotl10],
                  [rotl11],
                  [rotl12],
                  [rotl13],
                  [rotl14],
                  [rotl15],
                  [rotl16],
                  [rotl17],
                  [rotl18],
                  [rotl19],
                  [rotl20]]
                

        for x in rotm180:
            print(x)

    #rotate data 270 degrees
    if data[0] == "r" and data[1] == "o" and data[2] == "t" and data[3] == "2" and data[4] == "7" and data[5] == "0":
        rotl1 = [0] * 20
        rotl2 = [0] * 20
        rotl3 = [0] * 20
        rotl4 = [0] * 20
        rotl5 = [0] * 20
        rotl6 = [0] * 20
        rotl7 = [0] * 20
        rotl8 = [0] * 20
        rotl9 = [0] * 20
        rotl10 = [0] * 20
        rotl11 = [0] * 20
        rotl12 = [0] * 20
        rotl13 = [0] * 20
        rotl14 = [0] * 20
        rotl15 = [0] * 20
        rotl16 = [0] * 20
        rotl17 = [0] * 20
        num = 19
        line = 1
        newline = 17
        value = 0
        for val in range(0,17):
            for baa in rotl1:
                vars()["rotl" + str(line)][value] = vars()["arr340c" + str(newline)][value]
                num -= 1
                value += 1
            num = 19
            value = 0
            line += 1
            newline -= 1
        rotm90 = [[rotl1],
                  [rotl2],
                  [rotl3],
                  [rotl4],
                  [rotl5],
                  [rotl6],
                  [rotl7],
                  [rotl8],
                  [rotl9],
                  [rotl10],
                  [rotl11],
                  [rotl12],
                  [rotl13],
                  [rotl14],
                  [rotl15],
                  [rotl16],
                  [rotl17]]

        for array in rotm90:
            print(array)
    #rotate the matrix 90degrees clockwise
    if data[0] == "r" and data[1] == "o" and data[2] == "t" and data[3] == "9" and data[4] == "0":
        rotl1 = [0] * 20
        rotl2 = [0] * 20
        rotl3 = [0] * 20
        rotl4 = [0] * 20
        rotl5 = [0] * 20
        rotl6 = [0] * 20
        rotl7 = [0] * 20
        rotl8 = [0] * 20
        rotl9 = [0] * 20
        rotl10 = [0] * 20
        rotl11 = [0] * 20
        rotl12 = [0] * 20
        rotl13 = [0] * 20
        rotl14 = [0] * 20
        rotl15 = [0] * 20
        rotl16 = [0] * 20
        rotl17 = [0] * 20
        num = 19
        line = 1
        value = 0
        for val in range(0,17):
            for baa in rotl1:
                vars()["rotl" + str(line)][value] = vars()["arr340c" + str(line)][num]
                num -= 1
                value += 1
            num = 19
            value = 0
            line += 1
        rotm90 = [[rotl1],
                  [rotl2],
                  [rotl3],
                  [rotl4],
                  [rotl5],
                  [rotl6],
                  [rotl7],
                  [rotl8],
                  [rotl9],
                  [rotl10],
                  [rotl11],
                  [rotl12],
                  [rotl13],
                  [rotl14],
                  [rotl15],
                  [rotl16],
                  [rotl17]]

        for array in rotm90:
            print(array)
        
    #plot a grid from coordinates and size
    if data[0] == "g" and data[1] =="r" and data[2] == "i" and data[3] == "d" and data[4] == "(":
        if len(data) == 13:
            xpos = data[5]
            temp = data[5]
            ypos = data[7]
            xsize = data[9]
            ysize = data[11]
            newgridinc = 1
            gridl1 = [0] * int(xsize)
            gridl2 = [0] * int(xsize)
            gridl3 = [0] * int(xsize)
            gridl4 = [0] * int(xsize)
            gridl5 = [0] * int(xsize)
            gridl6 = [0] * int(xsize)
            gridl7 = [0] * int(xsize)
            gridl8 = [0] * int(xsize)
            gridl9 = [0] * int(xsize)
            gridl10 = [0] * int(xsize)
            gridl11 = [0] * int(xsize)
            gridl12 = [0] * int(xsize)
            gridl13 = [0] * int(xsize)
            gridl14 = [0] * int(xsize)
            gridl15 = [0] * int(xsize)
            gridl16 = [0] * int(xsize)
            gridl17 = [0] * int(xsize)
            gridl18 = [0] * int(xsize)
            gridl19 = [0] * int(xsize)
            gridl20 = [0] * int(xsize)
            if int(xpos) + int(xsize) > 17:
                print("grid is out of bounds of data")
            else:
                for yheight in range(0,int(ysize)):
                    for xlength in range(0,int(xsize)):
                        vars()["gridl" + str(newgridinc)][xlength] = vars()["arr340l" + str(ypos)][int(xpos) - 1]
                        xpos = int(xpos) + 1
                    print(vars()["gridl" + str(yheight + 1)])
                    xpos = temp
                    ypos =(int(ypos) + 1)
                    newgridinc += 1

        if len(data) == 14:
            newdata = str(data[5]) + str(data[6]) + str(data[7]) + str(data[8]) + str(data[9]) + str(data[10]) + str(data[11]) + str(data[12])
            temparray = newdata.split(',')
            xpos = temparray[0]
            temp = temparray[0]
            ypos = temparray[1]
            xsize = temparray[2]
            ysize = temparray[3]
            newgridinc = 1
            gridl1 = [0] * int(xsize)
            gridl2 = [0] * int(xsize)
            gridl3 = [0] * int(xsize)
            gridl4 = [0] * int(xsize)
            gridl5 = [0] * int(xsize)
            gridl6 = [0] * int(xsize)
            gridl7 = [0] * int(xsize)
            gridl8 = [0] * int(xsize)
            gridl9 = [0] * int(xsize)
            gridl10 = [0] * int(xsize)
            gridl11 = [0] * int(xsize)
            gridl12 = [0] * int(xsize)
            gridl13 = [0] * int(xsize)
            gridl14 = [0] * int(xsize)
            gridl15 = [0] * int(xsize)
            gridl16 = [0] * int(xsize)
            gridl17 = [0] * int(xsize)
            gridl18 = [0] * int(xsize)
            gridl19 = [0] * int(xsize)
            gridl20 = [0] * int(xsize)
            if int(xpos) + int(xsize) > 17:
                print("grid is out of bounds of data")
            else:
                for yheight in range(0,int(ysize)):
                    for xlength in range(0,int(xsize)):
                        vars()["gridl" + str(newgridinc)][xlength] = vars()["arr340l" + str(ypos)][int(xpos) - 1]
                        xpos = int(xpos) + 1
                    print(vars()["gridl" + str(yheight + 1)])
                    xpos = temp
                    ypos =(int(ypos) + 1)
                    newgridinc += 1
        if len(data) == 15:
            newdata = str(data[5]) + str(data[6]) + str(data[7]) + str(data[8]) + str(data[9]) + str(data[10]) + str(data[11]) + str(data[12]) + str(data[13])
            temparray = newdata.split(',')
            xpos = temparray[0]
            temp = temparray[0]
            ypos = temparray[1]
            xsize = temparray[2]
            ysize = temparray[3]
            newgridinc = 1
            gridl1 = [0] * int(xsize)
            gridl2 = [0] * int(xsize)
            gridl3 = [0] * int(xsize)
            gridl4 = [0] * int(xsize)
            gridl5 = [0] * int(xsize)
            gridl6 = [0] * int(xsize)
            gridl7 = [0] * int(xsize)
            gridl8 = [0] * int(xsize)
            gridl9 = [0] * int(xsize)
            gridl10 = [0] * int(xsize)
            gridl11 = [0] * int(xsize)
            gridl12 = [0] * int(xsize)
            gridl13 = [0] * int(xsize)
            gridl14 = [0] * int(xsize)
            gridl15 = [0] * int(xsize)
            gridl16 = [0] * int(xsize)
            gridl17 = [0] * int(xsize)
            gridl18 = [0] * int(xsize)
            gridl19 = [0] * int(xsize)
            gridl20 = [0] * int(xsize)
            if int(xpos) + int(xsize) > 17:
                print("grid is out of bounds of data")
            else:
                for yheight in range(0,int(ysize)):
                    for xlength in range(0,int(xsize)):
                        vars()["gridl" + str(newgridinc)][xlength] = vars()["arr340l" + str(ypos)][int(xpos) - 1]
                        xpos = int(xpos) + 1
                    print(vars()["gridl" + str(yheight + 1)])
                    xpos = temp
                    ypos =(int(ypos) + 1)
                    newgridinc += 1

        if len(data) == 16:
            newdata = str(data[5]) + str(data[6]) + str(data[7]) + str(data[8]) + str(data[9]) + str(data[10]) + str(data[11]) + str(data[12]) + str(data[13]) + str(data[14])
            temparray = newdata.split(',')
            xpos = temparray[0]
            temp = temparray[0]
            ypos = temparray[1]
            xsize = temparray[2]
            ysize = temparray[3]
            newgridinc = 1
            gridl1 = [0] * int(xsize)
            gridl2 = [0] * int(xsize)
            gridl3 = [0] * int(xsize)
            gridl4 = [0] * int(xsize)
            gridl5 = [0] * int(xsize)
            gridl6 = [0] * int(xsize)
            gridl7 = [0] * int(xsize)
            gridl8 = [0] * int(xsize)
            gridl9 = [0] * int(xsize)
            gridl10 = [0] * int(xsize)
            gridl11 = [0] * int(xsize)
            gridl12 = [0] * int(xsize)
            gridl13 = [0] * int(xsize)
            gridl14 = [0] * int(xsize)
            gridl15 = [0] * int(xsize)
            gridl16 = [0] * int(xsize)
            gridl17 = [0] * int(xsize)
            gridl18 = [0] * int(xsize)
            gridl19 = [0] * int(xsize)
            gridl20 = [0] * int(xsize)
            if int(xpos) + int(xsize) > 17:
                print("grid is out of bounds of data")
            else:
                for yheight in range(0,int(ysize)):
                    for xlength in range(0,int(xsize)):
                        vars()["gridl" + str(newgridinc)][xlength] = vars()["arr340l" + str(ypos)][int(xpos) - 1]
                        xpos = int(xpos) + 1
                    print(vars()["gridl" + str(yheight + 1)])
                    xpos = temp
                    ypos =(int(ypos) + 1)
                    newgridinc += 1
        
        if len(data) == 17:
            xpos = str(data[5]) + str(data[6])
            temp = str(data[5]) + str(data[6])
            ypos = str(data[8]) + str(data[9])
            xsize = str(data[11]) + str(data[12])
            ysize = str(data[14]) + str(data[15])
            newgridinc = 1
            gridl1 = [0] * int(xsize)
            gridl2 = [0] * int(xsize)
            gridl3 = [0] * int(xsize)
            gridl4 = [0] * int(xsize)
            gridl5 = [0] * int(xsize)
            gridl6 = [0] * int(xsize)
            gridl7 = [0] * int(xsize)
            gridl8 = [0] * int(xsize)
            gridl9 = [0] * int(xsize)
            gridl10 = [0] * int(xsize)
            gridl11 = [0] * int(xsize)
            gridl12 = [0] * int(xsize)
            gridl13 = [0] * int(xsize)
            gridl14 = [0] * int(xsize)
            gridl15 = [0] * int(xsize)
            gridl16 = [0] * int(xsize)
            gridl17 = [0] * int(xsize)
            gridl18 = [0] * int(xsize)
            gridl19 = [0] * int(xsize)
            gridl20 = [0] * int(xsize)
            if int(xpos) + int(xsize) > 17:
                print("grid is out of bounds of data")
            else:
                for yheight in range(0,int(ysize)):
                    for xlength in range(0,int(xsize)):
                        vars()["gridl" + str(newgridinc)][xlength] = vars()["arr340l" + str(ypos)][int(xpos) - 1]
                        xpos = int(xpos) + 1
                    print(vars()["gridl" + str(yheight + 1)])
                    xpos = temp
                    ypos =(int(ypos) + 1)
                    newgridinc += 1
