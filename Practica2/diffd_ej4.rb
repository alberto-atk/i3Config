

=begin
    Usage: Check if a path exists
    Name of method: checkDirectory
    Date of creation: 09/04/2021
    Members: Roberto Jiménez y Alberto Pérez
    Last modification: 09/04/2021
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
    Usage: Get parameters from ARGV
    Name of method: getParameters
    Date of creation: 09/04/2021
    Members: Roberto Jiménez y Alberto Pérez
    Last modification: 09/04/2021
    Parameters:
        Entry:
            - None
        Out: 
            - Array with parameters passed
=end

def getParameters
    array = []
    i = 0
    for arg in ARGV
        array[i] = arg
        i = i + 1
    end
    return array
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
def listFiles path
    list = []
    list = `ls #{path}`
    return list.split("\n")
end


=begin
    Usage: Remove directory name from a list of files
    Name of method: removeDirectory
    Date of creation: 09/04/2021
    Members: Roberto Jiménez y Alberto Pérez
    Last modification: 09/04/2021
    Parameters:
        Entry:
            - list: list that will be checked
        Out: 
            - Same list without directory names
=end
def removeDirectory list, dir
    newList = []
    
    for i in list
        path= dir + '/' + i
        if !checkDirectory path            
            newList.push(i)                    
        end
    end
    return newList
end

=begin
    Usage: Compare 2 directories to see if exists 
    file with the same name and reverse
    Name of method: diff
    Date of creation: 09/04/2021
    Members: Roberto Jiménez y Alberto Pérez
    Last modification: 09/04/2021
    Parameters:
        Entry:
            - dir1: first directory to check
            - dir2: second directory to check
            - reverse: boolean, to see if -r option is enabled
        Out: 
            - None
=end
def diff dir1, dir2, reverse

    filesDir1 = removeDirectory (listFiles dir1), dir1    
    filesDir2 = removeDirectory  (listFiles dir2), dir2        
            
    for i in filesDir1
        if filesDir2.include?(i) and reverse
            puts i + ' is in both directories'
        elsif !filesDir2.include?(i) and !reverse
            puts i + ' is only in ' + dir1
        end            
    end
    for i in filesDir2
        if !filesDir1.include?(i) and !reverse           
            puts i + ' is only in ' + dir2
        end
    end
end


list = getParameters
actualDir = `pwd`

case list[0]
when "-r"    
    if list.length == 3 and checkDirectory list[1] and checkDirectory list[2]        
        diff list[1], list[2], true

    elsif list.length == 2 and checkDirectory list[1]        
        diff list[1], actualDir, true
    else
        puts 'Syntax error, correct syntax:  ruby diffd_ej4.rb [-r] dir1 [dir2]'
    end
else
    case list.length
    when 0
        puts 'Error, it must be a directory into a parameters'
        puts 'Syntax: ruby diffd_ej4.rb [-r] dir1 [dir2]'
    when 1
        if checkDirectory list[0]                                  
            diff list[0], actualDir, false

        else
            puts 'Error, ' + list[0] + ' is not a directory'
        end
    when 2
        if checkDirectory list[0] and checkDirectory list[1]            
            diff list[0], list[1], false

        elsif checkDirectory list[0]
            puts 'Error, ' + list[1] + ' is not a directory'
        elsif checkDirectory list[1]
            puts 'Error, ' + list[0] + ' is not a directory'
        end
    else
        puts 'Too many arguments'
    end    
end

