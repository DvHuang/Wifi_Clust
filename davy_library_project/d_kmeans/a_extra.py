# -*- coding: utf-8 -*-

#建立表头


import string



def findSubstrings(substrings,destString):
    res =  map(lambda x:str([destString.index(x),x]),filter(lambda x:x in destString,substrings))
    print ("res=",res)
    if res:
        return ', '.join(list(res))
def findSubstrings(substrings,destString):
    return ', '.join([str([destString.index(x),x]) for x in substrings if x in destString])

def android_txt(datafile):
    f = open(datafile)             # 返回文件对象
    line = f.readline()
    feature_map=dict()
    zero_count=-1
    while line:
        tta_c=line.find("TP-LINK")
        tta_s=line.find("Chinanet")
        tta_tu=line.find("swust")
        tta_ti=line.find("tushuguan")
        tta_guan=line.find("TiYuGuan")
        # davy=line.find("davy_oriention")
        # if line[0:4] not in ("TP-LINK","Chinanet","swust","tushuguan","TiYuGuan"):
        #if tta_c!=-1 or tta_s!=-1or tta_tu!=-1 or tta_ti!=-1 or tta_guan!=-1 or davy!=-1:
        if tta_c!=-1 or tta_s!=-1or tta_tu!=-1 or tta_ti!=-1 or tta_guan!=-1 :

            line_sp=line.split('@/')
            if line_sp[1] not in feature_map:
                zero_count+=1
                feature_map[line_sp[1]]=zero_count
        line = f.readline()
    f.close()
    print ("len feature map =",len(feature_map))
    return feature_map

def normal_txt(feature_map,datafile,vectorfile):
    f = open(datafile)
    fileWriteObj = open(vectorfile, 'w')
    pointlist = []
    line = f.readline()
    x = [0 for n in range(len(feature_map))]
    first_line="first_line"
    index=0
    if first_line==first_line:
        line=f.readline()
    while line:
        # print ("new line=",line)
        tag_zero=line.find("new_point")
        tag_at=line.find("@/")
        if tag_zero!=-1:
            strx=""
            for i in range(0, len(x)):
                strx+=str(x[i])+"\t"
            print >> fileWriteObj, strx
            pointlist.append((index, x))
            x = [0 for n in range(len(feature_map))]
            index+=1
        if tag_at!=-1:
           line_sp=line.split('@/')
           if line_sp[1]=="zz:zz:zz:zz:zz":
                 linshi=int(round(string.atof(line_sp[2])))/3.6
           else:
                 linshi=(100-int(line_sp[2]))

           if line_sp[1] in feature_map:
            x[feature_map[line_sp[1]]]=int(linshi)
        line = f.readline()
    print ("len 1x==",len(x))
    fileWriteObj.close()
    f.close()
    return pointlist

def new_original_file(old_file,new_file,new_feature_map):
    f = open(old_file,'r')             # 返回文件对象
    f_write=open(new_file,'w')
    line = f.readline()

    while line:
        tta_newpoint=line.find("new_point")

        if tta_newpoint!=-1:
             f_write.writelines(line)
        else:
            tta_c=line.find("TP-LINK")
            tta_s=line.find("Chinanet")
            tta_tu=line.find("swust")
            tta_ti=line.find("tushuguan")
            tta_guan=line.find("TiYuGuan")
            davy=line.find("davy_oriention")
            # if line[0:4] not in ("TP-LINK","Chinanet","swust","tushuguan","TiYuGuan"):
            if tta_c!=-1 or tta_s!=-1or tta_tu!=-1 or tta_ti!=-1 or tta_guan!=-1 or davy!=-1:
                line_sp=line.split('@/')
                if line_sp[1]  in new_feature_map:
                    f_write.writelines(line)

        line = f.readline()
    f.close()
    f_write.close()

