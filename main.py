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
    
    def check_existing_att(self, school:bool=False, coaching:bool=False):
        date_today = self.date_today
        if school:
            exisiting_att = self.db.query(Attendance).filter(and_(Attendance.attendance_date == date_today, Attendance.school==True)).first()
            print(exisiting_att, date_today)
            if exisiting_att is not None:
                print(f'Your school attendance is already marked today as \"{exisiting_att.school}\"')
                return False
            return True
        
        elif coaching:
            exisiting_att = self.db.query(Attendance).filter(and_(Attendance.attendance_date == date_today, Attendance.coaching==True)).first()

            if exisiting_att is not None:
                print(f'Your school attendance is already marked today as \"{exisiting_att.school}\"')
                return False
            return True

    
    def mark_school(self, status:bool):
        is_not_exists = self.check_existing_att(school=True)
        if is_not_exists:
            new_attendance = Attendance(school=status, attendance_date=self.date_today)
            self.db.add(new_attendance)
            self.db.commit()
            self.db.close()

            print("your school attendance is marked as present.")

    def mark_coaching(self, status:bool):
        is_not_exists = self.check_existing_att(coaching=True)
        if is_not_exists:
            new_attendance = Attendance(coaching=status, attendance_date=self.date_today)
            self.db.add(new_attendance)
            self.db.commit()
            self.db.close()

            print("your coaching attendance is marked as present.")
    
    def main_func(self):
        print("Hey boss! I am ATLAS, How are you?")

        while True:
            for_school=input('Are you present in your school:\n')
            # for school:
            if for_school.lower() == 'yes':
                self.mark_school(True)

            elif for_school.lower() == 'no':
                self.mark_school(False)
            
            else:
                print("Enter only yes or no!")

            for_coaching=input('Are you present in your coaching:\n')
            # for coaching:
            if for_coaching.lower() == 'yes':
                self.mark_coaching(True)

            elif for_coaching.lower() == 'no':
                self.mark_coaching(False)

            else:
                print("Enter only yes or no!")
manager=AttendanceManager()
manager.main_func()

