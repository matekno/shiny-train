from selenium import webdriver
import time
import re
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datos
driver = webdriver.Chrome(executable_path=r"chromedriver.exe")

driver = datos.loginDS()

driver.get('https://twitter.com/Roobet')
codigoViejo = ''
mensajeViejo = ''
#input("presione enter: ")
time.sleep(4)
entro= False
codesGuardados=list()


while True:

    html = driver.page_source
    soup = bs(html, "html.parser")
    # print(soup)
    mensajes = soup.findAll(class_="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")
    #print(mensajes)

    for i in mensajes:
        codeNuevo = i.text
        mensajeNuevo = i.text
        #print(codeNuevo)
        if mensajeNuevo == mensajeViejo: continue
        mensajeViejo=mensajeNuevo
        if codeNuevo == codigoViejo : continue
        codigoViejo = codeNuevo
        try:
            if re.search('se code',codeNuevo):
                print('buenas!')
                entro = True
                break

            else:
                continue
        except:
            print(1)
            continue


    if entro == False: continue
    if codeNuevo in codesGuardados:continue
    codesGuardados.append(codeNuevo)
    #mandando al otro server:
    discord = driver.window_handles[0]
    driver.execute_script("window.open('about:blank', 'lazabot');")
    driver.switch_to.window("lazabot")
    driver.get('https://discord.com/channels/769427364362584104/769431300057858069')
    wait = WebDriverWait(driver, 60)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'markup-2BOw-j')))
    driver.find_elements_by_class_name("markup-2BOw-j")[-1].send_keys(codeNuevo + Keys.ENTER)
    driver.switch_to.window(discord)  # para que vuelva al server inicial


