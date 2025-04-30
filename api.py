from flask import Flask
from flask_restx import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app, title="Striking Vipers API", version="1.0", description="API for Teachers, Classes, and Students")

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:CPSC408!@localhost/StrikingVipers'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ------------------ MODELS ------------------

class Teacher(db.Model):
    __tablename__ = 'Teachers'
    TeacherID = db.Column(db.Integer, primary_key=True)
    TeacherFirstName = db.Column(db.String(255), nullable=False)
    TeacherLastName = db.Column(db.String(255), nullable=False)
    TeacherUserName = db.Column(db.String(255), nullable=False, unique=True)

class Class(db.Model):
    __tablename__ = 'Classes'
    ClassCode = db.Column(db.String(255), primary_key=True)
    ClassGrade = db.Column(db.Integer, nullable=False)
    TeacherID = db.Column(db.Integer, db.ForeignKey('Teachers.TeacherID'), nullable=False)

class Student(db.Model):
    __tablename__ = 'Students'
    StudentID = db.Column(db.Integer, primary_key=True)
    StudentFirstName = db.Column(db.String(255), nullable=False)
    StudentLastName = db.Column(db.String(255), nullable=False)
    StudentUserName = db.Column(db.String(255), nullable=False, unique=True)
    ClassCode = db.Column(db.String(255), db.ForeignKey('Classes.ClassCode'), nullable=False)

# ------------------ RESTX MODELS ------------------

teacher_model = api.model('Teacher', {
    'TeacherFirstName': fields.String(required=True),
    'TeacherLastName': fields.String(required=True),
    'TeacherUserName': fields.String(required=True),
})

class_model = api.model('Class', {
    'ClassCode': fields.String(required=True),
    'ClassGrade': fields.Integer(required=True),
    'TeacherID': fields.Integer(required=True),
})

student_model = api.model('Student', {
    'StudentFirstName': fields.String(required=True),
    'StudentLastName': fields.String(required=True),
    'StudentUserName': fields.String(required=True),
    'ClassCode': fields.String(required=True),
})

# ------------------ ENDPOINTS ------------------

@api.route('/teachers')
class TeacherList(Resource):
    @api.marshal_list_with(teacher_model)
    def get(self):
        return Teacher.query.all()

    @api.expect(teacher_model)
    def post(self):
        data = api.payload
        teacher = Teacher(**data)
        db.session.add(teacher)
        db.session.commit()
        return {'message': 'Teacher added successfully'}, 201

@api.route('/classes')
class ClassList(Resource):
    @api.marshal_list_with(class_model)
    def get(self):
        return Class.query.all()

    @api.expect(class_model)
    def post(self):
        data = api.payload
        classroom = Class(**data)
        db.session.add(classroom)
        db.session.commit()
        return {'message': 'Class added successfully'}, 201

@api.route('/students')
class StudentList(Resource):
    @api.marshal_list_with(student_model)
    def get(self):
        return Student.query.all()

    @api.expect(student_model)
    def post(self):
        data = api.payload
        student = Student(**data)
        db.session.add(student)
        db.session.commit()
        return {'message': 'Student added successfully'}, 201

# ------------------ RUN ------------------

if __name__ == '__main__':
    app.run(debug=True)
