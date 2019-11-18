# Author Errolyn McGahan

# Arcane Adventure

rooms = {
   'entrance': {'name': "Entry Room", 'doors': 1, 'locked_doors': 0, 'items': ['sword', 'unknown potion'], 'enemeys': 0, 'connections': [], 'description':""},
   'armory': {'name': "Armory Room", 'doors': 1, 'locked_doors': 0, 'items': ['empty chest', 'sharpening stone'], 'enemeys': 1, 'connections': [], 'description':""},
   'kitchen': {'name': "Kitchen", 'doors': 2, 'locked_doors': 0, 'items': ['knife','dried meat', 'wine'], 'enemeys': 2, 'connections': [], 'description':""},
   'chamber_1': {'name': "Guest Bedroom", 'doors': 1, 'locked_doors': 0, 'items': ['none'], 'enemeys': 1, 'connections': [], 'description':""},
   'chamber_2': {'name': "Kids Bedroom", 'doors': 2, 'locked_doors': 0, 'items': ['key'], 'enemeys': 1, 'connections': [], 'description':""},
   'tunnel_1': {'name': "Dark Tunnel", 'doors': 4, 'locked_doors': 1, 'items': ['none'], 'enemeys': 0, 'connections': [], 'description':""},
   'tunnel_2': {'name': "Hallway", 'doors': 4, 'locked_doors': 1, 'items': ['none'], 'enemeys': 0, 'connections': [], 'description':""},
   'stuck_door': {'name': "Stuck Door", 'doors': 0, 'locked_doors': 0, 'items': ['none'], 'enemeys': 0, 'connections': ['none'], 'description':""},
   'room_template': {'name': "", 'doors': 1, 'locked_doors': 0, 'items': ['none'], 'enemeys': 0, 'connections': ['none'], 'description':""}
}

def welcome():
    print("Welcome to the game")
    input("Would you like to play Arcane Adventure?")

def room_handler(current_room):
   print(rooms.keys())
   
   return 'entrance'
counter = 0
while True:
   
   def hi():
      print("this is a function")
   counter += 1
   print(counter)
   if counter > 4:
      hi()
      break

def main():
   player = {'name':"", 'hp': 10, 'items': ['lighter', 'gloves'], 'current_room':'entrance'}
   while True:
      current_room = player.get('current_room')
      player['current_room'] = room_handler(current_room)
      return print("good bye")
   

# Call main
if __name__ == "__main__":
    main()
    
