import requests
import telegram
import mss
import numpy as np
import sys
import time
import os
from os import listdir
import tkinter as tk
import flask

#print("Insira ChatID")
global chatID
#chatID = input(str())
escolhaAnuncio = 0
anuncioEntrada = 1
anuncioSaida = 2
anuncioCovid = 3
retAnuncio = 4
diaAtual = 0
unidadeUEOP = 0
alaDia = 0
efetOficial = 0
efetSubSgt = 0
efetCbSd = 0
chefeServico = 0
pathViaturas = r"C:\Users\eitin\source\repos\AnunciosDiarios\AnunciosDiarios\Lista Viaturas.txt"
pathEquipamentos = r"C:\Users\eitin\source\repos\AnunciosDiarios\AnunciosDiarios\Lista Equipamentos.txt"



#listaViaturas = np.loadtxt(pathViaturas, dtype=str)
#listaEquipamentos = np.loadtxt(pathEquipamentos, dtype = str)

#viaturasArray = np.array(listaViaturas)
#equipamentosArray = np.array(listaEquipamentos)

with open('ListaEquipamentos.txt','r') as f:
	listaEquipamentos = [line.strip() for line in f]
	
with open('ListaEquipamentos.txt','r') as aP:	
	arrayEquipamentos = [line.strip() for line in aP]


with open('ListaViaturas.txt','r') as g:
	listaViaturas = [line.strip() for line in g]

with open('ListaViaturas.txt','r') as aV:
	arrayViaturas = [line.strip() for line in aV]

#USANDO LINE.STRIP AS PAGINAS ESTAO LENDO CADA LINHA COM O ESPACO, AGORA LEMBRAR DE ATRIBUIR CADA POSICAO UMA VARIAVEL
#ATRIBUIR CADA VIATURA UMA VARIAVEL E TRABALHOSO E DEXA O CODIGO NAO ATUALIZAVEL

#usar o while para criar as variaveis da lista
#cria excessivas variaveis


	

#"1700341008" Chat ID Sgt silvestre
#"1098462734" Chat ID Sd Nicollas
chatIDSilvestre = 1700341008
chatIDNicollas =  1098462734



def telegram_bot_sendtext(bot_message):
	chatId = input("\nDigite o ChatID\n")
	bot_token = "##"

	bot_chatID = chatId
	send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
	response = requests.get(send_text)
	return response.json()

#test = telegram_bot_sendtext("🔌 Teste do Bot 3ala Caratinga!!!")




def funcaoCovid():
	
	
	return




def tipoAnuncio(escolhaAnuncio):
	if escolhaAnuncio == 0:
		print ("Favor realizar uma escolha valida")
		return escolhaAnuncio
	if escolhaAnuncio == 1:
		print ("Voce escolheu anuncio de entrada!")
		diaAtual = input("\n \n Digite o dia atual no formato dd/mm/aaaa \n")
		unidadeUEOP = input ("\n Digite a unidade/fracao no formao x Pel/y Cia/ Nome do Pelotao \n")
		alaDia = input("\n Digite a Ala de servico '(Somente o numero da ala 1234)'\n")
		#efetOficial = int(input("\n Digite a quanitade  de oficiais no Servico OPERACIONAL \n"))
		efetSubSgt = int(input("\n Digite a quanitade  de Sub/SGT no Servico OPERACIONAL \n"))
		efetCbSd = int(input("\n Digite a quantidade  de Cb/Sd no Servico OPERACIONAL \n"))
		chefeServico = input("\n Digite P/G e NOME DE GUERRA do Chefe de Servico \n")
		funcaoEntrada(diaAtual,unidadeUEOP,alaDia,efetSubSgt,efetCbSd,chefeServico)
		escolhaAnuncio = -1
		return escolhaAnuncio
	if escolhaAnuncio == 2:
		print("Voce escolheu Anuncio de Saida")
		diaAtual = input("\n \n Digite o dia atual no formado dd/mm/aaaa \n")
		unidadeUEOP = input ("\n Digite o nome da Unidade \n")
		alaDia = input("\n Digite a Ala de servico '(Somente o numero da ala 1234)'\n")
		funcaoSaida(diaAtual,unidadeUEOP,alaDia)
		return
	else:
		print("\n Escolha Ivalida \n")
		escolhaAnuncio = int(input("\n Escolha o tipo de anuncio \n"))
		return 
	return

def main():
    time.sleep(2)
    last = {
        "userChoice" : 0,
        "timesError" : 0,
    }



    escolhaAnuncio = int(input("\n Escolha o tipo de Anuncio, DIGITAR SOMENTE NUMEROS \n"))


    
    while escolhaAnuncio != -1:
        tipoAnuncio(escolhaAnuncio)
        return False
    return
def funcaoEntrada(diaAtual,unidadeUEOP,alaDia,efetSubSgt,efetCbSd,chefeServico):
    efetTotal = efetSubSgt+efetCbSd+efetOficial
    print("\nLista de viaturas\n")
    print("\nDigite somente ECD, Baixada ou Restricao - Motivo\n")
    i=0
    while (i<len(listaViaturas)):
        arrayViaturas[i] = ": "+str(input(listaViaturas[i]+": "))+"\n"
        i+=1
    i=0
    print("\nLista de equipamentos\n")
    print("\nDigite a quantidade de cada equipamento presente na carga\n")
    k = 0
    
    
    while (k<len(listaEquipamentos)):
        arrayEquipamentos[k]= ": "+str(input(listaEquipamentos[k]+": "))+"\n"
        k+=1



    listaFullViaturas = [i+j for i,j in zip(listaViaturas,arrayViaturas)]
    listaFullEquipamentos = [i+j for i,j in zip(listaEquipamentos,arrayEquipamentos)]
    stringFullviaturas = ''.join([str(item) for item in listaFullViaturas])
    stringFullEquipamentos = ''.join([str(item) for item in listaFullEquipamentos])


    obs = str(input("Observacoes: \n"))
    confirmaAnuncio = str(input("\n \n \nCONFIRME O TEXTO ABAIXO \n \n \n"+"Bom dia Senhor\nSegue anúncio do dia "+str(diaAtual)+"\n"+str(unidadeUEOP)+"\n"+str(alaDia)+"ª Ala\n"+"EFETIVO\n"+str(efetSubSgt)+" Sub/Sgt \n"+str(efetCbSd)+" Cb/Sd\n"+"total: "+str(efetTotal)+"\n \n"+"VIATURAS: \n"+str(stringFullviaturas)+"\n"+"EQUIPAMENTOS: \n"+str(stringFullEquipamentos)+"\n CHEFE SERVIÇO: \n"+chefeServico+"\n \n `S` PARA CONFIRMAR `N` PARA REFAZER \n"))
    if confirmaAnuncio == "S":
        test = telegram_bot_sendtext("Bom dia Senhor\nSegue anúncio do dia "+str(diaAtual)+"\n"+str(unidadeUEOP)+"\n"+str(alaDia)+"ª Ala\n"+"EFETIVO\n"+str(efetSubSgt)+" Sub/Sgt \n"+str(efetCbSd)+" Cb/Sd\n"+"total: "+str(efetTotal)+"\n \n"+"VIATURAS: \n"+str(stringFullviaturas)+"\n"+"EQUIPAMENTOS: \n"+str(stringFullEquipamentos)+"\n CHEFE SERVIÇO: \n"+chefeServico)
        return
    else:
        funcaoEntrada(diaAtual,unidadeUEOP,alaDia,efetSubSgt,efetCbSd,chefeServico)
        return        
    
    return


def funcaoSaida(diaAtual,unidadeUEOP,alaDia):
    ocorrenciasO= int(input("\n Ocorrencias O:"))
    ocorrenciasS= int(input("\n Ocorrencias S:"))
    ocorrenciasP= int(input("\n Ocorrencias P:"))
    ocorrenciasV= int(input("\n Ocorrencias V:"))
    ocorrenciasX= int(input("\n Ocorrencias X:"))
    ocorrenciasY= int(input("\n Ocorrencias Y:"))
    ocorrenciasQ= int(input("\n Ocorrencias Q:"))
    ocorrenciasW= int(input("\n Ocorrencias W:"))
    ocorrenciasR= int(input("\n Ocorrencias R;"))
    casosCovid  = int(input("\n COVID:"))
    observacoes = (input("\n OBSERVACOES:"))
    iapr = ocorrenciasO+ocorrenciasS+ocorrenciasV
    total = ocorrenciasO+ocorrenciasP+ocorrenciasQ+ocorrenciasQ+ocorrenciasR+ocorrenciasS+ocorrenciasV+ocorrenciasW+ocorrenciasX+ocorrenciasY
    chefeServicoSaida = str(input("\n Chefe de Servico:"))
    confirmaAnuncio = str(input("\n \n \nCONFIRME O TEXTO ABAIXO \n \n \n"+"Bom dia senhores! \n {0}Ala - {1} atendeu \nem {2}\n O = {3}\n S = {4}\n P = {5}\n V = {6}\n X = {7}\n Y = {8}\n Q = {9}\n W = {10}\n R = {11}\nCOVID : {12}\nTOTAL : {13}\n IAPR :{14}\nOBS:{15}\n{16} Chefe de Servico"+"\n \n `S` PARA CONFIRMAR `N` PARA REFAZER \n").format())
    ##TODO Atualizar os indicadores no final do input confirmaAnuncio....
    if confirmaAnuncio == "S":
        test = telegram_bot_sendtext("Bom dia senhores! \n"+str(alaDia)+"Ala -"+str(unidadeUEOP)+" atendeu \nem "+str(diaAtual)+"\n O = "+str(ocorrenciasO)+"\n S = "+str(ocorrenciasS)+"\n P = "+str(ocorrenciasP)+"\n V = "+str(ocorrenciasV)+"\n X = "+str(ocorrenciasX)+"\n Y = "+str(ocorrenciasY)+"\n Q = "+str(ocorrenciasQ)+"\n W = "+str(ocorrenciasW)+"\n R = "+str(ocorrenciasR)+"\n COVID : "+str(casosCovid)+"\n TOTAL : "+str(total)+"\n IAPR :"+str(iapr)+"\nOBS:"+str(observacoes)+"\n"+str(chefeServicoSaida)+" Chefe de Servico")
        return
    else:
	
        return

    return




main()
