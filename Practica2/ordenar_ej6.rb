=begin
Ejercicio 6. Escribir un script en ruby donde el usuario pasará un conjunto de valores por
consola y automáticamente devolverá todos los valores sin ordenar por consola y
posteriormente ordenados. Su sintaxis será:
./ordenar.rb 13 5 6 7 0 -6
El script deberá contemplar todos los casos de error existentes, como podría ser el paso de algún
parámetro de tipo no numérico. ¿qué sucedería si le pasamos al script más de 10 parámetros?
Implementar las oportunas modificaciones para que lo soporte. 
=end

=begin
Usage: Check if the object passed is a number 
Name of method: is_number?
Date of creation: 15/04/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 15/04/2021
    - Now you can check all type of objects, not only Strings.
Parameters:
    Entry:
        - object: object to check
    Out: 
        - boolean: return true if the object is a number
=end
def is_number? object
    true if Float(object) rescue false 
end

    
=begin
Usage: Deletes from argv all elements that aren't numbers
Name of method: listFiles
Date of creation: 15/04/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 15/04/2021
Parameters:
    Entry:
        - argv: list of elements to check
    Out: 
        - aux: argv, only formed by numbers
=end
def cleanArgv argv
    aux = []
    argv.each do |element|
        if is_number? element
            aux.push(element)
        else
            puts "Error, #{element} is not a number"
        end
    end
    return aux
end


=begin
Usage: Generates a string from an array 
Name of method: generateStringFromArray
Date of creation: 15/04/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 15/04/2021
Parameters:
    Entry:
        - array: array of elements
    Out: 
        - string: string got from the array 
=end
def generateStringFromArray array
    puts ""
    string = ""
    array.each do |n|
        string += "#{n} "
    end
    return string
end


=begin
Usage: Body of the program
Date of creation: 15/04/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 15/04/2021
Parameters:
    Entry:
        - Argv: Parameter introduced by console when program is called
    Out: 
        - None
=end

if ARGV.length > 0
    argvCleaned = cleanArgv(ARGV)

    numbers = generateStringFromArray argvCleaned
    sortedNumbers = generateStringFromArray argvCleaned.sort
    
    puts "The numbers without sorting are: #{numbers}"
    puts "The sorted numbers are: #{sortedNumbers}"
else
    puts "Error, you have to pass parameters"
end
