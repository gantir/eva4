
## Session 8

> Achieve 85% or more accuracy on CIFAR10 using Resnet within 50 epochs

Achieved 87.98% accuracy in 20 epochs

All the methods are in a separate python library. This library can be found at [evalib](https://github.com/gantir/evalib/tree/develop).

```
0%|          | 0/782 [00:00<?, ?it/s]Epoch: 1
Batch Id/Size: 782/50000, Training Loss: 1.86034894, Training Accuracy: 44.9400%: 100%|██████████| 782/782 [00:33<00:00, 23.02it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.001]
100%|██████████| 157/157 [00:03<00:00, 45.48it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.01796794, Test Accuracy: 59.5000%

Epoch: 2
Batch Id/Size: 782/50000, Training Loss: 1.36627829, Training Accuracy: 62.5200%: 100%|██████████| 782/782 [00:33<00:00, 23.12it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.001]
100%|██████████| 157/157 [00:03<00:00, 44.64it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.01425286, Test Accuracy: 67.7300%

Epoch: 3
Batch Id/Size: 782/50000, Training Loss: 0.93258286, Training Accuracy: 70.5100%: 100%|██████████| 782/782 [00:33<00:00, 23.30it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.001]
100%|██████████| 157/157 [00:03<00:00, 45.20it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.01176495, Test Accuracy: 74.0400%

Epoch: 4
Batch Id/Size: 782/50000, Training Loss: 0.88620764, Training Accuracy: 75.5160%: 100%|██████████| 782/782 [00:33<00:00, 23.32it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.001]
100%|██████████| 157/157 [00:03<00:00, 44.65it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00981071, Test Accuracy: 78.6900%

Epoch: 5
Batch Id/Size: 782/50000, Training Loss: 0.98571408, Training Accuracy: 78.5800%: 100%|██████████| 782/782 [00:33<00:00, 23.58it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.001]
100%|██████████| 157/157 [00:03<00:00, 45.02it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00944273, Test Accuracy: 79.7100%

Epoch: 6
Batch Id/Size: 782/50000, Training Loss: 0.91361731, Training Accuracy: 80.9600%: 100%|██████████| 782/782 [00:33<00:00, 23.51it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.001]
100%|██████████| 157/157 [00:03<00:00, 44.90it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00884416, Test Accuracy: 80.9500%

Epoch: 7
Batch Id/Size: 782/50000, Training Loss: 0.74368232, Training Accuracy: 82.7700%: 100%|██████████| 782/782 [00:33<00:00, 23.53it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.001]
100%|██████████| 157/157 [00:03<00:00, 44.67it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00832803, Test Accuracy: 82.0300%

Epoch: 8
Batch Id/Size: 782/50000, Training Loss: 0.60699546, Training Accuracy: 84.1180%: 100%|██████████| 782/782 [00:33<00:00, 23.41it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.001]
100%|██████████| 157/157 [00:03<00:00, 43.82it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00800765, Test Accuracy: 83.2100%

Epoch: 9
Batch Id/Size: 782/50000, Training Loss: 0.48458850, Training Accuracy: 85.5880%: 100%|██████████| 782/782 [00:33<00:00, 23.32it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.001]
100%|██████████| 157/157 [00:03<00:00, 44.93it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00755349, Test Accuracy: 84.1900%

Epoch: 10
Batch Id/Size: 782/50000, Training Loss: 0.27402481, Training Accuracy: 86.4480%: 100%|██████████| 782/782 [00:33<00:00, 23.28it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.001]
100%|██████████| 157/157 [00:03<00:00, 45.40it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00728424, Test Accuracy: 84.8600%

Epoch: 11
Batch Id/Size: 782/50000, Training Loss: 0.28077310, Training Accuracy: 89.2220%: 100%|██████████| 782/782 [00:33<00:00, 23.46it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.00025]
100%|██████████| 157/157 [00:03<00:00, 45.53it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00641463, Test Accuracy: 86.6400%

Epoch: 12
Batch Id/Size: 782/50000, Training Loss: 0.31868249, Training Accuracy: 90.0680%: 100%|██████████| 782/782 [00:33<00:00, 23.57it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.0005]
100%|██████████| 157/157 [00:03<00:00, 46.07it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00635253, Test Accuracy: 87.0300%

Epoch: 13
Batch Id/Size: 782/50000, Training Loss: 0.15509950, Training Accuracy: 90.3180%: 100%|██████████| 782/782 [00:33<00:00, 23.59it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.0005]
100%|██████████| 157/157 [00:03<00:00, 45.56it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00619025, Test Accuracy: 87.2900%

Epoch: 14
Batch Id/Size: 782/50000, Training Loss: 0.09341887, Training Accuracy: 90.8480%: 100%|██████████| 782/782 [00:33<00:00, 23.65it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.0005]
100%|██████████| 157/157 [00:03<00:00, 45.21it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00621973, Test Accuracy: 87.5300%

Epoch: 15
Batch Id/Size: 782/50000, Training Loss: 0.18377373, Training Accuracy: 91.3920%: 100%|██████████| 782/782 [00:32<00:00, 23.78it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.0005]
100%|██████████| 157/157 [00:03<00:00, 45.91it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00632424, Test Accuracy: 87.1800%

Epoch: 16
Batch Id/Size: 782/50000, Training Loss: 0.08602229, Training Accuracy: 91.7620%: 100%|██████████| 782/782 [00:32<00:00, 23.83it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.0005]
100%|██████████| 157/157 [00:03<00:00, 46.08it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00609178, Test Accuracy: 87.5300%

Epoch: 17
Batch Id/Size: 782/50000, Training Loss: 0.14529699, Training Accuracy: 92.2280%: 100%|██████████| 782/782 [00:32<00:00, 23.76it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.0005]
100%|██████████| 157/157 [00:03<00:00, 45.08it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00609921, Test Accuracy: 87.8500%

Epoch: 18
Batch Id/Size: 782/50000, Training Loss: 0.07565978, Training Accuracy: 92.8000%: 100%|██████████| 782/782 [00:32<00:00, 23.77it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.0005]
100%|██████████| 157/157 [00:03<00:00, 45.91it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00612490, Test Accuracy: 87.6600%

Epoch: 19
Batch Id/Size: 782/50000, Training Loss: 0.12831780, Training Accuracy: 92.8520%: 100%|██████████| 782/782 [00:33<00:00, 23.69it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.0005]
100%|██████████| 157/157 [00:03<00:00, 44.97it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00612850, Test Accuracy: 87.9300%

Epoch: 20
Batch Id/Size: 782/50000, Training Loss: 0.14866513, Training Accuracy: 93.1800%: 100%|██████████| 782/782 [00:33<00:00, 23.66it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.0005]
100%|██████████| 157/157 [00:03<00:00, 46.74it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00634952, Test Accuracy: 87.9800%
```

![ Accuracy and Loss](https://github.com/gantir/eva4/raw/develop/s8/aritfacts/s8.png)
