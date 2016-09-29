Ivoryanna Brown. Netid: itb2
2 - 19 - 15
I started this project on Feb 18th and finished on Feb 19th.
It took me approximately 3 hours all together.
I received help from Roxanne Baker in consulting hours.
I didn't have many issues with the required part of the project, but the extra credit 
made my brain hurt. I spent the bulk of my time trying to get it to work. 
I keep getting this error when I try to untransform the file:

Traceback (most recent call last):
  File "/Users/Ivory/Downloads/eclipse/Eclipse.app/Contents/MacOS/Cs101/sp15_cps101_asg4_transform/src/FileUntransform.py", line 124, in <module>
    transform_file()
  File "/Users/Ivory/Downloads/eclipse/Eclipse.app/Contents/MacOS/Cs101/sp15_cps101_asg4_transform/src/FileUntransform.py", line 86, in transform_file
    twords = transform(words, transform_rot13())
TypeError: transform_rot13() takes exactly 1 argument (0 given)

I know what a type error is, but given what is in that function in the FileUntransform.py module, I'm not sure
how to edit it to make it work. It says that I need to pass an argument through transform_rot13(), but I don't have
an argument at this point and it worked in the FileTransform.py module without an argument....

I would keep meddling with this, but I don't seem to be getting anywhere. 