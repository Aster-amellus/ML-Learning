# ML introduction

***Machine Learning:Looking for Function***
* Speech Recognition
* Image Recognition
* Playing Go

***Different types of Functions***
* **Regression**: The function outputs a scalar.
* **classification**: Given options(classes),the function outputs the correct one.
* ***Structured Learning***: create something with structure(image, document)

***How to Predict Views***(how to training)
1. Function with Unknown Parameters $\rightarrow$ $y =f ( ... )$<br>rough predict: $y = b + wx_1$ (based on domain knowledge)
     **$x_1$**: feature<br>**$w$**: weight<br>**$b$**: bias<br>**$y = f( ... )$**: model
2. Define Loss from Training Data <br> Loss is a function of parameters. $\rightarrow$ $L(b, w)$<br>**Label**: real value<br>ways to calculate loss: <br> 
   1. mean absolute error 
   2. mean square error
   3. cross entropy(if y and $y*hat$ is possibility)
3. Optimization   $w^*$ $b^*$ = $arg$ $min L$<br>Gradient Descent absolute   
    (require domain knowledge)$\rightarrow$get better on training data

$$Linear Model$$
> *All Piecewise Linear Curves* = constant + sum of a set of curves
***$Sigmoid Function$***: $y = c\frac{1}{1 + e^{-(b+wx_1)}}$$= c\ sigmoid(b+wx_1)$
<br> $y = b + \sum_{i} c_i\,sigmoid(b_i+w_ix_1)$
**More Features**
$y = b+wx_1$$\downarrow$
$y = b + \sum_{i} c_i\,sigmoid(b_i+w_ix_1)$$\downarrow$
$y = b + \sum_{j} w_jx_j$$\downarrow$
$y = b + \sum_{i} c_i\,sigmoid(b_i+\sum_{j} w_{ij}x_j)$
>
$y = b + c^T\sigma$$(b+Wx)$
**${\theta}^*$** = $arg$ $min_\theta L$
$g = \nabla L(\theta^0)$
>An epoch == update all batches>

>Sigmoid