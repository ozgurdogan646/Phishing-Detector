import numpy as np
import pandas as pd

signs = [".","-","_","/","?","=","@","&","!"," ","~",",","+","*","#","$","%"]
vowels = ["a","e","i","o","u"]
data = pd.read_csv("data/dataset_small.csv")

def get_features(url):
    urlFeatures = getFeaturesBasedOnUrl(url)
    domainFeatures = getFeaturesBasedOnDomain(url)
    directoryFeatures = getFeaturesBasedOnDirectory(url)
    filenameFeatures = getFeaturesBasedOFilename(url)
    paramsFeatures = getFeaturesBasedOParams(url)
    externalFeatures = getFeaturesBasedOnExternals(url)
    concatData = np.concatenate([urlFeatures,domainFeatures,directoryFeatures,filenameFeatures,paramsFeatures,externalFeatures])
    return concatData



def getFeaturesBasedOnUrl(url,
                          signs = signs,
                          vowels = vowels):
    features = list()
    for sign in signs:
        features.append(url.count(sign))
    topLevelDomain = url.split("//")[1]
    topLevelDomain = topLevelDomain.split("/")[0]
    features.append(len(topLevelDomain))
    features.append(len(url))
    features.append(0)
    features = np.array(features)
    return features

def getFeaturesBasedOnDomain(url,
                             signs = signs,
                             vowels = vowels):
    features = list()
    vowelCount = 0
    topLevelDomain = url.split("//")[1]
    topLevelDomain = topLevelDomain.split("/")[0]
    for sign in signs:
        features.append(topLevelDomain.count(sign))
    for vowel in vowels:
        vowelCount += topLevelDomain.count(vowel)
    features.append(vowelCount)
    features.append(len(topLevelDomain))
    features.append(0)
    features.append(0)
    features = np.array(features)
    return features
    
def getFeaturesBasedOnDirectory(url,
                                signs = signs,
                                vowels=vowels):
    features = list()
    directory = url.split("//")[1]
    directory = directory.split("/")[1]
    for sign in signs:
        features.append(directory.count(sign))
    features.append(len(directory))
    features = np.array(features)
    return features

def getFeaturesBasedOFilename(url,
                                signs = signs,
                                vowels=vowels):
    features = list()
    filename = url.split("//")[1]
    filename = filename.split("/")[2]
    for sign in signs:
        features.append(filename.count(sign))
    features.append(len(filename))
    features = np.array(features)
    return features

def getFeaturesBasedOParams(url,
                            signs = signs,
                            vowels=vowels,
                            data = data):
    features = list()
    params = url.split("//")[1]
    params = params.split("/")[3]
    for sign in signs:
        features.append(params.count(sign))
    features.append(len(params))
    features.append(0)
    qty_params = data["qty_params"].mean()
    features.append(qty_params)
    features = np.array(features)
    return features

def getFeaturesBasedOnExternals(url,
                                data = data):
    features = list()
    externals = ["time_response", "pass", "asn_ip", "time_domain_activation","time_domain_expiration","qty_ip_resolved","qty_nameservers","qty_mx_servers","ttl_hostname","pass","qty_redirects","pass","pass","pass"]
    for external in externals:
        if external == "pass":
            features.append(0)
        else:
            features.append(data[external].mean())
    features = np.array(features)
    return features 