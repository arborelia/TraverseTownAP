from enum import Enum

class ItemNames(str, Enum):
    def __str__(self) -> str:
        return self.value
    
    # Major Items
    melee = "Progressive Melee"
    fire_sword = "Fire Sword"
    fire_mace = "Fire Mace"
    force = "Progressive Force Wand"
    dynamite = "Progressive Dynamite"
    ice = "Progressive Ice Ring"
    chain = "Progressive Chain"
    roll = "Roll"
    loot = "Big Old Pile of Loot"
    fake_efcs = "Impossible Gates Pass"
    shard = "Secret Shard"
    f_key = "Forbidden Keys"

    # Upgrades
    force_upgrade = "Force Wand Upgrade"
    dynamite_upgrade = "Dynamite Upgrade"
    ice_upgrade = "Ice Ring Upgrade"
    chain_upgrade = "Chain Upgrade"

    # Minor Items
    tracker = "Progressive Tracker"
    headband = "Progressive Headband"
    amulet = "Progressive Amulet"
    tome = "Progressive Tome"
    lockpick = "Lockpick"
    crayon = "Crayon"
    scroll_cave = "Cave Scroll"
    scroll_portal = "Portal World Scroll"
    heart_yellow = "Yellow Heart"

    # Keys
    # All locks assume you have all keys or the key ring
    d1_key = "Pillow Fort Key"
    d2_key = "Sand Castle Key"
    d3_key = "Art Gallery Key"
    d4_key = "Trash Cave Key"
    d5_key = "Flooded Basement Key"
    d6_key = "Potassium Mines Keys"
    d7_key = "Boiling Grave Key"
    d8_key = "Grand Library Key"
    s1_key = "Sunken Labyrinth Key"
    s2_key = "Machine Fortress Key"
    s3_key = "Dark Hypostyle Key"
    s4_key = "Tomb of Simulacrum Key"
    # Wizardry Lab has no keys
    dd_key = "Syncope Key"
    dfc_key = "Antigram Key"
    di_key = "Bottomless Tower Key"
    da_key = "Quietus Key"

    # Key Rings
    d1_keyring = "Pillow Fort Key Ring"
    d2_keyring = "Sand Castle Key Ring"
    d3_keyring = "Art Gallery Key Ring"
    d4_keyring = "Trash Cave Key Ring"
    d5_keyring = "Flooded Basement Key Ring"
    d6_keyring = "Potassium Mines Key Ring"
    d7_keyring = "Boiling Grave Key Ring"
    d8_keyring = "Grand Library Key Ring"
    s1_keyring = "Sunken Labyrinth Key Ring"
    s2_keyring = "Machine Fortress Key Ring"
    s3_keyring = "Dark Hypostyle Key Ring"
    s4_keyring = "Tomb of Simulacrum Key Ring"
    dd_keyring = "Syncope Key Ring"
    dfc_keyring = "Antigram Key Ring"
    di_keyring = "Bottomless Tower Key Ring"
    da_keyring = "Quietus Key Ring"

    # Cards
    card_fishbun = "Card 1: Fishbun"
    card_bee = "Card 2: Stupid Bee"
    card_safety = "Card 3: Safety Jenny"
    card_shellbun = "Card 4: Shellbun"
    card_spikebun = "Card 5: Spikebun"
    card_gate = "Card 6: Feral Gate"
    card_snake = "Card 7: Candy Snake"
    card_mimic = "Card 8: Hermit Legs"
    card_ogler = "Card 9: Ogler"
    card_hyperdusa = "Card 10: Hyperdusa"
    card_easel = "Card 11: Evil Easel"
    card_warnip = "Card 12: Warnip"
    card_octacle = "Card 13: Octacle"
    card_rotnip = "Card 14: Rotnip"
    card_bees = "Card 15: Bee Swarm"
    card_volcano = "Card 16: Volcano"
    card_shark = "Card 17: Jenny Shark"
    card_swimmy = "Card 18: Swimmy Roger"
    card_bunboy = "Card 19: Bunboy"
    card_spectre = "Card 20: Spectre"
    card_brutus = "Card 21: Return of Brutus"
    card_jelly = "Card 22: Jelly"
    card_skullnip = "Card 23: Skullnip"
    card_slayer = "Card 24: Slayer Jenny"
    card_titan = "Card 25: Titan"
    card_chilly = "Card 26: Chilly Roger"
    card_flower = "Card 27: Jenny Flower"
    card_hexrot = "Card 28: Hexrot"
    card_mole = "Card 29: Jenny Mole"
    card_bun = "Card 30: Jenny Bun"
    card_cat = "Card 31: Jenny Cat" # Mjau
    card_mermaid = "Card 32: Jenny Mermaid"
    card_berry = "Card 33: Jenny Berry (Vacation)"
    card_mapman = "Card 34: Mapman"
    card_cyber = "Card 35: Cyberjenny"
    card_biadlo = "Card 36: Le Biadlo"
    card_lenny = "Card 37: Lenny"
    card_passel = "Card 38: Passel Carver"
    card_tippsie = "Card 39: Tippsie"
    card_ittle = "Card 40: Ittle Dew"
    card_fly = "Card 41: Napping Fly"

    # Outfits
    outfit_jenny = "Jenny Dew Outfit"
    outfit_swimsuit = "Swimsuit Outfit"
    outfit_tippsie = "Tippsie Outfit"
    outfit_dude = "Little Dude Outfit"
    outfit_tiger = "Tiger Jenny Outfit"
    outfit_id = "Ittle Dew 1 Outfit"
    outfit_delinquint = "Delinquint Outfit"
    outfit_berry = "Jenny Berry Outfit"
    outfit_apa = "Apathetic Frog Outfit"
    outfit_that_guy = "That Guy Outfit"

    # Tricks, abilities, and options
    can_open_chests = "Can Open Chests"
    can_break_weak_objects = "Can Break Weak Objects" # every weapon except roll, can be used to open caves
    can_break_stong_objects = "Can Break Strong Objects" # melee, dynamite, or ice, since force can't break everything
    can_kill_basic_enemies = "Can Kill Basic Enemies"
    can_phase_itemless = "Can Phase Itemless"
    can_phase_itemless_difficult = "Can Phase Itemless (Difficult)"
    can_phase_ice_itemless = "Can Phase to Existing Ice Blocks"
    can_phase_ice_itemless_difficult = "Can Phase to Existing Ice Blocks (Difficult)"
    can_phase_ice = "Can Phase to Ice Blocks"
    can_phase_ice_difficult = "Can Phase to Ice Blocks (Difficult)"
    can_phase_dynamite = "Can Dynamite-Ice Clip"
    can_phase_dynamite_difficult = "Can Dynamite-Ice Clip (Difficult)"
    can_phase_enemy = "Can Do Enemy Phases"
    can_phase_enemy_difficult = "Can Do Enemy Phases (Difficult)"

    # Events
    has_opened_d8 = "Has Opened Grand Library"
    has_opened_s1 = "Has Opened Sunken Labyrinth"
    has_opened_s2 = "Has Opened Machine Fortress"
    has_opened_s3 = "Has Opened Dark Hypostyle"
    has_opened_s4 = "Has Opened Tomb of Simulacrum"
    has_opened_dw = "Has Opened Dreamworld"
    has_opened_dd = "Has Opened Syncope"
    has_opened_df = "Has Opened Wizardry Lab"
    has_opened_dfc = "Has Opened Antigram"
    has_opened_di = "Has Opened Bottomless Tower"
    has_opened_da = "Has Opened Quietus"

    # Options
    option_phasing = "Option - Can Phase Itemless"
    option_phasing_ice = "Option - Can Phase to Ice Blocks"
    option_phasing_dynamite = "Option - Can Dynamite-Ice Clip"
    option_phasing_enemy = "Option - Can Do Enemy Phases"
    option_phasing_difficult = "Option - Can Do Difficult Phases"