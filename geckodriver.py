from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'C:\Users\Lena\Desktop\Python\geckodriver.exe')
driver.get("https://translate.google.com/?hl=ru#view=home&op=translate&sl=en&tl=ru&text=complecate")