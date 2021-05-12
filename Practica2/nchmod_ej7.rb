=begin
Ejercicio 7. Realizar un script en ruby denominado nchmod que nos visualice por el código en
decimal asociado a los permisos que le queramos dar a un fichero.
Ejemplo:
nchmod.rb r-sr-xr-x el resultado que devolverá será 4555
El script tendrá que controlar el número de caracteres insertados por el usuario, mostrando un
mensaje de error donde especifiquemos el uso
=end




=begin
Usage: doing nothing in a match
Name of method: pass
Date of creation: 22/04/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 22/04/2021
Parameters:
    Entry:
        - None
    Out: 
        - None
=end
def pass
end

=begin
Usage: Checks the firsts characters
Name of method: checkFirsts
Date of creation: 22/04/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 22/04/2021
Parameters:
    Entry:
        - characters: string to check
        - array: gets the number of permissions in octal
    Out: 
        - None
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
Usage: Checks the seconds characters
Name of method: checkSeconds
Date of creation: 22/04/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 22/04/2021
Parameters:
    Entry:
        - characters: string to check
        - array: gets the number of permissions in octal
    Out: 
        - None
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
Usage: Checks the seconds characters
Name of method: checkSeconds
Date of creation: 22/04/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 22/04/2021
Parameters:
    Entry:
        - characters: string to check
        - array: gets the number of permissions in octal
    Out: 
        - None
=end
def checkThirds characters, array
    for i in [3,6,9]
        if (i == 3) && (characters[i] == "x")
            array[1] = array[1] + 1
        elsif (i == 3) && (characters[i] == "s")
            array[0] = array[0] + 4
        elsif (i == 6) && (characters[i] == "x")
            array[2] = array[2] + 1
        elsif (i == 6) && (characters[i] == "s")
            array[0] = array[0] + 2
        elsif (i == 9) && (characters[i] == "x")
            array[3] = array[3] + 1 
        elsif (i == 9) && (characters[i] == "t")
            array[0] = array[0] + 1
        elsif (characters[i] == "-")
            pass
        else
            puts "Error, the letter #{characters[i]} does not belong to a permission"
            exit
        end
    end
end




=begin
Para la solucion de este ejercicio, se va a seguir el siguiente metodo de resolucion:
    - Se va a usar de ejemplo la cadena rwx-wxr-x.
    - Para el analisis de una cadena, se realizara de la siguiente forma:
        - checkFirsts --> analiza todas las primeras posiciones, es decir, r - r
        - checkSeconds --> analiza todas las segundas posiciones, es decir, w w -
        - checkThirds --> analiza todas las terceras posiciones, es decir, x x x
    - Mientras se analizan, se van sumando los valores a la posicion correspondiente del numero
=end

=begin
Usage: Body of the program
Date of creation: 22/04/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 22/04/2021
Parameters:
    Entry:
        - Argv: Parameter introduced by console when program is called
    Out: 
        - None
=end
if ARGV.length == 1
    characters = ARGV[0].chars
    if characters.length == 9
        permissions = [0,0,0,0]
        checkFirsts characters, permissions
        checkSeconds characters, permissions
        checkThirds characters, permissions
        puts permissions

    else
        puts "Error, the string is not correct (length is not 9)"
    end
else
    puts "Error 1 parameter is necessary to execute the script"
end

