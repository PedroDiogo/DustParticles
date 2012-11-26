# Dust Particle Counter #

After watching a video from Matthias Wandel (http://www.youtube.com/watch?v=OmehjfmoxPQ) where he made different shots of the dust particles on some rooms of his house and on his workshop before and after sawing some boards, I decided to create this little Python script to count how many dust particles are present on those images.

This script is far from perfect but it can give a ballpark estimate and you should be able to compare two (or more) different pictures from those results.

All images are credit of Matthias.

## Examples ##

Here are some screenshots as example:
  
    $ python dust.py -s images/box_bedroom-b.jpg 
  
    images/box_bedroom-b.jpg : 144 particles
    
![](http://pedrodiogo.github.com/DustParticles/bedroom.png)
  
    $ python dust.py -s images/box_tablesawed-b.jpg 
  
    images/box_tablesawed-b.jpg : 492 particles
    
![](http://pedrodiogo.github.com/DustParticles/workshop.png)