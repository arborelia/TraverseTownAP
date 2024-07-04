from enum import Enum


class LocationNames(str, Enum):
    def __str__(self) -> str:
        return self.value

    # names should be the same as in locations.py
    # Fluffy Fields Caves
    ffc_goldbun_combat = "Fluffy Fields Caves - Goldbun Combat Chest"
    ffc_portal_room = "Fluffy Fields Caves - Portal Room Chest"
    ffc_timed_bridge = "Fluffy Fields Caves - Timed Bridge Chest"
    ffc_hermit_hint = "Fluffy Fields Caves - Hermit Hint Chest"
    ffc_laser = "Fluffy Fields Caves - Laser Chest"
    ffc_number_blocks = "Fluffy Fields Caves - Number Blocks Chest"
    ffc_ice_blockade = "Fluffy Fields Caves - Ice Blockade Chest"
    ffc_double_spikebun_combat = "Fluffy Fields Caves - Double Spikebun Combat Chest"
    ffc_potion_bar = "Fluffy Fields Caves - Potion Bar Chest"
    ffc_six_buns_combat = "Fluffy Fields Caves - Six Buns Combat Chest"
    ffc_artist_backroom = "Fluffy Fields Caves - Artist Backroom Chest"
    ffc_jenny_berry_house = "Fluffy Fields Caves - Jenny Berry House Outfit"

    # Sweetwater Coast Caves
    scc_white_gates_combat = "Sweetwater Coast Caves - White Gates Combat Chest"
    scc_feral_gates_combat = "Sweetwater Coast Caves - Feral Gates Combat Chest"
    scc_three_teleporters = "Sweetwater Coast Caves - Three Teleporters Chest"
    scc_four_candy_snakes_combat = "Sweetwater Coast Caves - Four Candy Snakes Combat Chest"
    scc_portal_spikes_chest = "Sweetwater Coast Caves - Portal Spikes Chest"
    scc_hint_hermit = "Sweetwater Coast Caves - Hint Hermit Chest"
    scc_fake_chest_cave = "Sweetwater Coast Caves - Fake Chest Cave Chest"
    scc_wooden_balls_spike_floor = "Sweetwater Coast Caves - Wooden Balls Spike Floor Chest"
    scc_kung_fu_jenny = "Sweetwater Coast Caves - Kung Fu Jenny Chest"

    # Fancy Ruins Caves
    frc_two_torches = "Fancy Ruins Caves - Two Torches Chest"
    frc_numbered_torches = "Fancy Ruins Caves - Numbered Torches Chest"
    frc_two_crystals = "Fancy Ruins Caves - Two Crystals Chest"
    frc_big_ogler_combat = "Fancy Ruins Caves - Big Ogler Combat Chest"
    frc_hint_turnip = "Fancy Ruins Caves - Hint Turnip Chest"
    frc_rhythm_pillars = "Fancy Ruins Caves - Rhythm Pillars Chest"
    frc_teleporter_puzzle = "Fancy Ruins Caves - Teleporter Puzzle Chest"
    frc_four_oglers_combat = "Fancy Ruins Caves - Four Oglers Combat Chest"
    frc_spike_path = "Fancy Ruins Caves - Spike Path Chest"
    frc_hiding_hermit = "Fancy Ruins Caves - Hiding Hermit Chest"
    frc_ice_and_torch = "Fancy Ruins Caves - Ice and Torch Chest"

    # Star Woods Caves
    swc_turnip_combat = "Star Woods - Turnip Combat Chest"
    swc_barrel_blast = "Star Woods - Barrel Blast Chest"
    swc_four_crystals = "Star Woods - Four Crystals Chest"
    swc_sleeping_jenny = "Star Woods - Sleeping Safety Jenny Chest"
    swc_rotating_spikes = "Star Woods - Rotating Spikes Chest"
    swc_number_tiles = "Star Woods - Number Tiles Chest"
    swc_whirlwind = "Star Woods - Whirlwind Chest"
    swc_magic_crystal = "Star Woods - Magic Crystal Chest"
    swc_artist_turnip = "Star Woods - Artist Turnip Chest"
    swc_hint_bee = "Star Woods - Hint Bee Chest"
    swc_extinguish_flames = "Star Woods - Extinguish Flames Chest"

    # Slippery Slope Caves
    ssc_volcanic_path = "Slippery Slope - Volcanic Path Chest"
    ssc_ice_and_barrels = "Slippery Slope - Ice and Barrels Chest"
    ssc_eight_crystals = "Slippery Slope - Eight Crystals Chest"
    ssc_forgetful_jennies = "Slippery Slope - Forgetful Jennies Chest"
    ssc_push_the_crystals = "Slippery Slope - Push the Crystals Chest"
    ssc_exhausted_turnip = "Slippery Slope - Exhausted Turnip Chest"
    ssc_bee_nest_combat = "Slippery Slope - Bee Nest Combat Chest"
    ssc_pushable_fan = "Slippery Slope - Pushable Fan Chest"
    ssc_moving_crystals = "Slippery Slope - Moving Crystals Chest"
    ssc_shark_house = "Slippery Slope - Shark House"

    # Pepperpain Caves
    ppc_cowbun_combat = "Pepperpain Caves - Cowbun Combat Chest"
    ppc_brutus_combat = "Pepperpain Caves - Brutus Combat Chest"
    ppc_torch_disappearing_path = "Pepperpain Caves - Torch Disappearing Path Chest"
    ppc_spiky_hint_bee = "Pepperpain Caves - Spiky Hint Bee Chest"
    ppc_cannon_path = "Pepperpain Caves - Cannon Path Chest"
    ppc_volcano_trail = "Pepperpain Caves - Volcano Trail Chest"
    ppc_barrel_hint_bee = "Pepperpain Caves - Barrel Hint Bee Chest"
    ppc_haunted_guns = "Pepperpain Caves - Haunted Guns Chest"
    ppc_buzzsaw_path = "Pepperpain Caves - Buzzsaw Path Chest"
    ppc_number_tiles = "Pepperpain Caves - Number Tiles Chest"
    ppc_pacifist_brute = "Pepperpain Caves - Pacifist Brute Chest"

    # Frozen Court Caves
    fcc_bushfire = "Frozen Court Caves - Bushfire Chest"
    fcc_cannon_spinner = "Frozen Court Caves - Cannon Spinner Chest"
    fcc_mimicbuns = "Frozen Court Caves - Mimicbuns Combat Chest"
    fcc_teleporter_maze = "Frozen Court Caves - Teleporter Maze Chest"
    fcc_chilly_roger_combat = "Frozen Court Caves - Chilly Roger Combat Chest"
    fcc_rickety_bridge = "Frozen Court Caves - Rickety Bridge Chest"
    fcc_titans_combat = "Frozen Court Caves - Titans Combat Chest"
    fcc_crystal_path = "Frozen Court Caves - Crystal Path Chest"
    fcc_teleporter_grate = "Frozen Court Caves - Teleporter Grate Chest"
    fcc_hint_hermit = "Frozen Court Caves - Hint Hermit Chest"

    # Lonely Road
    lrc_timed_platforms = "Lonely Road Caves - Timed Platforms Chest"
    lrc_timed_number_tiles = "Lonely Road Caves - Timed Number Tiles Chest"
    lrc_volcano = "Lonely Road Caves - Volcano Chest"
    lrc_lava_fans = "Lonely Road Caves - Lava Fans Chest"
    lrc_force_turrets = "Lonely Road Caves - Force Turrets Chest"
    lrc_hint_shark = "Lonely Road Caves - Hint Shark Chest"
    lrc_teleporter_cube = "Lonely Road Caves - Teleporter Cube Chest"
    lrc_dark_maze = "Lonely Road Caves - Dark Maze Chest"
    lrc_block_factory = "Lonely Road Caves - Block Factory"

    # Pillow Fort
    d1_treasure = "Pillow Fort - Treasure Chest"
    d1_shellbun_nest = "Pillow Fort - Shellbun Nest Key"
    d1_crayon = "Pillow Fort - Crayon Chest"
    d1_safety_jenny_gate = "Pillow Fort - Safety Jenny Gate Key"
    d1_boss_reward = "Pillow Fort - Boss Reward Chest"

    # Sand Castle
    d2_crayon = "Sand Castle - Crayon Chest"
    d2_orbiting_balls = "Sand Castle - Orbiting Balls Key"
    d2_spikebun_dunes = "Sand Castle - Spikebun Dunes Key"
    d2_treasure = "Sand Castle - Treasure Chest"
    d2_boss_reward = "Sand Castle - Boss Reward Chest"

    # Art Exhibit
    d3_entry_combat = "Art Exhibit - Entry Combat Key"
    d3_evil_easels = "Art Exhibit - Evil Easels Key"
    d3_treasure = "Art Exhibit - Treasure Chest"
    d3_crayon = "Art Exhibit - Crayon Chest"
    d3_spike_floor = "Art Exhibit - Spike Floor Key"
    d3_business_casual_man = "Art Exhibit - Business Casual Man Key"
    d3_boss_reward = "Art Exhibit - Boss Reward Chest"

    # Trash Cave
    d4_crayon = "Trash Cave - Crayon Chest"
    d4_ice_barricade = "Trash Cave - Ice Barricade Key"
    d4_rotnip_combat = "Trash Cave - Rotnip Combat Key"
    d4_treasure = "Trash Cave - Treasure Chest"
    d4_mimic_combat = "Trash Cave - Mimic Combat Key"
    d4_block_maze = "Trash Cave - Block Maze Key"
    d4_boss_reward = "Trash Cave - Boss Reward Chest"

    # Flooded Basement
    d5_portal_cube = "Flooded Basement - Portal Cube Key"
    d5_crossway_combat = "Flooded Basement - Crossway Combat Key"
    d5_land_sharks = "Flooded Basement - Land Sharks Key"
    d5_treasure = "Flooded Basement - Treasure Chest"
    d5_crayon = "Flooded Basement - Crayon Chest"
    d5_keeled_fishbun = "Flooded Basement - Keeled Fishbun Key"
    d5_number_blocks = "Flooded Basement - Number Blocks Key"
    d5_boss_reward = "Flooded Basement - Boss Reward Chest"

    # Potassium Mine
    d6_hub_room = "Potassium Mine - Hub Room Key"
    d6_south_conveyor = "Potassium Mine - South conveyor Key"
    d6_crayon = "Potassium Mine - Crayon Chest"
    d6_west_minecart_track = "Potassium Mine - West Minecart Track Key"
    d6_number_tiles = "Potassium Mine - Number Tiles Key"
    d6_treasure = "Potassium Mine - Treasure Chest"
    d6_ice_tutorial = "Potassium Mine - Ice Tutorial Key"
    d6_boss_reward = "Potassium Mine - Boss Reward Chest"

    # Boiling Grave
    d7_skullnips_combat = "Boiling Grave - Skullnips Combat Key"
    d7_titans_combat = "Boiling Grave - Titans Combat Key"
    d7_treasure = "Boiling Grave - Treasure Chest"
    d7_roll_pillars = "Boiling Grave - Roll Pillars Key"
    d7_royal_tomb = "Boiling Grave - Royal Tomb Key"
    d7_crayon = "Boiling Grave - Crayon Chest"
    d7_chilly_roger_combat = "Boiling Grave - Chilly Roger Combat Key"
    d7_boss_reward = "Boiling Grave - Boss Reward Chest"

    # Grand Library
    d8_treasure = "Grand Library - Treasure Chest"
    d8_crayon = "Grand Library - Crayon Chest"
    d8_patient = "Grand Library - Patient Key"
    d8_hidden = "Grand Library - Hidden Key"
    d8_fighter_combat = "Grand Library - Fighter's Combat Key"
    d8_storied = "Grand Library - Storied Key"
    d8_delayed = "Grand Library - Delayed Key"
    d8_carrot_lobotomy = "Grand Library - Carrot Lobotomy Key"
    d8_crystal_button = "Grand Library - Crystals and Buttons Key"
    d8_hexrot_combat = "Grand Library - Hexrot Combat Key"
    d8_boss_key = "Grand Library - Boss Key Chest"
    d8_boss_reward = "Grand Library - Boss Reward Chest"
    d8_boss_reward_extra = "Grand Library - Extra Boss Reward Chest"

    # Sunken Labyrinth
    s1_gold_titan_combat = "Sunken Labyrinth - Gold Titan Combat Key"
    s1_death_ogler_combat = "Sunken Labyrinth - Death Ogler Combat Key"
    s1_treasure = "Sunken Labyrinth - Treasure Chest"
    s1_mimic_combat = "Sunken Labyrinth - Mimic Combat Key"
    s1_crayon = "Sunken Labyrinth - Crayon Chest"
    s1_boss_reward = "Sunken Labyrinth - Boss Reward Chest"

    # Machine Fortress
    s2_hyperdusa_conveyor = "Machine Fortress - Hyperdusa conveyor Key"
    s2_bee = "Machine Fortress - Bee Chest"
    s2_crayon = "Machine Fortress - Crayon Chest"
    s2_number_tiles = "Machine Fortress - Number Tiles Key"
    s2_cannon_conveyors = "Machine Fortress - Cannon conveyors Key"
    s2_light_bridge = "Machine Fortress - Light Bridge Key"
    s2_steel_skullnip_combat = "Machine Fortress - Steel Skullnip Combat Key"
    s2_treasure = "Machine Fortress - Treasure Chest"
    s2_boss_reward = "Machine Fortress - Boss Reward Chest"

    # Dark Hypostyle
    s3_initial_key = "Dark Hypostyle - Initial Key"
    s3_crayon = "Dark Hypostyle - Crayon Chest"
    s3_blue_path = "Dark Hypostyle - Blue Path Key"
    s3_yellow_path_monochrome = "Dark Hypostyle - Yellow Path Monochrome Key"
    s3_treasure = "Dark Hypostyle - Treasure Chest"
    s3_yellow_path = "Dark Hypostyle - Yellow Path Key"
    s3_red_path_cannon = "Dark Hypostyle - Red Path Cannon Key"
    s3_red_path = "Dark Hypostyle - Red Path Key"
    s3_boss_reward = "Dark Hypostyle - Boss Reward Chest"

    # Tomb of Simulacrum
    s4_mercury_jello_number_tiles = "Tomb of Simulacrum - Mercury Jello Number Tiles Key"
    s4_self_locked_tile = "Tomb of Simulacrum - Self Locked Tile Key"
    s4_eight_tile = "Tomb of Simulacrum - Eight Tile Key"
    s4_roundabout_crystal = "Tomb of Simulacrum - Roundabout Crystal Key"
    s4_corner_torch = "Tomb of Simulacrum - Corner Torch Key"
    s4_crayon = "Tomb of Simulacrum - Crayon Chest"
    s4_death_ogler_combat = "Tomb of Simulacrum - Death Ogler Combat Key"
    s4_efcs_door = "Tomb of Simulacrum - EFCS Door Key"
    s4_large_chasm = "Tomb of Simulacrum - Large Chasm Key"
    s4_spiked_orbitals = "Tomb of Simulacrum - Spiked Orbitals"
    s4_molten_conveyors = "Tomb of Simulacrum - Molten Conveyors Key"
    s4_treasure = "Tomb of Simulacrum - Treasure Chest"
    s4_boss_reward = "Tomb of Simulacrum - Boss Reward Chest"

    # Wizardry Lab
    df_entrance = "Wizardry Lab - Entrance Card"
    df_west_energy_source = "Wizardry Lab - West Energy Source Card"
    df_cannon = "Wizardry Lab - Cannon Card"
    df_east_mirrors = "Wizardry Lab - East Mirrors Card"
    df_east_energy_source = "Wizardry Lab - East Energy Source Card"
    df_reward_a = "Wizardry Lab - Reward Card A"
    df_reward_b = "Wizardry Lab - Reward Card B"
    df_reward_c = "Wizardry Lab - Reward Card C"

    # Syncope
    dd_shifting_blue_red = "Syncope - Shifting Blue Red Key"
    dd_shifting_blue_blue = "Syncope - Shifting Blue Blue Key"
    dd_switch_chamber = "Syncope - Switch Chamber Card"
    dd_foyer = "Syncope - Foyer Card"
    dd_garden = "Syncope - Garden Key"
    dd_piano = "Syncope - Piano Card"
    dd_knights_hint = "Syncope - Knights Hint Card"
    dd_shadow_walker = "Syncope - Shadow Walker Key"
    dd_force_turret_maze = "Syncope - Force Turret Maze"
    dd_reward_a = "Syncope - Reward Card A"
    dd_reward_b = "Syncope - Reward Card B"
    dd_reward_c = "Syncope - Reward Card C"

    # Bottomless Tower
    di_1f_card = "Bottomless Tower - First Floor Card"
    di_1f_key = "Bottomless Tower - First Floor Key"
    di_2f_card = "Bottomless Tower - Second Floor Card"
    di_2f_key = "Bottomless Tower - Second Floor Key"
    di_blue_portal = "Bottomless Tower - Blue Portal Card"
    di_3f_spike_gates = "Bottomless Tower - Third Floor Spike Gates Card"
    di_3f_key = "Bottomless Tower - Third Floor Key"
    di_3f_ice_square = "Bottomless Tower - Third Floor Ice Square Card"
    di_4f_key = "Bottomless Tower - Fourth Floor Key"
    di_reward_a = "Bottomless Tower - Reward Card A"
    di_reward_b = "Bottomless Tower - Reward Card B"
    di_reward_c = "Bottomless Tower - Reward Card C"

    # Antigram
    dfc_free = "Antigram - Free Key"
    dfc_west_light_bridge = "Antigram - West Light Bridge Card"
    dfc_east_light_bridge = "Antigram - East Light Bridge Card"
    dfc_west_ice = "Antigram - West Ice Card"
    dfc_east_ice = "Antigram - East Ice Card"
    dfc_west_bombs = "Antigram - West Bombs Key"
    dfc_east_bombs = "Antigram - East Bombs Key"
    dfc_end_east_bridge = "Antigram - End East Bridge Card"
    dfc_end_west_bridge = "Antigram - End West Bridge Key"
    dfc_reward_a = "Antigram - Reward Card A"
    dfc_reward_b = "Antigram - Reward Card B"
    dfc_reward_c = "Antigram - Reward Card C"

    # Quietus
    da_center = "Quietus - Center Card"
    da_alternating_floors = "Quietus - Alternating Floors Key"
    da_tangled_wires = "Quietus - Tangled Wires Key"
    da_push_the_coil = "Quietus - Push the Coil Key"
    da_giant_mess = "Quietus - Giant Mess Key"
    da_northwest_vault = "Quietus - Northwest Vault Card"
    da_northeast_vault = "Quietus - Northeast Vault Card"
    da_southwest_vault = "Quietus - Southwest Vault Card"
    da_southeast_vault = "Quietus - Southeast Vault Card"
    da_reward_a = "Quietus - Reward Card A"
    da_reward_b = "Quietus - Reward Card B"
    da_reward_c = "Quietus - Reward Card C"

    # Portal Worlds
    autumn_climb = "Autumn Climb - Chest"
    the_vault = "The Vault - Chest"
    painful_plain = "Painful Plain - Chest"
    farthest_shore = "Farthest Shore - Chest"
    scrap_yard = "Scrap Yard - Chest"
    brutal_oasis = "Brutal Oasis - Chest"
    former_colossus = "Former Colossus - Chest"
    sand_crucible = "Sand Crucible - Chest"
    ocean_castle = "Ocean Castle - Chest"
    promenade_path = "Promenade Path - Chest"
    maze_of_steel = "Maze of Steel - Chest"
    wall_of_text = "Wall of Text - Chest"
    lost_city = "Lost City of Avlopp - Chest"
    northern_end = "Northern End - Chest"
    moon_garden = "Moon Garden - Chest"

    # Miscellaneous Locations
    ludo_city = "Ludo City - Chest"
    promised_remedy = "Promised Remedy - That Guy Outfit"
    bad_dream = "Bad Dream - Card"

    # Event Locations
    event_all_d1_keys = "Received Pillow Fort Keys"
    event_all_d2_keys = "Received Sand Castle Keys"
    event_all_d3_keys = "Received Art Exhibit Keys"
    event_all_d4_keys = "Received Trash Cave Keys"
    event_all_d5_keys = "Received Flooded Basement Keys"
    event_all_d6_keys = "Received Potassium Mine Keys"
    event_all_d7_keys = "Received Boiling Grave Keys"
    event_all_d8_keys = "Received Grand Library Keys"
    # event_all_s1_keys = "Received Sunken Labyrinth Keys"
    # event_all_s2_keys = "Received Machine Fortress Keys"
    # event_all_s3_keys = "Received Dark Hypostyle Keys"
    # event_all_s4_keys = "Received Tomb of Simulacrum Keys"
    # event_all_dd_keys = "Received Syncope Keys"
    # event_all_dfc_keys = "Received Antigram Keys"
    # event_all_di_keys = "Received Bottomless Tower Keys"
    # event_all_da_keys = "Received Quietus Keys"
    event_fire_sword = "Received Fire Sword"
    event_fire_mace = "Received Fire Mace"
    event_force_jump = "Received Force Jumping"
    event_d8 = "Grand Library Accessible"
    event_s1 = "Sunken Labyrinth Accessible"
    event_s2 = "Machine Fortress Accessible"
    event_s3 = "Dark Hypostyle Accessible"
    event_s4 = "Tomb of Simulacrum Accessible"
    event_dw = "Dreamworld Accessible"
    event_dreamworld_2 = "Has two Dreamworld Dungeons Done"
    event_dreamworld_3 = "Has three Dreamworld Dungeons Done"
    event_dreamworld_4 = "Has four Dreamworld Dungeons Done"
    event_chest_opener = "Received Chest Opening"
    event_phase_itemless = "Received Itemless Phase Requirements"
    event_phase_itemless_difficult = "Received Difficult Itemless Phase Requirements"
    event_phase_ice_itemless = "Received Ice Itemless Phase Requirements"
    event_phase_ice_itemless_difficult = "Received Difficult Ice Itemless Phase Requirements"
    event_phase_ice = "Received Ice Ring Phase Requirements"
    event_phase_ice_difficult = "Received Difficult Ice Ring Phase Requirements"
    event_phase_dynamite = "Received Dynamite Ice Clip Requirements"
    event_phase_dynamite_difficult = "Received Difficult Dynamite Ice Clip Requirements"
    event_phase_enemy = "Received Enemy Phase Requirements"
    event_phase_enemy_difficult = "Received Difficult Enemy Phase Requirements"

    # events for reaching parts of dungeons
    d5_o_block = "Flooded Basement Crossway Access"
    d8_k_left_door = "Grand Library K Left Door"
    d8_k_right_door = "Grand Library K Right Door"
    switch_vault_left = "The Vault West Switch"
    switch_vault_right = "The Vault East Switch"
    block_scrap_yard_left = "Scrap Yard West Block"
    block_scrap_yard_right = "Scrap Yard East Block"

    victory_location = "VICTORY"
