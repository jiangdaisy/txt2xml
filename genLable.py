import os


def text2dotatxt(det_lable_path, txt_path, file_name):

    with open(det_lable_path + '\\' + file_name, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip('\n')  # 去除文本中的换行符
            linelist = line.split(' ')
            if float(linelist[1]) > 0.4:
                test_txt_path = txt_path + '\\' + linelist[0] + '.txt'
                with open(test_txt_path,'a',encoding='utf-8')as file:
                    fileline = linelist[2] + ' ' + linelist[3] + ' ' + linelist[4] + ' ' + linelist[5] + ' ' + linelist[6] + ' ' + linelist[7] + ' ' + linelist[8] + ' ' + linelist[9] + ' ' + file_name[6:-4] + ' ' + '0' + '\n'
                    file.write(fileline)






if __name__ == "__main__":

    det_lable_path = 'Task1_results'
    txt_path = 'test_txt'
    files = os.listdir(txt_path)
    for f in files:
        path = txt_path + '/' + f
        os.remove(path)

    for file_name in os.listdir(det_lable_path):
        print(file_name)
        text2dotatxt(det_lable_path, txt_path, file_name)
