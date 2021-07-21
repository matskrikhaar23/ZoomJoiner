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
        for testVar in dayList:
            if dayList[testVar].lower() in ["su", "sunday", "sun", "1",]:
                schedule.every().sunday.at(timeList[testVar]).do(joinMeeting)
            elif dayList[testVar].lower() in ["m", "monday", "mon", "2"]:
                schedule.every().monday.at(timeList[testVar]).do(joinMeeting)
            elif dayList[testVar].lower() in ["t", "tuesday", "tues", "3"]:
                schedule.every().tuesday.at(timeList[testVar]).do(joinMeeting)
            elif dayList[testVar].lower() in ["w", "wednesday", "wed", "4"]:
                schedule.every().wednesday.at(timeList[testVar]).do(joinMeeting)
            elif dayList[testVar].lower() in ["th", "thursday", "thurs", "5"]:
                schedule.every().thursday.at(timeList[testVar]).do(joinMeeting)
            elif dayList[testVar].lower() in ["f", "friday", "fri", "6"]:
                schedule.every().friday.at(timeList[testVar]).do(joinMeeting)
            elif dayList[testVar].lower() in ["sa", "s", "saturday", "sat", "7"]:
                schedule.every().monday.at(timeList[testVar]).do(joinMeeting)
            else:
                rumps.alert(title="Error", message="Please enter a valid day of the week", ok="OK")
        
        
    @rumps.clicked("Join Meeting Manually")
    def joinManually(self, _):
        webbrowser.open(urlList[0])

    global testFunction
    async def testFunction():
        schedule.run_pending()
        time.sleep(1)

    @rumps.clicked("Auto Join Meetings")
    def runFunction(self, sender):
        sender.state = not sender.state
        loop = asyncio.get_event_loop()
        loop.create_task(testFunction())
    
        loop.run_forever()

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
