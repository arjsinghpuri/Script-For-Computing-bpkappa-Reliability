
This text file has the instructions to use the bpkappa python script that will do the reliability for the coding two RAs in seconds.
For the first time you might need to install python in your system if it already doesn't have it and this might take 10-15 mins.
But after you have python in your system it'll be super quick

INSATLLING PYTHON (ONLY FOR THE FIRST TIME USING THIS PROGRAM)

(if using Mac) https://www.dataquest.io/blog/installing-python-on-mac/ (just follow the steps for installing till python YOU DO NOT NEED VISUAL STUDIO or anything else)
(if using Windows) https://www.digitalocean.com/community/tutorials/install-python-windows-10 (follow all steps here)

FORMATTING FOR THE EXCEL -
1. Name the excel "Excel for Reliability.xlsx"
2. The excel should have three sheets - the first - a codebook, the second - the coding by RA1, the third - coding by RA2
3. The sheets with the coding should have an ID as the first column and the data as the second column. The coding responses should begin third column onwards.
4. Make sure the the name and number of columns are identical for second and third sheets (the coding by the RAs)
5. Make sure that the values in the cells are consistent. Either Y/N or 1/0 will work. But make sure cells are not blank, don't have extra spaces after the characters, etc.

USING THE PROGRAM - 
1. Download the folder with this program
2. Move the excel that is formatted as described above into the same folder 

(if using a Mac)
3. Open Terminal
4. Copy paste this command to go to the folder that you have downloaded - cd Downloads/bpkappa  (this works only if you haven't moved the folder from the downloads folder)
5. Copy paste this command to execute the program - python3 bpkappa.py OR python bpkappa.py
6. A new excel should appear in the folder with the bpkappa scores
7. Make sure to remove the the resutling excel and the Excel for reliability form this folder before using it again to avoid confusion.

(if using windows)
3. Open the folder in the Windows Explorer
4. Type in "cmd" on top (the place with the path above or that are in the same place where you would type in a url in a web browser)
5. Copy paste this command to execute the program - python3 bpkappa.py OR python bpkappa.py
6. A new excel should appear in the folder with the bpkappa scores
7. Make sure to remove the the resutling excel and the Excel for reliability form this folder before using it again to avoid confusion.
