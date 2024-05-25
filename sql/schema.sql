CREATE TABLE Volumes (
    VolumeNumber INT PRIMARY KEY,
    ReleaseDate DATE
);

CREATE TABLE Arcs (
    ArcID INT PRIMARY KEY,
    ArcName VARCHAR(255)
);

CREATE TABLE Chapters (
    ChapterID INT PRIMARY KEY,
    VolumeNumber INT,
    ArcID INT,
    ChapterName VARCHAR(255),
    FOREIGN KEY (VolumeNumber) REFERENCES Volumes(VolumeNumber),
    FOREIGN KEY (ArcID) REFERENCES Arcs(ArcID)
);

CREATE TABLE Pages (
    PageID INT PRIMARY KEY,
    ChapterID INT,
    PageNumber INT,
    IsColorSpread BOOLEAN DEFAULT FALSE,
    IsDoubleSpread BOOLEAN DEFAULT FALSE,
    IsCoverPage BOOLEAN DEFAULT FALSE,
    IsColorCover BOOLEAN DEFAULT FALSE,
    IsCoverStory BOOLEAN DEFAULT FALSE,
    IsFanRequest BOOLEAN DEFAULT FALSE,
    IsAnimalTheater BOOLEAN DEFAULT FALSE,
    IsOther BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (ChapterID) REFERENCES Chapters(ChapterID)
);

CREATE TABLE Panels (
    PanelID INT PRIMARY KEY,
    PageID INT,
    IsFlashback BOOLEAN DEFAULT FALSE,
    Location VARCHAR(255) DEFAULT 'Unknown',
    FOREIGN KEY (PageID) REFERENCES Pages(PageID)
);

CREATE TABLE Characters (
    CharacterID INT PRIMARY KEY,
    Name VARCHAR(255),
    Status TEXT CHECK(Status IN ('Alive', 'Dead', 'Unknown')) DEFAULT 'Unknown'
);

CREATE TABLE Affiliations (
    AffiliationID INT PRIMARY KEY,
    AffiliationName VARCHAR(255)
);

CREATE TABLE CharacterAppearances (
    AppearanceID INT PRIMARY KEY,
    CharacterID INT,
    PanelID INT,
    Bounty BIGINT,
    FOREIGN KEY (CharacterID) REFERENCES Characters(CharacterID),
    FOREIGN KEY (PanelID) REFERENCES Panels(PanelID)
);

CREATE TABLE CharacterAffiliations (
    AppearanceID INT,
    AffiliationID INT,
    FOREIGN KEY (AppearanceID) REFERENCES CharacterAppearances(AppearanceID),
    FOREIGN KEY (AffiliationID) REFERENCES Affiliations(AffiliationID)
);

CREATE TABLE DevilFruits (
    FruitID INT PRIMARY KEY,
    FruitName VARCHAR(255),
    Type TEXT CHECK(Type IN ('Paramecia', 'Zoan', 'Logia'))
);

CREATE TABLE CharacterDevilFruits (
    AppearanceID INT,
    FruitID INT,
    FOREIGN KEY (AppearanceID) REFERENCES CharacterAppearances(AppearanceID),
    FOREIGN KEY (FruitID) REFERENCES DevilFruits(FruitID)
);

CREATE TABLE Abilities (
    AbilityID INT PRIMARY KEY,
    AbilityName VARCHAR(255)
);

CREATE TABLE CharacterAbilities (
    AppearanceID INT,
    AbilityID INT,
    FOREIGN KEY (AppearanceID) REFERENCES CharacterAppearances(AppearanceID),
    FOREIGN KEY (AbilityID) REFERENCES Abilities(AbilityID)
);

CREATE TABLE CharacterInteractions (
    InteractionID INT PRIMARY KEY,
    Character1ID INT,
    Character2ID INT,
    PanelID INT,
    IsFighting BOOLEAN DEFAULT FALSE,
    IsTalking BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (Character1ID) REFERENCES Characters(CharacterID),
    FOREIGN KEY (Character2ID) REFERENCES Characters(CharacterID),
    FOREIGN KEY (PanelID) REFERENCES Panels(PanelID)
);

CREATE TABLE FamilyRelationships (
    RelationshipID INT PRIMARY KEY,
    Character1ID INT,
    Character2ID INT,
    RelationshipType TEXT CHECK(RelationshipType IN ('Parent', 'Child', 'Sibling')),
    FOREIGN KEY (Character1ID) REFERENCES Characters(CharacterID),
    FOREIGN KEY (Character2ID) REFERENCES Characters(CharacterID)
);

CREATE TABLE RomanticRelationships (
    RelationshipID INT PRIMARY KEY,
    Character1ID INT,
    Character2ID INT,
    FOREIGN KEY (Character1ID) REFERENCES Characters(CharacterID),
    FOREIGN KEY (Character2ID) REFERENCES Characters(CharacterID)
);

CREATE TABLE CharacterRelationship (
    AppearanceID INT,
    RelationshipID INT,
    FOREIGN KEY (AppearanceID) REFERENCES CharacterAppearances(AppearanceID),
    FOREIGN KEY (RelationshipID) REFERENCES RomanticRelationships(RelationshipID)
);