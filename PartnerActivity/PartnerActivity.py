
#Partner activity.. Names:__Brayan Quintana, Armando Rubio, Mauricio Munoz___________________________________________
school = {
    "class": {
        "name": "Math 101",
        "students": {"student1": "A", "student2": "B", "student3": "C"}
    }
}


# Update the grade of student2
school["class"]["students"][2] = "A+"


#Find the student who is making an A and upgrade it to an A +
print([school]["class"]["students"][1])
school["class"]["students"][1] = "A+"

# Define the dictionary
product_inventory = {
    "warehouse1": {
        "products": ["apples", "oranges", "bananas"],
        "quantities": [50, 30, 20]
    },
    "warehouse2": {
        "products": ["grapes", "pears", "peaches"],
        "quantities": [60, 40, 30]
    }
}


# Find the total number of oranges in warehouse1
print(product_inventory["warehouse1"]["quantities"][1])

#Sum up all the quantities in the warehouse
product_quan1 = int(product_inventory["warehouse1"]["quantities"][1])
product_quan2 = int(product_inventory["warehouse1"]["quantities"][2])
product_quan3 = int(product_inventory["warehouse1"]["quantities"][3])
product_quan11 = int(product_inventory["warehouse2"]["quantities"][1])
product_quan22 = int(product_inventory["warehouse2"]["quantities"][2])
product_quan33 = int(product_inventory["warehouse2"]["quantities"][3])
print(product_quan1 + product_quan11 + product_quan2 + product_quan22 + product_quan3 + product_quan33)