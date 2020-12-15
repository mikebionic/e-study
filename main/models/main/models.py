from main import db
from datetime import datetime


class UpdatesInfo(object):
	CreatedDate = db.Column(db.DateTime,default=datetime.now())
	ModifiedDate = db.Column(db.DateTime,default=datetime.now(),onupdate=datetime.now())
	
	def createdInfo(self,UId):
		self.CreatedUId = UId

	def modifiedInfo(self,UId):
		self.ModifiedDate = datetime.now()
		self.ModifiedUId = UId