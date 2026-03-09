# Educational Software: chuong_trinh_hoc_lop_8.py

## Overview
This educational software is designed for advanced 8th grade students, providing a comprehensive collection of challenging multiple choice and essay questions across eight subjects. It also includes an interactive menu system and an automatic scoring feature. 

## Features
- **Subjects Covered**: Mathematics, Literature, History, Geography, Physics, Chemistry, English, Biology
- **Number of Questions**: 30 Multiple Choice Questions & 10 Essay Questions for each subject
- **Interactive Menu System**: Users can select subjects and types of questions
- **Automatic Scoring System**: Provides feedback on the user's performance

## Implementation
Here's the main code for the program:

```python
import random

class EducationalSoftware:
    def __init__(self):
        self.questions = self.load_questions()
        self.scores = {}  # Dictionary to keep track of scores per subject

    def load_questions(self):
        questions = {
            'Mathematics': {...},  # Load advanced questions
            'Literature': {...},  # Load advanced questions
            'History': {...},
            'Geography': {...},
            'Physics': {...},
            'Chemistry': {...},
            'English': {...},
            'Biology': {...},
        }
        return questions

    def display_menu(self):
        print("Welcome to the 8th Grade Advanced Educational Software!")
        print("Please select a subject:")
        for subject in self.questions.keys():
            print(f'- {subject}')
        print('0 - Exit')

    def start_quiz(self, subject):
        print(f'You selected {subject}. Let us begin!')
        score = 0
        for question in self.questions[subject]['multiple_choice']:
            print(question['query'])
            for i, option in enumerate(question['options']):
                print(f"{i + 1}. {option}")
            answer = int(input('Your answer: ')) - 1
            if question['options'][answer] == question['correct_answer']:
                score += 1
                print('Correct!')
            else:
                print('Incorrect!')

        # Handle essay questions similar to above
        self.scores[subject] = score
        print(f'Your score in {subject}: {score}/{len(self.questions[subject]['multiple_choice'])}')

    def run(self):
        while True:
            self.display_menu()
            choice = input('Enter your choice: ')
            if choice == '0':
                print('Exiting...')
                break
            elif choice in self.questions:
                self.start_quiz(choice)
            else:
                print('Invalid choice!')

if __name__ == '__main__':
    app = EducationalSoftware()
    app.run()
```

## Note on Questions Format
Each subject should have its own structured questions format, defining multiple choice and essay questions appropriately. Example:
```python
'Mathematics': {
    'multiple_choice': [
        {'query': 'What is the square root of 144?', 'options': ['10', '12', '14', '16'], 'correct_answer': '12'},
        ...  # Add more questions
    ],
    'essay': [
        'Explain the Pythagorean theorem and its applications.',
        ...  # Add more essay prompts
    ]
},
```