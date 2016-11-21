hOCR Shrink
===========

Why?
----

I use tesseract to OCR my scans and hocr2pdf to convert my scans into searchable pdfs.
This works fine with high-dpi images (for better OCR). But sometimes you need a small 
pdf that doesn't need hundreds of dpi.

Sadly the html output of tesseract seems to be in pixels, and hocr2pdf uses the pixels 
of the scanned image to align the word boxes.
So if you shrink the image to 1/4, text in the pdf is 4x too big (and out of place, of course)

This small script shrinks all bbox coordinates in the given inputfile by a given factor, so the 
text in the resulting pdf is in place again.

Usage
-----

Options:

* -i inputfile
* -o outputfile
* -s shrink factor (default 2)

Example:

    hocrShrink.py -i input.html -o outputOneFouth.html -s 4

or use stdin/out:

    hocrShrink.py -s4 < input.html

that can be handy for hocr2pdf, that needs stdin:

    hocrShrink.py -s2 < tesseractoutput.html | hocr2pdf -i shrunkBy2.tif -s -o little.pdf
    hocrShrink.py -s4 < tesseractoutput.html | hocr2pdf -i shrunkBy4.tif -s -o verysmall.pdf

