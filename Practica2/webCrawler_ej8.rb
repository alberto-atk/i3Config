require 'nokogiri'
require 'open-uri'

=begin 

=end
parsed_data = Nokogiri::HTML.parse(URI.open(ARGV[0]))
lista = []
puts parsed_data.class
tags = parsed_data.xpath("//a")
tags.each do |tag|
    lista.append("#{tag[:href]}\t#{tag.text}")
    #puts "#{tag[:href]}\t#{tag.text}"
end
lista2 = `echo #{lista} | grep -E 'http[s]*://[a-zA-Z0-9./?@=%&:_#-]*'`
lista3 =  lista2.split(',')
for linea in lista3
    auxLinea = linea.split()
    #puts auxLinea[0] 
    #puts  auxLinea[1]
    puts linea
end
#puts tags
#ruby webCrawler_ej8.rb https://moodle.unizar.es/add/ | grep -E 'https://[a-zA-Z0-9./?@=%&:_#-]*' 
#https://www.rubyguides.com/2012/01/parsing-html-in-ruby/