
# Framework of ML

1. step1:  function of unknow $\rightarrow$ $y = f_\theta(x)$
2. step2: define from training data$\rightarrow$ $L(\theta)$
3. step3: optimization $\theta^\star = arg min_\theta L$

# General Guide

 1.  $if$ loss on training data too large:
	  1.  The model is too simple. $\rightarrow$ redesign model to make it more flexible
		（增加模型复杂度以拟合更多函数）
				methods:
				1. More features 
				2. Deep Learning
	  2. Optimization Issue $\rightarrow$ 梯度下降的局部极小值 $\neq$ 最小值
	  Question：如何判断出了什么问题？
	  1.  Gaining gthe insights froms comparision（换模型）
	  2. Start from shallower networks(or other models),which are easier to optimize.
 2. $if$ loss on training data small
	1. The loss in testing data is too large
		   1. 过拟合 $\rightarrow$ 面向training data 编程 /"freestyle"
		   methods:
			1.  增加training data
			2.  Data augmentation（创造data，左右翻转，截图etc)（根据资料的特性，不能胡编乱造）
			3. constrain model
			4. Less parameters,sharing parameters; Less features; Early stopping; Regularization; dropout etc.
			5. Cross Validation(避免在private set上loss过大)
				具体实现：$n-fold$ **Cross** Validation
	2.  Mismatch $\rightarrow$ Training and testing data have different distriutions.(20年的新冠预测22年的新冠）`
			(依赖专家知识（？）)


