from pygeocoder import Geocoder

endereco = '1222, Lins de Vasconcelos, Sao Paulo, SP'
print(Geocoder('AIzaSyAIY0coggbHzTCe5rGF86FLUKXWKwyPMM').geocode(endereco).cooordinates)
