import pandas as pd
from django.core.management.base import BaseCommand
from school.models import Class, Student

class Command(BaseCommand):
    help = 'Import students from an Excel file with multiple sheets'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The path to the Excel file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        
        try:
            # Load the Excel file
            xls = pd.ExcelFile(file_path)
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error reading the Excel file: {e}"))
            return

        # Iterate through each sheet
        for sheet_name in xls.sheet_names:
            try:
                # Read the sheet into a DataFrame
                df = pd.read_excel(file_path, sheet_name=sheet_name)

                # Get or create the class based on the sheet name
                class_obj, created = Class.objects.get_or_create(name=sheet_name)

                for _, row in df.iterrows():
                    try:
                        # Create the student and associate it with the class
                        Student.objects.create(
                            class_number=row['class_number'],
                            first_name=row['first_name'],
                            last_name=row['last_name'],
                            class_name=class_obj
                        )
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f"Error importing row: {row} - {e}"))
                        continue
                
                self.stdout.write(self.style.SUCCESS(f"Successfully imported students for class: {sheet_name}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error processing sheet {sheet_name}: {e}"))
                continue
        
        self.stdout.write(self.style.SUCCESS('Successfully imported students from all sheets'))
