from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import winsound
import os
import pyttsx3
from googletrans import Translator
import openai


openai.api_key = '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'

def frendbot(frendbot):
    
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=f"You: What have you been up to?\nFriend: Watching old movies.\nYou: {frendbot}\nFriend:",
    temperature=0.5,
    max_tokens=60,
    top_p=1.0,
    frequency_penalty=0.5,
    presence_penalty=0.0,
    stop=["You:"]
    )
    
    return response.choices[0].text



driver = webdriver.Chrome(executable_path=r"chromedriver.exe")

linkstream = str(input("Введите ссылку на стрим : "))

# voice

tts = pyttsx3.init()

voices = tts.getProperty('voices')


tts.setProperty('voice', 'ru')

for voice in voices:

    if voice.name == 'Aleksandr':

        tts.setProperty('voice', voice.id)

#

driver.get(linkstream)
time.sleep(3)

while True:
    try:
        chatline = driver.find_element(By.CLASS_NAME, "chat-line__message")
        username = driver.find_element(By.CLASS_NAME, "chat-line__username")
        textfragment = driver.find_element(By.CLASS_NAME, "text-fragment")
        translator = Translator()
        translation = translator.translate(textfragment.text, dest='en')
        result = frendbot(translation.text)
        translator = Translator()
        translation = translator.translate(result, dest='ru')
        print(translation.text)
        tts.say(username.text)
        tts.runAndWait()
        tts.say(translation.text)
        tts.runAndWait()
        driver.execute_script("arguments[0].remove();", chatline)
    except:
        huesos = 1