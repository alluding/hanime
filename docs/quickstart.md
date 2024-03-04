# Jumpstart/Examples

# Supported Values

# Image
```
yuri
nsfw-general
traps
futa
yaoi
media
```

# Video
View `hanime/video.py` for the list of supported tags; the list is too big to fit here.

# Image

```python
from hanime import Image

image = Image()
result = image.get_uploads(
    ["nsfw-general"],  # Channels to fetch from.
    offset=1,  # Start at the second upload.
)
# Parse the JSON result into a more readable format, using an object/model for easy access via attributes and properties.
parsed = image._parse(result)
```

# Video

```python
from hanime import Video

video = Video()

random_video = video.random_video()  # Returns a random video, any tag.
random_video_tag = video.get_random_video_tag(
    num_tags=3,  # How many tags, defaults to 1.
    include_tags=["milf", "creampie"],  # Tags to ALWAYS include, no matter what.
    exclude_tags=["ntr", "rape"],  # Tags to NEVER include.
    page=2,  # The page number, defaults to 1.
)
video_info = video.information(123)  # Information for a video.
```

# User

```python
from hanime import User

user = User()
result = user.get_channel("channel")
```

# Search

Something you shouldn't touch unless you really know what you're doing; by default, it's used as more of a utility to help with some of the other categories/functions, such as building payloads, etc., for API requests to the `hanime` API.

Do **NOT** touch or use unless you know exactly what you're doing. I will not provide any documentation or guidance on how to use this. If you wish to figure it out, read the source code and figure it out yourself.