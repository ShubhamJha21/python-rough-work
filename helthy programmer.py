# to import music
from pygame import mixer
from  time import time
from datetime import datetime


def music_on_loop(file, stop):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(40)
    while True:
         print("Enter DONE to stop")
         Enter_User_Command = input()
         if Enter_User_Command==stop:
             mixer.music.stop()
         break
if __name__ == '__main__':
    initial_timeof_water = time()
    initial_timeof_eye = time()
    initial_timeof_exersice = time()
    eye_blink = 30*60
    water_second = 45*60
    exercise_timesec= 55*60
    def log_time(b):
      with open("log.txt","a") as f:
       f.write(f"{b}{str(datetime.now())}\n")

    while(1):
         if time() - initial_timeof_eye > eye_blink:
              print("REALEX YOUR EYES")
              music_on_loop("eyes.mp3", "DONE")
              log_time("YOU BLINK EYE AT")
              initial_timeof_eye = time()
         if time() - initial_timeof_water > water_second:
              print("Enter DONE to stop")
              music_on_loop("water.mp3","DONE")
              log_time("YOU DRINK AT")
              initial_timeof_water = time()
         if time() - initial_timeof_exersice> exercise_timesec:
               print("5 MINUTE EXERCISE TIME")
               music_on_loop("exer.mp3" ,"DONE")
               log_time("YOU DONE EXERCISE AT")
               initial_timeof_exersice = time()








