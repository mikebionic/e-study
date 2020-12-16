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


class Image(UpdatesInfo,db.Model):
	__tablename__="tbl_me_image"
	ImageId = db.Column(db.Integer,nullable=False,primary_key=True)
	ImageName = db.Column(db.String(100),nullable=False)

	def to_json(self):
		json_data = {
			"ImageId": self.ImageId,
			"ImageName": self.ImageName
		}
		return json_data


class Attachments(UpdatesInfo,db.Model):
	__tablename__="tbl_me_attachment"
	AttachmentId = db.Column(db.Integer,primary_key=True)
	AttachmentName = db.Column(db.String(100),nullable=False)
	AttachmentDescription = db.Column(db.String(500))
	AttachmentFileName = db.Column(db.String(100))
	AttachmentFilePath = db.Column(db.String(255))
	LessonIds = db.Column(db.Integer,db.ForeignKey("tbl_me_lesson.LessonId"))
	
	def to_json(self):
		json_data = {
			"AttachmentId": self.AttachmentId,
			"AttachmentName": self.AttachmentName,
			"AttachmentDescription": self.AttachmentDescription,
			"AttachmentFileName": self.AttachmentFileName,
			"AttachmentFilePath": self.AttachmentFilePath
		}
		return json_data