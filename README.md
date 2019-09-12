# Nuclosynthesis-Simulations

## Prerequisites
- User must have Python 3 installed
- User must have pip installed to install the following packages:
    - numpy
    - matplotlib


## Choreographed 
To create a choreographed video, run the following on the command line:
`python3 choreographed_animation.py choreographyfile.csv new_movie_file.mp4`
This will run the utility and save the choregraphy to the mp4 file. 

## Simulated Nucleosynthesis 
For this you will run a similar command: `python3 nuclear_synthesis_animation.py reaction*.csv new_movie_file.mp4`
The reactions can be input as wildcards such as `reaction*.csv` or by explictly stating them, such as `python3 nuclear_synthesis_animation.py reaction1a.csv reaction2a.csv  reaction3a.csv new_movie_file.mp4`