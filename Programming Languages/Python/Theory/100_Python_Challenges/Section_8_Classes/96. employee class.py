'''
Create a class Employee that will take a full_name as argument, as well as a set of none, one or more keywords. Each instance should have a first_name and a last_name attributes plus one more attribute for each of the keywords, if any. First and last names will be separated by a whitespace. The test will not include any middle names or initials. The value of the keywords can be an int, a str or a list.

Examples:

Nancy = Employee("Nancy Drew")

Maya = Employee("Maya Jones", salary=72000)

William = Employee("William Smith", salary=60000, dept='Accounting')

Allen = Employee("Allen Brown", salary=84000, dept='IT', age=45)



Expected output:

Nancy.first_name = 'Nancy'

Maya.last_name = 'Jones'

William_dept = 'Accounting'
'''