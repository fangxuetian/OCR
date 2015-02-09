# OCR
<u><b>OCR POC</b></u>

<h1> 1. Preprocessing module </h1>

<h2> 1.1 OnSuccess<h2>
<img src="http://i.gyazo.com/7ec254e11b77f4545497593fd23bd831.png">
<br>
<h2> 1.2 OnError<h2>
<img src="http://i.gyazo.com/294cac7bd7f924292de9d3406ba76618.png">
<br>
<h2><b style="color:#FF0000">1.3 Preprocessing test</b><h2>
<h3> 1.3.1 Source image:  </h3>
<img src="http://i.gyazo.com/6aa92fac21946e8c9391486a19439b21.png">
<h3> 1.3.2 Preprocessing result (aspect ratio 64x64, scalate 32x32): 
</h3><img src="http://i.gyazo.com/35ec454505ef87c58a512529ea0f88b4.png">

<h1> 2. Properties Extract </h1>
K-Dimensional vector for represent each pixel of an image.For train, sample requires correct class, for recognition only representation (k-dimensional vector).

Train sample of a 3: ([1,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,0,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,0,255,255,255,255,255,255,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],2)

Recognition sample of same 3: [1,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,0,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,0,255,255,255,255,255,255,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255]


<h1> 3. Classifier </h1>
<blink> Building... </blink>
