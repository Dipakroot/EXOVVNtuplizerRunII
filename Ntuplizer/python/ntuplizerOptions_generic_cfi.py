import FWCore.ParameterSet.Config as cms

config = dict()

#--------- general ----------#

#--------- Set Just one to true ----------#
config["RUNONMC"] = True
#-----------------------------------------#

#--------- For taus ----------#
config["USEDNN"] = True
config["DZCUT"] = 0.25 # this is fixed !!
config["FSIGCUT"] = 3
config["VPROBCUT"] = 0.05
config["DNNCUT"] = 0.1443


config["USEJSON"] =  (config["RUNONMC"])
config["USEJSON"] = True
#config["JSONFILE"] = "JSON/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt" #data 2017
#config["JSONFILE"] = "JSON/Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON.txt" # data 2016
#config["JSONFILE"] = "JSON/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt" # data 2018
config["USENOHF"] = False


#--------- basic sequences ----------#
config["DOGENPARTICLES"] = (True and config["RUNONMC"])
config["DOGENEVENT"] = (True and config["RUNONMC"])
config["DOPILEUP"] = (True and config["RUNONMC"])
config["DOVERTICES"] = True
config["DOMISSINGET"] = True

config["DOJPSIMU"] = False
config["DOJPSITAU"] = False
config["DOBSTAUTAU"] = True
config["DOBSTAUTAUFH"] = False
config["DOBSDSTARTAUNU"] = False
config["ISTRUTH"] = False

config["DOGENHIST"] = (True and config["RUNONMC"]);

if config["DOJPSITAU"]:
    config["DNNFILE"] = "data/DNN/BcJPsi/DUMMY"

if config["DOBSTAUTAU"] or config["DOBSTAUTAUFH"] or config["DOBSDSTARTAUNU"]:
    #config["DNNFILE"] = "data/DNN/BsTauTau/DUMMY" 
    config["DNNFILE"] = "mc/DNN/BsTauTau/DUMMY" 

#--------- JEC ----------#

config["CORRMETONTHEFLY"] = True  # at the moment JEC available just for MC Fall17

