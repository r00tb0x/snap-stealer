import urlparse

# List of domains associated with Snapchat.
domain = ['feelinsonice-hrd.appspot.com', 'data.flurry.com']

def start(context, flow):
	with open('logs.txt','a') as myfile:
		myfile.write('----- starting -----\n')
		
def response(context, flow):
	with open('logs.txt','a') as myfile:
		# If the data is not from Snapchat, skip analysis.
		if not (flow.response.request.host in domain):
			return
		# TODO: Get fancy with responses.
		myfile.write('Response from Snapchat. OOOW\n')

def request(context, flow):
	with open('logs.txt', 'a') as myfile:

		# If the data is not from Snapchat, skip analysis.
		if not (flow.request.host in domain):
			return

		# XXX: Untested, but should print the username from a request.
		url = flow.request.content
		r = urlparse.urlsplit(url)
		form = urlparse.parse_qs(r1.query)

		# Every request seems to have these three attributes.
		username = form["username"]
		timestamp = form["timestamp"]
		request_token = form["req_token"]

		# Start processing the request.

		if flow.request.path == '/bq/upload':
			myfile.write(username)
			myfile.write(' is uploading an image\n')
			"""
			media_id:   YOURUSERNAME~6AABF95C-C466-417B-904D-ED4CC3B1C45D
			type:       0 # I sent a picture, so I would imagine 0 is picture.
			username:   yourUserName
			zipped:     0
			data:
			"""

		if flow.request.path == '/bq/send':
			myfile.write(username)
			myfile.write(' sent the image to ')
			myfile.write(form["recipient"])
			myfile.write('\n')
			"""
			country_code:  US
			media_id:      YOURUSERNAME~6AABF95C-C466-417B-904D-ED4CC3B1C45D
			recipient:     whoYouSentItTo
			time:          6
			type:          0
			zipped:        0
			"""

		# I don't know the difference between updates and all_updates.
		if flow.request.path == '/bq/updates' or flow.request.path == '/bq/all_updates':
			myfile.write(username)
			myfile.write(' is updating.\n')
			"""
			"""

		if flow.request.path == '/bq/stories':
			myfile.write(username)
			myfile.write(' is updating their stories.\n')
			"""
			"""

		if flow.request.path == '/bq/bests':
			myfile.write(username)
			myfile.write(' is updating their stories.\n')
			"""
			friend_usernames:  ["yourUserName","friend1","friend2","friend3",...]
			"""

		if flow.request.path == '/bq/blob':
			myfile.write(username)
			myfile.write(' is blobing.\n')
			"""
			id:         513637398565409770r
			"""

		if flow.request.path == '/bq/blob':
			myfile.write(username)
			myfile.write(' is blobing.\n')
			# Thought: could we manipulate this json and make the time always be 10s?
			# Thought: could we manipulate this json and make the sender be someone else?

			"""
			added_friends_timestamp:  1395940738302
			events:                   [{"eventName":"START","params":{},"ts":1398563914.011596},{"eventName":"OPEN","params":{"type":"NORMAL"},"ts":1398563914.097597},{"eventName":"USER_PREVIEW_STATS","params":{"in_preview_but_expired":0,"in_preview":false,"smart_filters_enabled":false,"formaly_preview_not_in_preview":0},"ts":1398563914.70434},{"eventName":"REQUEST_ENDED","params":{"Time":0.9263189583334679,"Request_Size":197,"Path":"bq\/all_updates","Success":true,"Hit_Cache":false,"Return_Size":17653},"ts":1398563915.630106},{"eventName":"PAGE CAMERA","params":{},"ts":1398563916.667694},{"eventName":"CLOSE","params":{},"ts":1398563926.039474},{"eventName":"OPEN","params":{"type":"NORMAL"},"ts":1398565392.759993},{"eventName":"USER_PREVIEW_STATS","params":{"in_preview_but_expired":0,"in_preview":false,"smart_filters_enabled":false,"formaly_preview_not_in_preview":0},"ts":1398565392.770698},{"eventName":"REQUEST_ENDED","params":{"Time":2.305813916666921,"Request_Size":197,"Path":"bq\/all_updates","Success":true,"Hit_Cache":false,"Return_Size":17653},"ts":1398565395.073266},{"eventName":"NOTIFICATION_WHILE_OPEN","params":{},"ts":1398565413.952243},{"eventName":"REQUEST_ENDED","params":{"Time":1.38770362500054,"Request_Size":197,"Path":"bq\/all_updates","Success":true,"Hit_Cache":false,"Return_Size":17775},"ts":1398565415.343368},{"eventName":"SNAP_RECEIVED","params":{"type":"IMAGE","time":7,"friendCount":20,"id":"513637398565409770r","sender":"whoSentIt"},"ts":1398565415.354479},{"eventName":"REQUEST_ENDED","params":{"Time":0.5802297500003988,"Request_Size":200,"Path":"bq\/blob","Success":true,"Hit_Cache":false,"Return_Size":40880},"ts":1398565416.203418},{"eventName":"PAGEFEED","params":{},"ts":1398565419.327751},{"eventName":"PAGE FEED","params":{},"ts":1398565419.328078},{"eventName":"SNAP_VIEW","params":{"type":"IMAGE","time":7,"friendCount":20,"id":"513637398565409770r","sender":"whoSentIt"},"ts":1398565420.882285},{"eventName":"SNAP_EXPIRED","params":{"type":"IMAGE","time":7,"friendCount":20,"id":"513637398565409770r","sender":"whoSentIt","time_viewed":7.003291958333648},"ts":1398565427.888872}]  
			json:                     {"513637398565409770r":{"t":1398565420.881927,"sv":7.003291958333648}}
			"""


def end(context, flow):
	with open('logs.txt','a') as myfile:
		myfile.write('----- ending -----\n')

