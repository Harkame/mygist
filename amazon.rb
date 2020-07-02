require 'net/http'

uri = URI('https://www.amazon.fr/dp/B07YFW75X9')
response = Net::HTTP.get(uri)
puts response.body
