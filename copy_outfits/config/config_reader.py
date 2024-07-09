#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


import ast
from typing import Dict

from copy_outfits.enums.copy_outfits_age import CopyOutfitsAge
from copy_outfits.enums.default_head import DefaultHead
from lib import re


class ConfigReader:
    def __init__(self):
        self.classes = {
            'CopyOutfitsAge': CopyOutfitsAge,
            # 'CopyOutfitsMannequin': CopyOutfitsMannequin,
            'DefaultHead': DefaultHead,
            # 'OutfitCategory': OutfitCategory,
            # 'OutfitGroupId': OutfitGroupId,
            # 'OutfitGroups': OutfitGroups,
            # 'PhysicFilters': PhysicFilters,
            # 'PieMenuAction': PieMenuAction,
            # 'PieMenuActionId': PieMenuActionId,
            # 'SimDataGroupId': SimDataGroupId,
            # 'VariousFilters': VariousFilters,
        }

    def read_config(self, filename: str) -> Dict:
        config = {}
        with open(filename, "rt", encoding="UTF-8") as fp:
            cfg_string = fp.read()
            # Replace e.g.: '{ CopyOutfitsAge.CHILD: ...' with '{ "CopyOutfitsAge.CHILD": ...'
            # ast can't parse enums but copy strings 1:1
            tmp_cfg_string = re.sub(r"([A-Z][A-Za-z]*\.[A-Z_]*)", r'"\g<1>"', cfg_string)
            config = ast.literal_eval(tmp_cfg_string)
            config = self._parse_dict(config)
        return config

    def _parse_dict(self, d: Dict) -> Dict:
        # Replace e.g.: '{ "CopyOutfitsAge.CHILD": ...' with '{ 4: ...' using the 'CHILD' value of the 'CopyOutfitsAge' enum
        # Right now the classes must be loaded beforehand, this save a lot of code to dynamically locate and load enums.

        for k, v in d.items():
            if isinstance(v, list):
                new_list = []
                for list_item in v:
                    if isinstance(list_item, dict):
                        list_item = self._parse_dict(list_item)
                    new_list.append(list_item)
                d.update({k: new_list})
            elif isinstance(v, dict):
                d.update({k: self._parse_dict(v)})
            elif isinstance(v, str):
                if re.match(r"([A-Z][A-Za-z]*\.[A-Z_]*)", v):
                    class_name, _, value = v.partition('.')
                    if class_name not in self.classes.keys():
                        """ Here we could dynamically locate the enum class and add it to classes with importlib """
                    if class_name in self.classes.keys():
                        value = getattr(self.classes.get(class_name), value).value
                        d.update({k: value})  # Replace e.g. CopyOutfitsAge.CHILD with 4
        return d
