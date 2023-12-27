#notes of Review of deep learning: concepts, CNN architectures challenges, applications, future directions

*When to apply dl*
- 专家经验不可用
- 无法利用专家只是做出解释/决定
- 问题实时更新（股市，天气）
- 数据过大/数据不足

*Why dl?*
- Universal learning approach
- Robustness
- Generalization $\rightarrow$ Transfer Learning
- Scalability

*Classification of DL approaches *
1. **Deep supervised learning**
   - labeled data; relatively simple;guess$\rightarrow$update$\rightarrow$guess...;
   - techniques: RNN, CNN, DNN
   - RNNs' advantages:collect data or generate a data output from the prior knowledge. ; disadvantages: decision boundary might be overstrained when training set doesn’t own samples that should be in a class.
2. **Deep semi-supervised learning**
   - based on semi_labeled datasets;GANs.DRL;
   - advantage: minimize the amount of labeled data needed
   - disadvantage: irrelevant input feature present training data could furnish incorrect decisions
   - ideal for text document classification task
3. **Deep unsupervised learning**
   - no labels are required
   - generative networks;dimensionality reduction;**clustering**
   - disadvantages: unable to provide accurate information concerning data sorting and computationally complex.
4. **Deep reinforcement learning** 
   - no straightforward loss function 
   - complete access to the function, which requires optimization, meaning that it should be queried via interaction
   - state being interacted with is founded on an environment, where the input x; is based on the preceding actions
    