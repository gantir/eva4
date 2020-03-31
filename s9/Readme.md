Used albumentations for data augumentation

Wrote the grad cam module

Final Accuracy: 87.35%

```logs
0%|          | 0/782 [00:00<?, ?it/s]Epoch: 1
Batch Id/Size: 782/50000, Training Loss: 1.48750293, Training Accuracy: 44.8840%: 100%|██████████| 782/782 [00:58<00:00, 13.39it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.001]
100%|██████████| 157/157 [00:03<00:00, 43.97it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.01972901, Test Accuracy: 55.2600%

Epoch: 2
Batch Id/Size: 782/50000, Training Loss: 1.33455849, Training Accuracy: 60.9980%: 100%|██████████| 782/782 [00:58<00:00, 13.28it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.001]
100%|██████████| 157/157 [00:03<00:00, 42.74it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.01410067, Test Accuracy: 68.5100%

Epoch: 3
Batch Id/Size: 782/50000, Training Loss: 1.12363029, Training Accuracy: 68.2680%: 100%|██████████| 782/782 [00:59<00:00, 13.10it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.001]
100%|██████████| 157/157 [00:03<00:00, 43.67it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.01188006, Test Accuracy: 73.4300%

Epoch: 4
Batch Id/Size: 782/50000, Training Loss: 0.79519862, Training Accuracy: 72.6100%: 100%|██████████| 782/782 [01:00<00:00, 12.91it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.001]
100%|██████████| 157/157 [00:03<00:00, 42.60it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.01087954, Test Accuracy: 75.9400%

Epoch: 5
Batch Id/Size: 782/50000, Training Loss: 0.74907500, Training Accuracy: 75.9340%: 100%|██████████| 782/782 [01:00<00:00, 12.94it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.001]
100%|██████████| 157/157 [00:03<00:00, 42.07it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00985155, Test Accuracy: 78.3300%

Epoch: 6
Batch Id/Size: 782/50000, Training Loss: 0.50731510, Training Accuracy: 78.1360%: 100%|██████████| 782/782 [01:00<00:00, 12.93it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.001]
100%|██████████| 157/157 [00:03<00:00, 41.63it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00901872, Test Accuracy: 80.3900%

Epoch: 7
Batch Id/Size: 782/50000, Training Loss: 0.63364202, Training Accuracy: 79.9680%: 100%|██████████| 782/782 [01:00<00:00, 12.99it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.001]
100%|██████████| 157/157 [00:03<00:00, 43.32it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00799866, Test Accuracy: 82.5300%

Epoch: 8
Batch Id/Size: 782/50000, Training Loss: 0.52303255, Training Accuracy: 81.6100%: 100%|██████████| 782/782 [01:00<00:00, 12.93it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.001]
100%|██████████| 157/157 [00:03<00:00, 42.93it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00828509, Test Accuracy: 82.2300%

Epoch: 9
Batch Id/Size: 782/50000, Training Loss: 0.30386609, Training Accuracy: 82.7420%: 100%|██████████| 782/782 [01:00<00:00, 12.97it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.001]
100%|██████████| 157/157 [00:03<00:00, 44.08it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00788448, Test Accuracy: 83.3300%

Epoch: 10
Batch Id/Size: 782/50000, Training Loss: 0.30224818, Training Accuracy: 83.9720%: 100%|██████████| 782/782 [01:00<00:00, 13.02it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.001]
100%|██████████| 157/157 [00:03<00:00, 43.06it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00791269, Test Accuracy: 83.1100%

Epoch: 11
Batch Id/Size: 782/50000, Training Loss: 0.17066351, Training Accuracy: 87.1800%: 100%|██████████| 782/782 [01:00<00:00, 13.00it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.00025]
100%|██████████| 157/157 [00:03<00:00, 42.28it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00676521, Test Accuracy: 85.5000%

Epoch: 12
Batch Id/Size: 782/50000, Training Loss: 0.42692637, Training Accuracy: 88.0700%: 100%|██████████| 782/782 [01:00<00:00, 13.01it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.0005]
100%|██████████| 157/157 [00:03<00:00, 42.73it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00670523, Test Accuracy: 85.7100%

Epoch: 13
Batch Id/Size: 782/50000, Training Loss: 0.05897774, Training Accuracy: 88.8720%: 100%|██████████| 782/782 [01:00<00:00, 12.98it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.0005]
100%|██████████| 157/157 [00:03<00:00, 43.12it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00663350, Test Accuracy: 85.8100%

Epoch: 14
Batch Id/Size: 782/50000, Training Loss: 0.06116366, Training Accuracy: 89.4560%: 100%|██████████| 782/782 [01:00<00:00, 13.01it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.0005]
100%|██████████| 157/157 [00:03<00:00, 43.04it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00664964, Test Accuracy: 86.0100%

Epoch: 15
Batch Id/Size: 782/50000, Training Loss: 0.24247126, Training Accuracy: 89.8800%: 100%|██████████| 782/782 [00:59<00:00, 13.05it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.0005]
100%|██████████| 157/157 [00:03<00:00, 42.83it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00683285, Test Accuracy: 85.6700%

Epoch: 16
Batch Id/Size: 782/50000, Training Loss: 0.09957060, Training Accuracy: 90.3120%: 100%|██████████| 782/782 [01:00<00:00, 13.01it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.0005]
100%|██████████| 157/157 [00:03<00:00, 42.73it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00692100, Test Accuracy: 85.6500%

Epoch: 17
Batch Id/Size: 782/50000, Training Loss: 0.28919324, Training Accuracy: 90.4700%: 100%|██████████| 782/782 [01:00<00:00, 12.95it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.0005]
100%|██████████| 157/157 [00:03<00:00, 41.82it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00706718, Test Accuracy: 85.4500%

Epoch: 18
Batch Id/Size: 782/50000, Training Loss: 0.12096936, Training Accuracy: 91.2220%: 100%|██████████| 782/782 [01:00<00:00, 12.94it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.0005]
100%|██████████| 157/157 [00:03<00:00, 42.75it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00690870, Test Accuracy: 85.8500%

Epoch: 19
Batch Id/Size: 782/50000, Training Loss: 0.16020596, Training Accuracy: 91.4280%: 100%|██████████| 782/782 [01:00<00:00, 12.99it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.0005]
100%|██████████| 157/157 [00:03<00:00, 42.49it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00703327, Test Accuracy: 85.9400%

Epoch: 20
Batch Id/Size: 782/50000, Training Loss: 0.40951064, Training Accuracy: 91.7080%: 100%|██████████| 782/782 [01:00<00:00, 12.97it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.0005]
100%|██████████| 157/157 [00:03<00:00, 42.84it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00712283, Test Accuracy: 85.8300%

Epoch: 21
Batch Id/Size: 782/50000, Training Loss: 0.06741872, Training Accuracy: 93.1600%: 100%|██████████| 782/782 [00:59<00:00, 13.06it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.000125]
100%|██████████| 157/157 [00:03<00:00, 42.64it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00632093, Test Accuracy: 87.1500%

Epoch: 22
Batch Id/Size: 782/50000, Training Loss: 0.09531674, Training Accuracy: 93.7440%: 100%|██████████| 782/782 [01:00<00:00, 13.00it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.00025]
100%|██████████| 157/157 [00:03<00:00, 42.36it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00633895, Test Accuracy: 87.2800%

Epoch: 23
Batch Id/Size: 782/50000, Training Loss: 0.19380695, Training Accuracy: 94.1580%: 100%|██████████| 782/782 [00:59<00:00, 13.04it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.00025]
100%|██████████| 157/157 [00:03<00:00, 42.89it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00646691, Test Accuracy: 87.3800%

Epoch: 24
Batch Id/Size: 782/50000, Training Loss: 0.03292900, Training Accuracy: 94.4500%: 100%|██████████| 782/782 [00:59<00:00, 13.04it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.00025]
100%|██████████| 157/157 [00:03<00:00, 42.75it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00633275, Test Accuracy: 87.3500%

Epoch: 25
Batch Id/Size: 782/50000, Training Loss: 0.15512823, Training Accuracy: 94.5080%: 100%|██████████| 782/782 [01:00<00:00, 12.90it/s]
  0%|          | 0/157 [00:00<?, ?it/s]LR: [0.00025]
100%|██████████| 157/157 [00:03<00:00, 41.46it/s]
Batch Id/Size: 157/10000, Test Loss: 0.00649456, Test Accuracy: 87.2000%
```
