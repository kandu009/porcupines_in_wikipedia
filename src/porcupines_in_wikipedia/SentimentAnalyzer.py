import sys
import json
from pprint import pprint
from nltk.sentiment.vader import SentimentIntensityAnalyzer

conversation_id = 'conversations'
to_id = 'to'
from_id = 'from'
message_id = 'msg'
time_id = 'time'
compound_id = 'compound'

# method to return the sentiment associated with the comment.
# polarity_scores returns a json of format 
# 	{'neg': <float>, 'neu': <float>, 'pos': <float>, 'compound': <float>}
# method returns compound..
# if compound > 0 its positive; negative otherwise.
# the higher the absolute value is, the stronger the sentiment is.
def get_sentiment_scale(analyzer_obj, comment):
	return analyzer_obj.polarity_scores(comment)[compound_id]

# method to write the data to the output file for using it on BigQuery
def write_to_file(file_desc, data):
	file_desc.write(data+'\n')

if __name__ == '__main__':
	
	if len(sys.argv) != 3:
		print 'Invalid arguments, run using: python SimpleJSONParser.py <input_json_file> <output_csv_file>'
		sys.exit(1)
	
	else:
		# load the input arguments
		input_json_file = sys.argv[1]
		output_csv_file = sys.argv[2]
		
		# load the JSON data
		with open(input_json_file) as json_arr_file:
			conversations_arr = json.load(json_arr_file)
		
		# initialize the sentiment analyzer
		analyzer_obj = SentimentIntensityAnalyzer()
			
		# open the output file for writing
		output_fd = open(output_csv_file, 'w')

		# Get the data needed to generate the output file
		for obj in conversations_arr[conversation_id]:
			sentiment_scale = get_sentiment_scale(analyzer_obj, obj[message_id])
			output_data = obj[from_id] + ',' + obj[to_id] + "," + obj[time_id] + "," + str(sentiment_scale)
			write_to_file(output_fd, output_data)

		output_fd.close()