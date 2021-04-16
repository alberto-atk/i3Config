=begin
Ejercicio 3. Escribir un script “renombrar” que renombre un conjunto de ficheros, posibilitando
el cambio de la extensión del fichero, siendo la sintaxis la siguiente:
./renombrar extensión-anterior nueva-extensión
El script deberá contemplar los posibles casos de error, como por ejemplo el paso de parámetros
correcto
=end

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
def listFiles extension
    list = []
    list =  `ls *.#{extension} | nl`
    return list.split("\n")
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
def renameFile fileName, new_extension
    auxName = fileName.split(".")
    onlyName = auxName[0]
    `mv #{fileName} #{onlyName}.#{new_extension} `
    return "#{onlyName}.#{new_extension}"
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
if ARGV.length == 2
    current_extension = ARGV[0]
    new_extension = ARGV[1]    

    files = listFiles current_extension
    puts "Files available for rename: "
    puts files
    puts "Select the number of the file to rename: "
    fileToRename = (STDIN.gets.chomp.to_i - 1)
    
    if (fileToRename >= 0) && (fileToRename < files.length)
        auxFile = files[fileToRename].split(" ")
        renamedFile = renameFile auxFile[1], new_extension
        puts "#{auxFile[1]} renamed to: #{renamedFile}"
    else
        puts "Error, number of file invalid"
    end
end