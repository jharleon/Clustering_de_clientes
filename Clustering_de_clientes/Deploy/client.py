
from tracemalloc import start
import requests
import json
import time




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



'''O app irá perguntar ao cliente se ele deseja inserir os dados ou usar os dados já definidos em teste.
Caso os dados sejam inseridos, ao final da execução do programa irá retorna o resultado do modelo de'''

print('-------------------X-------------------')
print('     Digite a váriaveis de entrada ')
print('-------------------X-------------------')

resposta = input('Se deseja inputar as variáveis testes pressione s ')
if resposta == 's':
        data = json.dumps(data)
        start = time.time()
        send_request = requests.post(url, data)

        tempo_resposta = time.time()-start
        print("tempo de resposta: ", round(tempo_resposta,2))
        print(send_request)
        print(send_request.json())
        #print(type(send_request))
        exit
else:
                
        
        recencias = input('Recencias: ')
        frequencias = input('Frequências: ')
        valores = input('Valores: ')
        produto = input('Produto')
        categoria = input('Categoria: ')
        sub_categoria = input('Sub Categoria')
        item = input('Item: ')
        ship_first_classes = input('Ship First Classes: ')
        ship_second_classes = input('Ship Second Clases')
        ship_standard_classes= input('Ship Standard Classes')
        ship_same_days = input('Ship Same Days')
        segment_consumers = input('Segment Consumers')
        segment_corporates = input('Segment Corporates')
        segment_homeoffices = input('Segment HomeOffices')
        itens_furnitures = input('Itens Furnitues')
        itens_offices = input('Itens Offices: ')
        itens_techs = input('Itens Tech: ')



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



        data = json.dumps(data)
        start = time.time()
        send_request = requests.post(url, data)

        
        tempo_resposta = time.time()-start
        print("tempo de resposta: ", round(tempo_resposta,2))
        print(send_request)
        print(send_request.json())
        #print(type(send_request))



'''
if send_request == 0:
        print('Cluster 0 = Cliente desengajado')

elif send_request == 1:
        print('Cluster 1 = Cliente promissor')


elif send_request == 2:
        print('Cluster 2 = Cliente fiel (necessário atenção)')

elif send_request == 3:
        print('Cluster 3 = Cliente fiel')

else:
        print('Cluster 4 = Cliente em risco')

'''