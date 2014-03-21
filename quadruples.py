def create_quad(filename):
    f = open(filename,'r')
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i][lines[i].index(':')+1:]
        lines[i] = lines[i].strip()

    jump_list = {'<':'JLT', '>':'JGT', '<=':'JLE','>=':'JGT', '!=':'JNE', '==':'JEQ'}
    quad_list = []
    text_list = []
    operators = ['+','-','/','*']

    for i in lines:
        text_list.append(i.split(" "))

    print(text_list)

    for i in text_list:
        if(i[0] == 'end'):
            break
        if('goto' in i):
            if(len(i) > 2):
                quad_list.append([jump_list[i[2]], i[1], i[3], i[5]])
            else:
                quad_list.append(['JMP', 'None','None',i[-1]])
        elif ("" not in i):
            quad_list.append([i[3], i[2], i[4], i[0]])
        else:
            quad_list.append([i[2], i[-1], 'None', i[0]])

    g = open('quadxyz.txt', 'a')

    for i in quad_list:
        g.write(str(quad_list.index(i))+"\t"+'\t'.join(i)+"\n")

    g.close()
