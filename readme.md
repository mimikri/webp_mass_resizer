# mass webp resizer
it can resize webp images from a given folder<br><br>
max width -- can be set, if images come in big formats, you can somehow normalize them like this<br>
size in % -- you can shrink the pictures to a given % of the original size<br>
compression -- you can set the quality of the images<br>
path -- you can append something on the imagefile names and/or put the in an other folder<br>
fixed width -- can set fixed width in pixels, height will be calculated from image proportion, same for height<br>
fixed width and height -- can set both in pixels, will result in fixed image proportion but streched picture<br>
<br>

# the gui<br>
<img src="https://raw.githubusercontent.com/mimikri/webp_mass_resizer/main/gui.webp"><br>
<br>

# how to run<br>
run the install.sh script to install a local python version and the pillow libery, wich is used for the image functions<br>
if already installed:<br>
    run the start.sh <br>
    or in terminal venv/bin/python3 makepics.py<br>
<br>

# intension<br>
had to make different image versions for image sets of a website , wich have to choose the right image for the right resolution/densitiy<br>