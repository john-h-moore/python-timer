'''
Created on Jan 28, 2013

@author: John H Moore
'''
import time, winsound, datetime

def timer(t):
    print "Timer set for %d minutes" %t
    print "Starting time is", datetime.datetime.now().strftime("%H:%M")

    q = t/4
    r = t
    i = 0
    qnum = 1

    while (qnum < 4):
        time.sleep(q*60)
        r = t - qnum*q
        print "\nThe time is now", datetime.datetime.now().strftime("%H:%M")
        quarter_chime(qnum)
        print "%d minutes remaining" %r
        qnum += 1

    time.sleep(r*60)
    print "Ending time is", datetime.datetime.now().strftime("%H:%M")
    while (i < 60):
        winsound.MessageBeep()
        time.sleep(1)
        i += 1

def quarter_chime(qnum):
    i = 0
    while i < qnum:
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        i += 1
        time.sleep(0.75)

if __name__ == "__main__":
    while True:
        try:
            t = int(raw_input("Timer length in minutes: "))
            break
        except ValueError:
            print "You must enter a number"

    timer(t) 