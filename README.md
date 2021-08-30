# PDF-Filler-PoC
This is a simple proof of concept for a form-based PDF filler ecosystem.

## The flow
The currently planned flow functions like this:

At first the values provided (krs, cel, year) are passed to the FieldMapper object which generates a dictionary of values based on the mapping.
The desired mapping is provided to the FieldMapper constructor in JSON or in a simple python dict form.
Then, the value mapping is provided to the PDFFiller object which provides a simple interface to fill the PDF with the desired data.
 
 PDFFiller ought to work like this:
 It receives a dictionary that contains key-value pairs of the desired mapping, where the key is the field name (according to an accepted field-naming convention) and the value is the desired value of said field.

 Whether the PDFFiller should return the PDF to stdout or save it locally is to be established.