
## Pelican installation

```
mamba create -n pelican37 python=3.7
pip install pelican
pip install pelican-data-files
pip install bibtexparser
conda activate pelican
```

See GENERATING-PUBLICATIONS.md

## Running pelican

From the root directory, run
```
pelican content --ignore-cache
```

From somewhere else, you can run
```
pelican --listen
```
