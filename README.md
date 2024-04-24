
![image](https://user-images.githubusercontent.com/77064752/197388994-e4b645d6-ab59-4336-9e6e-6e2c175fdb1f.png)

As shown in the figure we see and mask of scale 3x3, this mask is moved over the image and operation is performed on pixel replacing it’s intensity with new one according to the given algorithm.

<br>
<hr>

Let’s understand some of the few important filters:

For Arithmetic mean,
Average (or mean) filtering is a method of 'smoothing' images by reducing the amount of intensity variation between neighbouring pixels. The average filter works by moving through the image pixel by pixel, replacing each value with the average value of neighbouring pixels, including itself.
The Arithmetic Mean (AM) or called average is the ratio of the sum of all observations to the total number of observations.
Here the observations are the intensity of all pixels in in given 3x3, 7x7 etc masking. 
We take these pixel intensity and replace the center pixel intensity with final mean value.

![image](https://user-images.githubusercontent.com/77064752/197389027-1f48631f-d0b9-4a9e-a215-e485d9bd442f.png)  
(Sum of all pixel intensity in masking)
	Where k,j = floor(scale) 
	Eg. For scale = 3,
	k = {-1, 0, 1} 		j = {-1, 0, 1} 
	Arithmetic mean filter is commonly used for noise reduction.
<hr>
For Geometric mean,

![image](https://user-images.githubusercontent.com/77064752/197389033-abc72f38-9dac-4749-9782-60e790077da9.png)

The geometric mean filter is most widely used to filter out Gaussian noise.
<hr>
For median filter,
	
Step 1: Arrange all intensities of mask in ascending or descending order.
Step2:  Let n = total no of intensities in mask
		
![image](https://user-images.githubusercontent.com/77064752/197389057-9777761d-6154-4247-bd08-07361723bc57.png)


It is very effective at removing impulse noise, the “pepper and salt” noise, in an image. The principle of the median filter is to replace the gray level of each pixel by the median of the gray levels in a neighborhood of the pixels, instead of using the average operation.
<hr>
For Max filter,

![image](https://user-images.githubusercontent.com/77064752/197389062-4ee4bb6e-3b49-4566-b3cf-c1e7536e1f25.png)
MaxFilter is a nonlinear filter commonly used to locally smooth data and diminish pepper-like noise, where the amount of smoothing is dependent on the value of r. The function applied to each range-r neighborhood is Max.
<hr>
For Min filter,

![image](https://user-images.githubusercontent.com/77064752/197389068-f6c7755c-136f-43f2-b7f1-13828230ac96.png)
MinFilter is a nonlinear filter commonly used to locally smooth data and diminish salt-like noise, where the amount of smoothing is dependent on the value of r. The function applied to each range-r neighborhood is Min. 
<hr>
For Midpoint filter,
The midpoint filter is typically used to filter images containing short tailed noise such as Gaussian and uniform type noises. The midpoint filter is defined as : where the coordinate (x+i, y+j ) is defined over the image A and the coordinate (i, j) is defined over the N x N size square mask.

![image](https://user-images.githubusercontent.com/77064752/197389073-cdbd4d79-43b6-48f8-852a-cb5304ad4a0c.png)
