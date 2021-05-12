require 'nokogiri'
require 'open-uri'

=begin
Ejercicio 8. Construir un Web Crawler (rastreador, araña, o robot) en Ruby capaz de analizar
una página web concreta y que cree una base de datos con la información obtenida
=end

=begin
    Usage: Gets source code and urls from a page
    Name of method: getSoruceCode
    Date of creation: 29/04/2021
    Members: Roberto Jiménez y Alberto Pérez
    Last modification: 06/05/2021
    Parameters:
        Entry:
            - URL: Parameter of the program
        Out: 
            - list with urls without parsing
=end

def getSourceCode url
    # Gets source code from page
    parsed_data = Nokogiri::HTML.parse(URI.open(url))
    list = []
    puts parsed_data.class

    #Gets all urls  from source code
    tags = parsed_data.xpath("//a")
    tags.each do |tag|
        list.append("#{tag[:href]}\t#{tag.text}")    
    end
    return list
end

=begin
    Usage: Insert data received into a DB
    Name of method: insertDB
    Date of creation: 29/04/2021
    Members: Roberto Jiménez y Alberto Pérez
    Last modification: 06/05/2021
    Parameters:
        Entry:
            - list: list with urls
            - url: URL from page to analyze
        Out: 
            - None, output is saved in DB
=end

def insertDB list, url
    #Insert data into DB 
    `echo -n #{url} > aux.csv`
    `echo " ~" >> aux.csv`
    `echo #{list} >> aux.csv`
    `sudo mysql --local-infile=1 -h "localhost" -u rober "-prober"  < insertarBD.sql`
end

#Parse information with Grep command
list = getSourceCode ARGV[0]
parsedList = `echo #{list} | grep -E 'http[s]*://[a-zA-Z0-9./?@=%&:_#-]*'`
finalList =  parsedList.split(',')
insertDB finalList, ARGV[0]
for url in finalList    
    puts url
end

