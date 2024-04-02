from pymysql import connect

def is_valid_fullname(fullname: str) -> bool:
    """Validates fullname

    Args:
        fullname (str): First and Last names separated by whitespaces

    Returns:
        bool: True or False, depends on validation
    """
    
    if len(fullname.split(" ")) != 2:
        return False
    
    first_name, last_name = fullname.split(" ")

    if len(first_name) < 3 or len(last_name) < 3:
        return False
    
    return True

def is_valid_age(age: str) -> bool:
    """Validates age

    Args:
        age (str): Age passed as text

    Returns:
        bool: _True or False, depends on validation
    """
    try:
        age = int(age)
        if age >= 18 and age <= 110:
            return True
        else:
            return False
    except:
        return False

database = connect(database='railway',
        user='root',
        password='WRVJVrBICiromDErUZqqdKVjCEuJIHMP',
        host='viaduct.proxy.rlwy.net',
        port=18056)

cursor = database.cursor()


cursor.execute('''
               CREATE TABLE IF NOT EXISTS users(
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    first_name VARCHAR(50) NOT NULL,
                    last_name VARCHAR(50) NOT NULL,
                    age INT NOT NULL,

                    UNIQUE(first_name, last_name)
               )''')
            
while True:
    fullname = input("Enter your last and first names seperated by space, ex. John Doe:" )

    fullname_is_valid = is_valid_fullname(fullname)

    if is_valid_fullname == False:
        print("Invalid First and Last names length")
        continue
    age = input("Enter your age, ex. 18-110: ")

    age_is_valid = is_valid_age(age)
    
    if age_is_valid == False:
        print("Invalid age")
        continue

    first_name, last_name = fullname.split(" ")
    try:
        cursor.execute('''
                       INSERT INTO users (first_name, last_name, age)
                       VALUES (%s, %s, %s)
                    ''', (first_name, last_name, age))
        database.commit()
        print(f"User has been succesfully registered in a system\n")
    except:
        print(f"User already exists in a system\n")