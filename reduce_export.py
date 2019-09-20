#!/usr/bin/env python

# Tutorial available at: https://www.youtube.com/watch?v=nmb-0KcgXzI
# Feedback welcome: jacksonbates@hotmail.com

from gimpfu import *

def reduce_export(image, drawable):
    # Image
    # Scale Image
    pdb.gimp_message("Reduce image size and export!\n"+image.name)

    scale_numerator = 3
    scale_denominator = 10
    new_width = (image.width*scale_numerator)/scale_denominator
    new_height = (image.height*scale_numerator)/scale_denominator
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
    "python-fu-reduce-export",
    "Reduce image and export files",
    "Reduce 850px by 1100px images to 255px by 330px and save as jpg, png and webp files.",
    "Ojars", "John Bortins", "2019",
    "Reduce and export",
    "", # type of image it works on (*, RGB, RGB*, RGBA, GRAY etc...)
    [
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None)
    ],
    [],
    reduce_export, menu="<Image>/Ojars")  # second item is menu location

main()
