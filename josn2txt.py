import json
import os


def json2txt(json_path, dota_path, filename):

    with open(json_path + "/" + filename,'r',encoding='UTF-8') as f:
        result = json.load(f)
        for object in result["rects"]:
            print(object)
            x1, x2 = object["x"]
            y1, y2 = object['y']
            x1 = str(x1)
            x2 = str(x2)
            y1 = str(y1)
            y2 = str(y2)
            type = object['type']
            dota_txt_path = dota_path + '/' + filename[:-4] + 'txt'
            with open(dota_txt_path, 'a',encoding='utf-8') as file:
                fileline = x1 + ' ' + y1 + ' ' + x1 + ' ' + y2 + ' ' + x2 + ' ' + y1 + ' ' + x2 + ' ' + y2 + ' ' + type + ' ' + '0' + '\n'
                file.write(fileline)



        # print(result["rects"][0])



if __name__ == "__main__":
    json_path = "Stampede/lable"
    dota_path = "Stampede/dotalable"
    files = os.listdir(dota_path)
    for f in files:
        path = dota_path + '/' + f
        os.remove(path)

    for file_name in os.listdir(json_path):
        print(file_name)
        json2txt(json_path, dota_path, file_name)


