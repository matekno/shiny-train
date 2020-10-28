import time
import re
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import requests
import json
def api():
    nombres = ['att_oficial','agusbob','bgiulietti','bibaboy','theblackjackgm','bstrdd','CABRA_SAFADO','candexnegri','capiow','caronigro','Carreraaa','Cawelag','coloradaxx','elpibecs1','erivillalva','Facubanzas','Forg1','Francobertello','frankkaster','ggnia','Godeto','hastad','iberru','immortal','heyitsjoe','IvoXxX','knut','lajefaok','lepajee','lucascristalino','luckraok','luquitarodriguez','malaso','markitonavaja','Momo','Nanocs','negrogatuxx','ninhafps','oAdanarg','robergalati','rojankhzxr','yuyumartinez','sajucsgo','seleneitor','Sionaron','submerzed','thebestiaoficial','themasterrodrigo','tuli_acosta','vgorefs','vovo','vroep','xandfps','xposed','RiiSki','Sr_ThuliuM','nosoynano','frostezor','sksfps1','snugtoes','jjuandamoli','yungshapez','Pulmonary0','jasonr']
    headers = {
        'client-id': 'ztiu0ovky0u70jxdj6qm6yq3gfv2kj',
        'Authorization': 'Bearer lozf40azik5h579m2sepvp1t0y3mcp',
    }
    inactivos=list()
    for nombre in nombres:
        params = (
            ('query', nombre),
        )

        response = requests.get('https://api.twitch.tv/helix/search/channels', headers=headers, params=params)
        rjson = response.json()
        #print(rjson['data'][0]['game_id'],rjson['data'][0]['is_live'])


        if (rjson['data'][0]['game_id'] =='498566' or rjson['data'][0]['game_id'] =='29452' or rjson['data'][0]['game_id'] =='509658' ) and rjson['data'][0]['is_live'] == True:
            inactivos.append('activo')
        else:
            inactivos.append('inactivo')
    return inactivos

'''
lista=api()
print(lista)

'''