# AI Engineering Journal

## Project
Student CGPA Performance Management System

## Development Environment
- IDE: Visual Studio Code
- Programming Language: Python
- Version Control: Git
- Repository: GitHub
- Testing Framework: pytest
- Formatter: Black
- Linter: Ruff
- AI Coding Assistant: AI-assisted development tool

## AI-Assisted Development Activities

### 1. Code Generation
AI was used to assist in generating the initial Python Student class
for storing student details and calculating percentage and CGPA.

### 2. Test Generation
AI was used to suggest test cases for:
- Percentage calculation
- CGPA calculation
- Empty marks
- Empty grade points
- Single subject
- Multiple grade points

The generated tests were reviewed and executed using pytest.

### 3. AI-Assisted Debugging
A deliberate error was introduced by changing:

self.marks

to:

self.mark

Pytest identified the resulting AttributeError.

AI was then used to identify and explain the error.

The developer manually validated the suggested correction and restored:

self.marks

All tests subsequently passed.

### 4. AI-Assisted Refactoring
AI was used to review the Student class and suggest improvements
for readability and maintainability.

The developer reviewed the suggestions and verified that the
existing functionality was not changed.

### 5. Human Validation
AI-generated suggestions were not accepted blindly.

The developer:
- Reviewed generated code
- Checked logic
- Executed automated tests
- Verified formatting
- Checked code quality
- Reviewed Git changes

## Quality Validation

### Automated Tests
pytest was executed successfully.

Result:

6 tests passed.

### Code Formatting
Black was executed successfully.

Result:

All files conform to Black formatting standards.

### Code Quality
Ruff was executed successfully.

Result:

All checks passed.

## AI Engineering Principles

1. AI suggestions must be reviewed by a human developer.
2. Generated code must be tested before acceptance.
3. Changes must be traceable through Git.
4. AI should assist development rather than replace developer responsibility.
5. Sensitive or confidential information should not be provided to AI tools.
6. Reproducible prompts and development decisions should be documented.

## Conclusion

AI-assisted development improved code generation, testing,
debugging, refactoring, and development productivity.

Human validation, automated testing, code-quality tools, and Git
traceability were used to maintain software reliability and
reproducibility.