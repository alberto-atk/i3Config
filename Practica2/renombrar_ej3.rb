=begin
Ejercicio 3. Escribir un script “renombrar” que renombre un conjunto de ficheros, posibilitando
el cambio de la extensión del fichero, siendo la sintaxis la siguiente:
./renombrar extensión-anterior nueva-extensión
El script deberá contemplar los posibles casos de error, como por ejemplo el paso de parámetros
correcto
=end




=begin
Usage: Check if a path exists
Name of method: checkDirectory
Date of creation: 08/04/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 08/04/2021
Parameters:
    Entry:
        - path: path that will be checked
    Out: 
        - boolean: True if exists
=end
def checkDirectory path
    return Dir.exist?(path)
end



=begin
Usage: List files of a directory
Name of method: listFiles
Date of creation: 08/04/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 08/04/2021
Parameters:
    Entry:
        - path: path that will be checked
    Out: 
        - List of files of path
=end
def listFiles path
    return `ls -l #{path}`
end


=begin
PREGUNTAR A VER LO DE LOS FICHEROS COMO SE PASAN Y ESO
Usage: Body of program
Date of creation: 08/04/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 08/04/2021
Parameters:
    Entry:
        - Argv: Parameter introduced by console when program is called
    Out: 
        - None
=end
if ARGV.length == 2
    current_extension = ARGV[0]
    new_extension = ARGV[1]    
    if checkDirectory path
        puts listFiles path
    else
        puts "Error, path is not correct"
    end
end