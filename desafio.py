import requests
import json
import hashlib

def main():
  url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=SEU_TOKEN'
  
  setMensage()
  decoder()
  sha1()
  arquivo = setAnswer()
  files = {"answer": open("answer.json", "rb")}
  response = requests.post(url, files=files)
  print(response.text)

def setMensage():
  url = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=SEU_TOKEN"
  resposta = requests.get(url)
  dado = resposta.json()
  dado = json.dumps(dado, indent=4)
  arquivo = open("answer.json", "w")#abrindo o arquivo para escrita
  arquivo.write(dado)#escrevendo no arquivo
  arquivo.close()#fechando o arquivo

def getMensage():
    arquivo = open("answer.json", "r")#abrindo o arquivo para leitura
    data = json.load(arquivo)#converte e lê
    menCrip = data['cifrado']
    return menCrip.lower()

def decoder():
  menCrip = getMensage()
  numero_casas = 9
  alfa = 'abcdefghijklmnopqrstuvwxyz'
  x = 0
  menDescrip = ''
  for x in range(len(menCrip)):
    for y in range(len(alfa)): 
      if menCrip[x] == alfa[y]:
        pos =  y - numero_casas
        if pos >= len(alfa):
          i = pos - len(alfa)
          menDescrip += alfa[i]
          break
        else:
          menDescrip += alfa[pos]
          break
      if menCrip[x] == ' ' or menCrip[x] == '.':
        menDescrip += menCrip[x]
        break
  return menDescrip

def sha1():
  mensage = decoder()
  resul = hashlib.sha1(mensage.encode())#converte no equivalente de byte
  resCrip = resul.hexdigest()#gera sequencia equivalente hexadecimal
  return resCrip

def setAnswer():
  decifrado = decoder()
  resumo_crip = sha1()
  dado = {
    "numero_casas": 9,
    "token": "SEU_TOKEN",
    "cifrado": "yjbcrwp lxmn oaxv cqn rwcnawnc rwcx yaxmdlcrxw lxmn rb urtn lqnfrwp pdv oxdwm rw cqn bcannc. dwtwxfw", 
    "decifrado":decifrado, 
    "resumo_criptografico": resumo_crip
  }
  dado = json.dumps(dado, indent=4)
  arquivo = open("answer.json", "w")
  arquivo.write(dado)
  arquivo.close()

  return arquivo

if __name__=="__main__":
  main()
