class Post():
    '''1. this class corresponds to the tipoff post structure, on the feeder side
    2. we will populate this class and then write json to flat files, making it convienent for logstash to consume it.
        Json example of a post:
{
               "text" => "@nollbit @johanni ja, klart det bara blir spekulationer. Men samhllsnyttig infrastruktur br vl vara delvis skyddad mot detta?",
               "lang" => "sv",
         "@timestamp" => "2014-01-09T10:01:30.449Z",
               "type" => "twitter",
            "post_id" => 418676219430047744,
           "up_votes" => 0,
       "user_mention" => "{\"id\"=>15809255, \"indices\"=>[0, 8], \"id_str\"=>\"15809255\", \"screen_name\"=>\"nollbit\", \"name\"=>\"johan\"},{\"id\"=>16311319, \"indices\"=>[9, 17], \"id_str\"=>\"16311319\", \"screen_name\"=>\"johanni\", \"name\"=>\"Johan Nilsson\"}",
         "place_name" => "Knivsta",
            "user_id" => "14235149",
       "user_img_url" => "http://pbs.twimg.com/profile_images/378800000478670862/88783a59c7c7e5c200627af584781212_normal.jpeg",
    "content_img_url" => "%{[entities][media_url]}",
              "coord" => "59.74596768,17.78693824"
}
    '''
    def __init__(self, post_id, text, created, content_img_url, user_img_url, user_id, place_name, coord, username, type, up_votes =0 ):
        # post_id is the internal _id of elasticsearch store
        #"user_id", "place_name", "text", "@timestamp", "type", "post_id", "user_img_url", "content_img_url", "coord", "up_votes", "username"
        self.post_id = post_id
        self.text = text
        self.created = created
        self.content_img_url = content_img_url
        self.user_img_url = user_img_url
        self.type = type
        self.up_votes = up_votes
        self.user_id = user_id
        self.place_name = place_name
        self.coord = coord
        self.username = username
    def get_as_dict(self):
        d = {"post_id": self.post_id, "text": self.text, "created": self.created.strftime("%Y-%m-%dT%H:%M:%SZ"),
             "content_img_url": self.content_img_url, "user_img_url":self.user_img_url, "source": self.type, "up_votes": self.up_votes,
             "user_id": self.user_id, "place_name": self.place_name, "coord": self.coord, "username": self.username}
        return d