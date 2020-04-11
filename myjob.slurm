#!/bin/bash

#SBATCH --job-name=comp480-hw3
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=16000m
#SBATCH --time=04:00:00
#SBATCH --mail-user=ys59@rice.edu # TODO: Input your net id
#SBATCH --mail-type=ALL
#SBATCH --export=ALL
#SBATCH --reservation=classroom
#SBATCH --partition=interactive
#SBATCH --exclusive
 
echo "My job ran on:"
pwd 

echo SLURM_NODELIST=$SLURM_NODELIST
echo USER=$USER

export HW3_FOLDER=$HOME/plagiarism-detector # TODO: Update this path to point to your hw 3 folder

if [[ ! -d $HW3_FOLDER ]]; then
    echo "The designated HW 3 folder ($HW3_FOLDER) does not seem to exist"
    exit 1
fi

cd $HW3_FOLDER

module load python
python detector.py