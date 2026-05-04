from datetime import date
from database.conn import get_db
from database.models import Attendance
from sqlalchemy import and_


# db=get_db()
# db.close()

# print('Welcome to the Attendance Management page.')
class AttendanceManager:
    def __init__(self):
        self.db=get_db()
        self.date_today = date.today()
    
    def check_attendance(self):
        date_today = self.date_today
        exisiting_att = self.db.query(Attendance).filter(Attendance.attendance_date == date_today).first()

        if exisiting_att is not None:

            return True, exisiting_att
        
        return False, None

    def mark_attendance(self, school:bool, coaching:bool):
        is_att_exists, db=self.check_attendance()

        if is_att_exists:
            print(f"Your attendance for today already exists.\nschool:{db.school}\ncoaching:{db.coaching}")
        
        elif not is_att_exists:
            new_attendance = Attendance(school=school, attendance_date=self.date_today, coaching=coaching)
            self.db.add(new_attendance)
            self.db.commit()
            self.db.close()

            print(f"your school attendance has been marked successfully.\nschool:{school}\ncoaching:{coaching}")
    
    
    def main_func(self, school, coaching):
        print("Hey boss! I am ATLAS, How are you?")

        self.mark_attendance(school, coaching)
# manager=AttendanceManager()
# manager.main_func(True, True)

