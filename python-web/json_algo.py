import json
from algorithm1 import algorithm1,Course,Student,random,TabuList,copy,map_price_demand,reset_update_prices,cmp_to_key,reset_students,time

def load_from_json_algorithm1(file_name: str):
    """
    Loads all the arguments from a json file and outputs the algorithm1 result.
    @param file_name: The path to the json file
    @returns True if the loading was successful, False o.w.
    """
    try:
        with open(file_name) as file:
            s = json.load(file)
            courses = []
            for course in s["courses"]:
                courses.append(
                    Course(name=course["name"], price = course["price"],
                        max_capacity= course["max_capacity"], capacity=course["capacity"])
                )
            helper = {course.name:course for course in courses}

            students = []
            for student in s["students"]:
                # pref = student["preferences"].split(",")
                preferences=json.loads(student["preferences"])
                students.append(
                    Student(name=student["name"], budget=student["budget"],
                        preferences=[helper[pre] for pre in preferences],
                        courses=[]
                    )
                )
            max_budget = s["max_budget"]
            if "time_to" in s:
                time_to = s["time_to"]
            if "seed" in s:
                seed = s["seed"]
            return str(algorithm1(students, courses, max_budget))
    except Exception as e:
        print(e)
        return str(False)
    finally:
        file.close()
        
from algorithm2 import algorithm2,Course,Student,csp_mapping,copy,math,cmp_to_key
def load_from_json_algorithm2(file_name: str):
    """
    Loads a graph from a json file.
    @param file_name: The path to the json file
    @returns True if the loading was successful, False o.w.
    """
    try:
        with open(file_name) as file:
            s = json.load(file)
            courses = []
            for course in s["courses"]:
                courses.append(
                    Course(name=course["name"], price = course["price"],
                        max_capacity= course["max_capacity"], capacity=course["capacity"])
                )
            helper = {course.name:course for course in courses}

            students = []
            for student in s["students"]:
                preferences=json.loads(student["preferences"])
                students.append(
                    Student(name=student["name"], budget=student["budget"],
                        preferences=[helper[pre] for pre in preferences],
                        courses=[]
                    )
                )
            price_vector = json.loads(s["price_vector"])
            maximum = s["maximum"]
            eps = s["eps"]
            return str(algorithm2(price_vector,maximum,eps, students,courses))
    except Exception as e:
        print(e)
        return str(False)
    finally:
        file.close()

from algorithm3 import algorithm3,mapping_csp
def load_from_json_algorithm3(file_name: str):
    """
    Loads a graph from a json file.
    @param file_name: The path to the json file
    @returns True if the loading was successful, False o.w.
    """
    try:
        with open(file_name) as file:
            s = json.load(file)
            courses = []
            for course in s["courses"]:
                courses.append(
                    Course(name=course["name"], price = course["price"],
                        max_capacity= course["max_capacity"], capacity=course["capacity"])
                )
            helper = {course.name:course for course in courses}

            students = []
            for student in s["students"]:
                preferences=json.loads(student["preferences"])
                students.append(
                    Student(name=student["name"], budget=student["budget"],
                        preferences=[helper[pre] for pre in preferences],
                        courses=[]
                    )
                )
            students_matrix = json.loads(s["students_matrix"])
            return algorithm3(courses, students, students_matrix)
    except Exception as e:
        print(e)
        return str(False)
    finally:
        file.close()