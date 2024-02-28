contacts = {
    'police' : 112,
    'emergency' : 101,
}
while True:
    name = input('🔍 search any contacts: ')
    if len(name) == 0:
        print('👋bye')
        break

    if name in contacts:
        print(f"📞{name} : {contacts[name]}")  
    elif name == "all":
        for name, number in contacts,item():
            print(f"📞{name}: {number}")
        print('-') 
    else:
        print(f"🚫{name} not found")
        ch = input('😒 want to add contacts? (y/n):')
        if  ch == 'y':
            number = input("📞 enter number")
            contacts[name] = number
            print(f"✌️{name} added to contacts")
            print('-'* 20)