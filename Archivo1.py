import datetime as dt
#si ponemos "git init" la carpeta donde lo allamos puesto, git trabajara con ellos, y saldran us 
ahora = dt.datetime.now() #al lado de los archivos y para guaradar el pogreso, pondremos 
#"git add Nombre del archivo" se guaradara los datos
print(f"estamos {ahora.day} del mes {ahora.month} del {ahora.year}.....")# Cuando se modifique archivos
print(f"Hora: {ahora.hour} --- Minutos: {ahora.minute} --- Segundos: {ahora.second}")
#aparecera una M y cuando los guardemos con "git add nombredelarchivo" se quitara la m y se pondra una A
# si ponemos git status saldra toda la informacion sobre si estan listo para ser enviados o no
#con el comando git commit -m "el cambio mas dastrico" se guradra en un repositotrio 
#simpre y cuando tus archivos esten con A