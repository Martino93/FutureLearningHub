-- Create the concepts table to store math concept categories and their hierarchy
CREATE TABLE concepts (
    concept_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    parent_id INTEGER,
    description TEXT,
    CONSTRAINT fk_parent_id FOREIGN KEY (parent_id) 
        REFERENCES concepts (concept_id) ON DELETE RESTRICT
);

-- Insert top-level categories
INSERT INTO concepts (name, description) VALUES
('Number and Quantity', 'Concepts related to numbers, operations, and quantities'),
('Algebra', 'Concepts involving algebraic expressions and equations'),
('Functions', 'Concepts related to mathematical functions and their properties'),
('Geometry', 'Concepts involving shapes, measurements, and spatial reasoning'),
('Statistics and Probability', 'Concepts related to data analysis and probability');

-- Insert subtopics under Number and Quantity
INSERT INTO concepts (name, parent_id, description) VALUES
('Real Number System', (SELECT concept_id FROM concepts WHERE name = 'Number and Quantity'), 'Properties and operations with real numbers'),
('Properties of real numbers', (SELECT concept_id FROM concepts WHERE name = 'Real Number System'), 'Commutative, associative, distributive properties'),
('Rational and irrational numbers', (SELECT concept_id FROM concepts WHERE name = 'Real Number System'), 'Classification of numbers'),
('Operations with fractions and decimals', (SELECT concept_id FROM concepts WHERE name = 'Real Number System'), 'Arithmetic with fractions and decimals'),
('Exponents and Radicals', (SELECT concept_id FROM concepts WHERE name = 'Number and Quantity'), 'Exponents, roots, and their properties'),
('Laws of exponents', (SELECT concept_id FROM concepts WHERE name = 'Exponents and Radicals'), 'Rules for manipulating exponents'),
('Simplifying radical expressions', (SELECT concept_id FROM concepts WHERE name = 'Exponents and Radicals'), 'Simplifying square roots and other radicals'),
('Rationalizing denominators', (SELECT concept_id FROM concepts WHERE name = 'Exponents and Radicals'), 'Eliminating radicals from denominators'),
('Complex Numbers', (SELECT concept_id FROM concepts WHERE name = 'Number and Quantity'), 'Operations and equations with complex numbers'),
('Operations with complex numbers', (SELECT concept_id FROM concepts WHERE name = 'Complex Numbers'), 'Addition, subtraction, multiplication, division'),
('Solving equations with complex solutions', (SELECT concept_id FROM concepts WHERE name = 'Complex Numbers'), 'Quadratic equations with complex roots'),
('Vectors and Matrices', (SELECT concept_id FROM concepts WHERE name = 'Number and Quantity'), 'Operations with vectors and matrices'),
('Vector addition and scalar multiplication', (SELECT concept_id FROM concepts WHERE name = 'Vectors and Matrices'), 'Basic vector operations'),
('Matrix operations', (SELECT concept_id FROM concepts WHERE name = 'Vectors and Matrices'), 'Matrix addition and multiplication'),
('Sequences and Series', (SELECT concept_id FROM concepts WHERE name = 'Number and Quantity'), 'Patterns in sequences and series'),
('Arithmetic sequences', (SELECT concept_id FROM concepts WHERE name = 'Sequences and Series'), 'Sequences with constant differences'),
('Geometric sequences', (SELECT concept_id FROM concepts WHERE name = 'Sequences and Series'), 'Sequences with constant ratios');

-- Insert subtopics under Algebra
INSERT INTO concepts (name, parent_id, description) VALUES
('Expressions and Equations', (SELECT concept_id FROM concepts WHERE name = 'Algebra'), 'Manipulating and solving algebraic expressions'),
('Simplifying algebraic expressions', (SELECT concept_id FROM concepts WHERE name = 'Expressions and Equations'), 'Combining like terms and factoring'),
('Solving linear equations', (SELECT concept_id FROM concepts WHERE name = 'Expressions and Equations'), 'Solving equations of the form ax + b = c'),
('Solving linear inequalities', (SELECT concept_id FROM concepts WHERE name = 'Expressions and Equations'), 'Solving inequalities like ax + b < c'),
('Graphing linear equations', (SELECT concept_id FROM concepts WHERE name = 'Expressions and Equations'), 'Plotting lines from equations'),
('Absolute Value', (SELECT concept_id FROM concepts WHERE name = 'Algebra'), 'Equations and inequalities involving absolute values'),
('Solving absolute value equations', (SELECT concept_id FROM concepts WHERE name = 'Absolute Value'), 'Solving equations like |x| = a'),
('Solving absolute value inequalities', (SELECT concept_id FROM concepts WHERE name = 'Absolute Value'), 'Solving inequalities like |x| < a'),
('Graphing absolute value functions', (SELECT concept_id FROM concepts WHERE name = 'Absolute Value'), 'Plotting V-shaped graphs'),
('Quadratic Equations and Functions', (SELECT concept_id FROM concepts WHERE name = 'Algebra'), 'Quadratic expressions and their graphs'),
('Factoring quadratics', (SELECT concept_id FROM concepts WHERE name = 'Quadratic Equations and Functions'), 'Factoring ax^2 + bx + c'),
('Solving quadratic equations', (SELECT concept_id FROM concepts WHERE name = 'Quadratic Equations and Functions'), 'Solving via factoring, quadratic formula'),
('Graphing quadratic functions', (SELECT concept_id FROM concepts WHERE name = 'Quadratic Equations and Functions'), 'Plotting parabolas'),
('Polynomial and Rational Expressions', (SELECT concept_id FROM concepts WHERE name = 'Algebra'), 'Operations with polynomials and rational functions'),
('Operations with polynomials', (SELECT concept_id FROM concepts WHERE name = 'Polynomial and Rational Expressions'), 'Adding, multiplying polynomials'),
('Solving rational equations', (SELECT concept_id FROM concepts WHERE name = 'Polynomial and Rational Expressions'), 'Solving equations with rational expressions'),
('Exponential and Logarithmic Functions', (SELECT concept_id FROM concepts WHERE name = 'Algebra'), 'Exponential and logarithmic relationships'),
('Solving exponential equations', (SELECT concept_id FROM concepts WHERE name = 'Exponential and Logarithmic Functions'), 'Solving equations like 2^x = 8'),
('Graphing logarithmic functions', (SELECT concept_id FROM concepts WHERE name = 'Exponential and Logarithmic Functions'), 'Plotting logarithmic curves');

-- Insert subtopics under Functions
INSERT INTO concepts (name, parent_id, description) VALUES
('Function Basics', (SELECT concept_id FROM concepts WHERE name = 'Functions'), 'Core concepts of functions'),
('Function notation', (SELECT concept_id FROM concepts WHERE name = 'Function Basics'), 'Using f(x) notation'),
('Domain and range', (SELECT concept_id FROM concepts WHERE name = 'Function Basics'), 'Identifying input and output sets'),
('Evaluating functions', (SELECT concept_id FROM concepts WHERE name = 'Function Basics'), 'Computing f(a) for given x'),
('Types of Functions', (SELECT concept_id FROM concepts WHERE name = 'Functions'), 'Different function families'),
('Linear functions', (SELECT concept_id FROM concepts WHERE name = 'Types of Functions'), 'Functions of the form f(x) = mx + b'),
('Quadratic functions', (SELECT concept_id FROM concepts WHERE name = 'Types of Functions'), 'Functions of the form f(x) = ax^2 + bx + c'),
('Exponential functions', (SELECT concept_id FROM concepts WHERE name = 'Types of Functions'), 'Functions of the form f(x) = a*b^x'),
('Parent Functions and Transformations', (SELECT concept_id FROM concepts WHERE name = 'Functions'), 'Standard functions and their modifications'),
('Identifying parent functions', (SELECT concept_id FROM concepts WHERE name = 'Parent Functions and Transformations'), 'Recognizing basic function shapes'),
('Transformations', (SELECT concept_id FROM concepts WHERE name = 'Parent Functions and Transformations'), 'Shifts, reflections, stretches'),
('Piecewise Functions', (SELECT concept_id FROM concepts WHERE name = 'Functions'), 'Functions defined by multiple rules'),
('Defining piecewise functions', (SELECT concept_id FROM concepts WHERE name = 'Piecewise Functions'), 'Writing piecewise function rules'),
('Graphing piecewise functions', (SELECT concept_id FROM concepts WHERE name = 'Piecewise Functions'), 'Plotting piecewise graphs'),
('Operations with Functions', (SELECT concept_id FROM concepts WHERE name = 'Functions'), 'Combining functions'),
('Function addition and multiplication', (SELECT concept_id FROM concepts WHERE name = 'Operations with Functions'), 'Computing (f + g)(x), (f * g)(x)'),
('Composition of functions', (SELECT concept_id FROM concepts WHERE name = 'Operations with Functions'), 'Computing (f o g)(x)'),
('Inverse Functions', (SELECT concept_id FROM concepts WHERE name = 'Functions'), 'Functions and their inverses'),
('Finding inverses', (SELECT concept_id FROM concepts WHERE name = 'Inverse Functions'), 'Algebraically finding f^(-1)(x)'),
('Graphing inverses', (SELECT concept_id FROM concepts WHERE name = 'Inverse Functions'), 'Plotting inverse functions');

-- Insert subtopics under Geometry
INSERT INTO concepts (name, parent_id, description) VALUES
('Points, Lines, and Planes', (SELECT concept_id FROM concepts WHERE name = 'Geometry'), 'Basic geometric constructs'),
('Distance and midpoint formulas', (SELECT concept_id FROM concepts WHERE name = 'Points, Lines, and Planes'), 'Calculating distances and midpoints'),
('Angles', (SELECT concept_id FROM concepts WHERE name = 'Geometry'), 'Properties of angles'),
('Angle relationships', (SELECT concept_id FROM concepts WHERE name = 'Angles'), 'Complementary, supplementary angles'),
('Triangles', (SELECT concept_id FROM concepts WHERE name = 'Geometry'), 'Properties and theorems of triangles'),
('Triangle congruence', (SELECT concept_id FROM concepts WHERE name = 'Triangles'), 'SSS, SAS congruence criteria'),
('Right triangle trigonometry', (SELECT concept_id FROM concepts WHERE name = 'Triangles'), 'Sine, cosine, tangent in right triangles'),
('Circles', (SELECT concept_id FROM concepts WHERE name = 'Geometry'), 'Properties of circles'),
('Arc length and sector area', (SELECT concept_id FROM concepts WHERE name = 'Circles'), 'Calculating arc lengths and areas'),
('Equations of circles', (SELECT concept_id FROM concepts WHERE name = 'Circles'), 'Writing circle equations'),
('Area and Volume', (SELECT concept_id FROM concepts WHERE name = 'Geometry'), 'Calculating areas and volumes'),
('Area of polygons', (SELECT concept_id FROM concepts WHERE name = 'Area and Volume'), 'Areas of triangles, rectangles, etc.'),
('Volume of solids', (SELECT concept_id FROM concepts WHERE name = 'Area and Volume'), 'Volumes of prisms, spheres, etc.');

-- Insert subtopics under Statistics and Probability
INSERT INTO concepts (name, parent_id, description) VALUES
('Data Representation', (SELECT concept_id FROM concepts WHERE name = 'Statistics and Probability'), 'Visualizing data'),
('Histograms and scatter plots', (SELECT concept_id FROM concepts WHERE name = 'Data Representation'), 'Creating and interpreting graphs'),
('Measures of Central Tendency', (SELECT concept_id FROM concepts WHERE name = 'Statistics and Probability'), 'Summarizing data'),
('Mean, median, mode', (SELECT concept_id FROM concepts WHERE name = 'Measures of Central Tendency'), 'Calculating central measures'),
('Measures of Spread', (SELECT concept_id FROM concepts WHERE name = 'Statistics and Probability'), 'Describing data variability'),
('Range and standard deviation', (SELECT concept_id FROM concepts WHERE name = 'Measures of Spread'), 'Measuring data dispersion'),
('Probability', (SELECT concept_id FROM concepts WHERE name = 'Statistics and Probability'), 'Calculating likelihoods'),
('Basic probability rules', (SELECT concept_id FROM concepts WHERE name = 'Probability'), 'Addition and multiplication rules'),
('Conditional probability', (SELECT concept_id FROM concepts WHERE name = 'Probability'), 'Probability given conditions');

-- Create an index on parent_id for faster queries
CREATE INDEX idx_concepts_parent_id ON concepts (parent_id);