
from tracemalloc import start
import requests
import json
import time


# url local - definida no app.py - executada pelo Flask
url = 'http://127.0.0.1:5000'

# parâmetros de entrada:
recencias = 190
frequencias =4.5
valores =800
produto = 300 
categoria = 3
sub_categoria = 6
item = 8
ship_first_classes=210 
ship_second_classes=270
ship_standard_classes=799 
ship_same_days=73
segment_consumers=156
segment_corporates=75 
segment_homeoffices=55 
itens_furnitures=1.5
itens_offices=5
itens_techs=2

# dados da chamada ao serviço
data = {'recencia': recencias, 
        'frequencia': frequencias , 
        'valor': valores, 
        'produtos': produto , 
        'categoria': categoria,
        'sub-categorias': sub_categoria , 
        'itens': item, 
        'ship_first_class': ship_first_classes, 
        'ship_second_class': ship_second_classes,
        'ship_standard_class': ship_standard_classes, 
        'ship_same_day': ship_same_days, 
        'segment_consumer': segment_consumers,
        'segment_corporate': segment_corporates, 
        'segment_homeoffice': segment_homeoffices, 
        'itens_furniture': itens_furnitures ,
        'itens_office': itens_offices, 
        'itens_tech': itens_techs}

print({'recencia': recencias, 
        'frequencia': frequencias , 
        'valor': valores, 
        'produtos': produto , 
        'categoria': categoria,
        'sub-categorias': sub_categoria , 
        'itens': item, 
        'ship_first_class': ship_first_classes, 
        'ship_second_class': ship_second_classes,
        'ship_standard_class': ship_standard_classes, 
        'ship_same_day': ship_same_days, 
        'segment_consumer': segment_consumers,
        'segment_corporate': segment_corporates, 
        'segment_homeoffice': segment_homeoffices, 
        'itens_furniture': itens_furnitures ,
        'itens_office': itens_offices, 
        'itens_tech': itens_techs})

data = json.dumps(data)
start = time.time()
send_request = requests.post(url, data)
print("tempo de resposta: ", time.time()-start)
print(send_request)
print(send_request.json())