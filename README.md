# Motivational Qualities of Songs for Daily Activities

This repository contains an analysis based on the research paper:

Kim, Y., Aiello, L.M. & Quercia, D. PepMusic: motivational qualities of songs for daily activities. EPJ Data Sci. 9, 13 (2020). https://doi.org/10.1140/epjds/s13688-020-0221-9

## Dataset

The analysis uses the dataset from [data_archive_20190201.json](data_archive_20190201.json) which contains song features and their associated activities. Each entry includes:

- trackId: Spotify track ID
- artists: Song artists
- songTitle: Song title
- features: Vector of extracted BMRI features including:
  - bpm: Beats per minute
  - chordsScale: Major/minor scale
  - chordsKey: Musical key
  - regularity: Rhythmic regularity
  - loudness: Song loudness
- activityType: Associated activity category
- clusteringLabel: Song cluster (calm, vibrant, intense)
- spotifyTrackURL: Link to Spotify track
- youtubeURL: Link to YouTube video
- youtubeId: YouTube video ID

## Analysis

The analysis is performed in [pepmusic_assignment.ipynb](pepmusic_assignment.ipynb) and includes:

- Data loading and preprocessing
- Feature extraction
- Clustering analysis using KMeans
- Analysis of musical features across different activity types
- Visualization of results

## Requirements

- Python 3
- Jupyter Notebook
- pandas
- scikit-learn
- matplotlib

## License

This project uses data from the referenced research paper. Please cite the original paper when using this analysis.
