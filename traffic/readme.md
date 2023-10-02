Initially:
16 convolutions -> 2by2 max pooling -> flatten -> output; loss = 4.59%
Then replaced 16 with 32, and that had loss = 4.22%
Then replaced 32 with 64 and that had loss = 6.33% (probably overfit
32 convolutions -> 2by2 max pooling -> flatten -> 128 hidden layer (relu) -> output; loss = 2.98%, but simulated loss was 0.57%
32 convolutions -> 2by2 max pooling -> flatten -> 128 hidden layer (relu) dropout 20% -> output; loss = 2.79%
32 convolutions -> 2by2 max pooling -> flatten -> 128 hidden layer (relu) dropout 50% -> output; loss = 2.08%, but simulated loss was 2.91%
32 convolutions -> 2by2 max pooling -> 32 convolutions -> flatten -> 128 hidden layer (relu) dropout 50% -> output; loss = 1.50%
32 convolutions -> 2by2 max pooling -> 32 convolutions -> 2by2 max pooling -> flatten -> 128 hidden layer (relu) dropout 50% -> output; loss = 1.72%
32 convolutions -> 2by2 max pooling -> 32 convolutions -> flatten -> 128 hidden layer (relu) dropout 20% -> 128 hidden layer (relu) dropout 20% -> output; loss = 0.64%
32 convolutions -> 2by2 max pooling -> 32 convolutions -> flatten -> 128 hidden layer (relu) dropout 30% -> 128 hidden layer (relu) dropout 30% -> output; loss = 0.43%, simulated loss = 0.78%
32 convolutions -> 2by2 max pooling -> 32 convolutions -> flatten -> 128 hidden layer (relu) dropout 40% -> 128 hidden layer (relu) dropout 40% -> output; loss = 1.12%
32 convolutions -> 4by4 max pooling -> 32 convolutions -> flatten -> 128 hidden layer (relu) dropout 30% -> 128 hidden layer (relu) dropout 30% -> output; loss = 1.09%
