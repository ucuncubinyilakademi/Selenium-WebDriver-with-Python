# Haberturkten euro fiyatını ve yüzdelik bilgisini alalım.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

driver_path = "chromedriver.exe"

opsiyonlar = Options()
opsiyonlar.add_argument("--headless")  # Veri çekme arka planda gerçekleşir.

# tarayıcı tanımladık.
browser = webdriver.Chrome(executable_path=driver_path, options=opsiyonlar)
browser.get("https://www.haberturk.com/")

# sayfadaki altin-tl-gr id li elementin içindeki text verilerini al.
# icerik = browser.find_element_by_id("altin-tl-gr").text
icerik = browser.find_element(By.ID,"euro").text
parcalar = icerik.split("\n")  # icerik 3 satırlık veri getirdiği için
# bu verideki her satırı ayrı ayrı ele almamızı sağladık.
# her satırdaki veriyi listenin bir elemanı olacak şekilde parçaladık.
# Satır satır parçalamak için \n den ayır dedik.
# print(parcalar[0]," -> ",parcalar[1])
# print(type(parcalar[1]))

euro = float(parcalar[1].replace(",", "."))  # float'a dönüştürebilmek için. , ile . yı değiştirdik.
yuzde = str(parcalar[2].replace(",", "."))
print("Euro:", euro)
print(yuzde)
print(type(euro))


















