#!/usr/bin/bash

/usr/bin/time -v STAR --runThreadN 8 --runMode genomeGenerate \
--genomeDir /projects/bgmp/jjacobso/bioinformatics/Bi623/Assignments/QAA/Alignment_stuff/Mus_musculus.GRCm39.dna.ens104.star_2.7.9a \
--genomeFastaFiles /projects/bgmp/jjacobso/bioinformatics/Bi623/Assignments/QAA/Alignment_stuff/Mus_musculus.GRCm39.dna.primary_assembly.fa \
--sjdbGTFfile /projects/bgmp/jjacobso/bioinformatics/Bi623/Assignments/QAA/Alignment_stuff/Mus_musculus.GRCm39.104.gtf
