How to use this:

1) Download "journey_mode_compiler.zip" and unzip the files into a folder.
2) Get the "TellMe" mod by masady (https://www.curseforge.com/minecraft/mc-mods/tellme) and install into the modpack containing the items you want to add.
3) Create or load a world with cheats enabled.
4) Type in chat the following command:
/tellme dump to-file simple items-registry-name-only
5) Click on the link to take you to the file location where the dump was stored and open the txt file.
6) Copy the registry names for all of the items you want to add into another txt file called "input.txt" in the same folder with the journey_mode_compiler.py file. Ideally, exclude any items with "journey_mode:" or "minecraft:" in front unless you want to overwrite their default values.
7) Open "compiler_config.txt" and change the number to change the default amount of items needed to research each item and unlock duplication (this value is normally 64).
8) Run "journey_mode_compiler.py", which will create "changes.json"; move this file to the config folder for your modpack.
9) Make sure to open "journeyMode-server.toml" and change "other_files" to "true" so the mod will read the changes.
10) If you want to make any additional changes, make edits to "changes.json" manually to remove specific items or change the amount needed to research each item.
