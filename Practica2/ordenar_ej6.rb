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
Usage: Sort 
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
def is_number? object
    true if Float(object) rescue false 
end



=begin
Usage: Sort 
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
def sortParameters argv
    aux = []
    j = 0
    for i in(argv.length)
        if is_number? argv[i]
            aux[j] = argv[i]
            puts "#{aux[j]}"
            j++
        
    
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
sortParameters(ARGV)