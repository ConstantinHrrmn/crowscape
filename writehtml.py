import time
from selenium import webdriver
import webbrowser

class HTMLWriter:
    def __init__(self):
        self.filename = "index.html"

    def write_html(self, title, content):
        f = open(self.filename, 'w')
        message = "<html><head></head><body><h1>"+ title +"</h1><h3>" + content + "</h3></body></html>"
        f.write(message)
        f.close()
    
    def create_tab(self):
        webbrowser.open_new_tab(self.filename)

    def refresh_page(self):
        driver = webdriver.Firefox()

        driver.get(self.filename)
        driver.refresh()
        driver.quit()

    
    