from datetime import date, timedelta
from database.conn import get_db
from database.models import Attendance
from sqlalchemy import and_, null, desc
from datetime import datetime


# db=get_db()
# db.close()

# print('Welcome to the Attendance Management page.')
class AttendanceManager:
    def __init__(self):
        self.db=get_db()
        self.attendance_date = date.today()
        self.date_today = date.today()
        print('Command Instruction:\n   Present: 1\n   Absent: 2\n   Holiday: 3\n')
    

    def mark_attendance(self, school:bool, coaching:bool):
        

        new_attendance = Attendance(school=school, attendance_date=self.attendance_date, coaching=coaching)
        self.db.add(new_attendance)
        self.db.commit()
        self.db.close()

        print(f"your school attendance has been marked successfully.\nschool:{school}\ncoaching:{coaching}\n\n")
    
    def status_format(self, school_status, coaching_status):

        school=None
        coaching=None

        # NOTE: if there will be no any status number i.e 1 or 2, then It will mark as null and means there is leave or holiday.

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


    def is_att_marked(self):
        date_today = self.date_today
        db = self.db

        att_check = db.query(Attendance).filter(Attendance.attendance_date == date_today).first()
        if att_check:
            print(f"Your attendance for today already exists.\nschool:{att_check.school}\ncoaching:{att_check.coaching}.")
            return False
        else:
            return True


    def day_checker(self, day: str = None):
        if day is None:
            day_name = datetime.now().strftime("%A")
            # day_name = datetime.now()
            if day_name == "Sunday":
                return False

            else:
                mark_att = self.is_att_marked()
                if mark_att:
                    return True
                else:
                    return False
        
        else:
            if day == "Sunday":
                print(f"{self.new_date} was sunday!\n")
                return False

            else:
                mark_att = self.is_att_marked()
                if mark_att:
                    return True
                else:
                    return False


    def prev_attendance(self):
        db = self.db

        # finding the last attendance
        last_att = db.query(Attendance).order_by(desc(Attendance.id)).first()
        if last_att is None:
            print('Your database has no data.....')
            self.direct_att_mark()
        last_date = last_att.attendance_date
        today_date = self.date_today

        date_gap = (today_date-last_date).days
        if date_gap >= 1:
            for i in range(1, date_gap+1):
                self.new_date = last_date+timedelta(days=i)
                new_day = self.new_date.strftime("%A")
                self.attendance_date = self.new_date
                day_check=self.day_checker(new_day)
                if day_check:
                    print(f"Your attendance of date {f"{self.new_date} and {new_day}" if (today_date-self.new_date).days > 0 else "Today"}")
                    self.user_input()
        else:
            day_check=self.day_checker(new_day)
            if day_check:
                print("Your Todays status.")
                self.user_input()
    
    def user_input(self):
        
        school_status = int(input("Your school status:\n"))
        coaching_status= int(input("Your coaching status:\n"))
        self.status_format(school_status, coaching_status)


    def direct_att_mark(self):
        # This is for the condition when the db has no data.
        
        day_check=self.day_checker()
        if day_check:
            self.user_input()
    
    def main(self):
        self.prev_attendance()
        

            

manager=AttendanceManager()
manager.main()


