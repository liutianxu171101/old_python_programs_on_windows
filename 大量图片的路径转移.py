import os
import shutil

alllist = os.listdir('E://Python/mydatas/APOD')
path = 'E://Python/mydatas/'
pathnames = []
for year in range(1995,2021):
    os.mkdir('E://Python/mydatas/'+str(year))
    pathnames.append('E://Python/mydatas/'+str(year))
    
for filename in alllist:
    string1 = filename[2:4]
    for pathname in pathnames:
        if (string1 ==pathname[-2:]):
            oldname = path + 'APOD/' + filename
            newname = pathname + '/' + filename
            shutil.copyfile(oldname,newname)
            break


    
