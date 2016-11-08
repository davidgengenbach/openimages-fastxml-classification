--CREATE DATABASE openimages;

CREATE TABLE IF NOT EXISTS Images (
  ImageID CHAR(16),
  Subset VARCHAR,
  OriginalURL VARCHAR,
  OriginalLandingURL VARCHAR,
  License VARCHAR,
  AuthorProfileURL VARCHAR,
  Author VARCHAR,
  Title VARCHAR,
  OriginalSize BIGINT,
  OriginalMD5 VARCHAR,
  Thumbnail300KURL VARCHAR,
  PRIMARY KEY(ImageID)
);

CREATE TABLE IF NOT EXISTS Dict (
  LabelName VARCHAR,
  DisplayLabelName VARCHAR,
  PRIMARY KEY (LabelName)
);

CREATE TABLE IF NOT EXISTS Labels (
  ImageID CHAR(16) REFERENCES Images(ImageID),
  Source VARCHAR,
  LabelName VARCHAR REFERENCES Dict(LabelName),
  Confidence REAL,
  PRIMARY KEY(ImageID, Source, LabelName)
);

\COPY Images FROM 'images_2016_08/validation/images.csv' DELIMITER ',' CSV HEADER
\COPY Images FROM 'images_2016_08/train/images.csv' DELIMITER ',' CSV HEADER;
\COPY Dict FROM 'dict.csv' DELIMITER ',' CSV;
\COPY Labels FROM 'human_ann_2016_08/validation/labels.csv' DELIMITER ',' CSV HEADER;
\COPY Labels FROM 'machine_ann_2016_08/validation/labels.csv' DELIMITER ',' CSV HEADER;
\COPY Labels FROM 'machine_ann_2016_08/train/labels.csv' DELIMITER ',' CSV HEADER;
