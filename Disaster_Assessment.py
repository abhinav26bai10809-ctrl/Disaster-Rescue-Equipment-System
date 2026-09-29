def disaster_assessment():
    print("\nStarting Disaster Assessment and Rescue Equipments System....")
    Dis1 = ("Flood")
    print(Dis1)
    Dis2 = ("Earthquake")
    print(Dis2)
    Dis3 = ("Cyclone")
    print(Dis3)
    Dis4 = ("Drought")
    print(Dis4)
    Dis5 = ("Landslide")
    print(Dis5)
    Dis6 = ("Tsunami")
    print(Dis6)
    Disaster = input("Enter the name of the disaster:").capitalize()
    if Disaster not in ("Flood" , "Earthquake" , "Tsunami" , "Cyclone" , "Drought" , "Landslide"):
        print("Invalid Choice!!!")
    Sev1 = ("High")
    print(Sev1)
    Sev2 = ("Mid")
    print(Sev2)
    Sev3 = ("Low")
    print(Sev3)
    Severity = input("Enter the severity of the disaster:").capitalize()
    if Severity not in ("High" , "Low" , "Mid"):
        print("Invalid Severity")
    elif Severity == "High":
        if Disaster == "Earthquake":
            print("Recommended Equipments are : Rescue helmets , Safety gloves , Safety goggles , Dust masks/respirators , First-aid kits , Stretchers , Rescue ropes , Shovels Picks , Crowbars , Cutting tools , Flashlights , Extra batteries , Two-way radios , Portable generators , Emergency food , Drinking water , Blankets , Emergency tents")
        elif Disaster == "Flood":
            print("Recommended Equipments are : Life jackets , Rescue boats , Rescue ropes , Throw bags , First-aid kits , Stretchers , Water pumps , Water purification equipment , Drinking-water containers , Two-way radios , Flashlights , Extra batteries , Portable generators , Emergency food , Blankets , Emergency tents")
        elif Disaster == "Cyclone":
            print("Recommended Equipments are : Rescue helmets , Safety gloves , Safety goggles , First-aid kits , Rescue ropes , Life jackets , Stretchers , Chainsaws/cutting tools , Flashlights , Extra batteries , Two-way radios , Portable generators , Water pumps , Emergency food , Drinking-water containers , Blankets , Tarpaulins , Emergency tents")
        elif Disaster == "Tsunami":
            print("Recommended Equipments are : Life jackets , Rescue boats , Rescue ropes , Throw bags , First-aid kits , Stretchers , Two-way radios , Megaphones , Flashlights , Extra batteries , Portable generators , Drinking-water containers , Water purification equipment , Emergency food , Blankets , Emergency tents , Tarpaulins")
        elif Disaster == "Drought": 
            print("Recommended Equipments are : Large water storage tanks , Water transport containers , Water pumps , Water purification systems , Water testing kits , Water distribution pipes/hoses , Drinking-water containers , Emergency food supplies , First-aid kits , Two-way radios , Portable generators , Flashlights , Extra batteries , Protective gloves , Emergency shelters/tents")
        elif Disaster == "Landslide":
            print("Recommended Equipments are : Rescue helmets , Safety gloves , Safety goggles , Dust masks/respirators , First-aid kits , Stretchers , Rescue ropes , Shovels , Picks , Crowbars , Cutting tools , Flashlights , Extra batteries , Two-way radios , Portable generators , Emergency food , Drinking water , Blankets , Emergency tents")
    elif Severity == "Mid":
        if Disaster == "Earthquake":
            print("Recommended Equipments are : First-aid kits , Helmets , Safety gloves , Safety goggles , Flashlights , Batteries , Two-way radios , Ropes , Stretchers , Basic rescue tools , Dust masks , Drinking water , Emergency food , Portable generators , Blankets")
        elif Disaster == "Flood":
            print("Recommended Equipments are : Life jackets , Rescue ropes , Rescue boats , First-aid kits , Flashlights , Batteries , Two-way radios , Water pumps , Drinking-water containers , Emergency food supplies , Blankets , Portable generators")
        elif Disaster == "Cyclone":
            print("Recommended Equipments are : Helmets , Safety gloves , First-aid kits , Flashlights , Batteries , Two-way radios , Ropes , Emergency food supplies , Drinking-water containers , Portable generators , Tarpaulins , Blankets")
        elif Disaster == "Tsunami":
            print("Recommended Equipments are : Life jackets , Rescue ropes , First-aid kits , Stretchers , Flashlights , Batteries , Two-way radios , Drinking-water containers , Emergency food supplies , Blankets , Portable generators , Emergency tents")
        elif Disaster == "Drought": 
            print("Recommended Equipments are : Drinking-water containers , Water tanks , Water purification tablets/filters , Water testing kits , Water pumps , Water distribution pipes/hoses , First-aid kits , Protective gloves , Masks , Communication radios , Emergency food supplies , Portable generators , Flashlights , Batteries")
        elif Disaster == "Landslide":
            print("Recommended Equipments are : Helmets , Safety gloves , Safety goggles , Dust masks , First-aid kits , Shovels , Picks , Ropes , Stretchers , Flashlights , Batteries , Two-way radios , Emergency food , Drinking water , Portable generators , Blankets")
    elif Severity == "Low":
        if Disaster == "Earthquake":
            print("Recommended Equipments are : First-aid kit , Safety helmet , Safety gloves , Flashlight , Extra batteries , Dust mask , Drinking water , Emergency food , Basic rescue rope , Two-way radio")
        elif Disaster == "Flood":
            print("Recommended Equipments are : Life jackets , Rescue rope , First-aid kit , Flashlight , Extra batteries , Drinking-water containers , Emergency food , Two-way radio , Basic water pump , Blankets")
        elif Disaster == "Cyclone":
            print("Recommended Equipments are : First-aid kit , Safety helmet , Safety gloves , Flashlight , Extra batteries , Two-way radio , Drinking water , Emergency food , Blankets , Tarpaulin")
        elif Disaster == "Tsunami":
            print("Recommended Equipments are : Life jackets , First-aid kit , Rescue rope , Flashlight , Extra batteries , Two-way radio , Drinking water , Emergency food , Blankets , Emergency tent")
        elif Disaster == "Drought": 
            print("Recommended Equipments are : Drinking-water containers , Small water storage tanks , Water purification tablets/filters , Water testing kit , Emergency food , First-aid kit , Protective gloves , Flashlight , Extra batteries , Two-way radio")
        elif Disaster == "Landslide":
            print("Recommended Equipments are : Safety helmet , Safety gloves , Dust mask , First-aid kit , Shovel , Rescue rope , Flashlight , Extra batteries , Two-way radio , Drinking water")