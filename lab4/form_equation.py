def form_equasion(b, accuracy):
    y = str(round(b[0], accuracy)) + " + " + str(round(b[1], accuracy)) + "x1 + " + str(
            round(b[2], accuracy)) + "x2 + " + str(round(b[3], accuracy)) + "x3 + " + str(
            round(b[4], accuracy)) + "x4 + " + str(round(b[5], accuracy)) + "x5 + " + str(
            round(b[6], accuracy)) + "x6 + " + str(round(b[7], accuracy)) + "x1x2 + " + str(
            round(b[8], accuracy)) + "x1x3 + " + str(round(b[9], accuracy)) + "x1x4 + " + str(
            round(b[10], accuracy)) + "x1x5 + \n" + str(round(b[11], accuracy)) + "x1x6 + " + str(
            round(b[12], accuracy)) + "x2x3 + " + str(round(b[13], accuracy)) + "x2x4 + " + str(
            round(b[14], accuracy)) + "x2x5 + " + str(round(b[15], accuracy)) + "x2x6 + " + str(
            round(b[16], accuracy)) + "x3x4 + " + str(round(b[17], accuracy)) + "x3x5 + " + str(
            round(b[18], accuracy)) + "x3x6 + " + str(round(b[19], accuracy)) + "x4x5 + " + str(
            round(b[20], accuracy)) + "x4x6 + " + str(round(b[21], accuracy)) + "x5x6 + \n" + str(
            round(b[64], accuracy)) + "x1^2 + " + str(round(b[65], accuracy)) + "x2^2 + " + str(
            round(b[66], accuracy)) + "x3^2 + " + str(round(b[67], accuracy)) + "x4^2 + " + str(
            round(b[68], accuracy)) + "x5^2 + " + str(round(b[69], accuracy)) + "x6^2 + ..."
    return y


def form_full_equasion(b, accuracy):
    y = "y = " + str(round(self.b[0], accuracy)) + " + " + str(round(self.b[1], accuracy)) + "x1 + " + str(
                    round(self.b[2], accuracy)) + "x2 + " + str(round(self.b[3], accuracy)) + "x3 + " + str(
                    round(self.b[4], accuracy)) + "x4 +" + str(round(self.b[5], accuracy)) + "x5 + " + str(
                    round(self.b[6], accuracy)) + "x6 + " + str(round(self.b[7], accuracy)) + "x1x2 + " + str(
                    round(self.b[8], accuracy)) + "x1x3 + " + str(round(self.b[9], accuracy)) + "x1x4 + " + str(
                    round(self.b[10], accuracy)) + "x1x5 + \n" + str(round(self.b[11], accuracy)) + "x1x6 + " + str(
                    round(self.b[12], accuracy)) + "x2x3 + " + str(round(self.b[13], accuracy)) + "x2x4 + " + str(
                    round(self.b[14], accuracy)) + "x2x5 + " + str(round(self.b[15], accuracy)) + "x2x6 + " + str(
                    round(self.b[16], accuracy)) + "x3x4 + " + str(round(self.b[17], accuracy)) + "x3x5 + " + str(
                    round(self.b[18], accuracy)) + "x3x6 + " + str(round(self.b[19], accuracy)) + "x4x5 + " + str(
                    round(self.b[20], accuracy)) + "x4x6 + " + str(round(self.b[21], accuracy)) + "x5x6 + \n" + str(
                    round(self.b[22], accuracy)) + "x1x2x3 + " + str(round(self.b[23], accuracy)) + "x1x2x4 + " + str(
                    round(self.b[24], accuracy)) + "x1x2x5 + " + str(round(self.b[25], accuracy)) + "x1x2x6 + " + str(
                    round(self.b[26], accuracy)) + "x1x3x4 + " + str(round(self.b[27], accuracy)) + "x1x3x5 + " + str(
                    round(self.b[28], accuracy)) + "x1x3x6 + " + str(round(self.b[28], accuracy)) + "x1x4x5 + " + str(
                    round(self.b[30], accuracy)) + "x1x4x6 + " + str(round(self.b[31], accuracy)) + "x1x5x6 + " + str(
                    round(self.b[32], accuracy)) + "x2x3x4 + \n" + str(round(self.b[33], accuracy)) + "x2x3x5 + " + str(
                    round(self.b[34], accuracy)) + "x2x3x6 + " + str(round(self.b[35], accuracy)) + "x2x4x5 + " + str(
                    round(self.b[36], accuracy)) + "x2x4x6 + " + str(round(self.b[37], accuracy)) + "x2x5x6 + " + str(
                    round(self.b[38], accuracy)) + "x3x4x5 + " + str(round(self.b[39], accuracy)) + "x3x4x6 + " + str(
                    round(self.b[40], accuracy)) + "x3x5x6 + " + str(round(self.b[41], accuracy)) + "x4x5x6 + " + str(
                    round(self.b[42], accuracy)) + "x1x2x3x4 + " + str(round(self.b[43], accuracy)) + "x1x2x3x5 + \n" + str(
                    round(self.b[44], accuracy)) + "x1x2x3x6 + " + str(round(self.b[45], accuracy)) + "x1x2x4x5 + " + str(
                    round(self.b[46], accuracy)) + "x1x2x4x6 + " + str(round(self.b[47], accuracy)) + "x1x2x5x6 + " + str(
                    round(self.b[48], accuracy)) + "x1x3x4x5 + " + str(round(self.b[49], accuracy)) + "x1x3x4x6 + " + str(
                    round(self.b[50], accuracy)) + "x1x3x5x6 + " + str(round(self.b[51], accuracy)) + "x1x4x5x6 + " + str(
                    round(self.b[52], accuracy)) + "x2x3x4x5 + " + str(round(self.b[53], accuracy)) + "x2x3x4x6 + " + str(
                    round(self.b[54], accuracy)) + "x2x3x5x6 + \n" + str(round(self.b[55], accuracy)) + "x2x4x5x6 + " + str(
                    round(self.b[56], accuracy)) + "x3x4x5x6 + " + str(round(self.b[57], accuracy)) + "x1x2x3x4x5 + " + str(
                    round(self.b[58], accuracy)) + "x1x2x3x4x6 + " + str(
                    round(self.b[59], accuracy)) + "x1x2x3x5x6 + " + str(
                    round(self.b[60], accuracy)) + "x1x2x4x5x6 + " + str(
                    round(self.b[61], accuracy)) + "x1x3x4x5x6 + " + str(
                    round(self.b[62], accuracy)) + "x2x3x4x5x6 + " + str(
                    round(self.b[63], accuracy)) + "x1x2x3x4x5x6 + \n" + str(
                    round(self.b[64], accuracy)) + "x1^2 + " + str(round(self.b[65], accuracy)) + "x2^2 + " + str(
                    round(self.b[66], accuracy)) + "x3^2 + " + str(round(self.b[67], accuracy)) + "x4^2 + " + str(
                    round(self.b[68], accuracy)) + "x5^2 + " + str(round(self.b[69], accuracy)) + "x6^2"
                    