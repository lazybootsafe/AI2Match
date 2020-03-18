## 中文分词学习
## 知识蒸馏

知识蒸馏来自哈工大，可自行查阅。

## bert and ernie

此项目基于BERT模型改进mask pre-trainning任务，引入了词遮掩模式，通过对词的连续mask提升预训练模型对中文词汇的学习。  

具体改进为，通过jieba分词，以词为单位随机选择预测字符，生成预测字符的概率沿用BERT。随机替换时把每个字符随机替换为一个随机字符，因此被随机替换掉的部分并不是一个正常的中文词汇。  

依赖：  
https://github.com/fxsjy/jieba  
https://github.com/tqdm/tqdm  

装requirements的时候，注意看下tensorflow是CPU的还是GPU版本就行了。

用法：
```
python create_ernie_pretraining_data.py \
    --input_file='original_data.txt' \
    --output_file='./pretrain.tf_record' \
    --vocab_file='BERT_DATA/vocab.txt'

```

# BERT
**\*\*\*\*\* New March 19th, 2019: Realize ERNIE \*\*\*\*\***

Use create_ernie_pretraining_data.py realize ERNIE.  
近期百度开源的ERNIE在多种中文文本任务中表现出色，相较于 BERT 随机[MASK]或替换字符，ERNIE 直接对词进行随机[MASK]或替换，增强了模型中文实体含义的表示能力。其实我们可以看出ERNIE与BERT非常相似，区别主要是在pretrain中选择[MASK]字符的逻辑。  
在此提供create_ernie_pretraining_data.py生成ERNIE的预训练数据，方便在Tensorflow中使用。  
