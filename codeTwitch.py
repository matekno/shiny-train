import time
import re
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
import funciones
import apiTwitch
#import twitch
import datos

driver = datos.loginDS()
linkBase = 'https://www.twitch.tv/popout/'
linkExtra ='/chat?popout='

nombres = ['att_oficial','agusbob','bgiulietti','bibaboy','theblackjackgm','bstrdd','CABRA_SAFADO','candexnegri','capiow','caronigro','Carreraaa','Cawelag','coloradaxx','elpibecs1','erivillalva','Facubanzas','Forg1','Francobertello','frankkaster','ggnia','Godeto','hastad','iberru','immortal','heyitsjoe','IvoXxX','knut','lajefaok','lepajee','lucascristalino','luckraok','luquitarodriguez','malaso','markitonavaja','Momo','Nanocs','negrogatuxx','ninhafps','oAdanarg','robergalati','rojankhzxr','yuyumartinez','sajucsgo','seleneitor','Sionaron','submerzed','thebestiaoficial','themasterrodrigo','tuli_acosta','vgorefs','vovo','vroep','xandfps','xposed','RiiSki','Sr_ThuliuM','nosoynano','frostezor','sksfps1','snugtoes','jjuandamoli','yungshapez','Pulmonary0','jasonr']

cantidadCanales = len(nombres)
inactivos = list()

mensajeViejo = ''


codesNuevos = list()
codesNuevos = range(cantidadCanales)
codesViejos = list()
codesViejos = range(cantidadCanales)






funcionesCodes =  ['code0', 'code1', 'code2', 'code3', 'code4', 'code5', 'code6', 'code7', 'code8', 'code9', 'code10', 'code11', 'code12', 'code13', 'code14', 'code15', 'code16', 'code17', 'code18', 'code19', 'code20', 'code21', 'code22', 'code23', 'code24', 'code25', 'code26', 'code27', 'code28', 'code29', 'code30', 'code31', 'code32', 'code33', 'code34', 'code35', 'code36', 'code37', 'code38', 'code39', 'code40', 'code41', 'code42', 'code43', 'code44', 'code45', 'code46', 'code47', 'code48', 'code49', 'code50', 'code51', 'code52', 'code53', 'code54', 'code55', 'code56', 'code57', 'code58', 'code59', 'code60', 'code61', 'code62','code63']
delay = time.time() + 60*15
contador = 0
glosario=list()
codigoEnviado=''
while True:

    if time.time() >=delay or contador == 0:
        contador+=1
        delay = time.time() + 60 * 15
        interacion = 0
        inactivos = apiTwitch.api()
        print(inactivos)
        for i in range(cantidadCanales):
            if (inactivos[i] == 'inactivo'): continue
            driver.execute_script(f"window.open('about:blank','{nombres[i]}');")
            driver.switch_to.window(nombres[i])
            driver.get(linkBase + str(nombres[i]) + linkExtra)
    else:
        for i in range(cantidadCanales):

            if(inactivos[i] == 'inactivo'): continue
            try:
                driver.switch_to.window(nombres[i])
                html = driver.page_source
                soup = bs(html, "html.parser")
                mensajes = soup.findAll(class_='text-fragment')
                texto = mensajes[-1].text
                #print(texto)
            except:
                #print(1000000000000)
                continue
            if (mensajeViejo == mensajes): continue
            mensajeViejo = mensajes
            streamer = getattr(funciones, funcionesCodes[i])  # get attributte
            codesNuevos = streamer(texto, codesViejos[i])
            if codesNuevos is glosario:continue
            glosario.append(codesNuevos)
            print(glosario)
            if type(codesNuevos) == int: continue
            print('hay code muchachos!')
            try:
                if codigoEnviado==codesNuevos: continue
                codigoEnviado=codesNuevos
                discord = driver.window_handles[0]
                driver.execute_script("window.open('about:blank', 'lazabot');")
                driver.switch_to.window("lazabot")
                driver.get('https://discord.com/channels/769427364362584104/769431300057858069')
                wait = WebDriverWait(driver, 60)
                element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'markup-2BOw-j')))
                driver.find_elements_by_class_name("markup-2BOw-j")[-1].send_keys(codesNuevos + Keys.ENTER)
                driver.switch_to.window(discord)  # para que vuelva al server inicial
            except:
                print(1)


