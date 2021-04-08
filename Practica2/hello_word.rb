

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

=begin
Documentacion
https://www.xn--linuxenespaol-skb.com/tutoriales/como-instalar-ruby-ubuntu/
https://makeitrealcamp.gitbook.io/ruby-book/primeros-pasos#:~:text=Nuestro%20primer%20programa,%C3%81brela%20con%20tu%20editor%20preferido.&text=Deber%C3%ADas%20ver%20la%20cadena%20de,Hola%20mundo%22%20en%20la%20consola.
https://stackoverflow.com/questions/41547162/ruby-and-shell-get-the-same-output-with-ls
https://www.rubyguides.com/2018/12/ruby-system/
http://es.railsbridge.org/ruby/ejecutar_programas_desde_un_archivo
https://www.honeybadger.io/blog/capturing-stdout-stderr-from-shell-commands-via-ruby/
https://stackoverflow.com/questions/9211813/is-there-a-way-to-access-method-arguments-in-ruby
https://zetcode.com/lang/rubytutorial/variables/
https://www.reddit.com/r/ruby/comments/35h41s/run_shell_command_and_save_its_output_in_ruby/
https://stackoverflow.com/questions/8159014/ruby-execute-bash-command-with-variables
https://stackoverflow.com/questions/4244611/pass-variables-to-ruby-script-via-command-line
https://code-maven.com/argv-the-command-line-arguments-in-ruby
https://stackoverflow.com/questions/1085218/how-to-check-if-a-given-directory-exists-in-ruby
https://www.tutorialspoint.com/ruby/ruby_if_else.htm
https://www.ruby-forum.com/t/manejo-de-comentarios/133169
    
=end