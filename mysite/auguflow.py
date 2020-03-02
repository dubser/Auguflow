import syslog,time
import threading

# Pour afficher en continu les logs de l'application
# tail -f /var/log/syslog | grep "manage.py"

syslog.syslog(time.strftime("#%S: ",time.localtime())+"Auguflow is starting.")


def ThAugflo():
    syslog.syslog(time.strftime("#%S: ",time.localtime())+"Thread auguflow .")
    time.sleep(0.1)

class AuguFlo (threading.Thread):
   def __init__(self, name):
      threading.Thread.__init__(self)
      self.name = name
   def run(self):
      syslog.syslog(time.strftime("#%S: ",time.localtime())+"Starting thread " + self.name)
      ThAufl(self.name)
      syslog.syslog(time.strftime("#%S: ",time.localtime())+"Exiting thread " + self.name)

def ThAufl(name):
   loop =5
   while loop:
      syslog.syslog(time.strftime("#%S: ",time.localtime())+"Thread auguflow running." + name)
      time.sleep(5)
      loop=loop-1
