# Introduction
[Wikipedia][wiki]: Face detection can be regarded as a specific case of object-class detection. In object-class detection, the task is to find the locations and sizes of all objects in an image that belong to a given class. Examples include upper torsos, pedestrians, and cars.
Face-detection algorithms focus on the detection of frontal human faces. It is analogous to image detection in which the image of a person is matched bit by bit. Image matches with the image stores in database. Any facial feature changes in the database will invalidate the matching process.
A reliable face-detection approach based on the genetic algorithm and the eigen-face[3] technique:[4]
Firstly, the possible human eye regions are detected by testing all the valley regions in the gray-level image. Then the genetic algorithm is used to generate all the possible face regions which include the eyebrows, the iris, the nostril and the mouth corners.
Each possible face candidates is normalized to reduce lightning effect caused due to uneven illumination and the shirring effect due to head movement. The fitness value of each candidate is measured based on its projection on the eigen-faces. After a number of iterations, all the face candidates with a high fitness value are selected for further verification. At this stage, the face symmetry is measured and the existence of the different facial features is verified for each face candidate.

* A face detector and tracker written in python using OpenCV and online available face image databases (free).  

### Tech

* [OpenCV][opencv] - OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library. 
* Python



### Usage

* You need to install OpenCV. Make sure you have the latest version of it. (I used OpenCV-3.1.0)
    - Follow the steps in these links:
        - [Link 1][1]
        - [Link 2][2]

**Face Detection**
	- Download *facedetect.py* in your working directory.
	- Open the file, and enter your image file's name (or the path to it if its not in your working directory)
	- Run the command ```python facedetect.py``` on terminal and you will see a rectangle on the faces in the image in a new pop-up window.
 
**Face Tracking**
	- Download *facetracking.py* in your working directory.
	- Open the file, and enter your video file's name (or the path to it if its not in your working directory)
	- Run the command ```python facetracking.py``` on terminal and you will see a rectangle on the faces in the video in a new pop-up window.

### Acknowledgements

* [Prof. G.S. Raghavan][profgsr] for guiding us and giving us an opportunity to learn a lot from such a project.
* My seniors for giving useful tips and ideas for successfully completing our project.

### Development

Want to contribute? Great!

   [wiki]: <https://en.wikipedia.org/wiki/Face_detection>
   [opencv]: <http://opencv.org/>
   [1]: <http://docs.opencv.org/2.4/doc/tutorials/introduction/linux_install/linux_install.html>
   [2]: <http://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/>
   [poster]: <https://www.dropbox.com/s/1iul44nl4no9l4s/elab%20poster.pptx?dl=0>
   [profgsr]: <http://www.iiitb.ac.in/faculty_page.php?name=GSrinivasaraghavan>
