#!/bin/sh
module load aria2-1.36.0-gcc-12.1.0
aria2c --seed-time=0 -d /scratch/jacobli/reddit-2024-12  /home/jacobli/reddit-data-collector-v2/arcticshift-processing/torrent-files/reddit-2024-12.torrent
aria2c --seed-time=0 -d /scratch/jacobli/reddit-2025-01 /home/jacobli/reddit-data-collector-v2/arcticshift-processing/torrent-files/reddit-2025-01.torrent
aria2c --seed-time=0 -d /scratch/jacobli/reddit-2025-02 /home/jacobli/reddit-data-collector-v2/arcticshift-processing/torrent-files/reddit-2025-02.torrent
aria2c --seed-time=0 -d /scratch/jacobli/reddit-2025-03 /home/jacobli/reddit-data-collector-v2/arcticshift-processing/torrent-files/reddit-2025-03.torrent
aria2c --seed-time=0 -d /scratch/jacobli/reddit-2025-04 /home/jacobli/reddit-data-collector-v2/arcticshift-processing/torrent-files/reddit-2025-04.torrent
aria2c --seed-time=0 -d /scratch/jacobli/reddit-2025-05 /home/jacobli/reddit-data-collector-v2/arcticshift-processing/torrent-files/reddit-2025-05.torrent
aria2c --seed-time=0 -d /scratch/jacobli/reddit-2025-06 /home/jacobli/reddit-data-collector-v2/arcticshift-processing/torrent-files/reddit-2025-06.torrent
aria2c --seed-time=0 -d /scratch/jacobli/reddit-2025-07 /home/jacobli/reddit-data-collector-v2/arcticshift-processing/torrent-files/reddit-2025-07.torrent
aria2c --seed-time=0 -d /scratch/jacobli/reddit-2025-08 /home/jacobli/reddit-data-collector-v2/arcticshift-processing/torrent-files/reddit-2025-08.torrent
aria2c --seed-time=0 -d /scratch/jacobli/reddit-2025-09 /home/jacobli/reddit-data-collector-v2/arcticshift-processing/torrent-files/reddit-2025-09.torrent
aria2c --seed-time=0 -d /scratch/jacobli/reddit-2025-10 /home/jacobli/reddit-data-collector-v2/arcticshift-processing/torrent-files/reddit-2025-10.torrent

