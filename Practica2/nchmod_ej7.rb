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
def pass
end

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
def checkFirsts characters, array

    for i in [1,4,7]
        if (i == 1) && (characters[i] == "r")
            array[1] = array[1] + 4
        elsif (i == 4) && (characters[i] == "r")
            array[2] = array[2] + 4
        elsif (i == 7) && (characters[i] == "r")
            array[3] = array[3] + 4   
        elsif (characters[i] == "-")
            pass
        else
            puts "Error, the letter #{characters[i]} does not belong to a permission"
            exit
        end
    end
end



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
def checkSeconds characters, array
    for i in [2,5,8]
        if (i == 2) && (characters[i] == "w")
            array[1] = array[1] + 2
        elsif (i == 5) && (characters[i] == "w")
            array[2] = array[2] + 2
        elsif (i == 8) && (characters[i] == "w")
            array[3] = array[3] + 2 
        elsif (characters[i] == "-")
            pass
        else
            puts "Error, the letter #{characters[i]} does not belong to a permission"
            exit
        end
    end
end

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
def checkThirds characters, array
    for i in [3,6,9]
        if (i == 3) && (characters[i] == "x")
            array[1] = array[1] + 1
        elsif (i == 6) && (characters[i] == "x")
            array[2] = array[2] + 1
        elsif (i == 9) && (characters[i] == "x")
            array[3] = array[3] + 1 
        elsif (characters[i] == "-")
            pass
        else
            puts "Error, the letter #{characters[i]} does not belong to a permission"
            exit
        end
    end
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
    characters = ARGV[0].chars
    if characters.length == 10
        permissions = [0,0,0,0]
        checkFirsts characters, permissions
        checkSeconds characters, permissions
        checkThirds characters, permissions
        puts permissions

    else
        puts "Error, the string is not correct (len is not 9)"
    end
else
    puts "Error 1 parameter is necessary to execute the script"
end