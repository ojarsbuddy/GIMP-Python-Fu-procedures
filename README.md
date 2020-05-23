# GIMP-Python-Fu-procedures
Here is a place to collect Python-Fu scripts, plug-ins, procedures (terminology appears to vary).

For Windows GIMP plug-ins live in ```C:\Users\ojars\AppData\Roaming\GIMP\2.10\plug-ins```.

For Linux GIMP plug-ins live in ```/home/ojars/.config/GIMP/2.10/plug-ins``` or ```/usr/lib/gimp/2.0/plug-ins```. File permissions must be set to allow execution, for example, ```chmod 755 reduce_export.py``` or ```sudo chmod 755 reduce-export.py```.

Remember to restart GIMP, if changes are made to the register function. GIMP will see other changes to the code.

## fixing missing dependencies
https://discourse.ubuntu.com/t/gimp-woes-in-20-04/15828/8

## reduce_export
This procedure takes an 850px by 1100px image, reduces same to a standard height while maintaining aspect ratio, and exports the reduced image in PNG, JPEG and WEBP formats.
