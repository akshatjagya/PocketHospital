import sys
import mysql.connector
from datetime import datetime

conn=mysql.connector.connect(user='root',host='localhost', passwd='qwerty',database='pocket_hospital')
mycursor=conn.cursor()

print("===========APPOINTMENT==========")
print("TO CONTINUE SELECT OPTION ")
print("1. AS USER")
print("2. AS ADMIN ")
print("3. TO EXIT")
ch1=int(input("Enter your selected option:"))

mycursor.execute("use pocket_hospital")
mycursor.execute("create table if not exists user_info(SNO int,USERNAME varchar(40),FIRST_NAME varchar(20),LAST_NAME varchar(20), AGE int, SEX varchar(10), DEPARTMENT_BOOKED  varchar(40), DOCTOR_NAME varchar(40), TIME_SLOT_BOOKED varchar(20),DATE_OF_BOOKING DATE ,NAPP int)")
SNO=int(input("Enter serial number:"))
USERNAME= input("Enter username:")
FIRST_NAME=input("Enter first name:")
LAST_NAME=input("Enter last name:")
AGE=int(input("Enter your age"))
SEX=input("Enter you sex(m/f/o):")
DATE_OF_BOOKING=datetime.now()
NAPP=0
DEPARTMENT_BOOKED=' '
DOCTOR_NAME=' '
TIME_SLOT_BOOKED='NULL'
count=0
rec=[SNO,USERNAME,FIRST_NAME,LAST_NAME,AGE,SEX,DEPARTMENT_BOOKED,DOCTOR_NAME, TIME_SLOT_BOOKED,DATE_OF_BOOKING ,NAPP]
m="insert into user_info values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
mycursor.execute(m,rec)
conn.commit()
#choice=input("Enter whether you want book appoinments(y/n):")
#while choice=='y':

      #  choice=input("Enter whether you want book appoinments(y/n):")
a=USERNAME
d=DEPARTMENT_BOOKED
def printdept():
     print("==========DEPARTMENTS==========")
     print("1.Immunologist")
     print("2.Cardiologist")
     print("3.Dermatologist")
     print("4.General phyrsician")
     print("5.Gastroenterologists")
     print("6.Hematologists")
     print("7.Nephrologists")
     print("8.Neurologists")
     print("9.Gynecologists")
     print("10.Oncologists")
     print("11.Ophthalmologists(eye doctor)")
     print("12.Pediatricians")
     print("13.General Surgeons")
     print("14.urologist")
     print("15.ENT")

choii="y"
mycursor.execute("use pocket_hospital")
mycursor.execute("create table if not exists appointment(DOCTOR_ID int, DEPARTMENT varchar(40), DOCTOR_NAME varchar(40),PHONE_NUMBER varchar(14),WING varchar(3), TIME_SLOT1 varchar(25), TIME_SLOT2 varchar(25),TIME_SLOT3 varchar(25))")
conn.commit()
while USERNAME==a:
   if ch1==1:
        print("WELCOME TO")
        print("PORTAL FOR USER")
        print("==================")
        print("ENTER  YOUR REQUEST")
        
        print("  1.BOOK APPOINTMENT")
        print("      1.1 Available doctors")
        print("      1.2 Book an Appointment")
        print("      1.3 Cancel appointment")
        print("  2. SEARCH FOR DOCTOR'S INFORMATION")
        ch2=int(input("Enter your choice:")) 

        if ch2==1:
           print(" 1.1 Available doctors")
           print(" 1.2 Book an Appointment")
           print(" 1.3 Cancel appointment")
           ch3=float(input("Enter your choice:"))
           if ch3==1.1:
              mycursor.execute("select * from appointment where TIMESLOT1 is NULL or TIMESLOT2 is NULL or TIMESLOT3 is NULL")
              m=mycursor.fetchall()
              m1=[("DOCTOR_ID","DEPARTMENT","DOCTOR_NAME","PHONE_NUMBER","WING","TIME_SLOT1","TIME_SLOT2","TIME_SLOT3","TIMESLOT1","TIMESLOT2","TIMESLOT3")]
              m1=m1+m
              for i in m1:
                 for j in i:
                    a=" "
                    a=a+str(j)
                    while len(a)<15:
                       a=a+' '
                    print(a,end=" ")
                 print()
              conn.commit()

                 
           elif ch3==1.2:
              
              while choii=="y":
                 '''print("==============AVAILABLE TIME SLOTS===============")
                 mycursor.execute("select DOCTOR_ID,DEPARTMENT,DOCTOR_NAME,TIME_SLOT1,TIME_SLOT2,TIME_SLOT3,TIMESLOT1,TIMESLOT2,TIMESLOT3 from appointment")
                 m=mycursor.fetchall()
                 n1=[("DOCTOR_ID","DEPARTMENT","DOCTOR_NAME","TIME_SLOT1","TIME_SLOT2","TIME_SLOT3","TIMESLOT1","TIMESLOT2","TIMESLOT3")]
                 n1=n1+m
                 for i in n1:
                    for j in i:
                       a=" "
                       a=a+str(j)
                       while len(a)<15:
                          a=a+' '
                       print(a,end=" ")
                    print()
                 conn.commit()
                 conn.close() '''                    
                 printdept()
                 K=['Immunologist',"Cardiologist","Dermatologist","General phyrsician","Gastroenterologists","Hematologists","Nephrologists",
                    "Neurologists","Gynecologists","Oncologists","Ophthalmologists(eye doctor)","Pediatricians","General Surgeons","urologist","ENT"]
                 dept=int(input("Select department for booking appointment:(enter serial number)"))
                 r=K[dept-1]
                 mycursor.execute("select * from appointment where DEPARTMENT='"+r+"'")
                 m=mycursor.fetchall()
                 n1=[("DOCTOR_ID","DEPARTMENT","DOCTOR_NAME","PHONE_NO","WING","TIME_SLOT1","TIME_SLOT2","TIME_SLOT3","TIMESLOT1","TIMESLOT2","TIMESLOT3")]
                 n1=n1+m
                 for i in n1:
                    for j in i:
                       a=" "
                       a=a+str(j)
                       while len(a)<15:
                          a=a+' '
                       print(a,end=" ")
                    print()
                 conn.commit()
                 sel=int(input("Enter doctor id to book appointment"))
                 mycursor.execute("select DOCTOR_NAME from appointment where DEPARTMENT='"+r+"' and DOCTOR_ID='"+str(sel)+"'")
                 f=mycursor.fetchall()
                 for i in f:
                       q=i[0]
                 
                 
                 print("======SELECT TIME SLOT IN WHICH YOU WANT TO BOOK AN APPOINTMENT======")
                 print("1.TIME SLOT 1")
                 print("2.TIME SLOT 2")
                 print("3.TIME SLOT 3")
                 ch9=int(input("Enter your choice:"))
                 time=" "
                 if count >3:
                    print("you cannot book more than three appointments")
                 else:
                      
                      if ch9==1:
                         x="booked"
                         mycursor.execute("select TIMESLOT1 from appointment where DEPARTMENT='"+r+"' and DOCTOR_ID='"+str(sel)+"'")
                         b=mycursor.fetchall()
                         if b!='booked':
                            mycursor.execute("update appointment set TIMESLOT1='"+x+"' where DEPARTMENT='"+r+"' and DOCTOR_ID='"+str(sel)+"'")
                            conn.commit()
                            time="TIME_SLOT1"
                            count=count+1
                         else:
                            print("SLOT NOT AVAILABLE")
                                          
                      elif ch9==2:
                         x="booked"
                         mycursor.execute("select TIMESLOT2 from appointment where DEPARTMENT='"+r+"' and DOCTOR_ID='"+str(sel)+"'")
                         b=mycursor.fetchall()
                         if b!='booked':
                            mycursor.execute("update appointment set TIMESLOT2='"+x+"' where DEPARTMENT='"+r+"' and DOCTOR_ID='"+str(sel)+"'")
                            conn.commit()
                            time="TIME_SLOT2"
                            count=count+1
                         else:
                            print("SLOT NOT AVAILABLE")
                                        
                      elif ch9==3:
                         x="booked"
                         mycursor.execute("select TIMESLOT2 from appointment where DEPARTMENT='"+r+"' and DOCTOR_ID='"+str(sel)+"'")
                         
                         
                         if b!='booked':
                            mycursor.execute("update appointment set TIMESLOT2='"+x+"' where DEPARTMENT='"+r+"' and DOCTOR_ID='"+str(sel)+"'")
                            conn.commit()
                            time="TIME_SLOT3"
                            count=count+1
                         else:
                            print("SLOT NOT AVAILABLE")
                                        
                      else:
                         print("invalid choice")
                      print("Appointment booked successfully")  
                 
                 
                    
                 mycursor.execute("update user_info set DEPARTMENT_BOOKED='"+r+"' where USERNAME='"+a+"'")
                 conn.commit()
                 mycursor.execute("update user_info set TIME_SLOT_BOOKED='"+time+"' where USERNAME='"+a+"'")
                 conn.commit()
                 mycursor.execute("update user_info set NAPP='"+str(count)+"' where USERNAME='"+a+"'")
                 conn.commit()
                 mycursor.execute("update user_info set DOCTOR_NAME='"+q+"' where USERNAME='"+a+"'")
                 conn.commit()
                 choii=input("Do you want to book more appointments?(y/n)")
           elif ch3==1.3 :
              printdept()
              K=['Immunologist',"Cardiologist","Dermatologist","General phyrsician","Gastroenterologists","Hematologists","Nephrologists",
                 "Neurologists","Gynecologists","Oncologists","Ophthalmologists(eye doctor)","Pediatricians","General Surgeons","urologist","ENT"]
              dept=int(input("Select department for canceling appointment:(enter serial number)"))
              
              r=K[dept-1]
              mycursor.execute("select * from appointment where DEPARTMENT='"+r+"'")
              m=mycursor.fetchall()
              n1=[("DOCTOR_ID","DEPARTMENT","DOCTOR_NAME","PHONE_NO","WING","TIME_SLOT1","TIME_SLOT2","TIME_SLOT3","TIMESLOT1","TIMESLOT2","TIMESLOT3")]
              n1=n1+m
              for i in n1:
                   for j in i:
                        a=" "
                        a=a+str(j)
                        while len(a)<15:
                             a=a+' '
                        print(a,end=" ")
                   print()
              conn.commit()
              sel=int(input("Enter doctor id for canceling appointment:"))
              delt=int(input("Enter the timeslot booked (1,2,3):"))
              
              
              mycursor.execute("select DOCTOR_NAME from appointment where DEPARTMENT='"+r+"' and DOCTOR_ID='"+str(delt)+"'")
              aa=mycursor.fetchall()
              q="NULL"
              for i in f:
                   r=i[0]    
                           
              print("Are you sure that you want to cancel your appointment with ",aa,"?(y/n)")
              sure=input()
              if sure=="y":
                   if delt==1:
                        mycursor.execute("update appointment set TIMESLOT1='"+q+"' where DEPARTMENT='"+r+"' and DOCTOR_ID='"+str(delt)+"'")
                        conn.commit()
                   elif delt==2:
                        mycursor.execute("update appointment set TIMESLOT2='"+q+"' where DEPARTMENT='"+r+"' and DOCTOR_ID='"+str(delt)+"'")
                        conn.commit()
                   elif delt==3:
                         mycursor.execute("update appointment set TIMESLOT3='"+q+"' where DEPARTMENT='"+r+"' and DOCTOR_ID='"+str(delt)+"'")
                         conn.commit()
                   else:
                         print("invalid choice")
                 
                 
                   print("Your appointment with ",aa,"for",r ,"has  been cancelled.")
                   count=count-1
              else:
                 print("Your appointment with ",aa,"for",r ,"has not been cancelled.")
              mycursor.execute("update user_info set NAPP='"+str(count)+"' where USERNAME='"+a+"'")
              conn.commit()

   elif ch1==2:
      print("WELCOME TO ")
      print("PORTAL FOR ADMIN")
      print("===================")
      print("ENTER YOUR REQUEST")

      print("  1.DOCTOR'S INFORMATION")
      print("      1.1 Add information")
      print("      1.2 Modify information")
      print("      1.3 Delete information")
      print("  2. BOOK APPOINTMENT")
      print("      2.1 Available doctors")
      print("      2.2 Book an Appointment" )
      print("      2.3 Cancel appointment")
      print("  3. SEARCH RECORD")
      print("  4. PATIENT INFORMATION")
      print("      4.1 User information")
      print("      4.2 Reset information")
      print("      4.3 Reset appointments")
      ch3=int(input("Enter your choice:"))
      if ch3==1:
         print("      1.1 Add information")
         print("      1.2 Modify information")
         print("      1.3 Delete information")
         ch4=float(input("Enter your choice:"))
         if ch4==1.1:
            DOCTOR_ID=int(input("Enter doctor's id:"))
            printdept()
            dep=int(input("Select doctor's department(Enter serial no.):"))

            L=['Immunologist',"Cardiologist","Dermatologist","General phyrsician","Gastroenterologists","Hematologists","Nephrologists",
                "Neurologists","Gynecologists","Oncologists","Ophthalmologists(eye doctor)","Pediatricians","General Surgeons","urologist","ENT"]
            
            q=L[dep-1]
            DEPARTMENT=q
            DOCTOR_NAME=input("Enter doctor's name")
            PHONE_NUMBER=input("Enter phone number:")
            WING=input("Enter hospital's wing")
            TIME_SLOT1=input("Enter time slot1 timings")
            TIME_SLOT2=input("Enter time slot2 timings")
            TIME_SLOT3=input("Enter time slot3 timings")
            TIMESLOT1="NULL"
            TIMESLOT2="NULL"
            TIMESLOT3="NULL"
            W=[DOCTOR_ID,DEPARTMENT,DOCTOR_NAME,PHONE_NUMBER,WING,TIME_SLOT1,TIME_SLOT2,TIME_SLOT3,TIMESLOT1,TIMESLOT2,TIMESLOT3]
            s="insert into appointment values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(s,W)
            conn.commit()
                    
            print("================RECORD ADDED SUCCESSFULLY===============")
            ex="select * from appointment"
            mycursor.execute(ex)
            
            m=mycursor.fetchall()
            m1=[("DOCTOR_ID","DEPARTMENT","DOCTOR_NAME","PHONE_NUMBER","WING","TIME_SLOT1","TIME_SLOT2","TIME_SLOT3","TIMESLOT1","TIMESLOT2","TIMESLOT3")]
            m1=m1+m
            for i in m1:
               for j in i:
                  a=" "
                  a=a+str(j)
                  while len(a)<15:
                     a=a+' '
                  print(a,end=" ")
               print()
            conn.commit()
              
         elif ch4==1.2:
            print("SELECT THE INFORMATION AREA YOU WANT TO MODIFY")
            print("1.Doctor's ID")
            print("2.Department")
            print("3.Doctor's Name")
            print("4.Phone Number")
            print("5.Wing")
            print("6.Time slot1")
            print("7.Time slot2")
            print("8.Time slot3")
            ch5=int(input("Enter your choice:"))
            if ch5==1:
               mycursor.execute("select DOCTOR_ID from appointment")
               m=mycursor.fetchall()
               wrong=int(input("Enter the doctor id you wish to modify:"))
               correction=int(input("Enter the updated DOCTOR ID:"))
               mycursor.execute("update appointment set DOCTOR_ID='"+str(correction)+"' where DOCTOR_ID='"+wrong+"'")
               conn.commit()
            elif ch5==2:
               printdept()
               K=['Immunologist',"Cardiologist","Dermatologist","General phyrsician","Gastroenterologists","Hematologists","Nephrologists",
                   "Neurologists","Gynecologists","Oncologists","Ophthalmologists(eye doctor)","Pediatricians","General Surgeons","urologist","ENT"]
                              
               dep=int(input("Select doctor's department(Enter serial no.) where you wish to modify:"))
               did=int(input("Enter doctor's id in which you wish to update department:"))
               dod=int(input("Select the changed department name:"))
               r=K[dep-1]
               t=K[dod-1]
               mycursor.execute("update appointment set DEPARTMENT='"+t+"' where DEPARTMENT='"+r+"' and DOCTOR_ID='"+str(did)+"'")
               conn,commit()
            elif ch5==3:
                  printdept()
                  K=['Immunologist',"Cardiologist","Dermatologist","General phyrsician","Gastroenterologists","Hematologists","Nephrologists",
                     "Neurologists","Gynecologists","Oncologists","Ophthalmologists(eye doctor)","Pediatricians","General Surgeons","urologist","ENT"]
                  u=K[dos-1]
                  doc=int(input("Enter doctor's id in which you wish to update doctor's name:"))
                  dos=int(input("Select doctor's department(Enter serial no.) where you wish to modify doctor's name:"))
                  update=input("Enter the updated information:")
                  mycursor.execute("update appointment set DOCTOR_NAME='"+update+"' where DEPARTMENT='"+u+"' and DOCTOR_ID='"+str(doc)+"'")
                  conn.commit()
                 
            elif ch5==4:
                  printdept()
                  K=['Immunologist',"Cardiologist","Dermatologist","General phyrsician","Gastroenterologists","Hematologists","Nephrologists",
                     "Neurologists","Gynecologists","Oncologists","Ophthalmologists(eye doctor)","Pediatricians","General Surgeons","urologist","ENT"]
                  dek=int(input("Select doctor's department(Enter serial no.) where you wish to modify doctor's contact details:"))
                  u=K[dek-1]
                  mycursor.execute("Select * from appointment where DEPARTMENT='"+u+"'")
                  m=mycursor.fetchall()
                  m1=[("DOCTOR_ID","DEPARTMENT","DOCTOR_NAME","PHONE_NUMBER","WING","TIME_SLOT1","TIME_SLOT2","TIME_SLOT3","TIMESLOT1","TIMESLOT2","TIMESLOT3")]
                  m1=m1+m
                  for i in m1:
                     for j in i:
                        a=" "
                        a=a+str(j)
                        while len(a)<15:
                           a=a+' '
                        print(a,end=" ")
                     print()
                  conn.commit()
                             
                  
                  den=int(input("Enter the doctor's id for the modification of information from above information:"))
                  corphn=input("Enter the updated phone number:")
                  mycursor.execute("update appointment set PHONE_NUMBER='"+corphn+"' where DEPARTMENT='"+u+"' and DOCTOR_ID='"+str(den)+"'")
                  conn.commit()
                              
            elif ch5==5:
                     printdept()
                     K=['Immunologist',"Cardiologist","Dermatologist","General phyrsician","Gastroenterologists","Hematologists","Nephrologists",
                        "Neurologists","Gynecologists","Oncologists","Ophthalmologists(eye doctor)","Pediatricians","General Surgeons","urologist","ENT"]
                     der=int(input("Select doctor's department(Enter serial no.) where you wish to modify hospital's wing:"))
                     v=K[der-1]
                     m1=[("WING")]
                     m1=m1+m
                     for i in m1:
                        for j in i:
                           a=" "
                           a=a+str(j)
                           while len(a)<22:
                              a=a+' '
                           print(a,end=" ")
                        print()
                     conn.commit()
                     ch6=int(input("Select your option for updation of hospital wing::"))
                     opt=list()
                     for i,row in enumerate(cursor.fetchall()):
                         opt.apphend(row[i])
                     sln=opt[ch6-1]
                     mycursor.execute("update appointment set WING='"+sln+"' where DEPARTMENT='"+v+"'")
                     conn.commit()
                              
            elif ch5==6:
                        printdept()
                        K=['Immunologist',"Cardiologist","Dermatologist","General phyrsician","Gastroenterologists","Hematologists","Nephrologists",
                           "Neurologists","Gynecologists","Oncologists","Ophthalmologists(eye doctor)","Pediatricians","General Surgeons","urologist","ENT"]
                        dem=int(input("Select doctor's department(Enter serial no.) where you wish to modify Time slot:"))
                        x=K[dem-1]
                        mycursor.execute("Select * from appointment where DEPARTMENT='"+x+"'")
                        m=mycursor.fetchall()
                        m1=[("DOCTOR_ID","DEPARTMENT","DOCTOR_NAME","PHONE_NUMBER","WING","TIME_SLOT1","TIME_SLOT2","TIME_SLOT3")]
                        m1=m1+m
                        for i in m1:
                              for j in i:
                                      a=" "
                                      a=a+str(j)
                                      while len(a)<15:
                                              a=a+' '
                                      print(a,end=" ")
                              print()
                        conn.commit()
                        didn=int(input("Select doctor's id from above where you wish to modify time slot:"))
                        tm1=input("Enter updated time slot:")
                        mycursor.execute("update appointment set TIME_SLOT1='"+tm1+"' where DEPARTMENT='"+x+"' and DOCTOR_ID='"+str(didn)+"'")
                        conn.commit()
            elif ch5==7:
                        printdept()
                        K=['Immunologist',"Cardiologist","Dermatologist","General phyrsician","Gastroenterologists","Hematologists","Nephrologists",
                           "Neurologists","Gynecologists","Oncologists","Ophthalmologists(eye doctor)","Pediatricians","General Surgeons","urologist","ENT"]
                        dem=int(input("Select doctor's department(Enter serial no.) where you wish to modify Time slot:"))
                        x=K[dem-1]
                        mycursor.execute("Select * from appointment where DEPARTMENT='"+x+"'")
                        m=mycursor.fetchall()
                        m1=[("DOCTOR_ID","DEPARTMENT","DOCTOR_NAME","PHONE_NUMBER","WING","TIME_SLOT1","TIME_SLOT2","TIME_SLOT3")]
                        m1=m1+m
                        for i in m1:
                           for j in i:
                              a=" "
                              a=a+str(j)
                              while len(a)<15:
                                 a=a+' '
                                 print(a,end=" ")
                           print()
                        conn.commit()
                        didn=int(input("Select doctor's id from above where you wish to modify time slot:"))
                        tm2=input("Enter updated time slot:")
                        mycursor.execute("update appointment set TIME_SLOT2='"+tm2+"' where DEPARTMENT='"+x+"' and DOCTOR_ID='"+str(didn)+"'")
                        conn.commit()
            elif ch5==8:
                        printdept()
                        K=['Immunologist',"Cardiologist","Dermatologist","General phyrsician","Gastroenterologists","Hematologists","Nephrologists",
                           "Neurologists","Gynecologists","Oncologists","Ophthalmologists(eye doctor)","Pediatricians","General Surgeons","urologist","ENT"]
                        dem=int(input("Select doctor's department(Enter serial no.) where you wish to modify Time slot:"))
                        x=K[dem-1]
                        mycursor.execute("Select * from appointment where DEPARTMENT='"+x+"'")
                        m=mycursor.fetchall()
                        m1=[("DOCTOR_ID","DEPARTMENT","DOCTOR_NAME","PHONE_NUMBER","WING","TIME_SLOT1","TIME_SLOT2","TIME_SLOT3")]
                        m1=m1+m
                        for i in m1:
                           for j in i:
                              a=" "
                              a=a+str(j)
                              while len(a)<15:
                                 a=a+' '
                              print(a,end=" ")
                           print()
                        conn.commit()
                        didn=int(input("Select doctor's id from above where you wish to modify time slot:"))
                        tm3=input("Enter updated time slot:")
                        mycursor.execute("update appointment set TIME_SLOT3='"+tm3+"' where DEPARTMENT='"+x+"' and DOCTOR_ID='"+str(didn)+"'")
                        conn.commit()
            else:
                         print("INVALID CHOICE")
         elif choice==1.3:
            printdept()
            K=['Immunologist',"Cardiologist","Dermatologist","General phyrsician","Gastroenterologists","Hematologists","Nephrologists",
              "Neurologists","Gynecologists","Oncologists","Ophthalmologists(eye doctor)","Pediatricians","General Surgeons","urologist","ENT"]
            deldep=int(input("Select doctor's department(Enter serial number) from which you want to delete record"))
            d=K[deldep-1]
            mycursor.execute("select * from appointment where DEPARTMENT='"+deldep+"'")
            m=mycursor.fetchall()
            m1=[("DOCTOR_ID","DEPARTMENT","DOCTOR_NAME","PHONE_NUMBER","WING","TIME_SLOT1","TIME_SLOT2","TIME_SLOT3")]
            m1=m1+m
            for i in m1:
               for j in i:
                  a=" "
                  a=a+str(j)
                  while len(a)<15:
                     a=a+' '
                  print(a,end=" ")
               print()
            conn.commit()
            doid=int(input("Enter doctor id from above which needs to be deleted:"))
            mycursor.execute("Delete from appointment where DEPARTMENT='"+d+"'and DOCTOR_ID='"+str(doid)+"'")
            conn.commit()
      elif ch3==2:
         print("2.1 Available doctors")
         print("2.2 Book an Appointment" )
         print("2.3 Cancel appointment")
         ch8=float(input("Enter your choice:"))
         if ch8==2.1:
            mycursor.execute("select * from appointment where TIME_SLOT1=NULL or TIME_SLOT2=NULL or TIME_SLOT3=NULL")
            m=mycursor.fetchall()
            m1=[("DOCTOR_ID","DEPARTMENT","DOCTOR_NAME","PHONE_NUMBER","WING","TIME_SLOT1","TIME_SLOT2","TIME_SLOT3")]
            m1=m1+m
            for i in m1:
               for j in i:
                  a=" "
                  a=a+str(j)
                  while len(a)<15:
                       a=a+' '
                  print(a,end=" ")
               print()
            conn.commit()
         elif ch8==2.2 :
            choii="y"
            while choii=="y":
               print("==============AVAILABLE TIME SLOTS===============")
            mycursor.execute("select * from appointment")
            m=mycursor.fetchall()
            n1=[("DOCTOR_ID,DEPARTMENT,DOCTOR_NAME,TIME_SLOT1,TIME_SLOT2,TIME_SLOT3,TIMESLOT1,TIMESLOT2,TIMESLOT3")]
            n1=n1+m
            for i in n1:
               for j in i:
                  a=" "
                  a=a+str(j)
                  while len(a)<15:
                     a=a+' '
                     print(a,end=" ")
               print()
            conn.commit()
                     
            printdept()
            K=['Immunologist',"Cardiologist","Dermatologist","General phyrsician","Gastroenterologists","Hematologists","Nephrologists",
                 "Neurologists","Gynecologists","Oncologists","Ophthalmologists(eye doctor)","Pediatricians","General Surgeons","urologist","ENT"]
            dept=int(input("Select department for booking appointment:(enter serial number)"))
            r=K[dept-1]
            mycursor.execute("select * from appointment where DEPARTMENT='"+r+"'")
            d=mycursor.fetchall()
            for i in d:
                 f=i[0]
            sel=int(input("Enter doctor id to book appointment"))
             
            print("======SELECT TIME SLOT IN WHICH YOU WANT TO BOOK AN APPOINTMENT======")
            print("1.TIME SLOT 1")
            print("2.TIME SLOT 2")
            print("3.TIME SLOT 3")
            ch9=int(input("Enter your choice:"))
            time=" "
            if count >3:
                      print("you cannot book more than three appointments")
            else:          
                      if ch9==1:
                         x="booked"
                         mycursor.execute("select TIMESLOT1 from appointment where DEPARTMENT='"+r+"' and DOCTOR_ID='"+str(sel)+"'")
                         b=mycursor.fetchall()
                         if b!='booked':
                            mycursor.execute("update appointment set TIMESLOT1='"+x+"' where DEPARTMENT='"+r+"' and DOCTOR_ID='"+str(sel)+"'")
                            conn.commit()
                            time=TIME_SLOT1
                            count=count+1
                         else:
                            print("SLOT NOT AVAILABLE")
                              
                      elif ch9==2:
                            x="booked"
                            mycursor.execute("select TIMESLOT2 from appointment where DEPARTMENT='"+r+"' and DOCTOR_ID='"+str(sel)+"'")
                            b=mycursor.fetchall()
                            if b!='booked':
                                mycursor.execute("update appointment set TIMESLOT2='"+x+"' where DEPARTMENT='"+r+"' and DOCTOR_ID='"+str(sel)+"'")
                                conn.commit()
                                time=TIME_SLOT2
                                count=count+1
                            else:
                                print("SLOT NOT AVAILABLE")
                            
                      elif ch9==3:
                            x="booked"
                            mycursor.execute("select TIMESLOT2 from appointment where DEPARTMENT='"+r+"' and DOCTOR_ID='"+str(sel)+"'")
                            b=mycursor.fetchall()
                            if b!='booked':
                                mycursor.execute("update appointment set TIMESLOT2='"+x+"' where DEPARTMENT='"+r+"' and DOCTOR_ID='"+str(sel)+"'")
                                conn.commit()
                                time=TIME_SLOT3
                                count=count+1
                            else:
                                print("SLOT NOT AVAILABLE")
                       
                      else:
                           print("invalid choice")
            print("Appointment booked successfully")  
           
            mycursor.execute("update user_info set DEPARTMENT_BOOKED='"+r+"' where USERNAME='"+a+"'")
            conn.commit()
            mycursor.execute("update user_info set TIME_SLOT_BOOKED='"+time+"' where USERNAME='"+a+"'")
            conn.commit()
            mycursor.execute("update user_info set NAPP='"+count+"' where USERNAME='"+a+"'")
            conn.commit()
            mycursor.execute("update user_info set DOCTOR_NAME='"+f+"' where USERNAME='"+a+"'")
            conn.commit()
            choii=input("Do you want to book more appointments?(y/n)")


         elif ch8==2.3:
            printdept()
            K=['Immunologist',"Cardiologist","Dermatologist","General phyrsician","Gastroenterologists","Hematologists","Nephrologists",
              "Neurologists","Gynecologists","Oncologists","Ophthalmologists(eye doctor)","Pediatricians","General Surgeons","urologist","ENT"]
            dept=int(input("Select department for canceling appointment:(enter serial number)"))
            r=K[dept-1]
            mycursor.execute("select * from timeslot where DEPARTMENT='"+r+"'")
            sel=int(input("Enter doctor id for canceling appointment:"))
            u="delete * from appointment where DEPARTMENT='"+r+"' and DOCTOR_ID='"+str(sel)+"'"
            mycursor.execute("select DOCTOR_NAME from appointment where DEPARTMENT='"+r+"' and DOCTOR_ID='"+str(sel)+"'")
            aa=mycursor.fetchall()
            for i in aa:
                 v=i[0]
            print("Are you sure that you want to cancel your appointment with ",aa,"?(y/n)")
            sure=input()
            if sure=="y":
                      if delt==1:
                        mycursor.execute("update appointment set TIMESLOT1='"+q+"' where DEPARTMENT='"+r+"' and DOCTOR_ID='"+str(delt)+"'")
                        conn.commit()
                      elif delt==2:
                        mycursor.execute("update appointment set TIMESLOT2='"+q+"' where DEPARTMENT='"+r+"' and DOCTOR_ID='"+str(delt)+"'")
                        conn.commit()
                      elif delt==3:
                          mycursor.execute("update appointment set TIMESLOT3='"+q+"' where DEPARTMENT='"+r+"' and DOCTOR_ID='"+str(delt)+"'")
                          conn.commit()
                      else:
                         print("invalid choice")
                 
                      print("Your appointment with ",v,"for",r ,"has  been cancelled.")
                      count=count-1
               
               
            else:
                print("Your appointment with ",v,"for",r ,"has not been cancelled.")
      elif ch3==4:
         print("4.1 User information")
         print("4.2 Reset information")
         print("4.3 Reset appointments")
         ch10=float(input("Enter your choice:"))
         if ch10==4.1:
           mycursor.execute("select * from user_info")
           l=mycursor.fetchall()
           n1=[("SNO","USERNAME","FIRST_NAME","LAST_NAME" , "AGE","SEX", "DEPARTMENT_BOOKED", "DOCTOR_NAME" , "TIME_SLOT_BOOKED","DATE_OF_BOOKING"  ,"NAPP")]
           n1=n1+l
           for i in n1:
              for j in i:
                 a=" "
                 a=a+str(j)
                 while len(a)<15:
                    a=a+' '
                 print(a,end=" ")
              print()
           conn.commit()
         elif ch==4.2:
           mycursor.execute("delete * from user_info")
           conn.commit()
         elif ch==4.3:
           mycursor.execute("alter appointment set TIMESLOT1=NULL AND TIMESLOT2=NULL AND TIMESLOT3=NULL")
           conn.commit()
         else:
              print("INVALID CHOICE")


      elif ch3==3:
         printdept()
         K=['Immunologist',"Cardiologist","Dermatologist","General phyrsician","Gastroenterologists","Hematologists","Nephrologists",
            "Neurologists","Gynecologists","Oncologists","Ophthalmologists(eye doctor)","Pediatricians","General Surgeons","urologist","ENT"]

         depse=int(input("Select the department(Enter serial number)for which you want to search information:"))
         z=K[depse-1]
         mycursor.execute("select DOCTOR_ID, DOCTOR_NAME from appointment where DEPARTMENT='"+depse+"'")
         m=mycursor.fetchall()
         m1=[("DOCTOR_ID","DOCTOR_NAME")]
         m1=m1+m
         for i in m1:
            for j in i:
               a=" "
               a=a+str(j)
               while len(a)<15:
                       a=a+' '
               print(a,end=" ")
            print()
            conn.commit()
         ch7=int(input("Enter doctor's id:"))
        

         mycursor.execute("Select * from appointment where DEPARTMENT='"+z+"' and DOCTOR_ID='"+str(ch7)+"'")
         conn.commit()

else:
   exit()























             
             
             
























 












    
