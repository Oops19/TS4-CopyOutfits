#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from ts4lib.utils.singleton import Singleton


class SimStore(object, metaclass=Singleton):
    sims = {}  # {AGE_ID: sim_info.sim_id}
