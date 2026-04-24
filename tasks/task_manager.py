import numpy as np
import requests
import csv 
import re 

# 1) CSV dosyasını NumPy ile oku
#NumPy kullanarak CSV dosyasını oku. İlk satır başlık, diğer satırlar veri.
#Input: "data/characters.csv"
#Output: np.ndarray
def read_character_data(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as f:
        okuyucu = csv.reader(f)
        next(okuyucu) 
        satirlar = [row for row in okuyucu]
    return np.array(satirlar)
    pass


# 2) Veri kümesinden eksik değerleri temizle
#None, boş string ("") veya "NaN" gibi eksik veri olan satırları çıkar.
# Input:
# [
#     ['Johnny', 'Rocker'],
#     ['V', None],
#     ['T-Bug', '']
# ]
# Output:
# [
#     ['Johnny', 'Rocker']
# ] 
def clean_missing_data(data: np.ndarray):
      temiz = []
      for satir in data:
        eksik = False
        for hucre in satir:
            if hucre is None or hucre == "" or hucre == "NaN":
                eksik = True
                break
        if not eksik:
            temiz.append(satir)
      return np.array(temiz)
      pass


# 3) Sadece belirli bir karakter sınıfına (örneğin "Netrunner") ait kayıtları döndür
#Belirtilen sınıfa sahip karakterleri getir.
#Input: 
# [
#     ['Johnny', 'Rocker'],
#     ['V', 'Solo'],
#     ['T-Bug', 'Netrunner']
# ], 'Netrunner'
#Output: [['T-Bug', 'Netrunner']]
def filter_by_class(data: np.ndarray, class_name: str):
    return data[data[:, 1] == class_name]
    pass


# 4) Karakter isimlerinden uzun olanları bul (örneğin 10 harften uzun)
# İsmi 10 harften uzun karakterleri bul.
# Input: 
# [
#     ['JohnnySilverhand', 'Rocker'],
#     ['V', 'Solo']
# ]
# Output: 
# ['JohnnySilverhand']
def get_long_names(data: np.ndarray):
     uzun = []
     for satir in data:
        isim = satir[0]
        if len(isim) > 10:
            uzun.append(isim)
     return uzun

     pass


# 5) İsimleri büyük harfe çevir ve yeniden döndür
# Tüm karakter isimlerini büyük harfe çevir (in-place ya da yeni dizi).
# Input: 
# [
#     ['v', 'Solo'],
#     ['t-bug', 'Netrunner']
# ]
# Output:
# [
#     ['V', 'Solo'],
#     ['T-BUG', 'Netrunner']
# ]
def uppercase_names(data: np.ndarray):
    sonuc = data.copy()
    for i in range(len(sonuc)):
        sonuc[i][0] = sonuc[i][0].upper()
    return sonuc
    pass

# 6) Sahte bir API'den karakter bilgilerini al
#Verilen URL'e GET isteği at ve response döndür.
#Kullanabileceğin örnel urller:
# https://dummyjson.com/users
# https://jsonplaceholder.typicode.com/users
# https://rickandmortyapi.com/api/character
# Output: requests.Response objesi (status_code + JSON data içeren)
def fetch_character_api_data(api_url: str):
    return requests.get(api_url)
    pass


# 7) API yanıtının geçerli olup olmadığını kontrol et (status code 200 mü?)
# API yanıtı başarılı mı? (status code 200 mü?)
# Input: requests.Response
# Output: True ya da False
def validate_api_response(response: requests.Response):
    return response.status_code == 200
    pass

# 8) API’den gelen JSON verisinden "name" alanlarını çek
# Amaç: JSON'dan name alanlarını bir listeye çıkar.
# Input:
# {
#   "users": [
#     {"id": 1, "name": "V"},
#     {"id": 2, "name": "Johnny"}
#   ]
# }
# Output: ['V', 'Johnny']
def extract_names_from_api(json_data: dict):
    liste = next(v for v in json_data.values() if isinstance(v, list))
    return [obj["name"] for obj in liste]
    pass

# 9) Bir string içindeki özel karakterleri temizle (örneğin: %, $, ! vs.)
# String içindeki özel karakterleri temizle (sadece harf ve rakamlar kalsın)
# Input: "Hello@Cyber#punk!"
# Output: "HelloCyberpunk"
def clean_special_characters(s: str):
     return re.sub(r'[^A-Za-z0-9]', '', s)

     pass

# 10) Dosyadan gelen verileri ve API'den gelenleri birleştir
# Amaç: Dosyadan gelen veriler ile API'den gelen name verilerini birleştirip liste olarak döndür.
# Input: 
# local_data = np.array([
#     ['Johnny', 'Rocker']
# ])
# api_names = ['V', 'T-Bug']
# Output: 
# [
#     ['Johnny', 'Rocker'],
#     ['V', 'API'],
#     ['T-Bug', 'API']
# ]
def merge_local_and_api_data(local_data: np.ndarray, api_names: list):
       birlesik = [list(satir) for satir in local_data]
       for isim in api_names:
        birlesik.append([isim, 'API'])
       return birlesik
       pass