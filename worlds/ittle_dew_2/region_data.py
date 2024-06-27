from typing import Dict, List, NamedTuple, Optional, Union
from enum import IntEnum
from .names_regions import RegionNames as rname
from .names_locations import LocationNames as lname
from .names_items import ItemNames as iname


class ID2Type(IntEnum):
    location = 1
    region = 2


class ID2Data(NamedTuple):
    type: ID2Type  # Either Location or Region
    rules: List[List[str]] = [[]]  # List of rules for access requirements
    # for rules to be satisfied, you need to have at least one set of the rules items
    grant_event: Optional[str] = None  # grants the specified event item when the location is collected


# First Union is the source region
# Second Union is the destination region or location
# The ID2Data is a list of requirements
traversal_requirements: Dict[rname, Dict[Union[lname, rname], ID2Data]] = {
    # Currently vanilla start will be the only available starting location
    # For now MVP is going to move starting logical location to be Sweetwater Coast
    rname.menu: {
        # rname.fluffy_fields: 
        # ID2Data(ID2Type.region),
        rname.sweetwater_coast:
            ID2Data(ID2Type.region),
    },
    # Overworld regions
    rname.fluffy_fields: {
        rname.pepperpain_prairie:
            ID2Data(ID2Type.region),
        rname.sweetwater_coast:
            ID2Data(ID2Type.region),
        rname.fancy_ruins:
            ID2Data(ID2Type.region),
        rname.star_woods:
            ID2Data(ID2Type.region),
        rname.slippery_slope:
            ID2Data(ID2Type.region),
        rname.dreamworld:
            ID2Data(ID2Type.region, [[]]),  # TODO add dream world event requirements
        rname.ffc_a:
            # Only melee can hit the musical pillars
            ID2Data(ID2Type.region, [[iname.melee.value]]),
        rname.ffc_b:
            ID2Data(ID2Type.region),
        rname.ffc_c:
            ID2Data(ID2Type.region),
        rname.ffc_d:
            ID2Data(ID2Type.region),
        rname.ffc_e:
            ID2Data(ID2Type.region, [[iname.can_break_weak_objects.value]]),
        rname.ffc_f:
            ID2Data(ID2Type.region),
        rname.ffc_g:
            ID2Data(ID2Type.region, [[iname.can_break_weak_objects.value]]),
        rname.ffc_h:
            ID2Data(ID2Type.region),
        rname.ffc_i:
            ID2Data(ID2Type.region),
        rname.ffc_j:
            ID2Data(ID2Type.region),
        rname.ffc_k:
            ID2Data(ID2Type.region, [[iname.can_break_weak_objects.value]]),
        rname.ffc_s:
            ID2Data(ID2Type.region),
    },
    rname.sweetwater_coast: {
        rname.fluffy_fields:
            ID2Data(ID2Type.region),
        rname.star_woods:
            ID2Data(ID2Type.region),
        rname.slippery_slope:
            ID2Data(ID2Type.region),
        rname.scc_a:
            ID2Data(ID2Type.region),
        rname.scc_b:
            ID2Data(ID2Type.region, [[iname.can_break_strong_objects.value]]),
        rname.scc_c:
            ID2Data(ID2Type.region),
        rname.scc_f:
        # transitional cave, gives access to d and e
            ID2Data(ID2Type.region, [[iname.can_break_weak_objects.value],
                                     [iname.can_phase_dynamite.value],
                                     [iname.can_phase_ice.value, iname.roll.value],
                                     [iname.can_phase_enemy_difficult.value, iname.roll.value]]),
        rname.scc_g:
            ID2Data(ID2Type.region, [[iname.can_break_strong_objects.value]]),
        rname.scc_h:
            ID2Data(ID2Type.region),
        rname.scc_i:
            ID2Data(ID2Type.region),
        rname.scc_j:
            ID2Data(ID2Type.region, [[iname.roll.value]]),
        rname.scc_k:
            ID2Data(ID2Type.region),
        rname.scc_l:
            ID2Data(ID2Type.region, [[iname.can_break_weak_objects.value]]),
        rname.scc_m:
            ID2Data(ID2Type.region),
        rname.scc_n:
            ID2Data(ID2Type.region),
        rname.scc_o:
            ID2Data(ID2Type.region, [[iname.can_break_weak_objects.value]]),
        rname.scc_p:
            ID2Data(ID2Type.region),
        rname.scc_q:
            ID2Data(ID2Type.region),
        rname.d2_g:
            ID2Data(ID2Type.region)
    },

    # Caves
    # Fluffy Fields Caves
    rname.ffc_a: {
        rname.autumn_climb:
            ID2Data(ID2Type.region, [[iname.can_kill_basic_enemies.value],
                                     [iname.can_phase_itemless.value]]),
    },
    rname.ffc_b: {
        lname.ffc_goldbun_combat:
            ID2Data(ID2Type.location, [[iname.can_kill_basic_enemies.value]]),
    },
    rname.ffc_c: {
        lname.ffc_portal_room:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
    },
    rname.ffc_d: {
        # clockwise tree house turnip
    },
    rname.ffc_e: {
        lname.ffc_timed_bridge:
            ID2Data(ID2Type.location, [[iname.can_break_weak_objects.value]]),
    },
    rname.ffc_f: {
        lname.ffc_hermit_hint:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
    },
    rname.ffc_g: {
        lname.ffc_laser:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
    },
    rname.ffc_h: {
        # transitional cave from one side of Fluffy to the other
        # ...SPRUCE THAT IS...
    },
    rname.ffc_i: {
        # lazy turnip cave
    },
    rname.ffc_j: {
        lname.ffc_number_blocks:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
    },
    rname.ffc_k: {
        lname.ffc_ice_blockade:
            ID2Data(ID2Type.location, [[iname.melee.value],
                                       # itemless ice phasing isn't possible due to some weird properties of the
                                       # natural ice blocks, still unknown why
                                       [iname.can_phase_ice],
                                       [iname.can_phase_dynamite]]),
    },
    rname.ffc_s: {
        # Status Effect Tutorial house
    },
    # Sweetwater Caves
    rname.scc_a: {
        # rock performance
    },
    rname.scc_b: {
        lname.scc_white_gates_combat:
            ID2Data(ID2Type.location, [[iname.can_kill_basic_enemies.value]])
    },
    rname.scc_c: {
        # pink friendly ogler
    },
    rname.scc_d: {
        # transitional cave from e to main coast
    },
    rname.scc_e: {
        rname.the_vault_d:
            ID2Data(ID2Type.region)
    },
    rname.scc_f: {
        rname.scc_d:
            ID2Data(ID2Type.region),
        rname.scc_e:
            ID2Data(ID2Type.region, [[iname.can_break_weak_objects.value]]),
    },
    rname.scc_g: {
        lname.scc_feral_gates_combat:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
    },
    rname.scc_h: {
        lname.scc_three_teleporters:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
    },
    rname.scc_i: {
        lname.scc_four_candy_snakes_combat:
            ID2Data(ID2Type.location, [[iname.can_kill_basic_enemies.value]])
    },
    rname.scc_j: {
        lname.scc_portal_spikes_chest:
            ID2Data(ID2Type.location, [[iname.can_break_weak_objects.value]])
    },
    rname.scc_k: {
        lname.scc_hint_hermit:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
    },
    rname.scc_l: {
        lname.scc_fake_chest_cave:
            ID2Data(ID2Type.location, [[iname.melee.value],
                                       [iname.force.value],
                                       [iname.ice.value]])
    },
    rname.scc_m: {
        lname.scc_wooden_balls_spike_floor:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
    },
    rname.scc_n: {
        lname.scc_kung_fu_jenny:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
    },
    rname.scc_o: {
        rname.painful_plain:
            ID2Data(ID2Type.region, [[iname.can_break_weak_objects.value]])
    },
    rname.scc_p: {
        # Transition cave to Fancy
    },
    rname.scc_q: {
        # Changing Tent
    },

    # Dungeons
    # Sand Castle
    rname.d2_a: {
        lname.d2_boss_reward:
            ID2Data(ID2Type.location, [[iname.can_kill_basic_enemies.value, iname.roll.value]]),
        rname.d2_b:
            ID2Data(ID2Type.region, [[iname.can_kill_basic_enemies.value, iname.roll.value]])
    },
    rname.d2_b: {
        rname.d2_a:
            ID2Data(ID2Type.region),
        rname.d2_f:
            ID2Data(ID2Type.region)
    },
    rname.d2_c: {
        rname.d2_d:
            ID2Data(ID2Type.region, [[iname.can_break_weak_objects.value]]),
        rname.d2_h:
            ID2Data(ID2Type.region, [[iname.can_break_weak_objects.value]])
    },
    rname.d2_d: {
        lname.d2_spikebun_dunes:
            ID2Data(ID2Type.location, [[iname.can_break_weak_objects.value]]),
        rname.d2_c:
            ID2Data(ID2Type.region, [[iname.can_break_weak_objects.value]]),
        rname.d2_h:
            ID2Data(ID2Type.region)
    },
    rname.d2_e: {
        rname.d2_f:
            ID2Data(ID2Type.region, [[iname.can_kill_basic_enemies.value]]),
        rname.d2_i:
            ID2Data(ID2Type.region, [[iname.can_use_d2_keys.value]])
    },
    rname.d2_f: {
        rname.d2_b:
            ID2Data(ID2Type.region, [[iname.force.value],
                                     [iname.can_phase_ice.value, iname.roll.value],
                                     [iname.can_phase_dynamite.value, iname.roll.value]]),
        rname.d2_g:
            ID2Data(ID2Type.region)
    },
    rname.d2_g: {
        lname.d2_crayon:
            ID2Data(ID2Type.location, [[iname.force.value],
                                       [iname.melee.value, iname.chain.value],
                                       [iname.dynamite.value],
                                       [iname.fire_mace.value],
                                       [iname.can_phase_ice.value],
                                       [iname.can_open_chests.value, iname.can_phase_enemy.value]]),
        rname.d2_h:
            ID2Data(ID2Type.region),
        rname.d2_i:
            ID2Data(ID2Type.region),
        rname.d2_f:
            ID2Data(ID2Type.region, [[iname.fire_sword.value]]),
        rname.sweetwater_coast:
            ID2Data(ID2Type.region)
    },
    rname.d2_h: {
        rname.d2_c:
            ID2Data(ID2Type.region, [[iname.can_break_weak_objects.value]]),
        rname.d2_d:
            ID2Data(ID2Type.region),
        rname.d2_g:
            ID2Data(ID2Type.region),
        rname.d2_j:
            ID2Data(ID2Type.region, [[iname.dynamite.value],
                                     [iname.can_phase_ice.value],
                                     [iname.can_phase_enemy.value]]),
        rname.d2_k:
            ID2Data(ID2Type.region, [[iname.can_use_d2_keys.value]])
    },
    rname.d2_i: {
        lname.d2_orbiting_balls:
            ID2Data(ID2Type.location, [[iname.melee.value, iname.roll.value]]),
        rname.d2_e:
            ID2Data(ID2Type.region, [[iname.can_use_d2_keys.value, iname.melee.value, iname.roll.value],
                                     [iname.can_phase_itemless.value, iname.roll.value],
                                     [iname.can_phase_itemless_difficult.value],
                                     [iname.can_phase_dynamite]]),
        rname.d2_g:
            ID2Data(ID2Type.region)
    },
    rname.d2_j: {
        lname.d2_treasure:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]], iname.victory),
        rname.d2_h:
            ID2Data(ID2Type.region, [[iname.force.value],
                                     [iname.can_phase_ice.value, iname.roll.value],
                                     [iname.can_phase_dynamite.value]])
    },
    rname.d2_k: {
        rname.d2_h:
            ID2Data(ID2Type.region, [[iname.can_use_d2_keys.value]]),
        rname.d2_j:
            ID2Data(ID2Type.region, [[iname.can_kill_basic_enemies.value]])
    },

    # Portal Worlds
    rname.autumn_climb: {
        lname.autumn_climb:
            ID2Data(ID2Type.region, [[iname.can_open_chests.value]]),
        rname.ffc_a:
            ID2Data(ID2Type.region),
    }

}
