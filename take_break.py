import webbrowser as wb
import sched, time
s = sched.scheduler(time.time, time.sleep)
def br(sc): 

	wb.get('windows-default').open('http://youtube.com')
	s.enter(1500, 1, br, (sc,))

s.enter(1500, 1, br, (s,))
s.run()