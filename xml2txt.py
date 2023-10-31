import os
import os.path
from xml.dom.minidom import parse
import math


def rotatePoint(xc, yc, xp, yp, theta):
    xoff = xp - xc
    yoff = yp - yc

    cosTheta = math.cos(theta)
    sinTheta = math.sin(theta)
    pResx = cosTheta * xoff + sinTheta * yoff
    pResy = - sinTheta * xoff + cosTheta * yoff
    # pRes = (xc + pResx, yc + pResy)

    return xc + pResx, yc + pResy
def xml2txt(xml_path, txt_path):
    filenames = os.listdir(xml_path)

    for filename in filenames:
        print(filename)
        if '.xml' in filename:
            file_data = ''
            xml_file = os.path.join(xml_path, filename)
            dom = parse(xml_file)
            root = dom.documentElement
            # 根据文件的树状结构，一级级找到point点所在的位置即可
            for obj in root.getElementsByTagName('object'):

                name = obj.getElementsByTagName('name')[0].childNodes[0].data
                name = name.strip('\n')
                if name == 'car':
                    print("###############################################################################################################################")
                try:
                    type = obj.getElementsByTagName('type')[0].childNodes[0].data

                except IndexError:
                    xmin = obj.getElementsByTagName('xmin')[0].childNodes[0].data
                    ymin = obj.getElementsByTagName('ymin')[0].childNodes[0].data
                    xmax = obj.getElementsByTagName('xmax')[0].childNodes[0].data
                    ymax = obj.getElementsByTagName('ymax')[0].childNodes[0].data
                    type = 'nothing'

                    x1, y1 = xmin, ymin
                    x2, y2 = xmin, ymax
                    x3, y3 = xmax, ymin
                    x4, y4 = xmax, ymax



                if type == 'bndbox':
                    xmin = obj.getElementsByTagName('xmin')[0].childNodes[0].data
                    ymin = obj.getElementsByTagName('ymin')[0].childNodes[0].data
                    xmax = obj.getElementsByTagName('xmax')[0].childNodes[0].data
                    ymax = obj.getElementsByTagName('ymax')[0].childNodes[0].data

                    x1, y1 = xmin, ymin
                    x2, y2 = xmin, ymax
                    x3, y3 = xmax, ymin
                    x4, y4 = xmax, ymax

                if type == 'robndbox':

                    angle = eval(obj.getElementsByTagName('angle')[0].childNodes[0].data)
                    cx = eval(obj.getElementsByTagName('cx')[0].childNodes[0].data)
                    cy = eval(obj.getElementsByTagName('cy')[0].childNodes[0].data)
                    w = eval(obj.getElementsByTagName('w')[0].childNodes[0].data)
                    h = eval(obj.getElementsByTagName('h')[0].childNodes[0].data)

                    # xmin = str(cx - 0.5 * w * math.cos(angle) + 0.5 * h * math.sin(angle))
                    # ymin = str(cy - 0.5 * w * math.sin(angle) - 0.5 * h * math.cos(angle))
                    # xmax = str(cx + 0.5 * w * math.cos(angle) - 0.5 * h * math.sin(angle))
                    # ymax = str(cy + 0.5 * w * math.sin(angle) + 0.5 * h * math.cos(angle))
                    x1, y1 = rotatePoint(cx, cy, cx - w/2, cy - h/2, -angle)
                    x2, y2 = rotatePoint(cx, cy, cx + w/2, cy - h/2, -angle)
                    x3, y3 = rotatePoint(cx, cy, cx + w/2, cy + h/2, -angle)
                    x4, y4 = rotatePoint(cx, cy, cx - w/2, cy + h/2, -angle)

                    x1, y1 = str(x1), str(y1)
                    x2, y2 = str(x2), str(y2)
                    x3, y3 = str(x3), str(y3)
                    x4, y4 = str(x4), str(y4)




                line = x1 + ' '+ y1 + ' ' + x2 + ' '+ y2 + ' ' + x3 + ' '+ y3 + ' ' + x4 + ' '+ y4 + ' ' + name + ' 0' + '\n'
                file_data += line
            with open(txt_path + filename.replace('.xml', '.txt'), 'w') as fw:
                # print('filename: ', filename)
                # print('file_data: ', file_data)
                fw.write(file_data)


if __name__ == "__main__":
    xml_path = 'label\\'

    txt_path = 'dotalabel\\'
    xml2txt(xml_path, txt_path)