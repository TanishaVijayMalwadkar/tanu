import csv
CSV_File='students.csv'
def read_csv():
    with open(CSV_File,mode='r',newline='') as file:
        reader=csv.DictReader(file)
        return list(reader)
    
def write_csv(data):
    with open(CSV_File,mode='w',newlinw='') as file:
        writer=csv.DictReader(file,fieldnames=['name','room_no','mobile_no','date','ragistor_no','fees','adress'])
        writer.writeheader()
        writer.writerows(data)

def add(name,room_no,mobile_no,date,ragistor_no,fees,adress):
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

def read_record(data):
    """
    Read and Display all the record.
    """
    students=read_csv()
    if not students:
      print("No record data found:")
      return 


    headers=['regNo','name','address','moNo','csrNm','sem','fee']
    col_widths={header:len(header) for header in headers}
    
    for student in students:
        for header in headers:
            col_widths[header]=max(col_widths[header],len(student[header.lower().replace(' ','_')]))
        separator='+-'+'-+-'.join(['-'*col_widths[header] for header in headers])+' | '
        header_row='| '+' |'.join([header.ljust(col_widths[header]) for header in headers])+' | '
        print(separator)
        print(header_row) 
        print(separator)
        for student in students:
            row='| '+' | '.join([student[header.lower().replace(' ','_')].ljust(col_widths[header])for header in headers]) + ' | '
            print(row)
        print(separator) 
    
def update_student(Regno,Name=None,Address=None,MoNo=None,CsrNm=None,Sem=None,Fee=None):
    data=read_csv()
    for student in data:
        if student['regNo']== Regno :
            if Name:
                student['name']==Name
            if Address:
                student['address']==Address
            if MoNo:
                student['moNo']==MoNo
            if CsrNm:
                student['csrNm']==CsrNm
            if Sem:
                student=['sem']==Sem                
            if Fee:
                student=['fee']==Fee                
            break
    write_csv(data) 
 
def delete_student(regNo):
    data=read_csv()
    data=[student for student in data if student['regNo'] != regNo] 
    write_csv(data)                          
