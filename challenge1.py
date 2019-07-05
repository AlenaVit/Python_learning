ipAd = input("Enter your ip: ")
if ipAd[-1] != ".":
    ipAd += "."

segment = 1
segm_len = 0
# character = " "

for character in ipAd:
    if character == ".":
        print("Segment number {} contains {} elements".format(segment, segm_len ))
        segment +=1
        segm_len = 0
    else:
        segm_len +=1

# if character != ".":
#   print("Segment number {} contains {} elements".format(segment, segm_len))