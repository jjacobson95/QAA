#! /usr/bin/bash

/usr/bin/time -v STAR --runThreadN 8 --runMode alignReads \
--outFilterMultimapNmax 3 \
--outSAMunmapped Within KeepPairs \
--alignIntronMax 1000000 --alignMatesGapMax 1000000 \
--readFilesCommand zcat \
--readFilesIn /home/jjacobso/bgmp/bioinformatics/Bi623/Assignments/QAA/24_R1_001_trimmo.fastq.gz /home/jjacobso/bgmp/bioinformatics/Bi623/Assignments/QAA/24_R2_001_trimmo.fastq.gz \
--genomeDir /projects/bgmp/jjacobso/bioinformatics/Bi623/Assignments/QAA/Alignment_stuff/Mus_musculus.GRCm39.dna.ens104.star_2.7.9a \
--outFileNamePrefix Mus_musculus_24_001

