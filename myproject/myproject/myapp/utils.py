from gradio_client import Client

client = Client("https://a84dbbbe78d3404c80.gradio.live/")
result = client.predict(
		"Hello!!",	# str  in 'input_text' Textbox component
							api_name="/predict"
)
print(result)