# Dataset Description name: NIH ChestX-ray14

## Dataset Overview
The NIH ChestX-ray14 dataset consists of over 112,000 frontal chest
X-ray images collected from more than 30,000 patients. Each image
is associated with up to 14 disease labels.

## Label Generation
Disease labels were extracted automatically from radiology reports
using natural language processing, resulting in weakly supervised
annotations.

## Strengths
- Large-scale real clinical data
- Widely adopted benchmark dataset
- Suitable for representation learning

## Known Limitations
- Weak and noisy labels
- Significant class imbalance
- Multi-label ambiguity
- No COVID-specific annotations

## Data Access Strategy
Due to the large size of the dataset, we access the data using a
streaming-based pipeline, allowing on-the-fly processing without
full local storage.