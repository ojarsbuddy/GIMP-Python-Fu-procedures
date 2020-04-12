#!/usr/bin/env python

# Tutorial available at: https://www.youtube.com/watch?v=nmb-0KcgXzI
# Feedback welcome: jacksonbates@hotmail.com

from gimpfu import *

def height_330(image, drawable):
    # Image
    # Scale Image
    pdb.gimp_message("Set image height to 330px and export!\n"+image.name)

    new_height = 330
    new_width = (new_height*image.width)/image.height
    
    pdb.gimp_image_scale(image, new_width, new_height)
    
    filename, extension =(pdb.gimp_image_get_filename(image)).split('.',1)

    pdb.file_png_save_defaults(image, drawable, filename+".png", filename+".png")
    pdb.gimp_message("Winter Is Coming.\n"+filename)

    quality=0.9
    smoothing=0
    optimize=0
    progressive=0
    comment="Husker Du!"
    subsmp=2
    baseline=0
    restart=0
    dct=0
    pdb.file_jpeg_save(image, drawable, filename+".jpg", filename+".jpg", quality, smoothing, optimize, progressive, comment, subsmp, baseline, restart, dct)

    pdb.gimp_message("Husker Du!\n"+filename)

    preset=0
    lossless=0
    quality=100
    alpha_quality=100
    animation=0
    anim_loop=0
    minimize_size=0
    kf_distance=0
    exif=0
    iptc=0
    xmp=0
    delay=0
    force_delay=0
    
    pdb.file_webp_save(image, drawable, filename+".webp", filename+".webp", preset, lossless, quality, alpha_quality, animation, anim_loop, minimize_size, kf_distance, exif, iptc, xmp, delay, force_delay)

    pdb.gimp_message("Not all those who wander are lost.\n"+filename)

register(
    "python-fu-height-330",
    "Reduce image and export files",
    "Reduce images to 330px high, preserve form factor and save as jpg, png and webp files.",
    "Ojars", "John Bortins", "2020",
    "Reduce height to 330px and export",
    "", # type of image it works on (*, RGB, RGB*, RGBA, GRAY etc...)
    [
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None)
    ],
    [],
    height_330, menu="<Image>/Ojars")  # second item is menu location

main()
