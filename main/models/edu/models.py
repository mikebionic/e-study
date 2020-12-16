from main import db
from main.models.main.models import UpdatesInfo


class Education(UpdatesInfo,db.Model):
	__tablename__="tbl_me_education"
	EducationId = db.Column(db.Integer,primary_key=True)
	EducationName = db.Column(db.String(100),nullable=False)
	EducationDescription = db.Column(db.String(500))
	EducationGroupId = db.Column(db.Integer,db.ForeignKey("tbl_me_education_group.EducationGroupId"))
	Faculty = db.relationship('Faculty',backref='education',lazy=True)
	# link with image
	# add column name in string

	def to_json(self):
		json_data = {
			"EducationId": self.EducationId,
			"EducationName": self.EducationName,
			"EducationDescription": self.EducationDescription,
			"EducationGroupId": self.EducationGroupId
		}
		return json_data


class Education_group(UpdatesInfo,db.Model):
	__tablename__="tbl_me_education_group"
	EducationGroupId = db.Column(db.Integer,primary_key=True)
	EducationGroupName = db.Column(db.String(100),nullable=False)
	EducationGroupDescription = db.Column(db.String(500))
	Education = db.relationship('Education',backref='education_group',lazy=True)
	# EducationGroup = db.relationship('EducationGroup',backref='education_sub_group',lazy=True)
	# many to many
	
	def to_json(self):
		json_data = {
			"EducationGroupId": self.EducationGroupId,
			"EducationGroupName": self.EducationGroupName,
			"EducationGroupDescription": self.EducationGroupDescription
		}
		return json_data


class Faculty(UpdatesInfo,db.Model):
	__tablename__="tbl_me_faculty"
	FacultyId = db.Column(db.Integer,primary_key=True)
	FacultyName = db.Column(db.String(100),nullable=False)
	FacultyDescription = db.Column(db.String(500))
	EducationId = db.Column(db.Integer,db.ForeignKey("tbl_me_education.EducationId"))
	Major = db.relationship('Major',backref='faculty',lazy=True)
	# link with image

	def to_json(self):
		json_data = {
			"FacultyId": self.FacultyId,
			"FacultyName": self.FacultyName,
			"FacultyDescription": self.FacultyDescription,
			"EducationId": self.EducationId
		}
		return json_data


class Major(UpdatesInfo,db.Model):
	__tablename__="tbl_me_major"
	MajorId = db.Column(db.Integer,nullable=False,primary_key=True)
	MajorName = db.Column(db.String(100),nullable=False)
	MajorDescription = db.Column(db.String(500))
	FacultyId = db.Column(db.Integer,db.ForeignKey("tbl_me_faculty.FacultyId"))
	Lesson = db.relationship('Lesson',backref='major',lazy=True)
	Reference = db.relationship('Reference',backref='major',lazy=True)
	Hometask = db.relationship('Hometask',backref='major',lazy=True)

	def to_json(self):
		json_data = {
			"MajorId": self.MajorId,
			"MajorName": self.MajorName,
			"MajorDescription": self.MajorDescription,
			"FacultyId": self.FacultyId
		}
		return json_data


class Subject(UpdatesInfo,db.Model):
	__tablename__="tbl_me_subject"
	SubjectId = db.Column(db.Integer,primary_key=True)
	SubjectName = db.Column(db.String(100),nullable=False)
	SubjectDescription = db.Column(db.String(500))
	Lesson = db.relationship('Lesson',backref='subject',lazy=True)
	Hometask = db.relationship('Hometask',backref='subject',lazy=True)

	def to_json(self):
		json_data = {
			"SubjectId": self.SubjectId,
			"SubjectName": self.SubjectName,
			"SubjectDescription": self.SubjectDescription
		}
		return json_data


class Course(UpdatesInfo,db.Model):
	__tablename__="tbl_me_course"
	CourseId = db.Column(db.Integer,nullable=False,primary_key=True)
	CourseName = db.Column(db.String(100),nullable=False)
	CourseDescription = db.Column(db.String(500))

	def to_json(self):
		json_data = {
			"CourseId": self.CourseId,
			"CourseName": self.CourseName,
			"CourseDescription": self.CourseDescription
		}
		return json_data


class Lesson(UpdatesInfo,db.Model):
	__tablename__="tbl_me_lesson"
	LessonId = db.Column(db.Integer,primary_key=True)
	LessonName = db.Column(db.String(100),nullable=False)
	LessonDescription = db.Column(db.String(500))
	SubjectId = db.Column(db.Integer,db.ForeignKey("tbl_me_subject.SubjectId"))
	MajorId = db.Column(db.Integer,db.ForeignKey("tbl_me_major.MajorId"))
	Attachments = db.relationship('Attachments',backref='lesson',lazy=True)

	def to_json(self):
		json_data = {
			"LessonId": self.LessonId,
			"LessonName": self.LessonName,
			"LessonDescription": self.LessonDescription,
			"SubjectId": self.SubjectId,
			"MajorId": self.MajorId
		}
		return json_data


class Reference(UpdatesInfo,db.Model):
	__tablename__="tbl_me_reference"
	ReferenceId = db.Column(db.Integer,primary_key=True)
	ReferenceName = db.Column(db.String(100),nullable=False)
	ReferenceDescription = db.Column(db.String(500))
	MajorId = db.Column(db.Integer,db.ForeignKey("tbl_me_major.MajorId"))

	def to_json(self):
		json_data = {
			"ReferenceId": self.ReferenceId,
			"ReferenceName": self.ReferenceName,
			"ReferenceDescription": self.ReferenceDescription,
			"MajorId": self.MajorId
		}
		return json_data


class Hometask(UpdatesInfo,db.Model):
	__tablename__="tbl_me_hometask"
	HometaskId = db.Column(db.Integer,primary_key=True)
	HometaskName = db.Column(db.String(100),nullable=False)
	HometaskDescription = db.Column(db.String(500))
	MajorId = db.Column(db.Integer,db.ForeignKey("tbl_me_major.MajorId"))
	SubjectId = db.Column(db.Integer,db.ForeignKey("tbl_me_subject.SubjectId"))
	Solution = db.relationship('Solution',backref='hometask',lazy=True)
	
	def to_json(self):
		json_data = {
			"HometaskId": self.HometaskId,
			"HometaskName": self.HometaskName,
			"HometaskDescription": self.HometaskDescription,
			"SubjectId": self.SubjectId,
			"MajorId": self.MajorId
		}
		return json_data


class Solution(UpdatesInfo,db.Model):
	__tablename__="tbl_me_solution"
	SolutionId = db.Column(db.Integer,primary_key=True)
	SolutionName = db.Column(db.String(100),nullable=False)
	SolutionDescription = db.Column(db.String(500))
	Completed = db.Column(db.Boolean)
	UserId = db.Column(db.Integer,db.ForeignKey("tbl_me_user.UserId"))
	HometaskId = db.Column(db.Integer,db.ForeignKey("tbl_me_hometask.HometaskId"))

	def to_json(self):
		json_data = {
			"SolutionId": self.SolutionId,
			"SolutionName": self.SolutionName,
			"SolutionDescription": self.SolutionDescription,
			"Completed": self.Completed,
			"UserId": self.UserId,
			"HometaskId": self.HometaskId
		}
		return json_data