class Employee:
    
    def __init__(self, name, id_number, department, job_title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title

    def set_name(self, name):
        self.__name = name

    def set_id_number(self, id_number):
        self.__id_number = id_number

    def set_department(self, set_department):
        self.__set_department = set_department

    def get_name(self):
        return self.__name

    def get_id_number(self):
        return self.__id_number

    def get_department(self):
        return self.__get_department

    def get_job_title(slef):
        return self.__get_job_title

    def __str__(self):
        return 'Name: ' + self.__name + '\nID number: ' + self.__id_number + '\nDepartment: ' + self.__department + '\nTitle: ' + self.__job_title
        
