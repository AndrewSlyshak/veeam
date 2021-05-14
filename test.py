import os

def readFile():
    file = {}
    for i in range(3):
        s = f.readline().strip('\n').strip('\t').strip().split('=')
        s[1] = s[1][1:-1]
        file[s[0]] = s[1]
        
    if file.get('source_path') != None and file.get('destination_path') != None and file.get('file_name') != None:
        return file
    return 'readError'

def fReplace(file):
    source_dir = os.path.join(file['source_path'], file['file_name'])
    dest_dir = os.path.join(file['destination_path'], file['file_name'])
    
    try:
        os.listdir(file['source_path'])
        os.listdir(file['destination_path'])
    except:
        return('dirError')
    
    if file['file_name'] in os.listdir(file['source_path']):
        os.replace(source_dir, dest_dir)
        if file['file_name'] in os.listdir(file['destination_path']):
            return('ok')
        else:
            return('replaceError')
    else:
        return(file['file_name'] + ' cant find')
    

def find():
    target = '/>'
    while True:
        line = f.readline()
        if line.strip() == '<file':
            return 'start'
        if line.strip() == '/>':
            return 'end'

        if line.strip() == '</config>' or line == '':
            return 'EOF'

    
log = []
f = open('config.xml')
if f.readline() == '<config>\n':

    while True:
        status = find()
        if status == 'start':
            file = readFile()
            if type(file) != dict:
                log.append('Read Error')
            else:
                log.append(fReplace(file))
            
        if status == 'EOF':
            break

f.close()
    

        
