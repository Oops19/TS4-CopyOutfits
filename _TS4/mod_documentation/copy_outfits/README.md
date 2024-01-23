# Copy Outfits
`Copy Outfits` allows to copy outfits and more. It is basically the same as [Outfit Tools - Copy Any Outfit v4](https://modthesims.info/d/541770/outfit-tools-copy-any-outfit-v4.html) 
by scumbumbo while the code has been written from scratch and menu interactions have been added to replace the cheat console input.
With the current update the sims appearance can be cloned completely.

It allows to copy outfits from one sim to the other and also to and from special categories.
Outfits for Toddlers are only available for Toddlers, the same applies to Children.
Outfits for Teen, Young Adult, Adult and Elder are shared for these age groups.

`Copy Outfits` is a 'hidden' debug menu as it is meant to fix issues or to prepare sims but not for normal game play.
Enable cheats with `testingcheats true` to activate it and Shift-click on sims to use it.

## Menu 'Copy Outfits'
* The most simple option is to use 'Copy' to copy the current outfit to the internal clipboard #0 and 'Paste' to paste from #0 to the current outfit.
    * Appearance modifiers are not taken into account. If the sim wears no shoes due to an appearance modifier (Snowy Escape DLC) the shoes will still be copied - and of course vice versa. If the sim wears boots due to an appearance modifier the boots will not be copied.
* The 'Copy/Paste ...' > '(X-)Picker ...' menus allow to select a specific outfit. It will be copied to/from clipboard 0. See `Menu Special-Picker` for details.
* 'Transfer ...' allows to copy other things from clipboard 0 to the current outfit. See `Menu Transfer` for details.

The other menu options may be used rarely:
* The 'Copy/Paste ...' > '(X-)Category ...' menus allow to copy/paste all outfits, up to five.
* 'Copy to ...' allows to copy the current outfit to one of the other clipboards [1..4].
* 'Paste from ...' allows to paste the outfit from another clipboards  [1..4] to the current outfit.
* 'Paste to ...' allows to paste the outfit from clipboard 0 to the current outfit category but to a specific index [0..4].

### Menu Special-Picker (X-Picker)
It allows to select individual special outfits. These include:
* Bathing[0] (Nude)
* Situation[0]
* Special[0..1] (0=Special 1=Nude with Towel)
* Career[0]
* Batuu[0..4]
             
### Menu Transfer
* 'Sim' includes everything (no sliders) which defines a sim. These are the head, teeth, hair, eye colors, and many skin details.
* 'Cloth' pastes the hat, full body or upper and lower outfit, shoes, cummerbund, gloves, socks, tights. The 'Paste' commands from above pastes these items.
* 'Body Paint' pastes all body paint. This includes tattoos, skin overlays, acne and nails.
* 'Hand Accessories' pastes bracelets and rings and other accessories attached to writs or fingers.
* 'Head Accessories' pastes ear rings, glasses and the necklace.
* 'Head Paint' includes lipstick, eyebrows, shadow and liner, blush, mascara and face paint.
* 'Head Piercings' includes brow, lip and nose piercings.
* 'occult_scars' includes all occult scars and also the non-occult forearm scar.
* 'Pet' includes the fur body, ears and tail (not tested).
* 'Complete Outfit' (previously All) pastes everything (see above) to the selected sim. Sliders are not transferred but the sims will look very similar.

### Menu X-Transfer
This is the sub menu which does not really has something to do with 'Copy Outfits'.
* 'Age & Gender' includes age, gender, '¿extended_species?', walk styles, body frame, clothing preferences and whether the sim can give/receive pregnancy. Existing pregnancies will neither be canceled or transferred.
* 'Genetics' is only '¿genetics?', whatever it is.
* 'Physics & Genetics' includes '?genetics?', physic, sliders, voice, skin and if available also pelt and/or '¿base_traits?', whatever this is.
* 'Traits' includes all traits.
* 'All' includes 'Complete Outfit' and everything from above.
* ~~'Sliders'~~ - not implemented as a standalone interaction, use 'All' or 'Physics & Genetics'
* ~~'Walkstyles'~~ - not implemented as a standalone interaction, use 'All' or 'Age & Gender'
* ~~'Relationships'~~ - not implemented
* ~~'Only Face Sliders'~~ - not implemented
* ~~'Only Body Sliders'~~ - not implemented
* 
### Menu More
* 'Print Clipboard' prints the copied outfits including the source sim. Outfit IDs are logged to the log file where you can copy them and will not flood the notification area.
* 'Clear All' removes all outfits from the cache.
* 'Clear ...' allows to remove a specific outfit from the cache. 

## Random sims
### Mermaids (Tail)
Special outfit categories aren't supported.
### Aliens (Disguise)
Special outfit categories aren't supported.
### Pets (Cats & Dogs)
Do not copy outfits from cats to dogs and vice versa. Technically it works but it looks odd.
### Witch, Vampire
These should work as every other sim
### Robots, Plant Sim, Ghost, Skeleton
Not tested. It is possible that they do not support special outfits and may throw an exception.

## Technical Details
There are five groups to store outfits:
* A: Teen, Young Adult, Adult and Elder
* B: Children
* C: Toddler
* D: Infants
* E: Unknown (non-sims, could be pets - not tested)

There are five clipboards [0..4] for the outfits. Each sim can have up to five outfits [0..4] for each normal category and 1 to 5 for special categories.

### History:
This mod has been inspired by 'Copy Any Outfit'. All code has been written from scratch.

### Update 2023-06
1.0.2 Conversion / update of links
1.0.1 Fix LE caused by non-functional code
1.0.0 Supports infants.



# Addendum

## Game compatibility
This mod has been tested with `The Sims 4` 1.101.290 (2023-09), S4CL 2.8 (2023-08), TS4Lib 0.1.8 (2023-09).
It is expected to be compatible with many upcoming releases of TS4, S4CL and TS4Lib.

## Dependencies
* [The Sims 4](https://www.ea.com/games/the-sims/the-sims-4)
* [TS4-Library](https://github.com/Oops19/TS4-Library/releases/latest)
* [S4CL](https://github.com/ColonolNutty/Sims4CommunityLibrary/releases/latest)

If not installed download and install TS4 and these mods.
All are available for free.

## Installation
* Locate the localized `The Sims 4` folder which contains the `Mods` folder.
* Extract the ZIP file into this `The Sims 4` folder.
* It will create the directories/files `Mods/_o19_/$mod_name.ts4script`, `Mods/_o19_/$mod_name.package`, `mod_data/$mod_name/*` and/or `mod_documentation/$mod_name/*`
* `mod_logs/$mod_name.txt` will be created as soon as data is logged.

### Manual Installation
If you don't want to extract the ZIP file into `The Sims 4` folder you might want to read this. 
* The files in `ZIP-File/mod_data` are usually required and should be extracted to `The Sims 4/mod_data`.
* The files in `ZIP-File/mod_documentation` are for you to read it. They are not needed to use this mod.
* The `Mods/_o19_/*.ts4script` files can be stored in a random folder within `Mods` or directly in `Mods`. I highly recommend to store it in `_o19_` so you know who created it.

## Usage Tracking / Privacy
This mod does not send any data to tracking servers. The code is open source, not obfuscated, and can be reviewed.

Some log entries in the log file ('mod_logs' folder) may contain the local username, especially if files are not found (WARN, ERROR).

## External Links
[Sources](https://v/Oops19/)
[Support](https://discord.gg/d8X9aQ3jbm)
[Donations](https://www.patreon.com/o19)

## Copyright and License
* © 2023 [Oops19](https://github.com/Oops19)
* License for '.package' files: [Electronic Arts TOS for UGC](https://tos.ea.com/legalapp/WEBTERMS/US/en/PC/)  
* License for other media unless specified differently: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) unless the Electronic Arts TOS for UGC overrides it.
This allows you to use this mod and re-use the code even if you don't own The Sims 4.
Have fun extending this mod and/or integrating it with your mods.

Oops19 / o19 is not endorsed by or affiliated with Electronic Arts or its licensors.
Game content and materials copyright Electronic Arts Inc. and its licensors. 
Trademarks are the property of their respective owners.

### TOS
* Please don't put it behind a paywall.
* Please don't create mods which break with every TS4 update.
* For simple tuning modifications use [Patch-XML](https://github.com/Oops19/TS4-PatchXML) 
* or [LiveXML](https://github.com/Oops19/TS4-LiveXML).
* To check the XML structure of custom tunings use [VanillaLogs](https://github.com/Oops19/TS4-VanillaLogs).
