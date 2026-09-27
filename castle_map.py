import Status

room_maps = {
    "main_hall": "",
    "second_hall": "",
    "third_hall": "",
    "dungeons": "",
    "deep_dungeons": "",
    "dungeons_corridor": "",
    "mountainside": "",
}

def show_map():
    current = Status.current_room
    if current in room_maps and room_maps[current]:
        print(room_maps[current])
    else:
        print("No map available for this area.")