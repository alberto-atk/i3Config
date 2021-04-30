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
Usage: List a directory passed by path
Name of method: listDirectory
Date of creation: 08/04/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 08/04/2021
Parameters:
    Entry:
        - path: path of the directory to list
    Out: 
        - list: result from ls if directory has reading permissions
=end
def listDirectory path
    if File.readable?(path)
        list = `ls #{path}`
        return list.split(" ")
    end 
    return ["Error, directory has not reading permissions"]
end


=begin
Usage: List all directories starting from path
Name of method: listDirectories
Date of creation: 08/04/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 9/04/2021
    - Added different colors in terminal for directories, files...
Parameters:
    Entry:
        - path: path that will be checked
    Out: 
=end
def listDirectories path
    auxDirectories = []
    files = listDirectory path
    puts "\e[1;34m#{path}\e[m"
    files.each do |element|
        newPath = path + "/" + element
        if checkDirectory newPath
            puts "\e[1;36m#{newPath}\e[m"
            auxDirectories.push(newPath)
        else
            puts "\e[1;37m#{element}\e[m"
        end
    end

    puts "\e[1;37m\n\e[m"

    auxDirectories.each do |directory|
        listDirectories directory   
    end
end


=begin
Usage: Body of the program
Date of creation: 08/04/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 08/04/2021
Parameters:
    Entry:
        - Path: Parameter requested from the user
    Out: 
        - None
=end
puts "Put the directory path  to list"
path = gets.chomp

if checkDirectory path
    listDirectories path
else
    puts "Error, path is not correct"
end