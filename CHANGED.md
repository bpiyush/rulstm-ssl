1. Move data to SSD folder `/ssd/pbagad/datasets/EK-action-anticipation/`
2. Remove data files from the repository folder
3. Symlink the data files to the repository folder
4. Only download RGB features from their provided script for EK-100


## Steps
1. Download the data from the 
```bash
bash ./scripts/download_data_ek100_full.sh
```
2. Only keep the training on RGB features in `./scripts/train_anticipation_ek100.sh` and run
```bash
bash ./scripts/train_anticipation_ek100.sh
```