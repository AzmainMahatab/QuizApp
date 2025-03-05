from django.db import migrations

app_label = 'quiz'

def add_sample_questions(apps, schema_editor):
    Question = apps.get_model(app_label, 'Question')
    Choice = apps.get_model(app_label, 'Choice')

    sample_data = [
        {
            'question': 'What is the capital of France?',
            'choices': [
                {'text': 'Paris', 'is_correct': True},
                {'text': 'London', 'is_correct': False},
                {'text': 'Berlin', 'is_correct': False},
                {'text': 'Madrid', 'is_correct': False},
            ]
        },
        {
            'question': 'Which planet is known as the Red Planet?',
            'choices': [
                {'text': 'Mars', 'is_correct': True},
                {'text': 'Venus', 'is_correct': False},
                {'text': 'Jupiter', 'is_correct': False},
                {'text': 'Saturn', 'is_correct': False},
            ]
        },
        {
            'question': 'Who wrote "Romeo and Juliet"?',
            'choices': [
                {'text': 'William Shakespeare', 'is_correct': True},
                {'text': 'Charles Dickens', 'is_correct': False},
                {'text': 'Jane Austen', 'is_correct': False},
                {'text': 'Mark Twain', 'is_correct': False},
            ]
        },
        {
            'question': 'Which is the largest ocean on Earth?',
            'choices': [
                {'text': 'Pacific Ocean', 'is_correct': True},
                {'text': 'Atlantic Ocean', 'is_correct': False},
                {'text': 'Indian Ocean', 'is_correct': False},
                {'text': 'Arctic Ocean', 'is_correct': False},
            ]
        },
        {
            'question': 'In which year did the Titanic sink?',
            'choices': [
                {'text': '1912', 'is_correct': True},
                {'text': '1905', 'is_correct': False},
                {'text': '1918', 'is_correct': False},
                {'text': '1925', 'is_correct': False},
            ]
        }
    ]

    for data in sample_data:
        question_text = data['question']
        choices_data = data['choices']

        question, created = Question.objects.get_or_create(
            html=question_text,
            defaults={'is_published': True, 'maximum_marks': 4}
        )

        if created:
            for choice_data in choices_data:
                Choice.objects.create(
                    question=question,
                    html=choice_data['text'],
                    is_correct=choice_data['is_correct']
                )


class Migration(migrations.Migration):

    dependencies = [
        # Define the migration's dependency on the initial migration
        (app_label, '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_sample_questions),
    ]