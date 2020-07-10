import shutil

# I use this simple script to rename the tracks in my audiobook playlist

# Find the most general name for the files
# Example: Disc disc_num track_num To Sell Is Human.mp3

# Plan Ahead!!

# Current Name: 01 Disc 05 To Sell Is Human.mp3
# Renamed: Disc 05 01 To Sell Is Human.mp3

# Find the number of files in the folder
num = int(input('Enter the number of files in the folder: '))

# Source Path
# e.g C:\\My Files\\Books\\July 2020\\To Sell Is Human\\Disc %s To Sell Is Human\\01 Disc 05 To Sell Is Human.mp3
# Destination Path
# e.g C:\\My Files\\Books\\July 2020\\To Sell Is Human\\Disc %s To Sell Is Human\\Disc 05 01 To Sell Is Human.mp3'

for i in range(1, num + 1):
    if i >= 10:
        # shutil.move(src, destination)
        shutil.move('C:\\My Files\\Books\\July 2020\\To Sell Is Human\\Disc %s To Sell Is Human\\%s Disc %s To Sell Is Human.mp3' % (disc_no, i, disc_no)
                , 'C:\\My Files\\Books\\July 2020\\To Sell Is Human\\Disc %s To Sell Is Human\\Disc %s %s To Sell Is Human.mp3' % (disc_no, disc_no, i))
    else:
        shutil.move(
            'C:\\My Files\\Books\\July 2020\\To Sell Is Human\\Disc %s To Sell Is Human\\%s Disc %s To Sell Is Human.mp3' % (disc_no, '0' + str(i), disc_no),
            'C:\\My Files\\Books\\July 2020\\To Sell Is Human\\Disc %s To Sell Is Human\\Disc %s %s To Sell Is Human.mp3'% (disc_no, disc_no, '0' + str(i)))