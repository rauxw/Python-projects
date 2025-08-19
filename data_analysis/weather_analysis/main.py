import pandas

data = pandas.read_csv("weather_data.csv")

data_dict = {
  "students":["Amy", "James", "Angela"],
  "scores":  [76, 56, 65]
}

data_students = pandas.DataFrame(data_dict)
data_students.to_csv("students_data.csv")
print(data_students)