# image-cartoonizer
Cartoonize images using Python
!["cartoon-like"]( https://github.com/wingun322/image-cartoonizer/blob/main/cartoon-like.JPG)
__cartoon-like__
!["not-cartoon-like"]( https://github.com/wingun322/image-cartoonizer/blob/main/not-cartoon-like.JPG)
__not-cartoon-like__

- the limits of an algorithm
  
- If the original image has clear outlines and bright colors, this algorithm can express a more cartoonish feel better.
However, images with many dark colors or fine details are difficult to cartoonize.
Dark colors make contour detection difficult, and fine-grained images can lose detail during midian blur and bidirectional filter processing.
This may make the conversion to cartoon style less effective.
