

=begin

=end
def checkDirectory path
    return Dir.exist?(path)
end


=begin

=end
def listFiles path
    return `ls -l #{path}`
end

=begin
 
=end
if ARGV.length == 1
    path = ARGV[0]    
    if checkDirectory path
        puts listFiles path
    else
        puts "Error, path is not correct"
    end
end