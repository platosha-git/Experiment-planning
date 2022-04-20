def form_equasion(b, accuracy, params):
    y = "y = " + str(round(abs(b[0]), accuracy)) + " + " + \
                    str(round(abs(b[1]), accuracy)) + "x1 + " + str(round(b[2], accuracy)) + "x2 + " + \
                    str(round(b[3], accuracy)) + "x3 + " + str(round(b[4], accuracy)) + "x4 + " + \
                    str(round(b[5], accuracy)) + "x5 + " + str(round(b[6], accuracy)) + "x6 + \n" + \
                    str(round(b[7], accuracy)) + "x1x2 + " + str(round(b[8], accuracy)) + "x1x3 + " + \
                    str(round(b[9], accuracy)) + "x1x4 + " + str(round(b[10], accuracy)) + "x1x5 + " + \
                    str(round(b[11], accuracy)) + "x1x6 + " + str(round(b[12], accuracy)) + "x2x3 + " + \
                    str(round(b[13], accuracy)) + "x2x4 + " + str(round(b[14], accuracy)) + "x2x5 + " + \
                    str(round(b[15], accuracy)) + "x2x6 + " + str(round(b[16], accuracy)) + "x3x4 + " + \
                    str(round(b[17], accuracy)) + "x3x5 + " + str(round(b[18], accuracy)) + "x3x6 + " + \
                    str(round(b[19], accuracy)) + "x4x5 + " + str(round(b[20], accuracy)) + "x4x6 + \n" + \
                    str(round(b[21], accuracy)) + "x5x6 + " + str(round(b[22], accuracy)) + "x1x2x3 + " + \
                    str(round(b[23], accuracy)) + "x1x2x4 + " + str(round(b[24], accuracy)) + "x1x2x5 + " + \
                    str(round(b[25], accuracy)) + "x1x2x6 + " + str(round(b[26], accuracy)) + "x1x3x4 + " + \
                    str(round(b[27], accuracy)) + "x1x3x5 + " + str(round(b[28], accuracy)) + "x1x3x6 + " + \
                    str(round(b[28], accuracy)) + "x1x4x5 + " + str(round(b[30], accuracy)) + "x1x4x6 + " + \
                    str(round(b[31], accuracy)) + "x1x5x6 + " + str(round(b[32], accuracy)) + "x2x3x4 + " + \
                    str(round(b[33], accuracy)) + "x2x3x5 + " + str(round(b[34], accuracy)) + "x2x3x6 + " + \
                    str(round(b[35], accuracy)) + "x2x4x5 + " + str(round(b[36], accuracy)) + "x2x4x6 + " + \
                    str(round(b[37], accuracy)) + "x2x5x6 + " + str(round(b[38], accuracy)) + "x3x4x5 + " + \
                    str(round(b[39], accuracy)) + "x3x4x6 + " + str(round(b[40], accuracy)) + "x3x5x6 + " + \
                    str(round(b[41], accuracy)) + "x4x5x6 + \n" + str(round(b[42], accuracy)) + "x1x2x3x4 + " + \
                    str(round(b[43], accuracy)) + "x1x2x3x5 + " + str(round(b[44], accuracy)) + "x1x2x3x6 + " + \
                    str(round(b[45], accuracy)) + "x1x2x4x5 + " + str(round(b[46], accuracy)) + "x1x2x4x6 + " + \
                    str(round(b[47], accuracy)) + "x1x2x5x6 + " + str(round(b[48], accuracy)) + "x1x3x4x5 + " + \
                    str(round(b[49], accuracy)) + "x1x3x4x6 + " + str(round(b[50], accuracy)) + "x1x3x5x6 + " + \
                    str(round(b[51], accuracy)) + "x1x4x5x6 + " + str(round(b[52], accuracy)) + "x2x3x4x5 + " + \
                    str(round(b[53], accuracy)) + "x2x3x4x6 + " + str(round(b[54], accuracy)) + "x2x3x5x6 + " + \
                    str(round(b[55], accuracy)) + "x2x4x5x6 + " + str(round(b[56], accuracy)) + "x3x4x5x6 + \n" + \
                    str(round(b[57], accuracy)) + "x1x2x3x4x5 + " + str(round(b[58], accuracy)) + "x1x2x3x4x6 + " + \
                    str(round(b[59], accuracy)) + "x1x2x3x5x6 + " + str(round(b[60], accuracy)) + "x1x2x4x5x6 + " + \
                    str(round(b[61], accuracy)) + "x1x3x4x5x6 + " + str(round(b[62], accuracy)) + "x2x3x4x5x6 + " + \
                    str(round(b[63], accuracy)) + "x1x2x3x4x5x6 + \n" + \
                    str(round(b[64], accuracy)) + "x1^2 + " + str(round(b[65], accuracy)) + "x2^2 + " + \
                    str(round(b[66], accuracy)) + "x3^2 + " + str(round(b[67], accuracy)) + "x4^2 + " + \
                    str(round(b[68], accuracy)) + "x5^2 + " + str(round(b[69], accuracy)) + "x6^2"
    return y
                    