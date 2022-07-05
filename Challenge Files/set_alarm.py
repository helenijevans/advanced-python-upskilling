import time
import simpleaudio as sa


def set_alarm(a_time, s_file, message):
    while time.time() < a_time:
        """waiting for alarm to go off """
    if time.time() >= a_time:
        print("🔔🔔🔔")
        print(message)
        wave_obj = sa.WaveObject.from_wave_file(s_file)
        play_obj = wave_obj.play()
        play_obj.wait_done()


set_alarm(time.time() + 5, 'alarm.wav', 'Wake up!')

"""
GIVEN SOLUTION
"""
# import sched
# import time
# import winsound as ws
#
# def set_alarm(alarm_time, wav_file, message):
#     s = sched.scheduler(time.time, time.sleep)
#     s.enterabs(alarm_time, 1, print, argument=(message,))
#     s.enterabs(alarm_time, 1, ws.PlaySound, argument=(wav_file, ws.SND_FILENAME))
#     print("Alarm set for", time.asctime(time.localtime(alarm_time)))
#     s.run()


## REFLECTION
# My solution seems to be simpler and more readable, however I do like the use of the schedule package.