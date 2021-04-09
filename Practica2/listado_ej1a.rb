=begin
Ejercicio 1a. Desarrollar un script donde se muestren los ficheros del pasado por
parámetro, así como los permisos asociados a cada uno de ellos, su identificador de usuario, su
identificador de grupo, así como permisos como “Setuid, Setgid, o hasta incluso si tiene activo
el bit sticky bit”.
Sintaxis: listado.rb [Dir]
 Dir será opcional de forma que si el usuario no lo inserta el script buscará en el directorio actual
 El script deberá capturar todas las posibles excepciones como pueden ser:
a. Debe permitir el paso de parámetros con una sintaxis correcta
b. Si se produce alguna excepción grave a la hora de la búsqueda en sí, el script deberá
comunicarlo.
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
if ARGV.length == 1
    path = ARGV[0]    
    if checkDirectory path
        puts listFiles path
    else
        puts "Error, path is not correct"
    end
end