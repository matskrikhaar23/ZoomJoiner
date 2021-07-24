#ATTENTION: This program only works on MacOS.
#If you are on Windows, or do not want to paste this code into Visual Studio, a video showing off how it works can be acessed here: https://www.youtube.com/watch?v=Rl1O77DEKGY
#Enjoy!

from re import L
import webbrowser
import time
import rumps
from rumps.rumps import Window
import schedule
import threading
import asyncio





class ZoomJoiner(rumps.App):
    def __init__(self):
        super(ZoomJoiner, self).__init__("ZoomJoiner")
        self.menu = ["Auto Join Meetings", "Schedule a Meeting", "View Schedule", "Join Meeting Manually"]
    


    

    @rumps.clicked("Schedule a Meeting")
    def calender(self, _):
        global meetingTime
        global meetingDay
        global urlList
        urlList = []
        global dayList
        dayList = []
        global timeList
        timeList = []
        

        
        zoomLink = Window(message='Please type the zoom link you would like to automate', title='Zoom Scheduler', default_text="", ok="OK", dimensions=(320, 160)).run()
        
        if("http" in zoomLink.text):
            url = zoomLink.text
            urlList.append(url)
        else:
            url = "https://" + zoomLink.text
            urlList.append(url)
        
        def dayScheduler():
        
            zoomDay = Window(message='Please enter a weekday on which you would like to join this meeting', title='Zoom Scheduler', default_text="", cancel="Done", ok="Add Another Weekday", dimensions=(320, 160)).run()
            meetingDay = zoomDay.text
            dayList.append(meetingDay)
            if zoomDay.clicked:
                print("Add another weekday")
                dayScheduler()
            
            else:
                print("Done")

        zoomTime = Window(message='Please enter the 24 hour time at which you would like to join this meeting', title='Zoom Scheduler', default_text="", ok="OK", dimensions=(320, 160)).run()
        meetingTime = zoomTime.text
        timeList.append(meetingTime)
        dayScheduler()

        def joinMeeting():
            webbrowser.open(urlList[0])

        print(meetingTime)
        testVar = -1
        # for testVar in dayList:
        #     testVar += 1
        if dayList[0].lower() in ["su", "sunday", "sun", "1",]:
            schedule.every().sunday.at(timeList[0]).do(joinMeeting)
        elif dayList[0].lower() in ["m", "monday", "mon", "2"]:
            schedule.every().monday.at(timeList[0]).do(joinMeeting)
        elif dayList[0].lower() in ["t", "tuesday", "tues", "3"]:
            schedule.every().tuesday.at(timeList[0]).do(joinMeeting)
        elif dayList[0].lower() in ["w", "wednesday", "wed", "4"]:
            schedule.every().wednesday.at(timeList[0]).do(joinMeeting)
        elif dayList[testVar].lower() in ["th", "thursday", "thurs", "5"]:
            schedule.every().thursday.at(timeList[testVar]).do(joinMeeting)
        elif dayList[0].lower() in ["f", "friday", "fri", "6"]:
            schedule.every().friday.at(timeList[0]).do(joinMeeting)
        elif dayList[0].lower() in ["sa", "s", "saturday", "sat", "7"]:
            schedule.every().saturday.at(timeList[0]).do(joinMeeting)
        else:
            rumps.alert(title="Error", message="Please enter a valid day of the week", ok="OK")
        
        
    @rumps.clicked("Join Meeting Manually")
    def joinManually(self, _):
        webbrowser.open(urlList[0])

    global testFunction
    def testFunction():
        schedule.run_pending()
        time.sleep(1)

    @rumps.clicked("Auto Join Meetings")
    def runFunction(self, sender):
        sender.state = not sender.state
        while True:
            schedule.run_pending()
            time.sleep(1)
            
    @rumps.clicked("View Schedule")
    def schedule(self, _):
        var = -1
        for i in dayList:
            var += 1
            rumps.alert(title="Schedule", message="You have a meeting on " + dayList[var] + " at " + timeList[var] + ".")
            

        
    # b = threading.Thread(name='testFunction', target=testFunction)
    # f = threading.Thread(name='calender', target=calender)
    # b.start()
    # f.start()


if __name__ == "__main__":
    ZoomJoiner().run()
