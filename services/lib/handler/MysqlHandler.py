"""
$Id: MysqlHandler.py,v 1.4 2002/07/02 13:13:34 magnun Exp $
$Source: /usr/local/cvs/navbak/navme/services/lib/handler/MysqlHandler.py,v $
"""

from job import JobHandler, Event
import Socket
class MysqlHandler(JobHandler):
	def __init__(self, serviceid, boksid, ip, args, version):
		port = args.get("port", 3306)
		JobHandler.__init__(self, "mysql", serviceid, boksid, (ip, port), args, version)
	def execute(self):
		s = Socket.Socket(self.getTimeout())
		s.connect(self.getAddress())
		line = s.readline()
		s.close()
		#this is ugly
		try:
			version = line.split('-')[1].split('\n')[1].strip()
			self.setVersion(version)
		except:
			return Event.DOWN, line
		return Event.UP, 'OK'

def getRequiredArgs():
	"""
	Returns a list of required arguments
	"""
	requiredArgs = []
	return requiredArgs
								
