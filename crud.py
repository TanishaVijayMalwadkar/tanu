import csv

csv_file='hostel.csv'
CSV_File='Hostel1.csv'
def read_csv():
    with open(csv_file,mode='r',newline='') as file:
        reader=csv.DictReader(file)
        return list(reader)
    
  with open(CSV_File,mode='r',newline='')as file:
    reader=csv.DictReader(file)
    return list(reader)

def write_csv(data):
    with open(csv_file,mode='w',newlinw='') as file:
        write=csv.DictReader(file,filednames=['name','room_no','mobile_no','date','ragistor_no','fees','adress'])
        writer.writeheader()
        writer.writerows(data)

def add(name,room_no,mobile_no,date,ragistor_name,fees,adress):
    data=read_csv
    new_rec={'Name':name,'Room_no':room_no,'Mobile_no':mobile_no,'Date':date,'Ragistor_no':ragistor_no,'Fees':fees,'Adress':adress}
    data.append(new_rec)
    write_csv(data)



def create_record(name,room_no,mobile_no,date,ragistor_no,fees,adress):
    """
    name(str):Name of student.
    room_no(str):Room_no of student
    mobile_no(str):Mobile_no of student
    date(str):Date of 
    ragistor_no(str):Ragistor_no of student
    fees(str):Fees of student
    adress(str):Adress of student
    """
    data=read_csv()
    new_record={'Name':name,'Room_no':room_no,'Mobile_no':mobile_no,'Date':date,'Ragistor_no':ragistor_no,'fees':fees,'Adress':adress}
    date.append(new_record)
    write_csv(data)

def read_record():
    """
    Read and Display all the record.
    """
    srecord=read_csv()
    if not srecord:
      print("No record data found:")
      return 
    with open(CSV_File,mode='w',newline='')as file:
       writer=csv.DictWriter(file,feildsname=['regNo','name','address','moNo','crsNm','sem','fee'])
       writer.writeheader()
       writer.writerows(data)

def addStudent(regNo,name,address,moNo,crsNm,sem,fee):
  data=read_csv()
  new_student={'regNo':regNo, 'name':name, 'address':address, 'moNo':moNo, 'csrNm':crsNm, 'sem':sem, 'fee':fee}
  data.append(new_student)
  write_csv(data)

def readStudent():
  students=read_csv()
  if not students:
    print(" No Stduent Data found:")
    return
  headers=['regNo','name','address','moNo','csrNm','sem','fee']
  col=widths={header:len(header) for header in headers}
  for student in student:
    for header in headers:
      col_widths[header]=max(col_widths[header],len(student[header.lower().replace('','_')]))
  separator='+-'+'-+-'.join(['-'*col_widths[header] for header in headers])+'|'
  header_row='| '+' |'.join([header.ljust(col_widths[header]) for header in headers])+'|'
  print(sepa)    
