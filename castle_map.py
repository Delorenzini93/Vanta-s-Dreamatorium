import Status

room_maps = {
    "main_hall": """
╔═══════════════════════════════════╗
║           VANTA'S DREAMATORIUM    ║
║              [ MAP ]              ║
╠═══════════════════════════════════╣
║                                   ║
║   [LIBRARY]      [PIANO ROOM]     ║
║       │               │           ║
║       └──────┬────────┘           ║
║         [MAIN HALL] ◄ YOU         ║
║       ┌──────┴────────┘           ║
║       │               │           ║
║   [GARDEN]        [BALCONY]       ║
║                                   ║
║         ▼ SECOND HALL             ║
╚═══════════════════════════════════╝
""",
    "second_hall": """
╔═══════════════════════════════════╗
║        VANTA'S DREAMATORIUM       ║
║           [ SECOND HALL ]         ║
╠═══════════════════════════════════╣
║                                   ║
║  ROOMS:                           ║
║  ► Flooded Library                ║
║  ► Echoing Corridor               ║
║  ► Dining Room                    ║
║  ► Outdoor Garden                 ║
║     └ Shed                        ║
║  ► Windy Corridor                 ║
║     ├ → Third Hall                ║
║     └ → Mountainside (night only) ║
║  ► Dungeons Corridor ▼            ║
║  ► [???]                          ║
║                                   ║
║  ▲ Main Hall                      ║
╚═══════════════════════════════════╝
""",
        "third_hall": """
╔═══════════════════════════════════╗
║        VANTA'S DREAMATORIUM       ║
║           [ THIRD HALL ]          ║
╠═══════════════════════════════════╣
║                                   ║
║  ROOMS:                           ║
║  ► Archane Room                   ║
║  ► Deep Dungeons                  ║
║  ▲ Corridor with Many Windows     ║ 
║  ▼ Windy Corridor                 ║
╚═══════════════════════════════════╝
""",
    "dungeons": """
╔═══════════════════════════════════╗
║        VANTA'S DREAMATORIUM       ║
║             [ DUNGEONS ]          ║
╠═══════════════════════════════════╣
║                                   ║
║  ROOMS:                           ║
║  ► Noisy Room (Zagnar)            ║
║  ► Secret Room                    ║
║  ► Trial Room                     ║
║  ► Upside Down Room               ║
║     └ → Hall of Trophies          ║
║  ► Dungeons East Wing             ║
║     └ → Hall of Trophies          ║
║                                   ║
║  ▼ Deep Dungeons                  ║
║  ▲ Dungeons Corridor              ║
╚═══════════════════════════════════╝
""",
    "deep_dungeons": """
╔═══════════════════════════════════╗
║        VANTA'S DREAMATORIUM       ║
║           [ DEEP DUNGEONS ]       ║
╠═══════════════════════════════════╣
║                                   ║
║  ROOMS:                           ║
║  ► Jail                           ║
║  ► Silence Room                   ║
║  ► Dungeons Library               ║
║  ► Basements                      ║
║                                   ║
║  ► Third Hall (door - night only) ║
║                                   ║
║  ▲ Dungeons                       ║
╚═══════════════════════════════════╝
""",
    "dungeons_corridor": """
╔═══════════════════════════════════╗
║        VANTA'S DREAMATORIUM       ║
║        [ DUNGEONS CORRIDOR ]      ║
╠═══════════════════════════════════╣
║                                   ║
║  ROOMS:                           ║
║  ► Goblin's Warehouse             ║
║  ► Hall of Mirrors                ║
║  ► Old Boticary                   ║
║  ► Room of Cauldrons              ║
║     └ Tunnel → Room o Cauldrons 2F║
║                                   ║
║  ▼ Dungeons                       ║
║  ▲ Second Hall                    ║
╚═══════════════════════════════════╝
""",
    "mountainside": """
╔═══════════════════════════════════╗
║        VANTA'S DREAMATORIUM       ║
║        [ MOUNTAINSIDE ]           ║
╠═══════════════════════════════════╣
║                                   ║
║  ROOMS:                           ║
║  ► Mountainside                   ║
║  ► Gorge                          ║
║  ► Sanctuary                      ║
║                                   ║
║  ▼ Third Hall                     ║
╚═══════════════════════════════════╝
""",
    "west_hall": """
╔═══════════════════════════════════╗
║        VANTA'S DREAMATORIUM       ║
║           [ WEST HALL ]           ║
╠═══════════════════════════════════╣
║                                   ║
║  ROOMS:                           ║
║  ► World Heritage Room            ║
║  ► Weather Forecast Room          ║
║  ► Factory Sabotage Room          ║
║  ► Botanical Classroom            ║
║     └ → Patio                     ║
║                                   ║
║  ▼ Corridor with Many Windows     ║
║  ▲ West Hall Piano Nobile         ║
╚═══════════════════════════════════╝
""",
}

def show_map():
    current = Status.current_room
    if current in room_maps and room_maps[current]:
        print(room_maps[current])
    else:
        print("No map available for this area.")