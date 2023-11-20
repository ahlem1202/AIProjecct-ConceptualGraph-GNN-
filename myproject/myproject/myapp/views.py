# myapp/views.py
from django.shortcuts import render
from .forms import WordSearchForm
from django.http import JsonResponse
from gradio_client import Client
from .serializers import ProcessedResultSerializer
import json
import logging  # Import the logging module

logger = logging.getLogger(__name__)  # Create a logger instance

def gradio_integration(request):
    gradio_result = None
    processed_result = None
    
    if request.method == 'POST':
        input_text = request.POST.get('text_input')
        client = Client("https://a84dbbbe78d3404c80.gradio.live/")

        try:
            result = client.predict(input_text, api_name="/predict")

            # Debugging: print the result from Gradio
            print("Gradio Result:", result)

            if isinstance(result, str):
                gradio_result = result
            else:
                gradio_result = result.get('result')

            processed_result = process_gradio_result(gradio_result)

            # Use the serializer to convert processed_result into JSON
            serializer = ProcessedResultSerializer(processed_result, many=True)
            serialized_data = serializer.data

            # Return JSON response
            return JsonResponse({'gradio_result': gradio_result, 'processed_result': serialized_data})

        except Exception as e:
            logger.error("Error in Gradio integration: %s", e)

    return render(request, 'search_page.html', {'gradio_result': gradio_result, 'processed_result': processed_result})





def process_gradio_result(gradio_result):
    # Split the result into sections based on '\n'
    sections = gradio_result.split('\n\n')

    # Create a list to store the processed result
    result_list = []

    # Iterate over the sections
    for section in sections:
        # Split each section into lines
        lines = section.strip().split('\n')

        # Create a dictionary to store the processed row
        row_dict = {}

        # Iterate over the lines
        for line in lines:
            # Debugging: print each line to the console
            print("Line:", line)

            # Split each line into key and value
            line_parts = line.split('-', 1)
            if len(line_parts) == 2:
                key, value = line_parts
                row_dict[key.strip()] = value.strip()
            else:
                # Handle cases where there is only one value (a string) for each line
                row_dict[line.strip()] = ''

        # Append the processed row to the result list
        result_list.append(row_dict)

    # Debugging: print the final result_list to the console
    print("Result List:", result_list)

    return result_list


def search_word(request):
    form = WordSearchForm()
    return render(request, 'search_page.html', {'form': form})
