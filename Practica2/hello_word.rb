

=begin
 Pruebas de todo en ruby   
=end
    
def listFiles x
    #exec ("ls -l "  + x)
    query = 'ls -l ' + x
    resul = `#{query}` #con `#{nombreVariable}` ejecutas y guardas el resultado en una variable
    puts resul
end
#para poner comentarios se ponen asi, print para no poner espacios
v1 = ARGV[0]
v2 = ARGV[1]
for arg in ARGV
    puts arg
end
if ARGV.length == 1
    puts "SOLOL 1"
    if File.directory?(ARGV[0]) and Dir.exist?(ARGV[0])
        puts "is directory"
    else
        puts "not a directory"
    end
end
puts "HOLA MUNDO " + v1 +" " 
puts (3 + 2)
#s = `ls -l /home/rober`
#puts(s)
listFiles '/home/'
