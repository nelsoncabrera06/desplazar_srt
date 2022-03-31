import sys
import re
import datetime

print (sys.argv)

filepath = ''
segundos = 0

if len(sys.argv) < 3:
    print('debe ingresar argumentos "path" "segundos_a_desplazar"')
    filepath = input('File path: ')
    segundos = int(input('Seconds: '))
    #raise SystemExit
    print(filepath + ' ------> seg: ' + str(segundos))
    
else:
    filepath =  sys.argv[1]
    segundos =  int(sys.argv[2])

f = open(filepath)
regex = "([\S\s]+)\/[\S\s]+.srt"
ruta = re.sub(regex,r"\1", filepath)

fout = open(ruta + "/desplazado.srt", "w")

Lines = f.readlines()
print("Total lines in file: " + str(len(Lines)))

def desplazar(t,d):
    date_and_time = datetime.datetime.strptime(t, "%H:%M:%S,%f")
    d = date_and_time + datetime.timedelta(seconds=d)
    new_time = str(d.strftime('%H:%M:%S,%f'))[:-3]
    return new_time
    
def analizar(l):
    #l = "00:00:49,091 --> 00:00:50,967"

    regex = " --> "
    time = re.search(regex, l)

    if time:
        #print(l)
        cadena = re.split(regex, l)
        start = cadena[0]
        end = cadena[1]
        #segundos = 3

        new_start = desplazar(start,segundos)
        new_end = desplazar(end,segundos)

        new_line = new_start + " --> " + new_end
        #print(new_line)
        fout.write(new_line + '\n')
    else:
        fout.write(l + '\n')

    

    """
    start = re.sub(r"The (\w+) in Spain", r"\1", txt)
    txt = "The rain in Spain"
    x = re.sub(r"The (\w+) in Spain", r"\1", txt)
    print(x)
    """
    
count = 0
# Strips the newline character
#for line in range(50):
for line in Lines:
    linea = Lines[count].strip()
    analizar(linea)
    count += 1
    porcentaje = count / len(Lines)
    #print("{0:.2f}%".format(porcentaje * 100) + " - " + str(count) + " of " + str(len(Lines)))


fout.close()
f.close()