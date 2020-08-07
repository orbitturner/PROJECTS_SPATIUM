#  === 🌌 WELCOME TO ORBIT CODE 🌌  ===
# *                     
# *	  By :
# *
# *     ██████╗ ██████╗ ██████╗ ██╗████████╗    ████████╗██╗   ██╗██████╗ ███╗   ██╗███████╗██████╗ 
# *    ██╔═══██╗██╔══██╗██╔══██╗██║╚══██╔══╝    ╚══██╔══╝██║   ██║██╔══██╗████╗  ██║██╔════╝██╔══██╗
# *    ██║   ██║██████╔╝██████╔╝██║   ██║          ██║   ██║   ██║██████╔╝██╔██╗ ██║█████╗  ██████╔╝
# *    ██║   ██║██╔══██╗██╔══██╗██║   ██║          ██║   ██║   ██║██╔══██╗██║╚██╗██║██╔══╝  ██╔══██╗
# *    ╚██████╔╝██║  ██║██████╔╝██║   ██║          ██║   ╚██████╔╝██║  ██║██║ ╚████║███████╗██║  ██║
# *     ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝   ╚═╝          ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
# *          
# *  AUTHOR : MOHAMED GUEYE [Orbit Turner] - Email: orbitturner@gmail.com - Country: Senegal

# THIS PROGRAM WILL RENAME ALL THE FILES IN A DIRECTORY USING INCREMENTAL NUMBER
import os

FList = os.listdir(os.getcwd())
FListC = FList[1:]

m = 1
for i in FListC:
    fileExtension = os.path.splitext(i)[1]
    if fileExtension == '.svg':
        os.rename(i,'feature-icon-'+str(m)+fileExtension)
        m = m+1
    else:
        print ('{} IS EXCLUDED'.format(i))