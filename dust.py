import sys, getopt
from SimpleCV import *

def showHelp(error=None):
    print "usage:", sys.argv[0],"-s -m <number> <file> [<file> ...]"
    print "\t-h: Show this help menu"
    print "\t-s: Show Particle Images"
    print "\t-m: Maximum Particles"
    sys.exit(error)
    
def analyseDust(file, showImage = False, maxParticles = 2000):
    
    img = Image(file)
    
    # X, Y, Width, Height
    cropped_img = img.crop(img.width/2, img.height/2, img.width/2, img.height/2, centered=True)
    
    dustParticles = cropped_img.findCorners(maxnum = maxParticles)
    
    if showImage:
        disp = Display()
        
        while disp.isNotDone():
            if disp.mouseLeft: break
            
            cropped_img.save(disp)
            
            if (dustParticles is not None):
                dustParticles.draw()
                
    return len(dustParticles)

def main(argv):
    showImage = False
    maxParticles = 2000

    try:
        opts, args = getopt.getopt(argv,"hsm:")
    except getopt.GetoptError:
        showHelp(2)
    
    if len(args) == 0:
        showHelp(3)
    
    for opt, arg in opts:
        if opt == '-h': showHelp()
        elif opt == "-s":showImage = True
        elif opt == "-m": maxParticles = int(arg)

    for file in args:
        numberParticles = analyseDust(file, showImage, maxParticles)
        print file, ":", numberParticles, "particles"

if __name__ == "__main__":
    main(sys.argv[1:])