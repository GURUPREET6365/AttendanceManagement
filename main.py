from datetime import date
from database.conn import get_db
from database.models import Attendance
from sqlalchemy import and_, null


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
    
    def status_format(self, school_status, coaching_status):

        school=None
        coaching=None

        # NOTE: We didn't used elif, because elif is run when previous condition is don't matched, and here we want that I will check each and every condtion even though, it matches or not.

        if school_status == 1:
            school=True
        
        if coaching_status == 1:
            coaching=True

        if school_status == 2:
            school=False        
        
        if coaching_status == 2:
            coaching=False       
        
        self.mark_attendance(school, coaching)
    def main_func(self):
        print("Hey boss! I am ATLAS, How are you?")
        print('Command Instruction:\nPresent or Absent: 1 or 2 and holiday: 3')
        
        school_status = int(input("Your school status:\n"))
        coaching_status= int(input("Your coaching status:\n"))

        self.status_format(school_status, coaching_status)

manager=AttendanceManager()
manager.main_func()

