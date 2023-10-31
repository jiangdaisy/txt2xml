import math
import os
from xml.dom.minidom import Document
from xml.dom.minidom import parse
import xml.dom.minidom
import numpy as np
import csv
import cv2
import string




def WriterXMLFiles(filename, path, box_list, label_list, w, h, d):
    # dict_box[filename]=json_dict[filename]
    doc = xml.dom.minidom.Document()
    root = doc.createElement('annotation')
    doc.appendChild(root)

    foldername = doc.createElement("folder")
    foldername.appendChild(doc.createTextNode("JPEGImages"))
    root.appendChild(foldername)

    nodeFilename = doc.createElement('filename')
    nodeFilename.appendChild(doc.createTextNode(filename))
    root.appendChild(nodeFilename)

    pathname = doc.createElement("path")
    pathname.appendChild(doc.createTextNode("xxxx"))
    root.appendChild(pathname)

    sourcename = doc.createElement("source")

    databasename = doc.createElement("database")
    databasename.appendChild(doc.createTextNode("The VOC2007 Database"))
    sourcename.appendChild(databasename)

    annotationname = doc.createElement("annotation")
    annotationname.appendChild(doc.createTextNode("PASCAL VOC2007"))
    sourcename.appendChild(annotationname)

    imagename = doc.createElement("image")
    imagename.appendChild(doc.createTextNode("flickr"))
    sourcename.appendChild(imagename)

    flickridname = doc.createElement("flickrid")
    flickridname.appendChild(doc.createTextNode("0"))
    sourcename.appendChild(flickridname)

    root.appendChild(sourcename)

    nodesize = doc.createElement('size')
    nodewidth = doc.createElement('width')
    nodewidth.appendChild(doc.createTextNode(str(w)))
    nodesize.appendChild(nodewidth)
    nodeheight = doc.createElement('height')
    nodeheight.appendChild(doc.createTextNode(str(h)))
    nodesize.appendChild(nodeheight)
    nodedepth = doc.createElement('depth')
    nodedepth.appendChild(doc.createTextNode(str(d)))
    nodesize.appendChild(nodedepth)
    root.appendChild(nodesize)

    segname = doc.createElement("segmented")
    segname.appendChild(doc.createTextNode("0"))
    root.appendChild(segname)

    for (box, label) in zip(box_list, label_list):
        nodeobject = doc.createElement('object')
        nodetype = doc.createElement('type')
        nodetype.appendChild(doc.createTextNode('robndbox'))
        nodeobject.appendChild(nodetype)

        nodename = doc.createElement('name')
        nodename.appendChild(doc.createTextNode(str(label)))
        nodeobject.appendChild(nodename)

        nodepose = doc.createElement('pose')
        nodepose.appendChild(doc.createTextNode('Unspecified'))
        nodeobject.appendChild(nodepose)

        nodetrun = doc.createElement('truncated')
        nodetrun.appendChild(doc.createTextNode('0'))
        nodeobject.appendChild(nodetrun)

        nodediff = doc.createElement('difficult')
        nodediff.appendChild(doc.createTextNode('0'))
        nodeobject.appendChild(nodediff)

        nodebndbox = doc.createElement('robndbox')
        nodex1 = doc.createElement('cx')
        nodex1.appendChild(doc.createTextNode(str(box[0])))
        nodebndbox.appendChild(nodex1)
        nodey1 = doc.createElement('cy')
        nodey1.appendChild(doc.createTextNode(str(box[1])))
        nodebndbox.appendChild(nodey1)
        nodex2 = doc.createElement('w')
        nodex2.appendChild(doc.createTextNode(str(box[2])))
        nodebndbox.appendChild(nodex2)
        nodey2 = doc.createElement('h')
        nodey2.appendChild(doc.createTextNode(str(box[3])))
        nodebndbox.appendChild(nodey2)
        nodeangle = doc.createElement('angle')
        nodeangle.appendChild(doc.createTextNode(str(box[4])))
        nodebndbox.appendChild(nodeangle)
        nodeobject.appendChild(nodebndbox)
        root.appendChild(nodeobject)
    fp = open(path + filename, 'w')
    doc.writexml(fp, indent='\n')
    fp.close()


def load_annoataion(p):
    '''
    load annotation from the text file
    :param p:
    :return:
    '''
    text_rects = []
    text_tags = []
    if not os.path.exists(p):
        return np.array(text_rects, dtype=np.float32)
    with open(p, 'r') as f:
        for line in f.readlines():
            x1, y1, x2, y2, x3, y3, x4, y4, label = line.split(' ')[0:9]
            text_poly = np.array(np.float32(([x1, y1], [x2, y2], [x3, y3], [x4, y4])))

            (cx, cy), (w, h), angle = cv2.minAreaRect(text_poly)  # x,y为左上点坐标
            angle = math.radians(angle)
            text_rects.append([cx, cy, w, h, angle])
            text_tags.append(label)

        return text_rects, text_tags


if __name__ == "__main__":
    txt_path = 'test_txt/'
    xml_path = 'test_xml/'
    img_path = 'img/'
    txts = os.listdir(txt_path)
    for count, t in enumerate(txts):
        boxes, labels = load_annoataion(os.path.join(txt_path, t))
        xml_name = t.replace('.txt', '.xml')
        img_name = t.replace('.txt', '.jpg')
        print(img_name)
        img = cv2.imread(os.path.join(img_path, img_name))
        h, w, d = img.shape
        WriterXMLFiles(xml_name, xml_path, boxes, labels, w, h, d)