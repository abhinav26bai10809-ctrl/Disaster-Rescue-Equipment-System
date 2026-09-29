def equipment_categories():
    print("\nEquipment Categories")
    Categories = ("Medical Equipments","Communication Equipments","Safety Equipments","Rescue Equipments")
    print("1.", Categories[0])
    print("2.", Categories[1])
    print("3.", Categories[2])
    print("4.", Categories[3])
    Category = input("Enter Your Category:").title()
    if Category == "Medical Equipments":
        print("Bandages, Stretchers, Emergency Medicines, Medical gloves")
    elif Category == "Communication Equipments":
        print("Two way radios, Megaphones, Mobile Phones, Signal Devices")
    elif Category == "Safety Equipments":
        print("Safety Helmets, Safety Gloves, Safety Goggles, Dust Masks, Respirators")
    elif Category == "Rescue Equipments":
        print("Rescue Ropes, Rescue Boats, Throw Bags, Shovels, Crowbars, Cutting Tools")