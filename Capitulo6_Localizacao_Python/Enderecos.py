from pygeocoder import Geocoder

endereco = 'avenida paulista 100 Sao Paulo'
resultado = Geocoder('AIzaSyAIY0coggbHzTCe5rGF86FLUKXWKwyPMM').reverse_geocode(endereco)
print(resultado)
