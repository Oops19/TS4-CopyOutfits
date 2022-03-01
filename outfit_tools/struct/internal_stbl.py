class InternalSTBL:
    list = {
        0x2598FABD: '',
        0x453A8BAE: "<font color='#199c2c'>{0.String}</font>",  # green
        0xFC089996: '{0.String}',
        0x92CCA68C: '{0.String}',
        0x6A251415: '{0.String}',
        0x847A4379: '{0.String}…',
        0xD8DE1CF9: ' • {0.String}',
        0xEE3A2E1C: '{0.String}\n{1.String}',
        0xB5F493B0: '{0.String}\n{1.String}',
        0x416E9F1B: '{0.String}\n\n{1.String}',
        0x5D808001: '{0.String} {1.String}',
        0xD22D3E78: '{0.String}: {1.String}',
        0x40AFB1B6: '{0.String}, {1.String}',
        0x4286250B: '{0.String} and {1.String}',
        0x1D2033C0: '{0.String}, and {1.String}',

        0xCA922667: '{0.String} ({1.Number})',

        0xA795DBC4: '{0.Money}',
        0xAC2CA174: 'for {0.Money}',
        0x0EF51AAC: '{0.String} ({1.Money})',
        0xABCCCD41: '{0.String}: {1.Money}',

        0xFA65EDB0: '{0.SimFirstName}',
        0x0C13E237: '{1.SimLastName}',
        0x58FCF93F: '{0.SimName}',
        0xF4670BCA: '{0.SimName}',

        0xF6A4E3C3: "Test Text: {0.Number}",  # TESTING_TEST_TEXT_WITH_NUMBER_TOKEN
        0x50A4AFDF: "Some Text For Testing",  # TESTING_SOME_TEXT_FOR_TESTING
        0xFF21D2D2: "Test Text: {0.SimFirstName} {0.SimLastName}",  # TESTING_TEST_TEXT_WITH_SIM_FIRST_AND_LAST_NAME
        0xB1746497: "Test Text: {0.String}",  # TESTING_TEST_TEXT_WITH_STRING_TOKEN
    }
    TS4_NOP = 0x2598FABD  # ''
    TS4_OUTFIT = 0x9423B843  # 'Outfit'
    TS4_SIM_NAME = 0x58FCF93F  # '{0.SimName}'
    TS4_SIM_NAME_ALT = 0xF4670BCA  # '{0.SimName}'
    TS4_STRING = 0xFC089996 # '{0.String}',

    O19_SELECT___OUTFIT = 0xA032F21C  # 'Select {0.String} Outfit'
    O19_SOURCE = 0xB7041F4E  # 'Source'
    O19_TARGET = 0x4ACA4866  # 'Target'

    O19_PASTE_CATEGORY = 0x2EB683EB  # 'Pasted {2.Number} {S2:outfit}{P2:outfits} to {0.String}.'
    O19_COPY_CATEGORY = 0xB3E6B2BF  # 'Copied {2.Number} {0.String} {S2:outfit}{P2:outfits} to clipboard.'
    O19_PASTE_TO_1_TO_4 = 0x049199FA  # 'Pasted outfit to {0.String}[{0.Number}].'
    O19_COPY_TO_1_TO_4 = 0x3A327E16  # 'Copied outfit {0.String}[{0.Number}] to clipboard [{1.Number}].'
    O19_PASTE_FAILED = 0x15DAFB7C  # 'No outfit found in clipboard [{1.Number}].'
    O19_CLEAR = 0x3EE477A6  # 'Removed {P2:all outfits}{S2:outfit} from clipboard {S2:[{1.Number}]}.'
    O19_OUTFIT_NAME_BATUU = 0xD9721CEA  # 'Batuu'
    O19_OUTFIT_NAME_SPECIAL = 0xABE6F428  # 'Special'
    O19_OUTFIT_NAME_SITUATION = 0xE8FC312D  # 'Situation'
    O19_OUTFIT_NAME_BATHING = 0x70ABA200  # 'Bathing'
    O19_OUTFIT_NAME_COLD_WEATHER = 0x51DD52EC  # 'Cold Weather'
    O19_OUTFIT_NAME_HOT_WEATHER = 0x22B898F5  # 'Hot Weather'
