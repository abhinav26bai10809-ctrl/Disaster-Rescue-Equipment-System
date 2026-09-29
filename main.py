from Disaster_Assessment import disaster_assessment
from Emergency_Checklist import emergency_checklist
from Equipment_Categories import equipment_categories
while True:
    A = ("Welcome to the Disaster Assessment and Rescue Equipments System")
    print(A.center(100, '*'))
    print("\n1. Select Disaster:")
    print("2. Exit")
    print("3. Emergency Checklist")
    print("4. Equipment Categories")
    Choice = input("\nEnter Your Choice:")
    if Choice == "1":
        disaster_assessment()
    elif Choice == "2":
        print("\nThank you for using the Disaster Assessment and Rescue Equipments System")
        break
    elif Choice == "3":
        emergency_checklist()
    elif Choice == "4":
        equipment_categories()
    else:
        print("\nInvalid Choice. Please enter 1 or 2 or 3 or 4")