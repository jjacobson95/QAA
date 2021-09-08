#! /usr/bin/python3.6

alignment_tracker = {}
mapped = 0
unmapped = 0
with open ("/projects/bgmp/jjacobso/bioinformatics/Bi623/Assignments/QAA/Alignment_stuff/Mus_musculus_24_001Aligned.out.sam", "r") as fh:
        for line in fh:
            if line.startswith("@"):
                do = "nothing"
            else:
                line = line.split("\t")
                flag = (int(line[1]))
                if((flag & 4) != 4) and ((flag & 256) != 256):
                        mapped +=1
                else:
                    if ((flag & 256) != 256):
                        unmapped +=1
                    
print ("Mapped read count:", mapped)
print("Unmapped read count:", unmapped)
