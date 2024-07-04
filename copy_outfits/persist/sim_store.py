#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from ts4lib.utils.singleton import Singleton


class SimStore(object, metaclass=Singleton):
    # Store the last source sim f(age)
    # It will be used for cloning
    sims = {}  # {AGE_ID: sim_info.sim_id}
