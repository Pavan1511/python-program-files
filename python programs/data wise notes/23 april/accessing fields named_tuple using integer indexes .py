#accessing fields named_tuple using integer indexes

from collections import namedtuple
def student_info():
	student=namedtuple('student',"usn name sem college cgpa")
	stud=student("ivi16is075","pavan",8,'vit',8.35)
	print(stud)
	#accessing field by using integer indexes
	print(stud[0],stud[1],stud[2],stud[3])
	print()

	#accessing field by using a built-in function --->getattr(ref,"field_name")
	print(getattr(stud,'usn'))
	print(getattr(stud,'sem'))
	#print the stud-->display named tuple
	print(stud.college)
	print(stud.sem)


if __name__ == '__main__':
	student_info()