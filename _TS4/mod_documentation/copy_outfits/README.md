#  Copy Outfits
`Copy Outfits` allows to copy outfits and more. It is basically the same as [Outfit Tools - Copy Any Outfit v4](https://modthesims.info/d/541770/outfit-tools-copy-any-outfit-v4.html) 
by scumbumbo while the code has been written from scratch and menu interactions have been added to replace the cheat console input.

This mod requires S4CL which can be downloaded from https://github.com/ColonolNutty/Sims4CommunityLibrary/releases/latest

It allows to copy outfits from one sim to the other and also to and from special categories.
Outfits for Toddlers are only available for Toddlers, the same applies to Children.
Outfits for Teen, Young Adult, Adult and Elder are shared for these age groups.

`Copy Outfits` is a hidden debug menu as it is meant to fix issues or to prepare sims but not for normal game play. 

### Copy Outfits
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
* Special[0..1]
* Career[0..2]
* Batuu[0..4]
             
### Menu Transfer
* 'Sim' includes everything (no sliders) which defines a sim. These are the head, teeth, hair, eye colors, and many skin details.
* 'Cloth' pastes the hat, full body or upper and lower outfit, shoes, cummerbund, gloves, socks, tights. The 'Paste' commands from above pastes these items.
* 'Body Paint' pastes all body paint. This includes tattoos, skin overlays, acne and nails.
* 'Hand Accessories' pastes bracelets and rings and other accessories attached to writs or fingers.
* 'Head Accessories' pastes ear rings, glasses and the necklace.
* 'Head Paint' includes lip stick, eye brows, shadow and liner, blush, mascara and face paint.
* 'Head Piercings' includes brow, lip and nose piercings.
* 'occult_scars' includes all occult scars and also the non-occult forearm scar.
* 'Pet' includes the fur body, ears and tail (not tested).
* 'All' pastes everything (see above) to the selected sim. Sliders are not transferred but the sims will look very similar.

* Sliders are not supported. They are not copied so they can not be pasted. Like traits and buffs they have nothing to do with the outfit.
       
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
Not tested. It is possible that they do not support special outfits. Trying to access it may cause an exception.

## Technical Details
There are four groups to store outfits:
* A: Teen, Young Adult, Adult and Elder
* B: Children
* C: Toddler
* D: Unknown (non-sims, could be pets - not tested)

There are five clipboards [0..4] for the outfits. Each sim can have up to five outfits [0..4] for each normal category and 1 to 5 for special categories.


History:
This mod has been inspired by 'Copy Any Outfit'. All code has been written from scratch.

© 2022 https://github.com/Oops19
Have fun extending this mod and/or integrating it within your mod. 
