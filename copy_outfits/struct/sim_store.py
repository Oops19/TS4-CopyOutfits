#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2022 https://github.com/Oops19
#


class O19COSimStore:
    sims = {}  # {AGE_ID: sim_info.sim_id}


'''
SimInfoBaseWrapper.copy_base_attributes(sim_info_a, sim_info_b) copies 'age', 'gender', 'extended_species'
SimInfoBaseWrapper.copy_genetic_data(sim_info_a, sim_info_b) copies 'genetic_data'
SimInfoBaseWrapper.copy_physical_attributes(sim_info_a, sim_info_b) copies 'genetic_data' (as above),
    'facial_attributes' (sliders), voice_pitch, voice_actor, voice_effect, skin_tone, skin_tone_val_shift, flags, pelt_layers, base_trait_ids

Paste > Age & Gender
Paste > Genetics
Paste > Physics & Genetics

'''