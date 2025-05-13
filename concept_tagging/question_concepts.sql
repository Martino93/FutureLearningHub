-- Create the linking table to associate questions with concepts
CREATE TABLE question_concepts (
    -- Column to store the Question ID, referencing the questions table
    question_id INT NOT NULL,
    -- Column to store the Concept ID, referencing the concepts table
    concept_id INT NOT NULL,

    -- Define the primary key as a composite of question_id and concept_id
    -- This ensures that each question-concept pair is unique
    PRIMARY KEY (question_id, concept_id),

    -- Define the foreign key constraint for question_id
    -- This links back to the 'id' column in the 'questions' table
    -- ON DELETE CASCADE means that if a question is deleted, its entries in this table are also deleted
    FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE,

    -- Define the foreign key constraint for concept_id
    -- This links back to the 'concept_id' column in the 'concepts' table
    -- ON DELETE CASCADE means that if a concept is deleted, its entries in this table are also deleted
    FOREIGN KEY (concept_id) REFERENCES concepts(concept_id) ON DELETE CASCADE
);

-- You can optionally add comments to the table and columns for better documentation
COMMENT ON TABLE question_concepts IS 'Links questions to concepts.';
COMMENT ON COLUMN question_concepts.question_id IS 'Foreign key referencing the questions table.';
COMMENT ON COLUMN question_concepts.concept_id IS 'Foreign key referencing the concepts table.';
