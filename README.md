# R5R Map Editor

A tool to build maps out of props in the Apex Legends mod, R5Reloaded

# Instuctions

1. Install R5R
2. Download this program
3. [Get the prop spawner tool](https://github.com/mostlyfireproof/scripts_r5/tree/ModelSpawner)
4. In the console, type `editor` to enable editing mode
5. Click to place the selected model   
    1. To change the model, type `model [model name]`
6. In the console, hit `copy`
7. Paste the logs in to a text file and save it
8. Run `main.py` and specify the input and output files to use
9. Copy the contents of the output file to the bottom of `vscripts\mp\levels\mp_rr_desertlands_common.nut`
10. Inside the functtion `EntitiesDidLoad()`, paste `SpawnEditorProps()`
11. Launch World's Edge


Join the official Discord server for R5Reloaded: SAjuUWXNdS