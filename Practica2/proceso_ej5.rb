=begin
Ejercicio 5. Desarrollar un script que nos muestre por consola información relevante del
identificador de proceso que el usuario inserte por consola.
Sintaxis: proceso.rb
El script deberá mostrar la siguiente información del proceso: identificador UID, propietario
PID, PPID, Prioridad absoluta ”C” , Prioridad Relativa “PRI” y la Dirección en memoria o en
disco del proceso “ADDR”
=end


=begin
    Usage: Body of code program who shows info about a process id    
    Name of method: 
    Date of creation: 10/04/2021
    Members: Roberto Jiménez y Alberto Pérez
    Last modification: 10/04/2021
    Parameters:
        Entry:
            - None, only a parameter passed by ARGV
        Out: 
            - None, output is shown in terminal
=end
if ARGV.length == 0
    puts 'Error, a process id is necesary'
elsif ARGV.length == 1    
    query = 'ps -o uid,pid,ppid,c,pri,addr ' + ARGV[0]
    result = `#{query}`
    puts result
else
    puts 'Error, only process id parameter is necessary'
end
