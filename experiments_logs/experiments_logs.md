
＃实验记录，之后就不用表格了很麻烦，在这里同步

#  SSD 

ssd300×300 focal loss 
batch_size：16

train_net: "models/VGGNet/VOC0712/SSD_300x300/train.prototxt"
test_net: "models/VGGNet/VOC0712/SSD_300x300/test.prototxt"
test_iter: 503
test_interval: 10000
base_lr: 0.0002
display: 20
max_iter: 30000
lr_policy: "multistep"
gamma: 0.1
momentum: 0.9
weight_decay: 0.0005
snapshot: 20000
snapshot_prefix: "models/VGGNet/VOC0712/SSD_300x300/VGG_VOC0712_SSD_300x300"
solver_mode: GPU
device_id: 0
debug_info: false
snapshot_after_train: true
test_initialization: false
average_loss: 10

stepvalue: 20000
stepvalue: 30000
iter_size: 1
type: "SGD"
eval_type: "detection"
ap_version: "11point"

ssd focal loss训练出来效果很差　39%,是比不用提升了一些，但是效果不好(不知道是不是迭代次数不够的原因)

通过观察，之前给分数较低的框，现在给出的分数很高。　0.3以上的很多，这有问题。训练到最后，loss依旧较高
<code> lamr=39% </code>
focal loss的使用可能有问题，maybe

 
# SSD 

数据未变，使用更长的迭代周期，和优化算法。

train_net: "models/VGGNet/VOC0712/SSD_300x300/train.prototxt"
test_net: "models/VGGNet/VOC0712/SSD_300x300/test.prototxt"
test_iter: 503
test_interval: 10000
base_lr: 0.0002
display: 10
max_iter: 120000
lr_policy: "multistep"
gamma: 0.1
momentum: 0.9
weight_decay: 0.0005
snapshot: 20000
snapshot_prefix: "models/VGGNet/VOC0712/SSD_300x300/VGG_VOC0712_SSD_300x300"
solver_mode: GPU
device_id: 0
debug_info: false
snapshot_after_train: true
test_initialization: false
average_loss: 10
stepvalue: 90000
stepvalue: 110000
iter_size: 1
type: "Adam"
eval_type: "detection"
ap_version: "11point"




这就是简单的调参，意义不大，要看到问题未表露出来的东西。由表及里。
预计到明天８点左右就ok

# rfcn
train_net: "/home/user/Disk1.8T/py-R-FCN/experiments/5_28_original/train_agnostic_ohem.prototxt"
base_lr: 0.0002
lr_policy: "step"
gamma: 0.1
stepsize: 50000
display: 20

momentum: 0.9
weight_decay: 0.0005
#### We disable standard caffe solver snapshotting and implement our own snapshot
#### function
snapshot: 0
#### We still use the snapshot prefix, though
snapshot_prefix: "resnet50_rfcn_ohem"
iter_size: 8
#### debug_info: true


case $DATASET in
  pascal_voc)
    TRAIN_IMDB="voc_0712_trainval"
    TEST_IMDB="voc_0712_test"
    PT_DIR="pascal_voc"
    ITERS=32000
    
    
数据用的是张姗姗老师的改进数据
rfcn的实验，我换用了　vis>0.6的数据。

就是为了让数据更加合理，e


train:640*1280
test:768*1280
map = 42%
log average miss rate = 18.7% 

用这个当做baseline, 然后做。

train:648*1280
test:640*1280
map = 28.8%
这样就很低，怎么回事？
log average miss rate = 17.6%


test:960*1280
0.29s
log average miss rate = 17.4%

test:1000*2000
0.30s         17.6%
fp有20000+ 

test:1400*2400
0.55s
fp只有4000+   22%


该rfcn实验，只是同上边的训练的尺度不同，其他的都一样

train:960*1280
test:960*1280

log average miss rate = 20%

多了很多在环境中的框，有点乱标的意思，怎么回事？



citypersons

30%

训练出来的效果特别好，没有在车上有很多分数较低的误检

但是在树干上，和树冠上，还存在一定的问题

将两种数据混合训练呢？

我觉得培钰的top-down效果就不错




实验，尝试rfcn训练　caltech vis>0.6 h > 50 头部大约40%的位置，用来进行训练

train_net: "/home/user/Disk1.8T/py-R-FCN_5_29/experiments/5_28_original_head_handle/train_agnostic_ohem.prototxt"
base_lr: 0.0002
lr_policy: "step"
gamma: 0.1
stepsize: 50000
display: 20

momentum: 0.9
weight_decay: 0.0005
 We disable standard caffe solver snapshotting and implement our own snapshot
 function
snapshot: 0
 We still use the snapshot prefix, though
snapshot_prefix: "resnet50_rfcn_ohem"
iter_size: 8
 debug_info: true


iters 32000

在车身上的误检是少了很多，但是，mr=28%

思路，用局部来回归整体，看效果怎么样？

尝试使用pspnet

PSPNet 就是为了整合不同区域的context来获取全局的context 信息。

中间模块是pyramid pooling module，是为了获得全局先验信息。在一个深度网络中+，感受野的尺寸大小决定有多少context 信息可以用。理论上ResNet 的感受野尺寸要比输入图像尺寸大。但是有文章指出CNN 的实际感受野尺寸要比理论尺寸小很多。之前提出的Global average pooling 对于复杂的ADE20K 数据库来说过于简单。因此，论文借鉴Spatial pyramid pooling（SPP空间金字塔池化方法）提出pyramid pooling module。

第一行是用global pooling 生成的一个单独的输出。第二行将特征图等分为4 块，每块分别用global pooling 得到bin output，接下来的行以此类推。上图四行分别对应1×1, 2×2, 3×3 和6×6。

为了减小维度和位置全局特征的权值，在每一行使用一个1×1 卷积层。接着我们使用双线性插值，使其和原始特征图尺寸一样大小。最后和原始特征图组合起来。


pspnet 这样来做，只是尝试一下，但是，可能不会太好

参数设置相同，就是网络结构不同




实验时间　 | 实验名称 | 实验内容 | 测试集 | 训练集 | 网络结构 | 具体参数 | 损失函数 | 实验记录 | 实验结果 | 备注 | more 
- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | -: 

