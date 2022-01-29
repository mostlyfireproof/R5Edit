# R5Edit

A tool to build maps out of props in the Apex Legends mod, R5Reloaded

# Instuctions

1. Install R5R
2. Download this program
3. [Get the prop spawner tool](https://github.com/mostlyfireproof/scripts_r5/tree/SalEditor)
4. In the dev menu, click on the editor menu and start editing
5. Place objects
6. Copy the logs when you want to save \([Example](https://cdn.upload.systems/uploads/3rsUNfag.png)\)
7. Paste the logs in to a text file and save it
8. Run `main.py` and specify the input and output files to use
   1. For example, `python3 main.py ../examples/sample1.txt ../examples/out1.nut` will parse the included sample1 file
   2. If `python3 ...` doesn't work, you may need to install [Python](https://www.python.org/downloads/), or run it as `python ...`
9. Copy the contents of the output file to the bottom of either `vscripts/mp/levels/mp_rr_canyonlands_common.nut` or `vscripts/mp/levels/mp_rr_desertlands_common.nut`
10. Replace the function `SpawnEditorProps()` with the contents of the output file
11. Launch King's Canyon or World's Edge, depending on where you pasted the output

[Tutorial video that covers most of this](https://youtu.be/yPEYbcOVi58)

Join the official Discord server for R5Reloaded: SAjuUWXNdS
